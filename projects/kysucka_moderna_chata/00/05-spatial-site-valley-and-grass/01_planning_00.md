# Plan coherent 3D spatial site, open valley vista, enclosed garden fence, and short-lawn / tall-meadow grass systems (v05)

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-spatial-site-valley-and-grass
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: BLENDER-MCP-SPATIAL-SITE-VALLEY-AND-GRASS-PLAN
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — bounded technical planning for world-space 360° terrain and +X valley vista, complete polygonal garden enclosure and gate, short-lawn vs tall-meadow grass masks/LOD/budget, and deterministic scripts/site_v05.py source/MCP synchronization using established Orchestrator MCP grounding
Recommended context capacity: approximately 250k tokens
Independence required: no

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: concise repository- and live-MCP-grounded technical plan specifying (1) protected terrace witnesses and continuous world-space 360° mountain/valley terrain & forest layout, (2) complete non-self-intersecting garden polygon, rustic fence continuation, closed gate, and path connection, (3) short-lawn (4–10 cm blades over ambientCG Grass005 PBR turf base) and tall-meadow (25–65 cm) masks, instancing/chunking, LOD, and triangle/memory/file-size budgets, and (4) exact source/output allowlist, deterministic scripts/site_v05.py hook, review camera poses (C1 before/after, site_overview, valley_from_inside, orbit_sheet, grass_details), semantic replay tolerances, and idempotence verification
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1

Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0

## Goal and Context

Produce a concise, decision-complete technical implementation plan for the logical whole `kysucka-moderna-chata-spatial-site-valley-and-grass`.

Accepted Cooperator and project decisions:
- Turn `v04`'s primarily camera-composed ribbon environment into a **coherent 3D mountain property (`blender/kysucka_chata_mcp_v05.blend`)** that works from `CAM_A_REFERENCE`, in 360° 3D viewport orbiting, and when looking out from inside the glazed living/dining room:
  1. **Continuous 360° mountain setting with an open `+X` valley vista** from the glazed gable (`X = 14.4 m`), replacing/hiding the floating camera-ribbon arches (`LANDSCAPE_hills_v04_1..4`) and reshaping/extending the terrain outside a declared protected flat terrace so there are no floating ribbon undersides, holes, exposed sheet backs, or flat terrain shelves covering the valley floor, while broadly retaining the accepted `CAM_A_REFERENCE` front hillside composition and re-grounding retained distant vegetation cleanly.
  2. **A complete, non-self-intersecting polygonal garden enclosure** (`~34–36 m × 24–26 m`) preserving the accepted `v03` foreground fence segment `(16.60, -8.62) -> (18.25, 1.00)` (`26` stakes, `2` rails) intact, continuing its ends around the property with `MAT_TIMBER_FENCE` (`rough_wood`), credible corner/anchor posts, terrain-following stakes/rails, one simple closed gate aligned with the entrance path (`X = 7.875 m`) plus a modest path-slab continuation to the gate, and generous unobstructed interior lawn reserved for future fruit trees (do not add new fruit trees in this whole).
  3. **Visibly distinct short lawn (`4–10 cm` real 3D blades over an `ambientCG Grass005` CC0 PBR turf/thatch base) inside the garden vs unmown tall meadow grass (`25–65 cm` stems/clumps with dry/seed-head variation) outside the garden and along forest/valley meadow edges**, derived from the same garden polygon, terrain height query, and hard-surface clearance masks.
- Keep `CAM_A_REFERENCE` (`[21.5, -10.0, 1.25] -> [8.5, 2.5, 1.25]`, `35 mm`, `sensor 36 mm`, `shift_x = 0.0`, `shift_y = 0.105`) active for the final saved `v05` scene (disclosing any `clip_end` increase if needed for the extended valley).
- Preserve S00, v01, v02, v03, and v04 `.blend` files, `reference/kysucka_chata_moderna.png`, `scripts/timber_fence_v03.py`, `scripts/landscape_v04.py`, normalized `assets/models/*` libraries, building architecture/roof/openings, interior furniture/partitions, chimney/fireplace, glazing, lights/world, and accepted `v03` timber/fence untouched.
- Communicate with the Cooperator in Slovak if addressing him directly; write your formal Worker report in English starting with `### Report for ORCHESTRATOR_CHAT`.
- **Important anti-stall constraint**: Do **not** print, quote, propose, or reproduce the project's literal Orchestrator-owned closure signal anywhere in your plan or report. Keep the managed AP block and the entire `Closure and Git gates` section of `AGENTS.md` untouched.

## Repository and Environment Prerequisites

Repository identity: `https://github.com/cisarik/kysucka_moderna_chata`
Working directory: `/home/agile/Projects/kysucka_moderna_chata`
Repository checkout topology: standalone checkout
Expected branch: `main`
Baseline: `f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c` (`feat: add Kysuce forested hills, orchard apple tree and natural garden in v04`)
Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` recorded in gitlink `.ap` (`160000 commit d7023cf037f6d17885c3ede5c04812c61640da50`; note that on this Linux workstation clone `.ap/` is currently uninitialized `-d7023cf037f6d17885c3ede5c04812c61640da50` — verify the gitlink read-only via `git ls-tree HEAD .ap` and read AP docs from `/home/agile/Projects/ap` during `01/01`; `01/02` will authorize `git submodule update --init --checkout .ap`)
Trace repository: `https://github.com/cisarik/meta` at `/home/agile/meta` (`HEAD` `bb274bdd179e1038da0d3679fea214dd81128fe4`; preserve all unrelated untracked files such as `projects/kronika/...` untouched)

Mandatory reading:
- `/home/agile/Projects/ap/AP.md` (Semantic Authority and WORKER row of Per-Role Minimum-Reading Spine; RF-03, RF-04, RF-06, RF-12, RF-16, RF-18, RF-19; §8 Worker Responsibilities; §18 Stopping Conditions)
- `/home/agile/Projects/ap/AP_WORKER.md` (`#worker-session-target`, `#reporting`)
- `/home/agile/Projects/ap/PROMPT_CONTRACTS.md` (`#worker-report-header`, `#planning-record`, `#cooperator-delivery-and-trace-destination-record`)
- `AGENTS.md`, `docs/OPERATIONS.md`, `README_SK.md`, `assets/ASSET_MANIFEST.md`, `model/parameters.json`, `scripts/build_scene.py`, `scripts/timber_fence_v03.py`, `scripts/landscape_v04.py`
- `/home/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden/01_closure.md`
- `/home/agile/meta/projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/00_handout.md` and `00_notes.md`

## Established Orchestrator MCP, Spatial Geometry, and Asset Grounding (Reuse Directly)

The Orchestrator has already verified the repository baseline (`f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c`), all protected S00/v01/v02/v03/v04 SHA-256 hashes, the live Blender 5.3.0 GUI session via MCP (`127.0.0.1:9876`), the 3D scene bounds/projections, and the official `ambientCG` API:

1. **Live Blender 5.3.0 state**:
   - Open file: `/home/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v04.blend` (`SHA-256 = c19b37cf75037969d2608677d276880d46e9ae7afc31aa11a78c340241fa3d43`, `is_saved: True`, `is_dirty: False`, `is_job_running('RENDER'): False`, `mode: OBJECT`, `2,373` scene objects, `16` off-scene master collections).
   - Locked `CAM_A_REFERENCE`: `location = [21.5, -10.0, 1.25]`, `target = [8.5, 2.5, 1.25]`, `lens = 35.0 mm`, `sensor_width = 36.0 mm`, `shift_x = 0.0`, `shift_y = 0.105`, `clip_end = 500.0`.
   - Predecessor baseline render `/home/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden/renders/after.png` (`7e2c7daa0e9c3be0a08ba7a987a187340d682117f1b10925c338dc53eb46b665`) is verified on disk with the exact comparison render profile (`1448 × 1086`, Cycles CPU, 96 samples, OIDN ON, seed 0, frame 0, AgX/None, exposure 0, gamma 1).
2. **Protected terrace witnesses (`Z = -0.055 m` flat ground support)**:
   - `SITE_terrain_proxy` (`45 × 52 = 2,340` vertices, `x = -45 + i*2.5`, `y = -18 + j*2.4`) has `Z = -0.055 m` for all `Y ≤ 12.0 m` (`585` vertices).
   - All near-cottage structures and contact witnesses rest on `Z = -0.055 m` inside `X ∈ [-15.0, 19.0], Y ∈ [-10.0, 11.5]`:
     - `BASE_slab` (`[0.0, 14.4] × [0.0, 8.4]`), `PORCH_paving*` (`[0.0, 14.4] × [-0.65, 0.0]`), `ENTRY_step_1..3` (`[6.7, 9.05] × [-1.05, 0.0]`), `BED_entry` (`[2.4, 15.2] × [-1.65, -0.75]`) + `168` `V04_BED_*` instances, `BOLLARD_*` at `(4.3, -1.65)` and `(12.8, -1.60)`,
     - `PATH_slab` .. `PATH_slab.007` (`8` slabs at `X ∈ [6.825, 8.925]`, `Y = -1.30 .. -5.50`, `Z ∈ [0.0, 0.11]`),
     - `V04_ORCHARD` (`(-1.1, -2.6, -0.095)`) + `28` `V04_APPLE_*`, `V04_YOUNG_00` (`(-8.0, 0.0, -0.067)`), `V04_YOUNG_01` (`(-13.5, 4.5, -0.067)`),
     - `FENCE_post_proxy` .. `.025` (`26` stakes) + `FENCE_rail_proxy*` (`2` rails) along `(16.60, -8.62) -> (18.25, 1.00)` (`foot_z = -0.075 m`), and `312` `V04_EDGE_GRASS_*` instances (`X ∈ [1.928, 18.824], Y ∈ [-8.634, 1.077], Z = -0.067 m`).
   - Outside that flat terrace: `V04_YOUNG_02` at `(13.0, 13.5, 0.4323)`, `V04_YOUNG_03` at `(10.0, 22.0, 2.7502)`, and `1,200` `V04_FOREST_*` instances (verified `0` of `1,200` `V04_FOREST_*` trees lie inside `X ∈ [-17.5, 21.0], Y ∈ [-10.5, 17.5]`).
3. **Garden polygon, gate, and camera-frustum geometry**:
   - A 5-vertex non-self-intersecting convex polygon `P0(16.60, -8.62) -> P1(18.25, 1.00) -> P2(19.20, 14.50) -> P3(-15.50, 15.50) -> P4(-15.00, -7.80) -> P0(16.60, -8.62)` (`34.70 m × 24.12 m`, area `~812 m²`) keeps `P0 -> P1` as the exact `v03` segment, places `P4 -> P0` outside the bottom-left frustum of `CAM_A_REFERENCE` (`u < -0.02`), places `P3 -> P4` (`X ≈ -15 m`) behind the orchard crown, and reserves `> 450 m²` of unobstructed west and rear lawn for future fruit trees.
   - The entrance path center `X = 7.875 m` intersects `P4 -> P0` at `Y ≈ -8.394 m`. Four continuation slabs (`V05_PATH_slab_00..03` at `Y = -6.10, -6.70, -7.30, -7.90`, `X = 7.875, Z = 0.055`, `[2.1, 0.55, 0.11]`, `MAT_CONCRETE`) reach a closed rustic timber gate (`V05_GATE_*`, clear opening `2.20 m` at `X ∈ [6.775, 8.975]`, using `MAT_TIMBER_FENCE`) without moving any existing `PATH_slab*`.
4. **Interior living/dining sightline (`valley_from_inside.png`)**:
   - Room `07` (`X ∈ [8.8, 14.1], Y ∈ [0.3, 8.1]`, `floor_z = 0.45 m`, `FLOOR_interior` top `0.494 m`) has unobstructed floor at `X ∈ [11.8, 14.0], Y ∈ [2.0, 5.2]` looking through the central bay (`Y ∈ [2.175, 4.200]`, transom `Z = 3.18 m`) of `G01_lower_glass` / `G02_upper_glass` (`X = 14.412 m`) toward `+X`. An interior camera at `[12.20, 3.20, 2.00]` (`1.55 m` standing eye height above `floor_z = 0.45 m`) targeting `[65.0, 3.20, 1.35]` (`lens = 28–32 mm`) looks cleanly through the unchanged glass into the `+X` valley.
5. **New turf PBR asset (`ambientCG Grass005`)**:
   - Verified via `https://ambientcg.com/api/v2/full_json?id=Grass005&include=downloadData`: `Grass005_2K-JPG.zip` (`https://ambientcg.com/get?file=Grass005_2K-JPG.zip`, `39,523,019` B) and `Grass005_1K-JPG.zip` (`https://ambientcg.com/get?file=Grass005_1K-JPG.zip`, `10,442,657` B), CC0 (`https://docs.ambientcg.com/license/`), procedural PBR with bitmap elements (not a photoscan). Retain only `Color`, `Roughness`, and `NormalGL` JPG maps in `assets/textures/grass/Grass005/` (fallback `Grass001` only if needed).

## Questions Your Plan Must Answer (Concise and Decision-Complete)

Perform one brief read-only MCP verification call (`get_scene_info` or a short read-only `execute_blender_code`) to confirm your session's live MCP connection to `blender/kysucka_chata_mcp_v04.blend`, then answer **only** these four questions:

1. **Protected terrace and world-space 360° mountain/valley layout**:
   - Define the exact protected flat terrace region (`Z = -0.055 m`) and its contact-height witness objects (`BASE_slab`, `PORCH_paving*`, `ENTRY_step_1..3`, `BED_entry` + `V04_BED_*`, `BOLLARD_*`, `PATH_slab*`, `V04_ORCHARD`, `V04_YOUNG_00/01`, `FENCE_post_proxy*`, `FENCE_rail_proxy*`), where vertex/contact heights remain `0.0 m` changed.
   - Specify the continuous world-space elevation function `terrain_height_v05(x, y)` and mesh architecture (reshaping `SITE_terrain_proxy` outside the protected terrace and stitching/extending a seamless surrounding world-space terrain mesh `V05_TERRAIN` across `~[-260, +320] × [-220, +260] m`, while hiding `LANDSCAPE_hills_v04_1..4` so no floating ribbon undersides, holes, or flat valley-covering shelves remain):
     - Gentle garden terrace grading to the fence boundary,
     - Open descending `+X` valley corridor (`X > 20 m`, centered around `Y ≈ 3 m`, descending to `Z ≈ -18..-26 m` with north/south forested valley side-ridges and a distant across-valley horizon ridge at `X ≈ 220..320 m`),
     - Continuous 360° surrounding hills in the `-X, +Y` (retaining `CAM_A_REFERENCE`'s layered ridge silhouette), `-X`, `+Y`, and `-Y` sectors,
     - Vertical re-grounding of retained `V04_FOREST_*` (`1,200` spruces) and `V04_YOUNG_02..03` onto the unified terrain surface plus additional `V05_FOREST_*` linked spruce placements (`Picea mariana` and `Picea abies` with irregular meadow edges/glades) around the west, south, north-east, and valley side-ridges.
2. **Complete garden polygon, fence continuation, and gate**:
   - Specify the exact non-self-intersecting garden polygon vertices (`[P0(16.60, -8.62), P1(18.25, 1.00), P2(19.20, 14.50), P3(-15.50, 15.50), P4(-15.00, -7.80)]` or equivalent verified coordinates, footprint dimensions, and area `~800–950 m²`), keeping `P0 -> P1` (`26` `FENCE_post_proxy*` stakes and `2` `FENCE_rail_proxy*` rails) 100% intact and reserving generous unobstructed west/rear garden space for future fruit trees.
   - Specify the `V05_FENCE_*` continuation stakes, corner/anchor posts, and terrain-following rails along `P1 -> P2 -> P3 -> P4 -> P0` (reusing `MAT_TIMBER_FENCE`, metric UVs, `V03_endgrain`, and stake dimensions without duplicate corner posts or floating rails), the closed rustic entrance gate (`V05_GATE_*`) centered at `X = 7.875 m` on `P4 -> P0`, and the `4` continuation slabs (`V05_PATH_slab_00..03`) connecting `PATH_slab.007` to the gate without moving existing slabs.
3. **Short-lawn and tall-meadow masks, materials, instancing/LOD, and budget**:
   - Specify how `ambientCG Grass005` (`Color`, `Roughness`, `NormalGL` 1K/2K JPGs) is acquired, verified, documented in `assets/ASSET_MANIFEST.md`, and built into `MAT_V05_LAWN_BASE` (inside the garden polygon) and `MAT_V05_MEADOW_BASE` (outside) with aperiodic world-space UVs.
   - Specify the derived compound 3D short-lawn blade patch masters (`V05_MASTER_LAWN_PATCH_*`, `4–10 cm` tapered/curved blades with green/olive/thatch variation on dedicated V05 materials, covering the entire enclosed garden lawn with higher density near `CAM_A_REFERENCE` / path / terrace and full 360° coverage across the west/rear lawn, plus handling of interior `V04_EDGE_GRASS_*` tufts so the lawn reads as maintained turf rather than isolated weeds).
   - Specify the tall unmown meadow system (`25–65 cm`, reusing `grass_medium_01` masters/maps with dedicated `MAT_V05_MEADOW_GREEN` / `MAT_V05_MEADOW_DRY` materials and compound meadow clusters `V05_MASTER_MEADOW_CLUSTER_*` outside the fence, along the descending `+X` valley foreground, and on 360° forest-edge meadows), and the exact hard-surface clearance masks (zero grass on house footprint, porch, steps, path slabs, gate opening/swing, `BED_entry`, or through fence posts).
   - Specify the triangle, memory, and file-size budget (`< 1.5 M` target / `< 3.0 M` hard ceiling unique evaluated triangles, `< 90 MiB` per tracked file, `< 3 GiB` target render RSS) and the small-patch/sector pre-measurement step before full scattering.
4. **Exact source/output scope, `scripts/site_v05.py` hook, and review poses**:
   - Specify the exact changed-path allowlist for `01/02` (`model/parameters.json` with `site_v05`, `scripts/site_v05.py`, `scripts/build_scene.py`, `assets/textures/grass/Grass005/*`, `assets/ASSET_MANIFEST.md`, `blender/kysucka_chata_mcp_v05.blend`, narrow updates to `AGENTS.md`, `README_SK.md`, `docs/OPERATIONS.md`, gitignored `work/` checkpoints/replay/downloads, `.ap` submodule checkout initialization at `d7023cf037f6d17885c3ede5c04812c61640da50`, and Meta outputs `renders/before.png`, `renders/after.png`, `renders/site_overview.png`, `renders/valley_from_inside.png`, `renders/orbit_sheet.png`, `renders/grass_details.png`, `renders/render_metadata.json`, `evidence/site_comparison.md`, `01_report_01.md`, `../00_RUN_MAP.md`).
   - Specify how `scripts/site_v05.py::apply_v05(scene, P, ROOT)` uses isolated `random.Random(13705)` after `apply_v03` and `apply_v04`, preserves `random.getstate()`, is idempotent on a second invocation, and passes cold CLI reopen and factory-startup source replay (`work/v05_source_replay.blend`).
   - Specify the exact camera poses, lenses, and render profiles for all required review images (`before.png`, `after.png`, `site_overview.png`, `valley_from_inside.png`, `orbit_sheet.png`, `grass_details.png`), keeping `CAM_A_REFERENCE` active in the saved `blender/kysucka_chata_mcp_v05.blend`.

## Execution Route and Authority (AP RF-16)

Execution route: **task-specific bounded deviation `blender-mcp-live-v1`** under AP RF-16:
- **Declared route not used alone**: `blender-local-v1` in `AGENTS.md` and `docs/OPERATIONS.md` (headless CLI inspection without MCP), which cannot perform live MCP inspection/control of the open Blender GUI session required by this logical whole.
- **Activated route for this task**: `blender-mcp-live-v1` using the session's exposed Blender MCP tools (`get_addon_status`, `get_scene_info`, `execute_blender_code`, `look`) connected to the running Blender 5.3.0 GUI (`127.0.0.1:9876`), supplemented by read-only local Git/file/hash inspection.
- **Evidence class**: directly observed MCP tool receipts and read-only repository/hash checks.
- **Bounded planning authority**: strictly read-only MCP observation and read-only local repository inspection. No project file writes, downloads, or scene mutations are authorized during planning.

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
Downloadable prompt filename: 01_planning_00.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass
Report filename: 01_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: ORCHESTRATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: none
Host/remote mutation: none
Trace persistence: none

Positive authority:
- Read-only inspection of `/home/agile/Projects/kysucka_moderna_chata`, `/home/agile/Projects/ap`, and `/home/agile/meta/projects/kysucka_moderna_chata/00/`.
- Read-only Blender MCP calls (`get_addon_status`, `get_scene_info`, read-only `execute_blender_code` printing JSON/text without modifying `bpy.data` or `bpy.context.scene`).
- **Satisfiable completion route for Native Plan Mode (`RF-19` / `00_handout.md`)**: Because the Worker client's Native Plan Mode blocks direct file writes, `Report persistence owner` is set to `ORCHESTRATOR` with `Trace persistence: none` for the Worker (if your client permits writing `/home/agile/meta/projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/01_report_00.md` directly and reading it back, you may do so; if Native Plan Mode blocks the file write, return your complete standard terminal report `### Report for ORCHESTRATOR_CHAT` ... directly in the session output with `status: PASS` once your read-only checks and technical plan are complete). The Orchestrator will persist your exact returned report bytes to `/home/agile/meta/projects/kysucka_moderna_chata/00/05-spatial-site-valley-and-grass/01_report_00.md` and verify full readback without another planning cycle.

Commands:
- Read-only file reads, `git status`, `git rev-parse`, `git ls-tree HEAD .ap`, `sha256sum`.
- Read-only Blender MCP tool calls (`get_addon_status`, `get_scene_info`, read-only `execute_blender_code`).

Git authority:
- Read-only in both `/home/agile/Projects/kysucka_moderna_chata` and `/home/agile/meta`. No `git fetch`, `git submodule update`, `git add`, `git commit`, `git push`, `git checkout`, `git reset`, or `git clean` during `01/01`.

Dependency, network, and secret authority:
- Dependency authority: none (no package, add-on, `uvx`, `pip`, or runtime installation/update).
- Network authority: localhost Blender MCP socket (`127.0.0.1:9876`) only during planning; external asset downloads are reserved for `01/02` implementation.
- Secret authority: none.
- Side-effect authority: strictly read-only inspection of repository and live Blender MCP state.

Negative authority:
- Do NOT mutate any file in `/home/agile/Projects/kysucka_moderna_chata` during planning.
- Do NOT mutate the live Blender scene, download assets, change camera/material/mesh values, save `.blend` files, or trigger `bpy.ops.render.render()` during planning.
- Do NOT install or update `mcp-for-blender`, modify client MCP config, change telemetry settings, or call `generate_3d` / `generate_gaussian_world` / `import_asset`.
- Do NOT quote, print, or reproduce the literal project closure signal from `AGENTS.md`.

## Validation and Stopping Conditions

Evidence tier: E2
Evidence tier basis: cross-cutting reversible 3D terrain/valley/enclosure/grass site realization, CC0 PBR turf map integration, multi-view Cycles verification, and deterministic factory-startup source replay
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: `git ls-tree HEAD .ap` and SHA-256 verification of protected S00/v01/v02/v03/v04 sources (plus `./.ap/ap doctor` once `.ap` is materialized in `01/02`)
Affected tests: none (read-only planning phase)
New causal regression: none — planning phase specifies the bounded `site_v05` refinement, multi-camera verification, and semantic source-replay checks
Broad or full suite: not-used
Runtime or testbed: `blender-mcp-live-v1` (read-only observation in planning)
Independent acceptance: not-required

Validation in this planning task:
1. Verify repository root `/home/agile/Projects/kysucka_moderna_chata`, branch `main`, HEAD `f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c`, clean status, recorded `.ap` gitlink `d7023cf037f6d17885c3ede5c04812c61640da50`, and the protected S00, v01, v02, v03, and v04 SHA-256 hashes.
2. Perform at least one read-only Blender MCP tool call confirming live connection to the open `kysucka_chata_mcp_v04.blend` scene (`CAM_A_REFERENCE` locked at `[21.5, -10.0, 1.25]`, `35 mm`, `shift_y = 0.105`) without changing `bpy.data.is_dirty` (`False`) or scene objects.
3. Verify that your plan answers all four required questions concisely and decision-completely.

Stopping conditions:
- Stop immediately if repository identity, baseline commit, or source hashes disagree with this grant.
- Stop and report `BLOCKED` if Blender MCP tools are unavailable in your session (do not substitute headless CLI or attempt installation/reconfiguration).
- Stop after submitting your terminal planning report; planning authority expires at the report (`Plan-to-Execution Gate`).

## Completion and Report Contract

Begin your report with `### Report for ORCHESTRATOR_CHAT` and echo once:
- `Logical whole identity: kysucka-moderna-chata-spatial-site-valley-and-grass`
- `Worker session ordinal: 01`
- `Worker exchange ordinal: 01`

Include the compact core (`status: PASS` once read-only verification and the four-part plan are complete; `Phase-qualified result: not-applicable`; `Start commit` and `End commit`: `f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c`; `Report justification: new-evidence`; `Logical-whole closure: not-closed`; `Orchestration critique` with `MEASURED` and `LEAD`; `Resolved Execution Issues / Near-Misses`; `Pre-Existing Failure Classification`; and `Authority expiry`). Keep the report concise (under ~240 lines) and decision-complete.

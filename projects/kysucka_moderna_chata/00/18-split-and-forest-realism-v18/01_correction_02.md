# V18 correction and Stage 3 completion (01/03) — 360° natural valley basin without bare green table, real 3D viewport tree/terrain models, true scene-split pruning, and dense forest-margin understory

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-split-and-forest-realism-v18
Worker session ordinal: 01
Worker exchange ordinal: 03
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker (same-session continuation of 01/01–01/02)
Phase: implementation
Task identity: SPLIT-AND-FOREST-V18-CORRECTION-AND-STAGE3 — repair the rejected 3D exterior spatial layout, viewport proxy models, scene-split bloat, and forest-margin ground cover, and complete Stage 3 full-margin forest and north trail continuation
Delivery route: manual Cooperator delivery
Continuity anchor: terminal report `01_report_01.md` (Worker session 01 / exchange 02) and Cooperator visual rejection (`Exterier velmi zly` with 3 live 3D-viewport screenshots) followed by Cooperator approval (`Suhlasi`) of the 4-point corrective specification recorded in `00_notes.md` on 2026-11-23
Authority renewal: prior authority expired at `01_report_01.md`; this prompt grants complete new bounded correction and Stage 3 completion authority with `Native planning mode: not-used`. Retained context is convenience, not authority. Re-gate repository, input hashes, and process state yourself; stop on any conflict between retained context and current repository evidence.
Evidence posture: non-independent
Implementation authority: explicit
Independence required: no
Reasoning recommendation: High — named risks: trimming/reshaping `V11_TERRAIN_EXTENSION` and redistributing the outer forest so no bare flat green table or artificial `foreground_sides` keyhole ring appears from any 3D orbit angle; replacing 156/214-triangle `V17 PREVIEW` cone/balloon viewport proxies with real 3D branch/crown meshes and dark forest-floor viewport shading; true `orphans_purge` pruning of split scenes while preserving `model/shared_envelope_v18.json`; dense 3D forest-margin understory without primitive geometric moss polygons; and continuous supported gravel trail to the actual northern terrain boundary
Recommended context capacity: approximately 250k tokens

## Active Amended Expectation Record
Amendment record: active
Cooperator decision ownership: COOPERATOR
Cooperator decision evidence: exact COOPERATOR acceptance evidence `Exterier velmi zly` (with 3 3D-viewport orbit screenshots of `blender/kysucka_chata_exterier.blend`) and `Suhlasi` in session on 2026-11-23
Superseded expectation: unpruned 716 MiB split copies retaining `V11_TERRAIN_EXTENSION` out to `[-752.45, 784.30] × [-621.50, 644.75] m` with a directional frustum wedge of trees and the `foreground_sides` semicircular ring, 156/214-triangle `V17 PREVIEW` cone/balloon viewport proxies with a flat green viewport terrain modifier, and sparse `0.42–1.60 m` ground cover with primitive geometric twig/moss meshes at the forest margin
Amended expectation: (1) trim the bare outer `V11_TERRAIN_EXTENSION` apron to a compact natural valley basin (`[-320, 340] × [-220, 340] m`), remove the artificial `foreground_sides` semicircular tree ring around the camera, and extend the forest continuously across the surrounding valley slopes/ridges all the way to the outer terrain perimeter (leaving the central valley meadow around the cottage and the `CAM_V11_VALLEY_REVIEW` valley sightline open) with the gravel trail reaching the actual northern terrain boundary (`Y = 340 m`); (2) remove `V17 PREVIEW Ihličnany`, `V17 PREVIEW Listnáče`, and `Povrch v pracovnom pohľade`, binding `IsViewport` to real 3D branch/crown meshes (`V12_WORK_FOREST` 5,400–6,300 tris and `V17_BROADLEAF_WORK` `tevy` LOD2 5,446–5,708 tris with textured/shaded bark and foliage materials and viewport `show_cavity = True`) and displaying dark brown forest-floor soil (`Forest Ground 01`) under the entire forest stand in both viewport and render; (3) genuinely prune and `orphans_purge` both `blender/kysucka_chata_exterier.blend` and `blender/kysucka_chata_interier.blend` while preserving the 289-object `model/shared_envelope_v18.json` (`87288303...`); and (4) remove primitive 3D geometric twig/moss polygons and populate dense continuous 3D grass, `shrub_01`, and low-skirted half-height juvenile spruces (~5% of active forest) at the forest margin and around broadleaf trunks
Amendment boundary: V18-3D-EXTERIOR-BASIN-VIEWPORT-AND-FOREST-REALISM
Cooperator decision authority effect: decision-only-no-worker-mutation-authority
Orchestrator superseded-expectation record: recorded by ORCHESTRATOR under V18-3D-EXTERIOR-BASIN-VIEWPORT-AND-FOREST-REALISM
Orchestrator authority issuance: issued by ORCHESTRATOR to Worker session 01 / exchange 03 for V18-3D-EXTERIOR-BASIN-VIEWPORT-AND-FOREST-REALISM only
Renewed task boundary: V18-3D-EXTERIOR-BASIN-VIEWPORT-AND-FOREST-REALISM only
Worker recipient: Worker session 01 / exchange 03
Worker implementation: pending in exchange 01/03
Worker validation: pending in exchange 01/03
Role sequence: COOPERATOR-decision -> ORCHESTRATOR-record -> ORCHESTRATOR-issuance -> WORKER-implementation -> WORKER-validation
Superseded expectation reported as failure: no
Unrelated scope change: none
Rendered acceptance ownership: COOPERATOR
## End Active Amended Expectation Record

## Exact diagnosis of the 4 failures in `01/02` and binding corrective specification

Michal opened `blender/kysucka_chata_exterier.blend` in his live Blender 5.3.0 3D viewport, orbited around the scene from above and obliquely (3 screenshots), and rejected the exterior (`Exterier velmi zly`). You must fix all four root causes in `scripts/v18_split_forest.py` and regenerate the final Stage 3 products `blender/kysucka_chata_exterier.blend` and `blender/kysucka_chata_interier.blend` (archiving the rejected `01/02` outputs first or overwriting via verified staged builds in `work/v18/stage3/`):

### 1. Eliminate the giant bare green table and the artificial "mushroom / keyhole ring" of trees (360° natural valley basin)

- **Why Screenshots 1 & 2 failed:** `V11_TERRAIN_EXTENSION` spans `[-752.45, 784.30] × [-621.50, 644.75] m` (`1,536 × 1,266 m`), while `99_EXTERIOR_V11` and `V10_HILL_FORESTS` were placed only in the forward viewing cone of `CAM_V11_VALLEY_REVIEW` plus an artificial semicircular corral (`foreground_sides: 409` trees around `station = -70 m` right behind the camera `[62, -27]`). More than 70% of the terrain rectangle is an empty flat green board, and from any 3D orbit angle the forest looks like a mushroom stamp with a semicircular fence of trees in front of the cottage.
- **Required fix in `kysucka_chata_exterier.blend`:**
  1. **Trim `V11_TERRAIN_EXTENSION` to a compact natural valley basin `[-320.0, 340.0] × [-220.0, 340.0] m`:**
     - Keep `V11_TERRAIN_NEAR` and `V11_TERRAIN_FAR` (`[-137.75, 169.60] × [-115.0, 138.25] m`) and all protected core/garden/cottage vertices 100% intact.
     - Rebuild/trim the owned `V11_TERRAIN_EXTENSION` rings so its outer perimeter is `[X_min, X_max] = [-320.0, 340.0] m` and `[Y_min, Y_max] = [-220.0, 340.0] m` (still stitched seamlessly at `j = 0` to `V11_TERRAIN_FAR`'s outer seam `[-137.75, 169.60] × [-115.0, 138.25] m`), gently raising the outer flanks/ridges on the West, North, and East/South-East flanks so the terrain forms a natural Carpathian/Kysuce valley trough opening toward the South-East (`+X, -Y`) without hundreds of metres of flat green apron.
     - Clip `V17_GROUND_COVER_POINTS` (and any exterior point clouds) cleanly to the trimmed terrain extent `[-320.0, 340.0] × [-220.0, 340.0] m` so zero floating instances exist outside the terrain mesh.
  2. **Remove the artificial `foreground_sides` keyhole corral and extend the forest continuously to the outer terrain edges:**
     - Remove the artificial `foreground_sides` semicircular ring of trees right across the front valley floor behind `[62, -27]` (especially those huge isolated balloon broadleaves standing in the front meadow in Screenshot 3!). Keep the central valley meadow floor and the `CAM_V11_VALLEY_REVIEW` (`[62, -27, 12]`) viewing corridor to the cottage (`[7.2, 4.2]`) and up the central valley axis open!
     - Redistribute/extend the hill and flank forest (`99_EXTERIOR_V11` + `V10_HILL_FORESTS` / `V18_BASIN_FOREST`) continuously across the left (West/South-West) slopes, right (North-East/East) slopes, and upper (North/North-West) ridge **all the way to the outer `[-320, 340] × [-220, 340] m` perimeter** of the terrain ( leaving only the open central valley floor/meadow and trail corridor clear, plus a natural open valley entry gap on the lower South-East floor). When viewed from any 3D orbit angle (like Michal's Screenshots 1, 2, 3), the forested hills must reach the outer edges of the terrain block rather than stopping inside a bare green square!
  3. **Extend the gravel trail (`V07_TRAIL`) to the actual northern boundary `Y = 340.0 m`:**
     - From the old `V07_TRAIL` seam `[42.0, 138.25, 1.157007]`, build the supported `1.25 m` wide, `15 mm` offset gravel continuation along the gently climbing valley/forest margin to the actual northern perimeter of the trimmed terrain at `Y = 340.0 m` (using your deterministic root-avoiding alignment and local terrain grading strip `≤ 2.5 m`, with longitudinal grade `≤ 28%` and clear `1.0 m × 2.2 m` walking envelope).

### 2. Replace the cartoonish 156/214-triangle `V17 PREVIEW` paper cones and balloon spheres with real 3D tree models and real terrain shading in the 3D viewport

- **Why Screenshot 3 failed:** `V17 PREVIEW Ihličnany` (`136–156` triangles — stacked star cones), `V17 PREVIEW Listnáče` (`214` triangles — blocky origami balloon spheres on thin sticks), and `Povrch v pracovnom pohľade` (a single flat green texture replacing all terrain materials in the viewport) make the 3D viewport look like a low-poly cartoon.
- **Required fix in `kysucka_chata_exterier.blend` (and `kysucka_chata_interier.blend`):**
  1. **Remove `V17 PREVIEW Ihličnany`, `V17 PREVIEW Listnáče`, `V17 PREVIEW V12_WRAP_V11_FOREST_GN`, `V17 PREVIEW V17_BROADLEAF_IsViewport`, and the `Povrch v pracovnom pohľade` modifier on `V11_TERRAIN_NEAR`, `V11_TERRAIN_FAR`, `V11_TERRAIN_EXTENSION`, and `V07_TRAIL`.**
  2. **Bind the `IsViewport` working branch of the forest Geometry Nodes groups to real 3D botanical meshes:**
     - For conifers (`V12_WRAP_V11_FOREST_GN`): bind the `IsViewport` branch to **`V12_WORK_FOREST`** (the 6 source-branch/foliage spruce meshes with `5,400–6,300` triangles each, updated so prototype `004` uses the fuller lower-whorl juvenile spruce mesh) AND assign compact textured/shaded bark and needle materials (`MAT_V12_WORK_BARK`, `MAT_V12_WORK_NEEDLES` with packed albedo texture nodes active and realistic dark spruce-green diffuse/base colors `(0.055, 0.095, 0.035)` so they render with natural 3D branch detail in BOTH Solid-Texture and Material Preview modes!).
     - For broadleaves (`V17_BROADLEAF_IsViewport`): bind the `IsViewport` branch to **`V17_BROADLEAF_WORK`** (the 2 actual `tevy` LOD2 3D beech and birch meshes with `5,708` and `5,446` triangles — real 3D trunks, branches, and leaf crowns, NEVER balloon spheres!) with active packed bark and leaf textures (`beech_bark_lod1`, `beech_leaves_lod1`, `birch_bark_lod1`, `birch_leaves_lod1` or compact 512px textured viewport equivalents with alpha clip/hash so leaf clusters have real botanical shape in the 3D viewport!).
  3. **Make the terrain and forest floor look realistic in the 3D viewport as well as Cycles:**
     - Instead of one flat green texture across the whole terrain, assign distinct polygon material slots on `V11_TERRAIN_NEAR`, `V11_TERRAIN_FAR`, and `V11_TERRAIN_EXTENSION` based on the actual spatial zones:
       - **Forest-stand polygons** (triangles under the forest canopy footprint / within `3.0 m` of forest trunks): assign the owned **dark brown needle/soil forest-floor material** (`MAT_V18_FOREST_FLOOR`, using packed `forrest_ground_01_diff_2k.jpg` + normal + roughness, with an active `ShaderNodeTexImage` and dark earthy brown `diffuse_color = (0.11, 0.085, 0.055, 1.0)`), and under broadleaf clusters assign `MAT_V18_BROADLEAF_LITTER` (`leaves_forest_ground_diff_2k.jpg`, `diffuse_color = (0.16, 0.11, 0.06, 1.0)`).
       - **Open meadow polygons**: use the multi-tone ecological meadow material (`diffuse_color = (0.16, 0.21, 0.075, 1.0)` with active grass image texture).
       - **Enclosed garden lawn polygons**: use the mown garden lawn material (`diffuse_color = (0.18, 0.24, 0.085, 1.0)` with active grass image texture).
       - **Trail shoulder / verge polygons**: use the earthy loam/shoulder material (`diffuse_color = (0.19, 0.16, 0.11, 1.0)`).
     - That way, even in fast 3D viewport Solid/Texture and Material Preview modes (without evaluating heavy procedural shader math), the forest stands on a dark earthy needle/litter forest floor, the trail has textured gravel and soil shoulders, and the meadow and garden are distinct!
     - In `V17 | 3D scéna` workspace 3D viewports, enable `space.shading.show_cavity = True` (`cavity_type = 'BOTH'`, `ridge_factor = 0.6`, `valley_factor = 0.6`) so 3D crown and terrain depth are immediately readable when orbiting.

### 3. Genuinely separate and lighten `blender/kysucka_chata_exterier.blend` and `blender/kysucka_chata_interier.blend`

- **Why `01/02` failed to reduce file size:** In `01/02`, both files kept all `5,371` objects (`716 MiB`) because you checked `ID.users` while collections were still linked to `scene.collection`.
- **Required pruning procedure (preserving `model/shared_envelope_v18.json` digest `8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50` in BOTH files):**
  1. **In BOTH `kysucka_chata_exterier.blend` and `kysucka_chata_interier.blend`:**
     - Unlink and remove `90_VEGETATION_PROXY` (263 obsolete S00 proxy objects), the 61 hidden predecessors inside `50_INTERIOR_PROXY` (retaining the 12 active `PARTITION_proposed` meshes), and all hidden/superseded historical objects and unused off-scene master collections from `95_LANDSCAPE_V04`, `96_SITE_V05`, `97_VEGETATION_V06`, `98_VEGETATION_V08`, `99_NATURE_STUDY_V09`, and `V07_ROOT` that are not referenced by any active render object or active `IsViewport` node group.
  2. **In `blender/kysucka_chata_exterier.blend` additionally:**
     - Keep all 289 shared-envelope meshes (`model/shared_envelope_v18.json`) and the architectural/furniture/lighting elements of `55_INTERIOR_V10` that contribute through the glazing (`V10_FLOOR_oak`, `V10_CEILING_*`, `V10_WALL_plaster`, `V10_FIREPLACE_*`, `V10_GALLERY_slab/railing/edge_*`, `V10_STAIR_*`, `V10_UNDERSTAIR_CABINET`, `V10_KITCHEN_BASE/TALL/WALL`, `V10_DINING_TABLE`, `V10_DINING_CHAIR_1..6`, `V10_SOFA*`, `V10_ARMCHAIR`, `V10_COFFEE_TABLE`, `V10_SIDE_TABLE`, `V10_RUG_LIVING`, `V10_GALLERY_ARMCHAIR/OTTOMAN/RUG/SHELF/LAMP`, `V10_WALL_SHELF`, `V10_SHELF_FRAME`, `V10_PENDANT`, `V10_ARC_LAMP`, `V10_SPOT_fixtures`, and active lights).
     - Remove the tiny high-poly interior prop objects (`V10_SHELF_BOOKS_*`, `V10_GALLERY_SHELF_BOOKS_*`, `V10_DECOR_*`, `V10_KITCHEN_POT_*`, `V10_KITCHEN_VASE`, `V10_DINING_BOWL/BRANCHES/CANDLE_*`, `V10_HEARTH_BASKET_*`, `V10_HEARTH_LANTERN_*`, `V10_PICTURE_*`, `V10_PLANT_LIVING_*`, `V10_GALLERY_PLANT_*`, `V10_SHELF_PLANT_*`, `V10_SHELF_VASE_*`) and clear fake users on their unused 4K prop textures/meshes before running `bpy.data.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)`.
  3. **In `blender/kysucka_chata_interier.blend` additionally:**
     - Keep full `55_INTERIOR_V10` (all 151 objects and 138 interior textures), `56_BASEMENT_V18` (with `V18 | Podklad pre pivnicu`), the 12 active `PARTITION_proposed` meshes, all 289 shared-envelope objects (`model/shared_envelope_v18.json`), garden/fence/gate/orchard/trail, `V11_TERRAIN_NEAR` + `V11_TERRAIN_FAR`, and near-valley vegetation/forest within window view; remove `V11_TERRAIN_EXTENSION` and distant hill-forest chunks outside window sightlines, then run `bpy.data.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)`.
  4. Re-verify both files in `/tmp/opencode/v18_verify/` using `bwrap --unshare-net` with `R` masked (zero libraries, zero linked IDs, all reachable images packed, identical `model/shared_envelope_v18.json` digest `8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50`).

### 4. Fix the forest-margin understory, broadleaf trunk bases, and ~5% half-height juvenile cohort in Cycles and 3D

- **Why `after-forest.png` and `after-root.png` failed:**
  - In `after-forest.png`, `V17_GROUND_COVER_POINTS` had `0.42–1.60 m` spacing at `~100 m` from `CAM_V11_VALLEY_REVIEW`, leaving 90% of the slope in `CAM_V18_FOREST_MARGIN` as bare smooth green plastic with isolated tufts, a stark white birch pole sticking directly into bare green ground, and 176 primitive procedural geometric polygons ("twigs and moss") in `after-root.png`.
- **Required fix across the right-valley sector AND the Stage 3 readable forest margins:**
  1. **Delete the 176 primitive geometric twig/moss mesh pieces from `01/02`.** Do not place artificial low-poly sticks or green polygon pads on the ground.
  2. **Dense continuous 3D ground cover and ecotone transition at the forest margin:**
     - Across the right-valley witness sector (visible in `CAM_V18_FOREST_MARGIN` and `after-right.png`) and along the readable forest-to-meadow margins, add a dense 3D ecotone ground-cover cloud (`0.18–0.24 m` spacing in the `CAM_V18_FOREST_MARGIN` foreground/midground `[0..35 m]` from `CAM_V18_FOREST_MARGIN`, feathering to `0.35 m` along the readable margins) using existing instanced 3D meadow grass tufts (`V16_MASTER_MEADOW_RENDER` / `V17_GROUND_COVER_RENDER`), `grass_medium_01`, `shrub_01`, and `periwinkle_plant` ground clusters so **zero bare smooth green terrain** is exposed between tufts!
     - Around the base of every visible margin broadleaf (beech and birch) and focal adult spruce, place an irregular cluster of `shrub_01` (`0.30–0.55 m` tall), `grass_medium_01`, and young spruce seedlings (`0.60–1.40 m` tall) over the `Leaves Forest Ground` / `Forest Ground 01` substrate so no birch or beech trunk ever sticks out of bare smooth grass like a pole!
  3. **Full Stage 3 ~1-in-20 (~5%) half-height juvenile spruce cohort:**
     - Across the complete active forest population in `kysucka_chata_exterier.blend`, ensure approximately **1 in 20 active forest render instances (`5.0%`, e.g., `468` of `9,361` or exact `5.0%` of the reshaped basin forest population)** belong to the half-height juvenile cohort (ratio `0.45–0.55` of the comparable local adult tree height, using the fuller lower-whorl juvenile spruce mesh whose lowest branches reach down close to the ground/undergrowth), grouped naturally in 2–4 tree clusters along the sunlit forest margins and stand gaps.
     - Record in `work/v18/stage3/cohort.csv` and `release.json` the total active forest render instances, the exact count and percentage of the half-height cohort, and the height ratios of each juvenile tree to its adult comparator.

## Repository gate and exact baseline

Working directory: `R = /home/agile/Projects/kysucka_moderna_chata`
Trace directory: `T = /home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18`
Exact baseline: `78534bd46020bb2bfc97eef69b05e583cba5a5e5` on `main`

Immutable input hashes (verify before and after execution):
- `work/v17/complete_3d/kysucka_chata_v17_komplet_3d.blend`: `8a733770f3f4b96922dce76d662e81b281d2047affee5adceac849fb8948113e`
- `work/v17/nature_detail_01/checkpoints/candidate_exterior_v17.blend`: `f2e0942b63c25ec813b64ad483ea535d4a44b5e0c3a9f6dcfc0eebf7cb3ec4be`
- `work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend`: `5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1`
- `reference/01.png`: `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d`
- `work/v12/profile_03/isolated_config/userpref.blend`: `d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561`
- `/home/agile/.config/blender/5.3/config/userpref.blend`: `8c52b5cf0d5ac23a35c9496e442a37c69399203b47b32842dd76d05653c29c02`

Mandatory reading: governing WORKER spine (`.ap/AP.md`, `.ap/AP_WORKER.md`, `.ap/PROMPT_CONTRACTS.md`); `AGENTS.md`; `T/00_handout.md`; `T/00_notes.md`; `T/01_report_00.md`; and `T/01_report_01.md`.

## Execution route and resource/process guards

Canonical execution route: **isolated native Blender 5.3.0 CLI route** (`/home/agile/Applications/Blender/blender --background --disable-autoexec --threads 4`), serialized one child at a time with `nice -n 10`, isolated MCP-disabled preferences (`work/v12/profile_03/isolated_config/userpref.blend`), `PYTHONPYCACHEPREFIX` in the job's runtime directory, `PYTHONDONTWRITEBYTECODE=1`, and `sys.dont_write_bytecode = True`.
- Note: Michal currently has a live Blender GUI process (`PID 104220`) running on the machine. **Never signal, touch, or interfere with `PID 104220` or any owner GUI process.** Build and verify the updated files in `work/v18/stage3/` first, and promote them atomically (`os.replace` / copy via temporary file in `blender/`) to `blender/kysucka_chata_exterier.blend` and `blender/kysucka_chata_interier.blend` only after all Stage 3 checks pass.
- Resource guards: verify available RAM ≥10 GiB before each child launch; stop your own child if own RSS >9 GiB or available RAM <4.5 GiB on two consecutive samples; 360 s watchdog for 960×540 / build jobs and 900 s for high-detail jobs.

## Authority and mutation axes

Changed-path allowlist:
- `blender/kysucka_chata_exterier.blend`
- `blender/kysucka_chata_interier.blend`
- `model/shared_envelope_v18.json`
- `model/parameters.json` (only updating `forest_realism_v18`; all 20 prior top-level keys unchanged)
- `scripts/v18_split_forest.py`
- `assets/ASSET_MANIFEST.md`
- `work/v18/stage1/**` (updating Stage 1 portability/size receipts if needed while preserving the basement handoff package)
- `work/v18/stage2/**`
- `work/v18/stage3/{before.blend,candidate.blend,interier.blend,release.json,cohort.csv,connector.csv,trail_stations.csv,resources.json,overhead.svg}`
- `work/v18/stage3/{before,after}-{wide,right,forest,root,trail,hills}.png`
- `work/v18/stage3/viewport-{overview_se,overview_nw,overview_cottage}.png` (3 high-angle 3D overview renders matching Michal's 3 screenshot angles, rendered using the **viewport (`IsViewport=True`) tree/terrain representation** or OpenGL/Workbench/Cycles-viewport-branch evaluation to prove that the 3D scene has zero bare green table, zero keyhole ring, real 3D tree crowns, dark forest-floor soil under the forest, and a continuous trail to the north boundary!)
- Temporary sandbox directory `/tmp/opencode/v18_verify/**` (must be completely removed after readback before submitting the report)
- Direct-write terminal report `/home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/01_report_02.md`

Negative authority: no modification of `work/v17/**`, `work/v16/**`, `work/v10/**`, or any existing `blender/kysucka_chata_mcp_*.blend` / `kysucka_chata_seed.blend` file; no live MCP calls (`tools.blender.*` prohibited); no touching owner GUI `PID 104220` or global preferences; no network calls needed (all Stage 0 raw assets are already cached and verified under `work/v18/stage0/raw/` and `assets/`); no Git stage, commit, or push; and never emit the project closure signal.

Repository mutation: `blender/kysucka_chata_exterier.blend`, `blender/kysucka_chata_interier.blend`, `model/shared_envelope_v18.json`, `model/parameters.json`, `scripts/v18_split_forest.py`, `assets/ASSET_MANIFEST.md`, and untracked `work/v18/{stage1,stage2,stage3}/**` in the Changed-path allowlist
Host/remote mutation: temporary `/tmp/opencode/v18_verify` sandbox directory for isolated headless Blender 5.3.0 `bwrap --unshare-net` verification only (must be removed before report; zero persistent host change)
Trace persistence: direct-write `/home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/01_report_02.md`

External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 18-split-and-forest-realism-v18
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_correction_02.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18
Report filename: 01_report_02.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

## Validation and required evidence

Evidence tier: E2
Evidence tier basis: bounded correction of 3D exterior spatial layout, viewport proxy models, scene-split pruning, forest-margin understory, and Stage 3 full-margin + north trail continuation with offline sandbox verification
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: `bwrap --unshare-net` masked-root offline cold-open portability, shared-envelope digest (`87288303...`), second-apply idempotence, triangle-evaluated root support, and trail walking-corridor clearance
Affected tests: Stage 3 matched renders (`{before,after}-{wide,right,forest,root,trail,hills}.png`) and 3D overview witnesses (`viewport-{overview_se,overview_nw,overview_cottage}.png`)
New causal regression: 3D basin extent/coverage check (proving zero bare outer green table and zero `foreground_sides` keyhole corral across `[-320, 340] × [-220, 340] m`), real 3D viewport proxy triangle-count check (`≥ 5,000` tris/prototype for conifers and broadleaves, zero 156/214-triangle `V17 PREVIEW` cones/balloons), and continuous supported gravel trail from gate (`s = 0`) through `[42, 138.25]` to the actual north terrain perimeter (`Y = 340.0 m`)
Broad or full suite: not-used
Runtime or testbed: isolated headless Blender 5.3.0 CLI with MCP-disabled preferences and `bwrap --unshare-net`
Independent acceptance: not-required

Acceptance and Correction Record:
Acceptance candidate: `work/v18/stage2/candidate.blend` (`5b9985f966765f61bb64e3de9bcfc477919e8332fbe93f1ee4798c544b20145b`) and `blender/kysucka_chata_exterier.blend` (`c1f59ecee56499552f88cf86e0c891e8215e6015415f63cb33e6f6336d08085f`) from exchange `01/02`
Acceptance owner map: `T/00_handout.md` and `T/00_notes.md`
Acceptance allowlist: Changed-path allowlist above
Acceptance risk claims: 360° 3D valley basin without bare outer green board or `foreground_sides` keyhole ring; real 3D branch/crown viewport models and dark forest-floor soil under forest stands; genuinely pruned standalone exterior/interior `.blend` files with identical 289-object shared envelope; dense 3D forest-margin understory with ~5% half-height juvenile spruces; continuous gravel trail to the actual northern boundary
Acceptance control matrix: positive controls = `after-{wide,right,forest,root,trail,hills}.png`, `viewport-{overview_se,overview_nw,overview_cottage}.png`, `bwrap --unshare-net` cold open, shared-envelope digest `87288303...`, `cohort.csv`, `connector.csv`; negative controls = zero `V17 PREVIEW` 156/214-tri cone/balloon objects, zero primitive geometric twig/moss objects, zero floating vegetation outside `[-320, 340] × [-220, 340] m`, zero untouched-input hash drift
Acceptance independence: not-required
Primary fresh acceptances used: 0
Automatic corrections used: 1
Correction re-acceptance: scoped
Named missing-evidence probe: none
Out-of-scope observations: none

Stopping conditions: failed repository/input SHA-256 gate; interference with owner GUI `PID 104220`; own RSS >9 GiB or available RAM <4.5 GiB; offline portability or shared-envelope digest mismatch; support/clearance/idempotence failure; `/tmp/opencode/v18_verify` cleanup failure. If the same visual/spatial defects survive this correction, return `PARTIAL` or `BLOCKED` with `Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`.

Completion and report contract: begin `01_report_02.md` on line 1 with `### Report for ORCHESTRATOR_CHAT`; echo the coordinates (`kysucka-moderna-chata-split-and-forest-realism-v18`, `01`, `03`) once; include the compact core (`Status: PASS | PARTIAL | BLOCKED`, `Phase-qualified result: implementation-PASS | not-applicable`, `Start commit` / `End commit`, complete changed/created files and SHA-256 table including the updated `blender/kysucka_chata_exterier.blend` and `blender/kysucka_chata_interier.blend` with their reduced file sizes and object/image counts, `scripts/v18_split_forest.py`, and all Stage 3 renders and `viewport-overview_*.png` proofs, validation summary with wall times, peak RSS, minimum available RAM, 360° basin forest coverage, ~5% half-height juvenile spruce statistics, and full trail coordinates to `Y = 340.0 m`, Git result = no writes, deviations/risks, one smallest next step, `Report justification: new-mutation`, authority-expiry statement, `Orchestration critique` `MEASURED` / `LEAD`, `Resolved Execution Issues / Near-Misses`, and `Pre-Existing Failure Classification`). Set `Logical-whole closure: not-closed`. Write `T/01_report_02.md` directly and read it back completely before returning your short completion notice.

Authority expiry: this terminal report, cancellation, or supersession ends this grant; retained context is convenience, not continuing authority.

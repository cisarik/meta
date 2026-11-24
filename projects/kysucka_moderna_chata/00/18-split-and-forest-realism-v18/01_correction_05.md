# V18 RTX-3080 live-viewport and meadow/forest refinement (01/06) — match `meadow.png` with 4K seamless valley terrain, full-3D viewport meadow grass/wildflowers/specimen trees, thinner forest (~4,800–5,400 trees), and 28k–48k-triangle multi-lobed 3D tree crowns

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-split-and-forest-realism-v18
Worker session ordinal: 01
Worker exchange ordinal: 06
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker (same-session continuation of 01/01–01/05)
Phase: implementation
Task identity: SPLIT-AND-FOREST-V18-RTX3080-LIVE-VIEWPORT-AND-MEADOW — refine the live Blender 3D viewport and Cycles scene against Cooperator reference `T/meadow.png`: eliminate jagged polygon-boundary steps with a 4096×4096 world-space valley terrain texture, enable full 3D meadow grass/wildflowers and freestanding specimen trees in the live viewport, thin the forest to ~4,800–5,400 well-spaced trees, and increase per-tree 3D crown detail to 28,000–48,000 triangles using multi-lobed photogrammetric/3D foliage clusters in both viewport and render
Delivery route: manual Cooperator delivery
Continuity anchor: terminal report `01_report_04.md` (SHA-256 `431f0ceb1aafc685ba50a74367dea452d474ec20830eca4b0a587e82691dce0e`, Worker session 01 / exchange 05) and Cooperator live-viewport feedback (`report vygenerovany, ale live view v Blenderi treba doladit, les nemusi byt az tak husty radsej pridajme detailov na kazdy strom a hlavne luka nie je dobra chceme predsa len z 3080 RTX vymackat maximum`) with live Blender viewport screenshot and target reference `T/meadow.png` (SHA-256 `d81ee48d1552cd03e2f8afeff05b9f2c4dbbe653d492b6862a5068c02926b081`), reconciled in `00_notes.md` on 2026-11-24
Authority renewal: prior authority expired at `01_report_04.md`; this prompt grants complete new bounded authority at exchange `01/06` with `Native planning mode: not-used`. Retained context is convenience, not authority. Re-gate repository, input hashes, and process state yourself; stop on any conflict between retained context and current repository evidence.
Evidence posture: non-independent
Implementation authority: explicit
Independence required: no
Reasoning recommendation: High — named risks: eliminating the jagged 4 m polygon-material staircase along the meadow border in Solid-Texture viewport via a unified 4096×4096 world-space terrain texture; removing viewport `Delete Geometry` decimation on meadow grass/flowers and adding foreground specimen trees/shrubs/violet-white-yellow wildflower drifts to match `T/meadow.png`; thinning the forest from 11,535 to ~4,800–5,400 trees while upgrading every tree prototype in the live viewport to 28,000–48,000 triangles of dense multi-lobed 3D foliage
Recommended context capacity: approximately 250k tokens

## Active Amended Expectation Record
Amendment record: active
Cooperator decision ownership: COOPERATOR
Cooperator decision evidence: exact COOPERATOR acceptance evidence `report vygenerovany, ale live view v Blenderi treba doladit, les nemusi byt az tak husty radsej pridajme detailov na kazdy strom a hlavne luka nie je dobra chceme predsa len z 3080 RTX vymackat maximum` with live viewport screenshot and target reference `T/meadow.png` (`d81ee48d1552cd03e2f8afeff05b9f2c4dbbe653d492b6862a5068c02926b081`) on 2026-11-24
Superseded expectation: 11,535 tightly packed forest trees (`2.2–2.8 m` spacing) using 7,058–7,308-triangle `_WORK` viewport meshes (`~960` tiny isolated diamond leaves on thick brown tube pipes), per-polygon material slot assignment between `V18 Meadow` and `MAT_V18_SPRING_ECOTONE` creating a jagged sawtooth staircase along the meadow edges in the live viewport, and 87.5%–97% viewport deletion (`Delete Geometry` via `v17_view_skip` / `Index % 8`) leaving the meadow bare and flat in the live 3D viewport
Amended expectation: leverage the workstation's `NVIDIA GeForce RTX 3080` (10 GiB VRAM) to make the live Blender 3D viewport (as well as Cycles) closely match `T/meadow.png`: (1) thin the forest population from 11,535 to **4,600–5,400 well-spaced trees** (`4.6–7.2 m` spacing, retaining the `5.0%` half-height juvenile cohort on the new total and increasing spring broadleaves to ~45–50% of the basin and ~60–65% of the visible valley slopes); (2) eliminate reduced `_WORK` tree and shrub meshes — bind `IsViewport = True` directly to the full high-detail render masters and upgrade the 4 Spring Broadleaf masters to **28,000–48,000 triangles each** and the 4 Spring Shrub masters to **8,000–14,000 triangles each** built from dense, volumetric, multi-lobed 3D foliage domes (combining multiple transformed 3D foliage-cluster lobes from `V04_ORCHARD` with dense outer leaf layers and a 2048×2048 sunlit-to-shaded spring crown texture atlas so crowns read as lush, bright spring-green 3D domes in Solid-Texture viewport and Cycles); (3) replace per-polygon meadow/ecotone material switching with **one unified 4096×4096 world-space valley terrain texture (`V18_VALLEY_TERRAIN_4K.png`, ~16 cm/pixel)** across all top polygons of `V11_TERRAIN_NEAR`, `V11_TERRAIN_FAR`, and `V11_TERRAIN_EXTENSION` so the jagged sawtooth triangle staircase completely disappears in the live viewport and golden-green sunlit meadow swaths, mossy tree/shrub shadow halos, and forest-floor transitions are 100% smooth; and (4) enrich the meadow in both live viewport and Cycles to match `T/meadow.png` — remove the `Delete Geometry` viewport skipping on meadow grass/flowers inside the valley meadow so full 3D grass tufts (`V16_MASTER_MEADOW_RENDER` / `V04_MASTER_GRASS_MEDIUM_01_*`), tall golden-green grass panicles, 4,500–7,000 spring wildflowers (violet-purple meadow sage/knapweed, white daisies/umbels, yellow buttercups/dandelions), scattered meadow bush clumps, and **3 picturesque freestanding specimen broadleaf trees in the open meadow** (left foreground `~[29, -18]`, right foreground `~[36, 5]`, and right trail-bend `~[10, 29]`) are fully visible in the live 3D viewport
Amendment boundary: V18-RTX3080-LIVE-VIEWPORT-AND-MEADOW-REALISM
Cooperator decision authority effect: decision-only-no-worker-mutation-authority
Orchestrator superseded-expectation record: recorded by ORCHESTRATOR under V18-RTX3080-LIVE-VIEWPORT-AND-MEADOW-REALISM
Orchestrator authority issuance: issued by ORCHESTRATOR to Worker session 01 / exchange 06 for V18-RTX3080-LIVE-VIEWPORT-AND-MEADOW-REALISM only
Renewed task boundary: V18-RTX3080-LIVE-VIEWPORT-AND-MEADOW-REALISM only
Worker recipient: Worker session 01 / exchange 06
Worker implementation: pending in exchange 01/06
Worker validation: pending in exchange 01/06
Role sequence: COOPERATOR-decision -> ORCHESTRATOR-record -> ORCHESTRATOR-issuance -> WORKER-implementation -> WORKER-validation
Superseded expectation reported as failure: no
Unrelated scope change: none
Rendered acceptance ownership: COOPERATOR
## End Active Amended Expectation Record

## First mandatory action: inspect `T/meadow.png` vs current `viewport-overview_cottage.png`

Read and visually inspect `/home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/meadow.png` (`d81ee48d1552cd03e2f8afeff05b9f2c4dbbe653d492b6862a5068c02926b081`) alongside `work/v18/stage3/viewport-overview_cottage.png` and `work/v18/stage3/viewport-broadleaf_closeup.png`.
Observe the four exact visual differences that Michal pointed out:

### 1. Eliminate the Jagged Sawtooth Triangle Staircase and Flat Green Floor on the Meadow (`4096 × 4096` World-Space Valley Terrain Atlas)

- **Why the live viewport screenshot had a jagged sawtooth meadow border:**
  In `spring_soil()` (`scripts/v18_split_forest.py` lines 3698–3715), you assigned `material_index` per polygon (`V18 Meadow` vs `MAT_V18_SPRING_ECOTONE` vs `MAT_V18_FOREST_FLOOR`) on `V11_TERRAIN_NEAR`, `V11_TERRAIN_FAR`, and `V11_TERRAIN_EXTENSION`. Because those terrain triangles are `2.5–4.5 m` wide, switching materials per triangle created a harsh, jagged sawtooth staircase along both edges of the meadow in the live Blender viewport!
- **Required fix:**
  1. Assign **one single unified terrain material (`MAT_V18_VALLEY_TERRAIN_4K`)** to ALL top polygons (`~V05_shell`) of `V11_TERRAIN_NEAR`, `V11_TERRAIN_FAR`, and `V11_TERRAIN_EXTENSION`.
  2. Create a normalized world-XY UV layer `V18_WORLD_UV` (`u = (x - (-320.0)) / 660.0`, `v = (y - (-220.0)) / 560.0`) and set it as `mesh.uv_layers.active` on all three terrain meshes.
  3. Generate and pack a **4096 × 4096 pixel high-resolution RGB terrain texture (`V18_VALLEY_TERRAIN_4K.png`, `~16 cm` per pixel)** and bind it to an active `ShaderNodeTexImage` (`nodes.active = tex`, using `UVMap = 'V18_WORLD_UV'`) in `MAT_V18_VALLEY_TERRAIN_4K` (for Solid-Texture viewport) AND wire it into `Principled BSDF Base Color` (combined with multi-scale world-position bump/normal from `Grass005` / `forrest_ground_01` for Material Preview and Cycles).
  4. Synthesize `V18_VALLEY_TERRAIN_4K.png` by tiling and blending the actual high-frequency RGB detail of `Grass005_1K-JPG_Color.jpg`, `forrest_ground_01_diff_2k.jpg`, and `leaves_forest_ground_diff_2k.jpg` at true metric scale across the `4096 × 4096` grid with smooth continuous spatial masks (zero polygon-edge steps!):
     - **Open valley meadow (`forest_field < -3 m`):** rich, natural spring meadow color variation matching `T/meadow.png` — warm sunlit golden-green grass swaths (`sRGB` `(0.52, 0.60, 0.22)` to `(0.58, 0.62, 0.26)`), lush spring emerald-green swaths (`sRGB` `(0.35, 0.50, 0.16)`), and subtle darker green moisture/shadow contours following the terrain undulations.
     - **Mown garden lawn inside the fence polygon:** neat fresh spring lawn (`sRGB` `(0.38, 0.53, 0.18)`), smoothly feathered across `0.6 m` at the fence line.
     - **Trail verge / country double-track transition (`distance_to_trail < 2.2 m`):** warm earthy loam/grass blend (`sRGB` `(0.44, 0.42, 0.26)`).
     - **Soft mossy shadow halos (`radius 1.2..1.45 × crown_radius`) under every meadow specimen tree, shrub group, and across the forest-to-meadow ecotone (`forest_field ∈ [-6 m, +10 m]`):** smooth mossy olive-green (`sRGB` `(0.24, 0.36, 0.11)`), completely eliminating the sawtooth polygon border!
     - **Deep forest interior (`forest_field > +10 m`):** natural blend of `forrest_ground_01` needle soil and `leaves_forest_ground` leaf litter (`sRGB` `(0.22, 0.18, 0.12)` to `(0.28, 0.24, 0.15)`).

### 2. Transform the Meadow in the Live 3D Viewport (`IsViewport = True`) and Cycles to Match `T/meadow.png`

- **Why the meadow looked bare and flat in Michal's live Blender viewport screenshot:**
  1. `V17_GROUND_COVER_IsViewport` had `Delete Geometry` (`v17_view_skip`) deleting **96.9% of the 219,626 grass points in the viewport** and replacing the rest with 6-triangle green slivers (`V17_GROUND_COVER_WORK`)!
  2. `V16_MEADOW_IsViewport`, `V12_WRAP_V11_CORE_LAWN_GN`, and `V12_WRAP_V11_CORE_MEADOW_GN` had `Delete Geometry` (`Index % 8`) deleting **87.5% of the meadow tufts in the viewport** and replacing the rest with untextured monochrome green 64-triangle proxies!
  3. The open meadow in front of and around the cottage had zero freestanding specimen trees and almost no visible 3D bushes or tall golden grass/wildflower structure in the live viewport.
- **Required fix (unleashing the RTX 3080 in the live viewport):**
  1. **Add the picturesque freestanding meadow specimen trees and scattered meadow shrub groups matching `T/meadow.png`:**
     - Place **3 prominent, full-crowned freestanding spring broadleaf specimen trees** in the open meadow (with verified terrain triangle root seating, clear of the cottage sightline and trail):
       - **Left-foreground spreading meadow tree** at `(X = 29.5, Y = -18.5)` (`height ≈ 7.2 m`, broad spreading dome `width ≈ 6.8 m`, using the lush multi-lobed Spring Oak/Beech/Apple crown),
       - **Right-foreground medium rounded meadow tree** at `(X = 36.5, Y = 5.0)` (`height ≈ 5.3 m`, `width ≈ 4.8 m`),
       - **Mid-valley right trail-bend broadleaf specimen** at `(X = 10.5, Y = 29.0)` (`height ≈ 6.8 m`, `width ≈ 5.6 m`),
       - Plus **4–6 smaller freestanding young broadleaf/blossoming trees (`3.2–5.2 m` tall)** along the upper meadow pockets (`Y = 55..135 m`) and outer foreground flanks (`X = 42..54 m, Y = -35..20 m`) just like in `T/meadow.png`!
     - Place **45–70 scattered low meadow bush & shrub clusters (`0.7–2.1 m` tall)** across the meadow edges, near the bases of the freestanding meadow trees, along the outer curve of the front trail loop (outside the clear corridor), and in natural clumps breaking up the open meadow floor.
  2. **Enable rich 3D meadow grass, tall golden-green grass panicles, and wildflowers directly in the live 3D viewport (`IsViewport = True`):**
     - In `V16_MEADOW_IsViewport`, `V12_WRAP_V11_CORE_LAWN_GN`, `V12_WRAP_V11_CORE_MEADOW_GN`, `V16_SHOULDER_IsViewport`, `V17_TRAIL_EDGE_IsViewport`, `V17_BOTANICAL_IsViewport`, and `V18_SPRING_FLOWERS_IsViewport`: **remove the `Delete Geometry` node on the `IsViewport = True` branch and wire `IsViewport = True` directly to the full-detail render collections** (`V16_MASTER_MEADOW_RENDER`, `V09_MASTER_LAWN_RENDER`, `V09_MASTER_MEADOW_RENDER`, `V17_BOTANICAL_RENDER`, `V18_MASTER_SPRING_FLOWERS`), ensuring every grass/flower material has an active packed `ShaderNodeTexImage` with natural spring green / golden-green / blossom colors so Solid-Texture viewport renders them with rich color variation!
     - In `V17_GROUND_COVER_IsViewport` (`219,626` points): upgrade the collection instanced in the viewport to `V17_GROUND_COVER_RENDER` (35-triangle multi-blade 3D grass tufts with textured green/olive/golden-thatch materials instead of 6-triangle slivers) and keep **100% of points within `165 m` of the cottage/camera** (`Delete Geometry` disabled for all visible valley meadow points!), so the entire valley meadow has a dense, furry 3D grass carpet in the live Blender viewport!
     - **Enrich the meadow with 5,000–8,000 3D spring wildflowers and tall golden-green grass clumps (`V18_SPRING_FLOWERS` + `V18_MEADOW_TALL_GRASS`):**
       - Include **4 flower & tall-grass color families** matching the foreground and middle meadow of `T/meadow.png`:
         1. **Violet-purple meadow sage / knapweed clusters (`Salvia pratensis` / `Centaurea jacea`, `0.32–0.58 m` tall, rich violet-purple `sRGB` `(0.48, 0.28, 0.64)` and `(0.58, 0.36, 0.70)`)** — prominent in drifts across the lower/foreground meadow just like in `T/meadow.png`!
         2. **Creamy-white meadow umbels / yarrow / daisy clusters (`0.28–0.52 m` tall, `sRGB` `(0.93, 0.92, 0.85)`)**,
         3. **Golden-yellow buttercups and dandelions (`0.22–0.42 m` tall, `sRGB` `(0.92, 0.74, 0.10)`)**,
         4. **Tall golden-green flowering grass panicles & `V04_MASTER_GRASS_MEDIUM_01_0..2` clumps (`0.35–0.75 m` tall, warm sunlit golden-green `sRGB` `(0.54, 0.60, 0.24)`)** distributed in natural sweeping drifts across the open meadow so the meadow has rich 3D height and golden-green texture in both the live viewport and Cycles!

### 3. Thin the Forest (`~4,800–5,400` Trees) and Maximize Per-Tree 3D Crown Detail (`28,000–48,000` Triangles per Tree in Live Viewport & Render!)

- **Why the trees in `01/05` (`viewport-broadleaf_closeup.png` and Image 1) failed:**
  In `01/05`, `SpringPlantMesh` built each broadleaf tree from thick 7-sided brown tubes and only `~1,924` tiny individual diamond leaves (`~960` leaves in `_WORK`!), which left 85% of the crown empty and exposed a dark brown wire-brush skeleton of tubes, while `11,535` trees were packed `2.2–2.8 m` apart with dark olive/almost-black materials.
- **Required fix for Trees and Shrubs (maximizing RTX 3080 detail per tree):**
  1. **Thin the active forest population from `11,535` to `4,600–5,400` well-spaced trees:**
     - Increase minimum tree-to-tree spacing in the basin to `4.6–7.2 m` (while still covering all four outer perimeter bands `west, east, south, north` within `≤ 14 m` max nearest-tree distance so no bare outer board appears!).
     - Increase the **Spring Broadleaf share to `45%–52%` of the basin forest** (and `~60%–65%` on the lower and middle valley slopes facing the meadow, with Norway spruce mixing in at `~35%–40%` on the slopes and `~60%` on the higher ridges, matching `T/meadow.png`!).
     - Recompute the **`5.0%` half-height juvenile cohort** on the new total active tree count (`round(0.05 * total_active)`, e.g. `~250` trees at height ratio `0.45–0.55` of their adult comparator, recorded in `cohort.csv`).
  2. **Eliminate reduced `_WORK` meshes — use full high-detail 3D models (`28,000–48,000` triangles per broadleaf tree, `21,000–84,240` triangles per spruce, `8,000–14,000` triangles per shrub) in BOTH the live viewport (`IsViewport = True`) and Cycles:**
     - Wire both the `False` (render) and `True` (viewport) branches of `V12_WRAP_V11_FOREST_GN`, `V17_BROADLEAF_IsViewport`, `V18_FOREST_PILOT_IsViewport`, and `V18_SPRING_SHRUB_BELT_IsViewport` to the **exact same full-detail master collections** (or make `_WORK` objects share the exact high-detail `ob.data` meshes of `_RENDER`!).
  3. **Build dense, volumetric, multi-lobed 3D canopies (`28,000–48,000` triangles per broadleaf master; `8,000–14,000` triangles per shrub master) that look like `T/meadow.png`:**
     - Why does `V04_ORCHARD` (`scene().objects['V04_ORCHARD']`, `80,000` triangles) look like a real tree in the live viewport whereas `SpringPlantMesh` looked like brown sticks? Because `V04_ORCHARD`'s crown is a **dense 3D photogrammetric shell of continuous volumetric leaf clusters** (`~72,000` foliage triangles) where the inner branches are covered by lush 3D foliage lobes!
     - Construct the **4 Spring Broadleaf masters (`28,000–48,000` triangles each)** and **4 Spring Shrub masters (`8,000–14,000` triangles each)** by combining:
       - A natural tapering trunk and primary branch skeleton (with **hidden/thin terminal twigs `radius ≤ 1.2 cm`** that stay inside the foliage lobes, NEVER thick brown pipes sticking out of the crown!), AND
       - **14 to 24 overlapping, organically transformed (rotated/scaled/deformed) 3D volumetric foliage-cluster lobes extracted and decimated from `V04_ORCHARD`'s high-detail 3D foliage canopy (`z > 1.35 m` of `V04_ORCHARD`) supplemented by dense outer 3D leaf clusters**, arranged into distinct botanical crown silhouettes:
         - `V18_BROADLEAF_0_SPRING_BEECH` (`32,000–45,000` tris): broad, multi-domed spring beech/oak canopy (`height 11.0 m, width 7.6 m`),
         - `V18_BROADLEAF_1_SPRING_BIRCH` (`28,000–40,000` tris): taller, multi-stemmed airy spring birch/maple (`height 12.0 m, width 6.2 m`) with dappled white-and-charcoal birch trunk visible at the base and full 3D foliage lobes above `22%` height,
         - `V18_BROADLEAF_2_SPRING_CHERRY` (`30,000–44,000` tris): rounded spring wild cherry / meadow specimen tree (`height 8.2 m, width 6.8 m`) with fresh spring foliage and white-pink blossom clusters,
         - `V18_BROADLEAF_3_SPRING_ALDER` (`28,000–38,000` tris): low-branching, multi-lobed forest-edge broadleaf (`height 6.4 m, width 5.6 m`) reaching nearly to the ground.
     - **Bake a rich `2048 × 2048` Sunlit-Crown 3D Foliage Texture Atlas for each broadleaf, shrub, and conifer family:**
       - Map the UV coordinates of the 3D crown lobes so that **upper and outer sunlit crown surfaces sample bright, vibrant sunlit spring yellow-green (`sRGB` `(0.48, 0.65, 0.19)` to `(0.56, 0.71, 0.24)`)** with high-frequency photographic leaf detail (from `Apple_tree.jpg`), **mid-crown surfaces sample rich spring green (`sRGB` `(0.34, 0.51, 0.14)`)**, and **lower/inner recesses sample deeper shaded green (`sRGB` `(0.19, 0.32, 0.08)`)**!
       - Do the same for the **Norway spruce masters (`V11_MASTER_FOREST_RENDER` / `V12_WORK_FOREST`, upgraded to `21,000–45,000` triangles per prototype)**: brighten their needle texture and `diffuse_color` to a natural sunlit spring conifer green (`sRGB` `(0.28, 0.44, 0.14)` with `(0.42, 0.57, 0.20)` sunlit outer shoot tips) so conifers and broadleaves form one harmonious, sunlit spring forest in the live Blender Solid-Texture and Material Preview viewport!

## Repository gate and exact baseline

Working directory: `R = /home/agile/Projects/kysucka_moderna_chata`
Trace directory: `T = /home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18`
Exact baseline: `78534bd46020bb2bfc97eef69b05e583cba5a5e5` on `main`

Immutable input hashes (verify before and after execution):
- `work/v17/complete_3d/kysucka_chata_v17_komplet_3d.blend`: `8a733770f3f4b96922dce76d662e81b281d2047affee5adceac849fb8948113e`
- `work/v17/nature_detail_01/checkpoints/candidate_exterior_v17.blend`: `f2e0942b63c25ec813b64ad483ea535d4a44b5e0c3a9f6dcfc0eebf7cb3ec4be`
- `work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend`: `5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1`
- `reference/01.png`: `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d`
- `T/meadow.png`: `d81ee48d1552cd03e2f8afeff05b9f2c4dbbe653d492b6862a5068c02926b081`
- `work/v12/profile_03/isolated_config/userpref.blend`: `d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561`
- `/home/agile/.config/blender/5.3/config/userpref.blend`: `8c52b5cf0d5ac23a35c9496e442a37c69399203b47b32842dd76d05653c29c02`
- `T/01_report_04.md`: `431f0ceb1aafc685ba50a74367dea452d474ec20830eca4b0a587e82691dce0e`

## Execution route and resource/process guards

Canonical execution route: **isolated native Blender 5.3.0 CLI route** (`/home/agile/Applications/Blender/blender --background --disable-autoexec --threads 4`), serialized one child at a time with `nice -n 10`, isolated MCP-disabled preferences (`work/v12/profile_03/isolated_config/userpref.blend`), `PYTHONPYCACHEPREFIX` in the job's runtime directory, `PYTHONDONTWRITEBYTECODE=1`, and `sys.dont_write_bytecode = True`.
- **Protect Michal's live Blender GUI:** never signal, close, or touch any running owner GUI process. Build and verify in `work/v18/stage3/` and `/tmp/opencode/v18_verify/`, then promote atomically to `blender/kysucka_chata_exterier.blend` and `blender/kysucka_chata_interier.blend`.
- Resource guards: verify available RAM ≥10 GiB before each child launch; stop your own child if own RSS >9 GiB or available RAM <4.5 GiB on two consecutive samples; 360 s watchdog for 960×540 / build jobs and 900 s for detailed jobs.

## Authority and mutation axes

Changed-path allowlist:
- `blender/kysucka_chata_exterier.blend`
- `blender/kysucka_chata_interier.blend`
- `model/shared_envelope_v18.json`
- `model/parameters.json` (only updating `forest_realism_v18`; all 21 prior top-level keys unchanged)
- `scripts/v18_split_forest.py`
- `assets/ASSET_MANIFEST.md`
- `work/v18/stage3/{before.blend,candidate.blend,interier.blend,release.json,cohort.csv,connector.csv,trail_stations.csv,resources.json,overhead.svg}`
- `work/v18/stage3/{before,after}-{wide,right,forest,root,trail,hills}.png`
- `work/v18/stage3/viewport-{overview_se,overview_nw,overview_cottage,broadleaf_closeup,meadow_live}.png` (including `viewport-meadow_live.png` rendered in **Workbench Solid Texture mode from the exact camera angle of Michal's live screenshot / `T/meadow.png`** so we directly verify that the live Blender viewport has zero sawtooth polygon steps, lush multi-lobed 3D trees, freestanding meadow specimen trees, and a rich 3D spring meadow!)
- Temporary sandbox directory `/tmp/opencode/v18_verify/**` (must be completely removed after readback before submitting the report)
- Direct-write terminal report `/home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/01_report_05.md`

Negative authority: no modification of `work/v17/**`, `work/v16/**`, `work/v10/**`, `T/meadow.png`, or any existing `blender/kysucka_chata_mcp_*.blend` / `kysucka_chata_seed.blend` file; no live MCP calls (`tools.blender.*` prohibited); no touching any owner GUI process or global preferences; no network calls; no Git stage, commit, or push; and never emit the project closure signal.

Repository mutation: `blender/kysucka_chata_exterier.blend`, `blender/kysucka_chata_interier.blend`, `model/shared_envelope_v18.json`, `model/parameters.json`, `scripts/v18_split_forest.py`, `assets/ASSET_MANIFEST.md`, and untracked `work/v18/stage3/**` in the Changed-path allowlist
Host/remote mutation: temporary `/tmp/opencode/v18_verify` sandbox directory for isolated headless Blender 5.3.0 `bwrap --unshare-net` verification only (must be removed before report; zero persistent host change)
Trace persistence: direct-write `/home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/01_report_05.md`

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
Downloadable prompt filename: 01_correction_05.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18
Report filename: 01_report_05.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

## Validation and required evidence

Evidence tier: E2
Evidence tier basis: RTX-3080 live-viewport and Cycles visual refinement of valley terrain texture, 3D meadow grass/wildflowers/specimen trees, forest thinning, and high-detail multi-lobed 3D tree crowns with offline sandbox verification
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: `bwrap --unshare-net` masked-root offline cold-open portability, shared-envelope digest (`87288303...`), second-apply idempotence, triangle-evaluated root support, ~5% half-height juvenile cohort, and continuous north trail (`Y = 340.0 m`)
Affected tests: `after-{wide,right,forest,root,trail,hills}.png` and `viewport-{overview_se,overview_nw,overview_cottage,broadleaf_closeup,meadow_live}.png`
New causal regression:
1. **Zero polygon-staircase terrain gate:** all top faces of `V11_TERRAIN_NEAR`, `V11_TERRAIN_FAR`, and `V11_TERRAIN_EXTENSION` use the unified `4096 × 4096` packed world-space terrain texture (`V18_VALLEY_TERRAIN_4K.png`) with zero per-polygon meadow-to-ecotone material slot jumps.
2. **High-detail RTX-3080 viewport tree & shrub gate:** total active forest tree count is between `4,400` and `5,600` (with `5.0%` half-height juvenile cohort); every broadleaf prototype has `28,000–48,000` triangles in BOTH render and viewport (`IsViewport = True`), every conifer prototype has `≥ 21,000` triangles in BOTH render and viewport, and every shrub prototype has `8,000–14,000` triangles in BOTH render and viewport.
3. **Full-3D live-viewport meadow gate:** zero `Delete Geometry` point skipping on `V16_MEADOW_IsViewport`, `V12_WRAP_V11_CORE_LAWN_GN`, `V12_WRAP_V11_CORE_MEADOW_GN`, `V17_BOTANICAL_IsViewport`, `V18_SPRING_FLOWERS_IsViewport`, and the visible valley meadow of `V17_GROUND_COVER_IsViewport`; at least 3 freestanding meadow specimen broadleaf trees and ≥4,500 3D wildflower/tall-grass instances (including violet-purple, white, and yellow drifts) are active in the live viewport.
Broad or full suite: not-used
Runtime or testbed: isolated headless Blender 5.3.0 CLI with MCP-disabled preferences and `bwrap --unshare-net`
Independent acceptance: not-required

Completion and report contract: begin `01_report_05.md` on line 1 with `### Report for ORCHESTRATOR_CHAT`; echo the coordinates (`kysucka-moderna-chata-split-and-forest-realism-v18`, `01`, `06`) once; include the compact core (`Status: PASS | PARTIAL | BLOCKED`, `Phase-qualified result: implementation-PASS | not-applicable`, `Start commit` / `End commit`, complete changed/created files and SHA-256 table including the updated `blender/kysucka_chata_exterier.blend` and `blender/kysucka_chata_interier.blend`, `scripts/v18_split_forest.py`, and all updated renders including `viewport-meadow_live.png`, validation summary with 4K terrain texture verification, per-prototype viewport/render triangle counts, thinned forest & ~5% juvenile cohort statistics, freestanding meadow specimen tree & wildflower counts, and resource metrics, Git result = no writes, deviations/risks, one smallest next step, `Report justification: new-mutation`, authority-expiry statement, `Orchestration critique` `MEASURED` / `LEAD`, `Resolved Execution Issues / Near-Misses`, and `Pre-Existing Failure Classification`). Set `Logical-whole closure: not-closed`. Write `T/01_report_05.md` directly and read it back completely before returning your short completion notice.

Authority expiry: this terminal report, cancellation, or supersession ends this grant; retained context is convenience, not continuing authority.

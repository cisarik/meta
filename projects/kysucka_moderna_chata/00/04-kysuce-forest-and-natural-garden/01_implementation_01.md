# Implement Kysuce forest and natural garden environment pass (v04)

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-kysuce-forest-and-natural-garden
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker (operating as a current-session implementation continuation of the accepted plan)
Phase: implementation
Task identity: BLENDER-MCP-KYSUCE-FOREST-AND-NATURAL-GARDEN-IMPLEMENT
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — bounded implementation of one already-accepted environment plan with Cooperator-selected archives in /Users/agile/Downloads: asset acquisition and normalization, deterministic landscape source module, live Blender MCP scene application, semantic replay and matched renders
Recommended context capacity: approximately 250k tokens
Independence required: no

Continuity anchor: terminal PASS report `01_report_00.md` (SHA-256 `d119f1e3a2ca296bdb6d8d68e8903c00255ffb8d1533c650966610df4102c028`) for Worker exchange 01/01, accepted by the Orchestrator as the plan of record and reconciled with the Cooperator's downloaded Sketchfab archives and dense-forest requirement
Authority renewal: prior planning authority expired at the terminal planning report; this exchange grants a new, complete and bounded implementation authority for the accepted plan and Cooperator-selected archives only
Evidence posture: non-independent — this session produced the plan; the Orchestrator performs acceptance on the delivered renders, crops and replay receipts

## Implementation authority

Implementation authority: explicit
Exact baseline: `623d12abe0c0eb2742cd02c9962c1712b53437e2` (`feat: add PBR exterior timber and reposition foreground rustic fence in v03`) on `main`
Changed-path allowlist: see "Exact allowed paths" below
Implementation boundaries: see "Positive authority" / "Negative authority" below
Independence required: no

## Goal and accepted decisions

Turn the accepted `v03` working scene into `blender/kysucka_chata_mcp_v04.blend`: a coherent, realistic **Kysuce setting with rolling hills covered by a dense, tightly packed spruce forest extending from behind the cottage all the way to the left, right, and upper edges of the scene, nearby smaller spruces, an apple-bearing orchard tree in the left garden and natural front planting**, replacing the empty horizon and the geometric proxy vegetation, while keeping the selected camera, v03 timber/fence, building, openings, interior, chimney/fireplace, paving/steps/bollards, world/lights and glass unchanged.

Accepted decisions (do not redesign):
- Camera `CAM_A_REFERENCE` stays exactly at `location = [21.5, -10.0, 1.25]`, `target = [8.5, 2.5, 1.25]`, `lens = 35 mm`, `sensor_width = 36 mm`, `shift_x = 0.0`, `shift_y = 0.105`, `clip_end = 500.0`. Never move or re-aim it.
- `scripts/timber_fence_v03.py` and its settings are preserved; `apply_v03` is **not** re-run in the live scene.
- Shared deterministic module `scripts/landscape_v04.py` with `apply_v04(scene, P, ROOT)` and `configure_comparison_render(scene)`, invoked (a) live through Blender MCP on the open `v03` scene and (b) from `scripts/build_scene.py` immediately after `apply_v03`, before packing and saving. Isolated `random.Random(13704)` only; the global `random.getstate()` must be unchanged around `apply_v04`.
- Accepted layout, asset paths, seeds, densities, LODs and anchors live in `model/parameters.json` under a new `landscape_v04` section; camera, building and v03 parameters stay unchanged.
- `SITE_terrain_proxy` vertex positions and `BED_entry` geometry are preserved exactly; only new dedicated lawn/soil shader assignments on those two objects are authorized.
- The 263 superseded proxy objects (`SHRUB_proxy*` 19, `FLOWER_proxy*` 7, `TREE_trunk_proxy*` 38, `CONIFER_proxy*` 152, `APPLE_trunk_proxy` 1, `APPLE_branch_proxy*` 23, `APPLE_foliage_proxy*` 23) are hidden for viewport and render only; their data and the `90_VEGETATION_PROXY` collection are preserved, and no unrelated object is touched. All 393 non-vegetation objects are preserved.
- Render profile for every delivered image: `1448 × 1086` at `100 %`, Cycles CPU, 8 threads, `96` samples, OpenImageDenoise ON, frame `0`, seed `0`, `AgX`, look `None`, exposure `0.0`, gamma `1.0`, unchanged world and lights (`configure_comparison_render`).
- Budget: combined unique source geometry target below 1.5 M triangles, hard ceiling strictly below 3 M; every tracked file below `90 × 1024²` bytes; 1K maps for fruit, grass, flowers and distant foliage, 2K for orchard, near spruce and shrubs; no LFS, no new runtime, no per-instance material/image duplication, no destructive realization of the forest.
- One small asset board, at most two cheap composition previews, and one focused correction for an observed defect. One render job at a time; poll an existing job instead of re-submitting after a timeout.

## Accepted plan specifics & Cooperator-selected archives (`01_report_00.md` + Cooperator selection)

**1. Verified Sketchfab archives already present in `/Users/agile/Downloads/` (no missing files!):**
Michal has downloaded and selected the following exact Sketchfab CC-BY-4.0 archives in `/Users/agile/Downloads/`:
- **Orchard apple tree**: `/Users/agile/Downloads/blossoming-apple-tree.zip` (`88,293,821` B, SHA-256 `32ec7eeacfaa985a4f335fe34dc916158d1e4793582496ed7db5a85db260ed0b`) — Sketchfab UID `7df0631398f443379fa4541e9efc2343`, **Blossoming apple tree** by **Lassi Kaukonen** (`thesidekick`, `https://sketchfab.com/3d-models/blossoming-apple-tree-7df0631398f443379fa4541e9efc2343`), CC Attribution 4.0 (`https://creativecommons.org/licenses/by/4.0/`). Retain normalized library at `assets/models/sketchfab_7df0631398f443379fa4541e9efc2343/`.
- **Primary Norway spruce (`Picea abies` — near-garden spruces & forest edge/canopy)**: `/Users/agile/Downloads/realistic-hd-norway-spruce.zip` (`168,359,153` B, SHA-256 `4f634d5172a3a4b662c2faef666bca7e6234a92724306ab7a4e4802a03a25e95`) — Sketchfab UID `bf500546e2874f9ea086ba6abb11357e`, **Realistic HD Norway spruce (3/43)** (`Picea abies HD_Standard mat 50`, height `9.586 m`, width `4.05 m`) by **PlantCatalog** (`https://sketchfab.com/3d-models/realistic-hd-norway-spruce-343-bf500546e2874f9ea086ba6abb11357e`), CC Attribution 4.0. Retain normalized library at `assets/models/sketchfab_bf500546e2874f9ea086ba6abb11357e/`.
- **Dense-forest stand spruce (`Picea mariana` — Michal's explicit selection for tightly packed dense forest behind the cottage to the scene edges)**: `/Users/agile/Downloads/realistic-hd-black-spruce-1938.zip` (`165,128,196` B, SHA-256 `714b68f1a205b8686c29b1b42a43198a2f8a5be8deeca315bce7a41fe3fd643d`) — Sketchfab UID `3232c3022f2947b7999de0941ede5653`, **Realistic HD Black spruce (19/38)** (`Picea mariana HD_Forest mat 75`, height `11.224 m`, narrow `1.71 × 1.60 m` forest-stand habit) by **PlantCatalog** (`https://sketchfab.com/3d-models/realistic-hd-black-spruce-1938-3232c3022f2947b7999de0941ede5653`), CC Attribution 4.0. Retain normalized library at `assets/models/sketchfab_3232c3022f2947b7999de0941ede5653/`.
- *(Optional auxiliary low-poly spruce also present in `/Users/agile/Downloads/spruce-tree.zip`, SHA-256 `abdcb35464fd74536f677d223c66de6473ef6d40d151867b63a0fed82dcbaeb`, UID `7a5db417827244d98827459bce0cc944`, if desired for ultra-light distant under-canopy filler at `assets/models/sketchfab_7a5db417827244d98827459bce0cc944/`, rescaled from cm/mm `153,648` units to metres).*

**2. Poly Haven CC0 models via `https://api.polyhaven.com/files/<asset_id>`:**
Download only the returned `dl.polyhaven.org` files into `work/downloads/<asset_id>/`:
- `food_apple_01` (`food_apple_01_1k.blend`, 445545 B, MD5 `d319fcdce53e2c88946ae7079c219a0e`)
- `grass_medium_01` (`grass_medium_01_1k.blend`, 1832028 B, MD5 `e37f4fa4c90ddeb807ce6b4c09e3033d`)
- `shrub_01` (`shrub_01_1k.blend`, 6535174 B, MD5 `dfbacf2c8c64823862ec8b9747d7687e`)
- `periwinkle_plant` (`periwinkle_plant_1k.blend`, 1680482 B, MD5 `6920bf78874cc7b966c63e73f1a14ddb`)
Verify published MD5 and byte counts, compute SHA-256, verify staged bytes before import.

**3. Normalization (critical geometry findings from Orchestrator read-only inspection):**
In a separate Blender process with `--disable-autoexec`, stage extraction under `work/downloads/`, import only selected mesh components, and retain each asset as `assets/models/<asset_id>/master.blend`, `textures/<file>` and `LICENSE.txt` with metre dimensions, Z-up orientation, applied transforms and trunk/plant-base origins:
- **Orchard apple tree (`blossoming-apple-tree.zip` -> `assets/models/sketchfab_7df0631398f443379fa4541e9efc2343/`)**:
  - Contains `source/Apple_tree_SF.zip` with `Apple_tree_SF.obj` (`404,181` tris). After `bpy.ops.wm.obj_import`, its world bounding box is `x ∈ [-0.850, 0.842], y ∈ [-0.812, 0.539], z ∈ [-0.010, 1.184]`.
  - **Crucial photogrammetry ground-mound cleanup**: In `Apple_tree_SF.obj`, `world_z ∈ [-0.01, 0.175]` contains a `1.08 × 1.10 m` wide photogrammetry ground mound (`54,625` vertices), while `world_z ∈ [0.18, 0.39]` is the narrow trunk (`~0.13 m` diameter) and `world_z ∈ [0.39, 1.184]` is the branching crown (`1.69 × 1.21 m`). Prune the ground-mound skirt vertices (`world_z < 0.175` outside the trunk radius `r > 0.085 m` around the trunk axis), shift the trunk base down to `Z = 0.0` (with a small `-0.04 m` root embed), apply rotation and scale so the tree is `~4.0–4.3 m` tall (`scale ≈ 3.8–4.1`), decimate the static mesh to `~60k–90k` triangles, downscale the 8K JPEG textures (`Apple_tree.jpg`, `Apple_tree_normal.jpg`, `Apple_tree_occlusion.jpg`) to 2K (`2048 × 2048`) in `textures/`, grade the crown shader slightly toward natural leafy orchard green so it harmonizes with the summer garden while preserving bark/branch detail, and attach **24–32 linked `food_apple_01` instances** (`6–9 cm` diameter) onto the outer/lower-crown surfaces (`Z ≈ 1.7..3.7 m`) so red/blushed apples are clearly readable in the crown crop and full frame.
- **Norway spruce (`realistic-hd-norway-spruce.zip` -> `assets/models/sketchfab_bf500546e2874f9ea086ba6abb11357e/`)**:
  - Contains `source/Picea abies HD_Standard mat 50.zip` with Z-up FBX meshes (`9.586 m` tall, `4.05 m` wide, base at `Z = 0.0`).
  - Use `zzz_LODs/LOD2/Picea abies HD_Standard mat 50_LOD2.fbx` (`84,240` tris, with compact `LOD1`/`LOD2` PNG maps from `zzz_LODs/LOD1` or `LOD2`) as the high-detail master (`LOD0`), plus a decimated distant variant (`LOD1`, e.g. `~15k–25k` tris sharing the same materials/maps) AND a derived narrower young-spruce master (`XZ` crown width scaled by `0.72` relative to height, continuous leader and ground-reaching lower branches) for the near-garden young spruces.
  - Ensure all foliage material slots (`Picea fol *`) connect their `_a_LOD*_Transparency.png` map (`Non-Color`) to Principled BSDF `Alpha` (in PlantCatalog, the transparency PNG has white=opaque needles, black=cutout background; verify in the asset board render that needle cards have clean alpha cutouts and zero black borders!).
- **Black spruce for dense forest (`realistic-hd-black-spruce-1938.zip` -> `assets/models/sketchfab_3232c3022f2947b7999de0941ede5653/`)**:
  - Contains `source/Picea mariana HD_Forest mat 75.zip` with Z-up FBX meshes (`11.224 m` tall, narrow `1.71 × 1.60 m` crown designed for dense forest stands, base at `Z = 0.0`).
  - Use `zzz_LODs/LOD2/Picea mariana HD_Forest mat 75_LOD2.fbx` (`69,701` tris, with compact `LOD2` PNG maps from `zzz_LODs/LOD2/`) as `LOD0` and a decimated variant (`LOD1`, `~12k–20k` tris sharing the same materials/maps) for the dense background forest. Connect all `_a_LOD*_Transparency.png` maps to BSDF `Alpha` and verify in the asset board render that foliage (`Picea mariana fol 1` / `fol 2`) is graded to a healthy deep Kysuce spruce green (note: `fol_1_gray` is greyscale for tinting in PlantCatalog — multiply/grade it to natural deep conifer green `(0.06, 0.16, 0.05)` in the shader so the needles are lush dark spruce green, not grey!).

**4. Layout (incorporating Michal's dense-forest requirement `za chatou až po okraj scény husto pri sebe`):**
- New collection `95_LANDSCAPE_V04` with separate hills, forest, near-tree, orchard, planting and edge-grass groups.
- **Background hills (`LANDSCAPE_hills_v04_*`) spanning the full background width behind the cottage to the left and right edges of the scene (`u = -0.08..1.08`)**:
  - Build three smooth overlapping terrain layers using the Orchestrator-supplied crest anchors at nominal 70 m, 110 m and 160 m (`v ≈ 0.40 / 0.30 / 0.22` across `u = 0.00..0.65`) AND extend the hillside continuously behind the right roof and beyond the glazed gable (`u = 0.65..1.08`, rising to `v ≈ 0.28..0.55` behind the right side of the house, passing through and rising behind the right-side anchors `(13.03, 13.47, 2.80)` and `(6.16, 26.56, 6.58)` at `D = 45..120 m`). Smoothly join all hill feet to existing terrain without modifying `SITE_terrain_proxy`.
- **Dense, tightly packed spruce forest (`za chatou až po okraj scény husto pri sebe`)**:
  - Scatter **900–1,500 linked instances** combining **Black spruce (`Picea mariana HD_Forest mat 75`)** (`~65 %` of forest instances, packed tightly side-by-side with `2.2–4.0 m` spacing inside dense stands) and **Norway spruce (`Picea abies HD_Standard mat 50`)** (`~35 %` of forest instances along stand edges, ridges, and foreground slopes) across all three hill layers and the right-side hillside (`u = -0.05..1.05`, `v = 0.14..0.68` wherever not occluded by the cottage).
  - Keep trees densely packed (`husto pri sebe`) so the hills behind the cottage all the way to the left and right edges of the frame are covered by a rich, continuous, interlocking Kysuce spruce forest canopy, leaving only a few small, natural sub-ridge meadow glade strips (`~12–18 %` area) so the layered terrain topography remains readable as in `reference/kysucka_chata_moderna.png`. Ground every trunk on its owning hill surface and keep growth vertical (`Z-up`) with varied height (`7–13 m`) and random `Z` rotation.
- **Young spruces near the cottage (`4–5` trees, `1.8–3.2 m` height, base Z sampled from the supporting surface)**:
  - Left perimeter behind orchard/wood-bay: `(-8.0, 0.0)` (`2.1 m`, `u ≈ 0.044`) and `(-13.5, 4.5)` (`3.0 m`, `u ≈ 0.088` — shifted left from `(-10, 3)` so it stays cleanly left of the front-left roof eave corner at `u = 0.1202, v = 0.5730`).
  - Right perimeter beyond glazed gable (`gable_right_corner` is at `u = 0.9538`): `(13.0, 13.5)` (`2.3 m`, `base_z = 0.345 m`, `u ≈ 0.979`) and `(10.0, 22.0)` (`3.0 m`, `base_z = 2.947 m`, `u ≈ 0.982`).
- **Orchard apple tree in the left garden**:
  - Replace the proxies at `(-0.6, -3.0)` (or slightly adjusted `(-1.1, -2.6)` so the crown frames `u ≈ 0.00..0.14` cleanly to the left of the wood bay `u = 0.1665` with open sky above) with the normalized static `Blossoming apple tree` master (`~4.0–4.3 m` high) and its **24–32 attached `food_apple_01` instances** (`6–9 cm` diameter, stems within `2 cm` of supporting branches/twigs).
- **Front planting in `BED_entry` & lawn/fence edge grass tufts**:
  - Three irregular groups in `BED_entry` (`12–16` low `shrub_01` clumps, `20–28` airy `grass_medium_01` tufts, `10–14` `periwinkle_plant` accents) across `X ∈ [2.6, 6.35]`, `[9.35, 10.05]`, and `[12.55, 15.0]`, keeping `X = 6.5..9.2` (entry steps) and `X = 10.2..12.4` (bench) clear.
  - `~80–120` restrained `grass_medium_01` tufts along visible lawn and foreground fence edges, excluding paving and post bases.
  - Dedicated lawn and soil shaders assigned only to `SITE_terrain_proxy`, `LANDSCAPE_hills_v04_*`, and `BED_entry` (metre-scale colour variation, matte roughness, millimetre-scale bump).

**5. Instancing, performance budget, determinism, replay, and acceptance:**
- Append each normalized master library once; use collection instances or objects sharing mesh data, materials and images; keep master source collections outside the scene root (or hidden from viewport/render); never realize the forest.
- Combined unique source geometry target `< 1.5 M` triangles (hard ceiling `< 3.0 M`); every tracked file `< 90 × 1024²` bytes (`90 MiB`). Measure and record unique stored triangles, evaluated unique and instance-expanded triangles, instance/mesh/material/image counts, decoded texture-memory estimate, Blender process RSS before import, after scatter and during rendering, renderer-reported memory, sampled maximum RSS, preview and final wall time.
- Tag owned `v04` data, make `apply_v04(scene, P, ROOT)` idempotent on a second call, pack used textures once, and retain `//../assets/models/...` relative paths.
- Verify by separate MCP readback, cold CLI reopen (`--disable-autoexec`), and factory-startup source replay to `work/v04_source_replay.blend` using semantic tolerances (`≤ 1e-5 m` position/bounds, `≤ 1e-6 rad` rotation, `≤ 1e-6` scale/UV/shader values, exact names/counts/assignments/packed images, unchanged global RNG — **do not** gate on UI caches, binary `.blend` identity, or a cross-version default-RNA dump).
- Deliver matched `1448 × 1086` Cycles CPU 96-sample OIDN renders (`renders/before.png` reusing canonical v03 `3c77ef772bb5578aa54227df98615356cc301c9542fffe982071bed62b0d69d1` after verifying profile match, and `renders/after.png`), native-pixel crop sheet `renders/landscape_details.png` (ridge/dense forest, young spruce, orchard fruit/crown, front planting), `renders/render_metadata.json`, `evidence/landscape_comparison.md`, and `01_report_01.md`.

## Repository and environment prerequisites

Repository identity: `https://github.com/cisarik/kysucka_moderna_chata`
Working directory: `/Users/agile/Projects/kysucka_moderna_chata`
Repository checkout topology: standalone checkout
Expected branch: `main`
Expected HEAD: `623d12abe0c0eb2742cd02c9962c1712b53437e2`
Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `/Users/agile/Projects/kysucka_moderna_chata/.ap` (pinned submodule checkout; detached HEAD equal to gitlink accepted)
Trace repository: `https://github.com/cisarik/meta` at `/Users/agile/meta` (HEAD `a46e62d7a1876bc04e5af5e7c139d9a9f40d793f`)

Mandatory reading:
- `.ap/AP.md` (WORKER row of the Per-Role Minimum-Reading Spine; RF-03, RF-06, RF-12, RF-16, RF-18, RF-19; §8 Worker Responsibilities; §18 Stopping Conditions)
- `.ap/AP_WORKER.md` (`#worker-session-target`, `#reporting`)
- `.ap/PROMPT_CONTRACTS.md` (`#worker-report-header`, `#implementation-authority-record`, `#mutation-axes-record`, `#cooperator-delivery-and-trace-destination-record`, `#validation-ladder-record`)
- `AGENTS.md`, `docs/OPERATIONS.md`, `README_SK.md`, `assets/ASSET_MANIFEST.md`, `model/parameters.json`, `scripts/build_scene.py`, `scripts/timber_fence_v03.py`
- `/Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/01_closure.md`
- `/Users/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden/00_handout.md`, `00_notes.md` and the accepted plan `01_report_00.md`

Repository gate (re-check before any mutation): physical Git root `/Users/agile/Projects/kysucka_moderna_chata`, canonical origin `https://github.com/cisarik/kysucka_moderna_chata`, branch `main`, HEAD `623d12abe0c0eb2742cd02c9962c1712b53437e2`, clean index and worktree apart from the paths you are granted, `.ap` gitlink and checkout equal to `d7023cf037f6d17885c3ede5c04812c61640da50`, `./.ap/ap doctor` `PASS`, and the protected SHA-256 values of `blender/kysucka_chata_seed.blend`, `blender/kysucka_chata_mcp_v01.blend`, `blender/kysucka_chata_mcp_v02.blend`, `blender/kysucka_chata_mcp_v03.blend`, `model/parameters.json`, `scripts/build_scene.py`, `scripts/timber_fence_v03.py` and `reference/kysucka_chata_moderna.png`. Preserve unsaved GUI work: confirm via MCP that the live session still has `is_dirty == False` and the expected file path, and stop on conflict.

## Execution route and authority (AP RF-16)

Execution route: **task-specific bounded deviation `blender-mcp-live-v1`** under AP RF-16.
- Declared route not used alone: `blender-local-v1` in `AGENTS.md` and `docs/OPERATIONS.md` (headless CLI inspection), which cannot inspect or control the open Blender 5.2.3 LTS GUI session this whole requires.
- Activated route for this task: `blender-mcp-live-v1` — the session's Blender MCP tools (`get_addon_status`, `get_scene_info`, `execute_blender_code`, `look`) against the running Blender 5.2.3 LTS GUI, supplemented by read-only local Git/file/hash inspection and separate isolated Blender CLI processes for normalization and source replay.
- Evidence class: directly observed MCP tool receipts plus read-only repository/hash checks and separate-process CLI receipts.

External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 00/04-kysuce-forest-and-natural-garden
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_implementation_01.md
Destination path: /Users/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden
Report filename: 01_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: /Users/agile/Projects/kysucka_moderna_chata — scripts/landscape_v04.py, scripts/build_scene.py, model/parameters.json, assets/ASSET_MANIFEST.md, assets/models/**, blender/kysucka_chata_mcp_v04.blend, AGENTS.md, docs/OPERATIONS.md, README_SK.md
Host/remote mutation: local Blender 5.2.3 LTS GUI session via MCP (checkpoint, scene edits, renders, packing, saves) and local file system under /Users/agile/Projects/kysucka_moderna_chata/work/**; read-only network download from dl.polyhaven.org and api.polyhaven.com; read-only intake from /Users/agile/Downloads
Trace persistence: direct-write /Users/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden/renders/before.png, /Users/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden/renders/after.png, /Users/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden/renders/landscape_details.png, /Users/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden/renders/render_metadata.json, /Users/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden/evidence/landscape_comparison.md, /Users/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden/01_report_01.md, /Users/agile/meta/projects/kysucka_moderna_chata/00/00_RUN_MAP.md

### Exact allowed paths

Project repository (write):
```text
scripts/landscape_v04.py
scripts/build_scene.py
model/parameters.json
assets/ASSET_MANIFEST.md
assets/models/sketchfab_7df0631398f443379fa4541e9efc2343/**
assets/models/sketchfab_bf500546e2874f9ea086ba6abb11357e/**
assets/models/sketchfab_3232c3022f2947b7999de0941ede5653/**
assets/models/sketchfab_7a5db417827244d98827459bce0cc944/**
assets/models/food_apple_01/**
assets/models/grass_medium_01/**
assets/models/shrub_01/**
assets/models/periwinkle_plant/**
blender/kysucka_chata_mcp_v04.blend
AGENTS.md
docs/OPERATIONS.md
README_SK.md
```
Within each `assets/models/<asset_id>/` directory keep only `master.blend`, the selected `textures/` files and `LICENSE.txt`.

Project repository (temporary, gitignored `/work/`):
```text
work/mcp-v04-before.blend
work/v04_source_replay.blend
work/v04_verify.py
work/v04_*
work/downloads/**
```

Meta trace (write): the seven exact paths listed under `Trace persistence` above.

Everything else is out of scope, including `blender/kysucka_chata_seed.blend`, `blender/kysucka_chata_mcp_v01.blend`, `blender/kysucka_chata_mcp_v02.blend`, `blender/kysucka_chata_mcp_v03.blend`, `scripts/timber_fence_v03.py`, `scripts/design.py`, `reference/`, `cad/`, `docs/*.pdf`, `previews/`, `manifest/`, `tools/`, `.ap/` and the whole `Closure and Git gates` section plus the managed AP block in `AGENTS.md`.

### Positive authority

- Live Blender MCP control of the open `blender/kysucka_chata_mcp_v03.blend` session: checkpoint save, scene edits, material and object creation, texture packing, renders, and saving `blender/kysucka_chata_mcp_v04.blend`.
- Read-only network download of the specified Poly Haven CC0 files from `dl.polyhaven.org` (URLs resolved through `api.polyhaven.com`) into `work/downloads/`, with MD5/SHA-256 verification.
- Read-only intake of the Cooperator-downloaded Sketchfab archives from `/Users/agile/Downloads/` (`blossoming-apple-tree.zip`, `realistic-hd-norway-spruce.zip`, `realistic-hd-black-spruce-1938.zip`, and optional `spruce-tree.zip`).
- Separate isolated Blender CLI processes (`--background --disable-autoexec`, and `--factory-startup` for the source replay) for asset normalization, verification and replay; they must never open over the live GUI scene.
- Writing the allowed project paths above and the seven allowed Meta paths above; the Worker writes and reads back its own `01_report_01.md`.
- Writing `00_notes.md` is **not** granted — notes are Orchestrator-authored.

### Negative authority

- Do not move, re-aim, re-lens or re-shift `CAM_A_REFERENCE`; do not change the world, lights, glass, roof, walls, openings, chimney/fireplace, interior furniture/partitions, paving/steps/bollards or the v03 timber/fence materials, UVs or geometry.
- Do not modify `SITE_terrain_proxy` vertex positions, `BED_entry` geometry, or any object outside the exact superseded-proxy list.
- Do not `git add`, `git commit`, `git push`, `git fetch`, `git checkout`, `git reset` or `git clean` in either repository; Meta Git is Cooperator-owned and project publication needs a separate explicit grant.
- Do not create accounts, authenticate to Sketchfab, bypass access controls, use paid sources, or substitute another species for spruce or apple tree.
- Do not install or update `mcp-for-blender` or any runtime, do not change MCP client configuration or telemetry settings, and do not call `generate_3d`, `generate_gaussian_world` or `import_asset`.
- Do not quote, print, propose or reproduce the project's literal Orchestrator-owned closure signal anywhere in files, code, comments or the report.
- Do not regenerate CAD/PDF, replace the reference image, touch the AP submodule, or write outside the granted paths.

### Commands

- Read-only file reads, `git status`, `git rev-parse`, `shasum -a 256`, `./.ap/ap doctor`.
- Blender MCP tool calls (`get_addon_status`, `get_scene_info`, `execute_blender_code`, `look`).
- Isolated Blender CLI processes as named above, and `curl` only against `dl.polyhaven.org` and `api.polyhaven.com`.

### Git authority

Read-only in both repositories. No `git add`, `git commit`, `git push`, `git fetch`, `git checkout`, `git reset` or `git clean`. Staged and committed project state is produced later under a separate explicit grant.

### Dependency, network, and secret authority

- Dependency authority: none — no package, add-on, `uvx`, `pip` or runtime installation/update.
- Network authority: `dl.polyhaven.org` and `api.polyhaven.com` only, read-only downloads; localhost Blender MCP socket. No other network destination.
- Secret authority: none — no credential inspection, no account creation, no authenticated API use.
- Side-effect authority: reversible local mutation (repository files under the allowlist, gitignored `work/` files, the live Blender scene and the new `v04` scene) plus read-only network downloads. No destructive or irreversible operation, no remote mutation, no billing.

## Validation and stopping conditions

Evidence tier: E2
Evidence tier basis: cross-cutting reversible live-scene environment and vegetation replacement with third-party asset integration, source-replay verification and matched visual comparison
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: `./.ap/ap doctor`
Affected tests: none (no automated test suite in this project)
New causal regression: none — this visual-change whole has no unit-test surface; the semantic replay table and the native-pixel crop sheet are the causal evidence
Broad or full suite: not-used
Runtime or testbed: `blender-mcp-live-v1` plus isolated Blender CLI processes
Independent acceptance: not-required — the Orchestrator performs acceptance on the delivered renders, crops and replay receipts; the implementing Worker never self-certifies

Validation:
1. Repository gate and all protected hashes re-verified before the first mutation, and again before completion.
2. Asset board render (one small representative render) proving leaf/needle alpha, OpenGL normals, translucency, natural deep spruce green needle colour on `Picea mariana` / `Picea abies`, trimmed ground skirt on `Blossoming apple tree`, complete textures and physical dimensions before scattering.
3. Cold CLI reopen of `blender/kysucka_chata_mcp_v04.blend` with `--disable-autoexec` and a factory-startup source replay to `work/v04_source_replay.blend`, compared semantically against the live scene with the tolerances above.
4. Matched `before.png` / `after.png` at the specified profile, plus `landscape_details.png` with native-pixel crops of the ridge/dense forest, a young spruce, the orchard fruit/leaves and the front planting, with recorded crop bounds.
5. `renders/render_metadata.json` and `evidence/landscape_comparison.md` written with the actual scene, camera, render settings, hashes, imports, licenses, MCP readback receipts, projection decisions, budget measurements, replay results and remaining limitations.
6. `../00_RUN_MAP.md` reconciled: apply the Master-authored snapshot from `00_handout.md` where it is newer than the current file, preserve anything newer than the snapshot, and do not invent run statuses.

Stopping conditions:
- Stop and report `BLOCKED` if the repository identity, baseline commit, protected hashes, live Blender file path or saved/dirty state disagree with this grant, or if the live session has unsaved owner work.
- Stop if an imported asset needs a species substitute, an account, an access-control bypass, or a paid source.
- Stop if the unique-triangle or tracked-file-size ceilings cannot be met without exceeding the authorized paths.
- Stop after the terminal report; this grant expires with it. Any further step needs a new explicit prompt.

## Completion and report contract

Write the complete terminal report to `/Users/agile/meta/projects/kysucka_moderna_chata/00/04-kysuce-forest-and-natural-garden/01_report_01.md` only if that file does not yet exist; read it back completely and verify path and content before the final notice. If the file already exists, do not overwrite it — return the complete report in-session instead.

Begin the report with `### Report for ORCHESTRATOR_CHAT` and echo once:
- `Logical whole identity: kysucka-moderna-chata-kysuce-forest-and-natural-garden`
- `Worker session ordinal: 01`
- `Worker exchange ordinal: 02`

Include the compact core: `status` (`PASS` only when the environment, the deterministic source replay and the matched renders are complete; `PARTIAL` when the deterministic parts are delivered but a required input is missing; `BLOCKED` when a prerequisite failed), `Phase-qualified result: implementation-PASS` only on a complete candidate, `Start commit` and `End commit` (`623d12abe0c0eb2742cd02c9962c1712b53437e2`), changed files and purpose, validation with the actual measured numbers, commit/push result (`not authorized; none performed`), deviations, risks or missing evidence, one smallest next step, exactly one `Report justification` (`new-mutation`, `new-evidence`, `new-material-risk`, `changed-external-state`, `final-acceptance` or `explicit-closure`), `Logical-whole closure: not-closed`, the `Orchestration critique` block with `MEASURED` and `LEAD`, `Resolved Execution Issues / Near-Misses`, `Pre-Existing Failure Classification`, the persisted-file readback receipt, and an authority-expiry statement. Keep it concise and evidence-dense; do not restate this prompt.

After the report is saved and read back, notify the Cooperator in Slovak that `renders/render_metadata.json` is ignored by the Meta Git policy and needs explicit `git add -f` staging by him, and state the actual saved/idle status of the live Blender session and the final `v04` path plus SHA-256.
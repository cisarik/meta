# V18 planning — split into standalone exterior and interior Blender scenes and realistic Kysuce forest pilot

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-split-and-forest-realism-v18
Worker session ordinal: 01
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: SPLIT-AND-FOREST-V18-PLAN — one decision-complete implementation plan for the V18 exterior/interior scene split and the right-valley Kysuce forest realism pilot
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risks: dependency-safe splitting of the 716.1 MiB packed complete scene into two standalone offline-portable Blender files while preserving glazing/reflection/shadow fidelity and all IsViewport working branches; KTX2-sidecar glTF and Poly Haven ground-material verification in isolated Blender 5.3.0; three-layer Kysuce forest-edge composition with ~5% half-height young trees; upper-bend gravel trail occlusion/support diagnosis; and slab-to-terrain cross-section measurement for the north sub-plinth shadow gap and follow-up basement study
Recommended context capacity: approximately 250k tokens
Independence required: no

Planning cycle: initial
Prior planning report: none
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository-, scene-, and isolated-probe-grounded technical planning for V18 (Stage 1 split of `kysucka_chata_v17_komplet_3d.blend` into standalone `kysucka_chata_exterier.blend` and `kysucka_chata_interier.blend` with shared-envelope manifest and basement-ready collection/cross-section measurements, followed by Stage 2 right-valley Kysuce forest-edge pilot and Stage 3 full readable forest margins and trail continuity verification on `kysucka_chata_exterier.blend`)
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1

## Goal and Cooperator-selected scope

Produce one decision-complete, measured implementation plan (no scene save in `R/` or `R/work/`, no persistent repository or `work/` mutation in this planning exchange) for logical whole **V18** (`kysucka-moderna-chata-split-and-forest-realism-v18`).

Michal approved splitting the project into two standalone, offline-portable Blender scene products (`kysucka_chata_exterier.blend` and `kysucka_chata_interier.blend`) from the verified common source `work/v17/complete_3d/kysucka_chata_v17_komplet_3d.blend` (`8a733770f3f4b96922dce76d662e81b281d2047affee5adceac849fb8948113e`), so that:
- **Outcome 1 (Stage 1 — two verified project copies + shared-envelope and slab/terrain cross-section proof):** `kysucka_chata_exterier.blend` and `kysucka_chata_interier.blend` are created from the frozen source, verified by cold reopen in isolated sessions and matched visual comparisons, and `kysucka_chata_interier.blend` includes a dedicated collection and measured slab/plinth/corridor/stair/terrain cross-section data ready for the follow-up basement (`pivnica`) study without waiting for the forest build.
- **Outcome 2 (Stage 2 — right-valley Kysuce forest pilot + single-tree/soil proof + full trail continuity diagnosis on `kysucka_chata_exterier.blend`, followed by Stage 3 expansion to readable forest margins):** the exterior candidate receives a three-layer Kysuce forest treatment from forest floor to canopy in a visible right-valley meadow-to-forest transition sector first, with ~1 in 20 active forest render instances at roughly half adult height, selective replacement/regrouping of scattered broadleaves and historical North American black spruce (`Picea mariana`), and full-route gravel trail continuity verification to the scene boundary.

## Reconciled V17 state and required scene comparison in planning

During Continuation Bootstrap Stage 1, the Orchestrator verified the exact local genealogy (recorded in `T/00_notes.md`):
- `work/v17/nature_detail_01/checkpoints/candidate_exterior_v17.blend` (`f2e0942b63c25ec813b64ad483ea535d4a44b5e0c3a9f6dcfc0eebf7cb3ec4be`, 481,097,097 B, `semantic_sha256: 69db11b1fb2c58009d5b7214ac498a3d1f7cb075d45e0fd37ee6fd9297b54d56`) is the completed Stage 2 V17 exterior scene built on V16 B (`5d82ecf4...`), containing `V17_NATURE_DETAIL` (`V17_GROUND_COVER_POINTS` 297,566 points, `V17_BOTANICAL_POINTS` 175 points, `V17_BROADLEAF_POINTS` 8 trees, `V17_TRAIL_EDGE_POINTS` 243 points), 6,196 V11 conifer points (`99_EXTERIOR_V11`), and `50_INTERIOR_PROXY` (73 objects).
- `work/v10/complete_scene/kysucka_chata_mcp_v10.blend` (`8628822a730d6a1f574126b81fb6a9ee7d109c1f8a254f1331215461526cab70`, 697,689,026 B) was assembled by `work/v10/complete_scene/assembly.py` directly from `candidate_exterior_v17.blend` (`f2e0942b...`) + `work/v10/study/interior_study_v10.blend` (`0a85006a0fa1efec720ebb5791fea9a076cb76a8fe0d6d3db2568cc23deedadb`, collection `55_INTERIOR_V10`: 151 objects, 114 meshes, 21 lights, 6 cameras, 138 packed maps, hiding 86 superseded V10 predecessors via `v10_hide_registry`) + the added hill-forest collection `V10_HILL_FORESTS` (122 point-cloud objects, 3,157 additional trees with seed `1372010`: 3,006 conifers and 151 broadleaves across six hill zones).
- `work/v17/complete_3d/kysucka_chata_v17_komplet_3d.blend` (`8a733770f3f4b96922dce76d662e81b281d2047affee5adceac849fb8948113e`, 716,141,423 B) was built by `work/v17/complete_3d/prepare.py` directly from `kysucka_chata_mcp_v10.blend` (`8628822a...`) with 100% unchanged render branches (`render_branches_unchanged: true`), adding ultra-light viewport preview branches (`V17 PREVIEW Ihličnany` 136–156 tris, `V17 PREVIEW Listnáče` 214 tris), viewport-only (`show_render=False`) Material Preview modifiers with 512px compact albedos (248 packed images total), collection `00 | Kamery V17` (8 timeline-marker cameras `Záber 01..08` at frames `1, 31, 61, 91, 121, 151, 181, 211`), and workspaces `V17 | 3D scéna`, `V17 | Kamery`, `V17 | Render`.

In your read-only planning audit, verify and record from both `kysucka_chata_v17_komplet_3d.blend` and `candidate_exterior_v17.blend`:
- Exact absolute paths, SHA-256 digests, building envelope transforms, visible interior collections (`55_INTERIOR_V10` vs `50_INTERIOR_PROXY` and `v10_hide_registry`), forest sources (`99_EXTERIOR_V11` + `V17_BROADLEAF_POINTS` vs `V10_HILL_FORESTS`), cameras and their parameters, and confirm that terrain (`V11_TERRAIN_NEAR`, `V11_TERRAIN_FAR`, `V11_TERRAIN_EXTENSION`), trail (`V07_TRAIL`), and V17 meadow/botanical/trail-edge layers are identical in render while `V10_HILL_FORESTS` is the exact layer that added the 3,157 hill trees (3,006 conifers + 151 broadleaves) responsible for the larger edge crowns and scattered slope trees in `render_valley.png`.

## Candidate assets and isolated Blender 5.3.0 import/format check

Evaluate existing local assets (`assets/models/sketchfab_bf500546e2874f9ea086ba6abb11357e` PlantCatalog Norway spruce `ABIES_LOD0`/`LOD1`/`YOUNG`, `assets/models/sketchfab_3232c3022f2947b7999de0941ede5653` Black spruce `MARIANA_LOD0`/`LOD1`, `assets/models/shrub_01`, `assets/models/grass_medium_01`, `assets/models/periwinkle_plant`, and `work/v17/nature_detail_01/assets/v17_masters.blend` with `tevy European Beech v1`, `tevy Silver Birch v1`, `tevy Wildflower Patch v1`, and `Poly Haven Dandelion 01`) together with the handout's new CC0 candidates:
- Distinct adult/young Norway spruce silhouette (`Picea abies`): `tevy Norway Spruce v1` (`https://tevy.dev/models/norway-spruce`, CC0, GLB LODs with `meshopt` + `KTX2`)
- Forest floor under conifers: `Poly Haven Forest Ground 01` (`https://polyhaven.com/a/forrest_ground_01`, CC0)
- Leaf litter under beech/broadleaves: `Poly Haven Leaves Forest Ground` (`https://polyhaven.com/a/leaves_forest_ground`, CC0)

In your isolated headless Blender 5.3.0 probe inside `/tmp/opencode/v18_plan_inspect`:
- If outbound HTTPS is available in Native Plan Mode, fetch and test `tevy Norway Spruce v1` (using the proven V17 KTX2-sidecar externalization + stock Blender 5.3.0 `.gltf` import with `import_ktx_texture=True, import_pack_images=True`) and the Poly Haven forest-floor/leaf-litter maps inside `/tmp/opencode/v18_plan_inspect`, recording exact URLs, SHA-256 hashes, LOD triangle counts, metric dimensions, trunk base/bark/branching gradient/needle alpha/backlight behavior vs local `ABIES_LOD0`, and cleaning `/tmp/opencode/v18_plan_inspect` completely before finishing.
- If network access is restricted during Native Plan Mode, record that exact observation and specify the deterministic Stage-0 offline asset acquisition, SHA-256 pinning, KTX2-sidecar normalization, and single-tree/soil comparison test in your plan.

## Sources, identity, and repository gate

Working directory: `R = /home/agile/Projects/kysucka_moderna_chata`
Trace directory: `T = /home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18`

Repository identity and baseline:
- Project checkout: standalone checkout at `R`, branch `main`, expected HEAD `78534bd46020bb2bfc97eef69b05e583cba5a5e5` (tracked working tree and index clean; untracked owner file `reference/01.png` with SHA-256 `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d` is classified under RF-12 as `unrelated-owner-work` and must remain untouched).
- Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `.ap` (gitlink = submodule HEAD).
- Meta repository: `/home/agile/meta`, branch `main`, HEAD `27595fe2af3263ef7c3d0f29bf6373b779c9b0b6`.

Verified immutable input hashes:
- `work/v17/complete_3d/kysucka_chata_v17_komplet_3d.blend`: `8a733770f3f4b96922dce76d662e81b281d2047affee5adceac849fb8948113e`
- `work/v17/nature_detail_01/checkpoints/candidate_exterior_v17.blend`: `f2e0942b63c25ec813b64ad483ea535d4a44b5e0c3a9f6dcfc0eebf7cb3ec4be`
- `work/v10/complete_scene/kysucka_chata_mcp_v10.blend`: `8628822a730d6a1f574126b81fb6a9ee7d109c1f8a254f1331215461526cab70`
- `work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend`: `5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1`
- `work/v17/nature_detail_01/assets/v17_masters.blend`: `4849e1ca967a8a1bd20c4f1a691ba0dec475c865b4915f6debc4abf0935e5411`
- `work/v16/meadow_trail_01/renders/B_v16_960.png`: `92f865ec1e04190a9d28aed213a93f85a2eac58f32ce2a2961872ddc2f0dece6`
- `work/v17/nature_detail_01/renders/V17_valley_960.png`: `80c81c22550b2e7a9e170b9fc6998c6f8c0531dcedc1eae98a92e93eaf641df1`
- `work/v17/complete_3d/render_valley.png`: `594cd5977ca0f6ada93a2c7a163922ab5e8685fc7e59d35ec5ac109d934f650d`
- `work/v17/complete_3d/render_north.png`: `b0d9c6fbc03b635c981343761b0de24e544b12b5c5cfc84cd4822209d70a509c`
- `work/v17/complete_3d/render_interior.png`: `41b4465b3067422fc850530b43564ad4c2bd24b86bfbedd9615a1eb5e206da77`
- Local AI concept reference `reference/01.png`: `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d`
- Isolated MCP-disabled preferences `work/v12/profile_03/isolated_config/userpref.blend`: `d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561`

Mandatory reading:
- Governing WORKER spine: `.ap/AP.md` Semantic Authority + WORKER row, RF-03/RF-06/RF-12/RF-18, §8, §18; `.ap/AP_WORKER.md` Worker Session Target and Reporting; `.ap/PROMPT_CONTRACTS.md` Worker Report Header, Planning Record, Plan-to-Execution Gate, Worker Exchange Identity, Mutation Axes Record, Cooperator Delivery and Trace Destination Record.
- Project `AGENTS.md`, `assets/ASSET_MANIFEST.md`, `model/parameters.json`, `/home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space/evidence/design_basis_v10.md`, `/home/agile/meta/projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17/01_report_02.md`, `T/00_handout.md`, and `T/00_notes.md`.
- Visual inputs (inspect actual images): `reference/01.png`, `work/v16/meadow_trail_01/renders/B_v16_960.png`, `work/v17/nature_detail_01/renders/V17_valley_960.png`, `work/v17/complete_3d/render_valley.png`, `work/v17/complete_3d/render_north.png`, and `work/v17/complete_3d/render_interior.png`.
- Existing source scripts and receipts: `work/v17/complete_3d/prepare.py`, `work/v17/complete_3d/build.json`, `work/v17/complete_3d/source_inspection.json`, `work/v10/complete_scene/assembly.py`, `work/v10/complete_scene/assembly.json`, `work/v17/nature_detail_01/source/nature_detail_v17.py`, `work/v17/nature_detail_01/source/nature_detail_v17.json`, `work/v11/source/exterior_v11.py`, and `scripts/forest_trail_v07.py`.

## Execution route for isolated headless Blender 5.3.0 probe

Canonical inspection route: **isolated headless Blender 5.3.0 CLI probe** (explicit bounded task route; live MCP `tools.blender.*` is prohibited):
- Verify before and after running that no foreign background Blender process is tampered with, global `/home/agile/.config/blender/5.3/config/userpref.blend` (`8c52b5cf0d5ac23a35c9496e442a37c69399203b47b32842dd76d05653c29c02`) is unchanged, and available system RAM is ≥10 GiB.
- Run `/home/agile/Applications/Blender/blender --background --disable-autoexec --threads 4` with `nice -n 10` and isolated environment (`BLENDER_USER_CONFIG`, `XDG_CACHE_HOME`, `TMPDIR`, `TMP`, `TEMP`, `PYTHONPYCACHEPREFIX=/tmp/opencode/v18_plan_inspect/pycache`, `PYTHONDONTWRITEBYTECODE=1`) inside `/tmp/opencode/v18_plan_inspect` initialized with a copy of `work/v12/profile_03/isolated_config/userpref.blend` (`d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561`). Put `import sys; sys.dont_write_bytecode = True` before any project module import. Any existing or interpreter-generated `__pycache__/*.pyc` under `/home/agile/Applications/Blender/` or project `scripts/__pycache__` is explicitly permitted as benign interpreter cache and is not a containment stop.
- Never write into `R/` or `R/work/`; remove `/tmp/opencode/v18_plan_inspect` completely before submitting your report and verify that all pinned `.blend` hashes are unchanged.

## Planning deliverables required in `01_report_00.md`

1. **V17 scene comparison and collection-dependency audit:**
   - Exact comparison table between `work/v17/complete_3d/kysucka_chata_v17_komplet_3d.blend` (`8a733770...`) and `work/v17/nature_detail_01/checkpoints/candidate_exterior_v17.blend` (`f2e0942b...`): absolute paths, SHA-256, building transforms, visible interior collections (`55_INTERIOR_V10` vs `50_INTERIOR_PROXY`, `v10_hide_registry`), forest collections (`99_EXTERIOR_V11`, `V17_BROADLEAF_POINTS`, `V10_HILL_FORESTS`), cameras/markers (`00 | Kamery V17`), terrain, trail, and `IsViewport` working branches (`V17 PREVIEW *` vs `V12_WORK_*` / `V17_*_WORK`).
   - Full dependency map of every top-level collection (`00_REFERENCE`, `00 | Kamery V17`, `10_ENVELOPE`, `20_ROOF`, `30_GLAZING`, `40_ENTRY_DETAILS`, `50_INTERIOR_PROXY`, `55_INTERIOR_V10`, `60_LIGHTS`, `70_SITE`, `80_CAMERAS`, `90_VEGETATION_PROXY`, `95_LANDSCAPE_V04`, `96_SITE_V05`, `97_VEGETATION_V06`, `98_VEGETATION_V08`, `99_EXTERIOR_V11`, `99_NATURE_STUDY_V09`, `V07_ROOT`, `V10_HILL_FORESTS`, `V13_COHERENT_EXTERIOR_MEADOW`, `V16_SHOULDERS`, `V17_NATURE_DETAIL`) covering Geometry Nodes modifiers, off-scene master collections, materials, packed textures, lights, shadow casters, world, and timeline camera markers.
2. **Stage 1 Scene-Split Specification (`kysucka_chata_exterier.blend` and `kysucka_chata_interier.blend`):**
   - Exact destination paths (propose canonical project-working paths and `work/v18/...` staging/evidence paths), ownership rules, and shared-geometry manifest specification (source hash `8a733770...`, units = metres, world transforms, axes, elevation datum `+0.450 m` floor / `+0.200 m` slab bottom, exact object list and vertex/matrix digests for shared envelope `10_ENVELOPE`, openings, glazing `30_GLAZING` + `V10_FRONT_GLAZING_*` / `V10_GLASS_*`, roof `20_ROOF`, chimney, and plinth/slab `BASE_slab`).
   - Exact retention/pruning specification for `kysucka_chata_exterier.blend`: keep valley, forest, meadow, terrain, fence, gate, gravel trail, facade, exterior cameras, and all interior geometry/lights/materials visible through glazing, in reflection, or in shadow (starting from a complete working exterior copy and only pruning zero-impact data proven by matched comparison).
   - Exact retention/pruning specification for `kysucka_chata_interier.blend`: keep full `55_INTERIOR_V10` (including gallery, stairs, and fireplace), shared building envelope, interior cameras, near-house terrain/garden/fence/orchard and horizon/forest visible through windows, reflections, and lighting, plus create a dedicated collection for the future basement study (e.g. `56_BASEMENT_V18`) while pruning heavy exterior-only point clouds/masters that have zero window/reflection/shadow impact if and only if proven by matched window/interior comparison.
   - Offline portability gate: packed dependencies, zero external `bpy.data.libraries`, cold reopen in an independent directory/session, shared-geometry digest equality, and matched visual comparison renders (wide exterior, gable-behind-glass crop, and interior view through window).
3. **Slab/Terrain Cross-Section & Basement Study Handoff Measurements:**
   - Measure directly from `kysucka_chata_v17_komplet_3d.blend` the exact local elevation profile of `BASE_slab` (`+0.20..+0.45 m`), walls, plinth, and `V11_TERRAIN_NEAR` around all four facades (`X` and `Y` transects), proving the exact geometric cause of the dark sub-slab gap visible on `render_north.png` (`Záber 04 | Severná strana`).
   - Measure the V10 ground-floor plan coordinates for the basement handoff: corridor width (`Y` axis, nominal `1.15 m`), gallery stair footprint and headroom (`V10_STAIR_*`, `V10_UNDERSTAIR_CABINET`), fireplace (`V10_FIREPLACE_*`), western service/back-room zones, and exterior terrain elevations on the less-exposed flanks so that the follow-up interior basement task receives exact coordinates and cross-sections immediately after Stage 1 split verification.
4. **Stage 2 Right-Valley Kysuce Forest Pilot Specification (on `kysucka_chata_exterier.blend`):**
   - **Target right-valley sector & witness cameras:** exact world XY / station coordinates for the visible right-hand valley sector at the meadow-to-forest transition; exact crop rectangle in `CAM_V11_VALLEY_REVIEW` (`Záber 01 | Chata a údolie`) and exact pose of one new human-eye-height (~1.65 m above terrain) forest-margin witness camera (`CAM_V18_FOREST_MARGIN`) that simultaneously shows: (a) an adult trunk base on forest soil, (b) a young half-height spruce, (c) a broadleaf grouped with undergrowth, and (d) a sunlit gap looking into a deeper forest layer, under unchanged lighting (`V16_WORLD_MEADOW_BALANCE` + `V15_SUN_REFERENCE_KEY`).
   - **Single-tree & soil test design:** controlled A/B test comparing local PlantCatalog `ABIES_LOD0` against `tevy Norway Spruce v1` (`Picea abies`) and testing the forest-floor shader (`Poly Haven Forest Ground 01` + `Poly Haven Leaves Forest Ground`), checking root flare/trunk base, bark, branching gradient, needle overlap, card alpha, backlight response, juvenile crown shape with denser lower branches for young spruces, and offline packed textures. Specify how historical North American `Picea mariana` is documented as an original visual proxy and selectively replaced in the near sector where verified improvement is shown.
   - **Three interpenetrating forest layers:**
     1. Under-canopy ground layer: needle/soil substrate (`Forest Ground 01`), root flares, sparse dead branches/twigs, and local moss, plus restrained beech leaf litter (`Leaves Forest Ground`) under beech crowns, at true metric UV scale with small 3D detail where visible in the low eye-level view.
     2. Sunlit gap and margin-ecotone layer: irregular clusters of spruce seedlings/saplings, low shrubs (`shrub_01`), and sparse grass feathering irregularly out into the open meadow.
     3. Canopy and broadleaf-grouping layer: regrouping scattered broadleaves (from V17 / `V10_HILL_FORESTS`, which currently expose isolated pale trunks in bare grass) into natural crown-and-undergrowth clusters at the forest margin, and selectively replacing/thinning uniform edge conifers so light catches grouped forest projections and gaps rather than a single dark wall, while preserving the open valley sightline and surrounding forest arc.
   - **Young-tree inventory and ~1-in-20 (~5%) half-height cohort specification:**
     - Audit the current active render instances across `99_EXTERIOR_V11`, `V17_BROADLEAF_POINTS`, and `V10_HILL_FORESTS` (total count, prototype source heights in metres, actual instance Z-scales and world heights in metres, and actual height ratios to comparable adult trees, noting why historical `Young` labels alone do not establish a ~0.5 ratio).
     - Specify the exact target population so that approximately 1 in 20 active forest render instances (~5%) has roughly half the height of a comparable adult tree (with juvenile denser-lower-branch morphology), arranged in small natural groups with sunlit gaps both along the margin and inside the stand, with verified triangle-evaluated terrain support, fence/trail crown clearances, proper render LOD, instanced shared meshes/materials, and lightweight `IsViewport` working proxies.
5. **Gravel Trail Continuity & Upper-Bend Terrain Proof:**
   - Measure the entire `V07_TRAIL` route from the entry paving and gate to the actual scene boundary in V17/V11 world coordinates (comparing with V07's `[42, 138.25]` pre-V11 coordinate exit).
   - Diagnose the apparent interruption of the grey gravel trace in the upper right bend in `V17_valley_960.png` / `render_valley.png`: compute camera rays from `CAM_V11_VALLEY_REVIEW` to all trail stations `s` around the upper bend and check mesh connectivity, terrain elevation delta (`V07_TRAIL` vs `V11_TERRAIN_NEAR` / `V11_TERRAIN_FAR`), shader alpha/mix factors, and line-of-sight terrain-wave grazing occlusion.
   - Specify either the local support/mask repair (if a geometry/shader defect exists) or the overhead plan-view continuity proof (if normal terrain-wave occlusion), plus the compacted grey-brown gravel, soil, and irregular low verge treatment on the trail section adjacent to the right-valley forest pilot and continuous passable center verification along the full route.
6. **Implementation Stages, Render Budget, Verification Gates, and Exact Path Allowlist:**
   - Stage 0: offline asset normalization & single-tree/soil test.
   - Stage 1: freeze source, produce and cold-verify `kysucka_chata_exterier.blend` and `kysucka_chata_interier.blend` + shared-geometry manifest + slab/terrain cross-section and basement handoff package.
   - Stage 2: right-valley forest pilot on `kysucka_chata_exterier.blend` + fast matched renders (`960 × 540` wide camera `CAM_V11_VALLEY_REVIEW`, 1:1 right-valley sector crop, eye-level forest witness `CAM_V18_FOREST_MARGIN`, trunk-base/soil detail crop, and overhead full-trail continuity witness) with wall-time and peak-RSS measurement before committing to any 24-minute `3200 × 1800` render.
   - Stage 3: expansion of the proven forest-margin composition to readable valley margins on `kysucka_chata_exterier.blend`, cold-open and `IsViewport` working-view verification, asset manifest update, and exact file allowlist.

## Authority and mutation axes

Positive authority: read-only inspection of `R`, `R/work/v07`–`R/work/v17`, `/home/agile/meta/projects/kysucka_moderna_chata/00/**`, and `reference/01.png`; bounded isolated headless Blender 5.3.0 inspection and candidate-asset import probe strictly inside temporary `/tmp/opencode/v18_plan_inspect` (cleaned before report); return the complete terminal report in session output for Orchestrator persistence.

Negative authority: no writes to tracked repository files, `R/blender/**`, `R/work/**`, or `/home/agile/meta/**`; no scene save in `R/` or `R/work/**`; no live MCP calls (`tools.blender.*` prohibited); no touching global Blender preferences; no Blender installation/importer modification; no package/runtime installation; no Git writes in any repository; no closure signal emission.

Repository mutation: none
Host/remote mutation: bounded temporary `/tmp/opencode/v18_plan_inspect` directory for isolated headless Blender 5.3.0 inspection and candidate-asset import probe only (must be removed before report; zero persistent host change; benign Python `__pycache__/*.pyc` interpreter cache permitted)
Trace persistence: none

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
Downloadable prompt filename: 01_planning_00.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18
Report filename: 01_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: ORCHESTRATOR — named exact-content relay in session output because Native Plan Mode blocks direct file writes
Git publication owner: COOPERATOR
Archival: wait-for-report

Evidence tier: E0
Evidence tier basis: read-only technical planning and isolated temporary headless Blender probe with full cleanup
Validation ladder: not-used
Independent acceptance: not-required

Stopping conditions: failed repository/hash gate; unexplained divergence; foreign background Blender process tampering; temporary directory cleanup failure; instruction conflict. Stop at the terminal planning report; planning authority expires there.

Completion and report contract: begin the report on line 1 with `### Report for ORCHESTRATOR_CHAT`; echo the coordinates (`kysucka-moderna-chata-split-and-forest-realism-v18`, `01`, `01`) once; include the compact core (`Status: PASS | PARTIAL | BLOCKED`, `Phase-qualified result: not-applicable`, `Start commit` / `End commit`, changed files = none, validation summary including `/tmp/opencode/v18_plan_inspect` cleanup and unchanged `.blend` SHA-256 hashes, Git result = no writes, deviations/risks, one smallest next step, `Report justification: new-evidence`, authority-expiry statement, `Orchestration critique` `MEASURED` / `LEAD`, `Resolved Execution Issues / Near-Misses`, and `Pre-Existing Failure Classification`). Set `Logical-whole closure: not-closed`. Output the complete report text in the session so the Orchestrator can persist it to `T/01_report_00.md`, then stop.

Authority expiry: this terminal planning report, cancellation, or supersession ends this grant; retained context is convenience, not continuing authority.

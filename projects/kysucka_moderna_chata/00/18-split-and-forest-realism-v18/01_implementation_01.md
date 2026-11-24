# V18 implementation (Stage 0–2) — asset normalization, standalone exterior/interior scene split with basement handoff, and right-valley Kysuce forest pilot

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-split-and-forest-realism-v18
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker (same-session continuation of Planner 01/01)
Phase: implementation
Task identity: SPLIT-AND-FOREST-V18-IMPL-STAGE0-2 — execute Stage 0 asset normalization and single-tree/soil A/B test, Stage 1 standalone exterior/interior scene split and basement handoff, and Stage 2 right-valley Kysuce forest pilot and trail diagnosis
Delivery route: manual Cooperator delivery
Continuity anchor: accepted V18 implementation plan `01_report_00.md` (SHA-256 `6a6e5c340b8e348fd43971d9a63878e5106fe2fb38d385fa72afb1ae4873c31b`, Worker session 01 / exchange 01), reconciled and accepted by this whole's ORCHESTRATOR on 2026-11-23 (recorded in `00_notes.md`)
Authority renewal: prior planning authority expired at `01_report_00.md`; this prompt grants complete new bounded implementation authority for Stage 0, Stage 1, and Stage 2 with `Native planning mode: not-used`. Retained context is convenience, not authority. Re-gate repository, input hashes, and process state yourself; stop on any conflict between retained context and current repository evidence.
Evidence posture: non-independent
Implementation authority: explicit
Independence required: no
Reasoning recommendation: High — named risks: offline KTX2-sidecar normalization and single-tree/soil A/B verification, dependency-safe splitting and `bwrap --unshare-net` cold-open verification of the 716.1 MiB packed scene into standalone `blender/kysucka_chata_exterier.blend` and `blender/kysucka_chata_interier.blend`, exact 289-object shared-envelope manifest and basement cross-section handoff, and three-layer right-valley Kysuce forest pilot + trail continuity proof inside strict CPU/RAM guards
Recommended context capacity: approximately 250k tokens

## Binding specification and goal

Your accepted plan `01_report_00.md` (§§1–5) is the binding technical specification for **V18**. In this exchange (`01/02`), implement **Stage 0, Stage 1, and Stage 2 (right-valley forest pilot and trail continuity proof)** starting from immutable `work/v17/complete_3d/kysucka_chata_v17_komplet_3d.blend` (`8a733770f3f4b96922dce76d662e81b281d2047affee5adceac849fb8948113e`), and **stop at the Stage 2 pilot visual gate before Stage 3 expansion**:

1. **Stage 0 — Offline asset normalization and controlled single-tree & soil A/B test (`work/v18/stage0/`, `assets/`):**
   - Download (if not cached) and verify the exact pinned SHA-256 hashes of the 11 raw CC0 files from `01_report_00.md` §2 under `work/v18/stage0/raw/`:
     - `tevy Norway Spruce v1`: `lod0.glb` (`63d364cdec9bbcef366c25ed0397d17f3cff57d3e62cf8aff2ce06fc987fbbf7`), `lod1.glb` (`1a99b9b1d8c5307337c204e4db26cecaf6493e4c2e11f51f6254d822dd1e6d07`), `lod2.glb` (`2dbb026f880470e94924e9eb99acba144a7486ecc27908487235a1558b91285f`).
     - `Poly Haven Forest Ground 01` (2K): `forrest_ground_01_diff_2k.jpg` (`e4d557ff61a0b42712a58e8a2e91c6010738977d4e172b7af47abd7d406ae735`), `forrest_ground_01_nor_gl_2k.jpg` (`aa23fa930c6303490f842f7c016c19d838263e8e4538d42508a9332e3fd76b69`), `forrest_ground_01_rough_2k.jpg` (`e09258c7f055156a7607f1b21dccf38c7efd847e7d030271d5ffcc4a722df37d`), `forrest_ground_01_disp_2k.png` (`1d8cb8bbe9039ee2cd22068d457617a1748170405aacd49d33fcf637e08bb12b`).
     - `Poly Haven Leaves Forest Ground` (2K): `leaves_forest_ground_diff_2k.jpg` (`bda0ffc30570af7c067a3d6922cb1c7f31ada4fcece24b8f2cc4c5dde742e22c`), `leaves_forest_ground_nor_gl_2k.jpg` (`2713002b4a75b8b47b983c75d3f388d79f0775f305ca14884eae6a277b8f48bd`), `leaves_forest_ground_rough_2k.jpg` (`a08b1aaba9ca87924abfbe65a1c6be03c6cc7fcfcf140dc784ccf35205c307f0`), `leaves_forest_ground_disp_2k.png` (`38294b4ce4c1f6c99611876cb972f7973ecf65ae5be0ed406a11b705699411bd`).
   - Externalize KTX2 bufferViews to `work/v18/stage0/sidecars/lod{0,1,2}/`, import via stock Blender 5.3.0 `.gltf` (`import_ktx_texture=True, import_pack_images=True, merge_vertices=False`), normalize planting collars, build `work/v18/stage0/normalized.blend`, and cold-verify all 20 packed images offline with `bwrap --unshare-net`.
   - Copy the adopted raw inputs into `assets/models/tevy_norway_spruce_v1/` and `assets/textures/forest_v18/{forrest_ground_01,leaves_forest_ground}/` and document provenance, licenses, SHA-256 hashes, and modifications in `assets/ASSET_MANIFEST.md` (preserving all existing sections).
   - Render the Stage 0 controlled A/B comparison images `work/v18/stage0/comparison-{crown,root,bark,soil}.png` comparing local `ABIES_LOD0` against `tevy Norway Spruce v1` at matched 9.5862 m height under `V16_WORLD_MEADOW_BALANCE` and `V15_SUN_REFERENCE_KEY`, and testing `Forest Ground 01` (2.00 m repeat) and `Leaves Forest Ground` (1.26 m repeat). Write `work/v18/stage0/{assets,resources}.json`.

2. **Stage 1 — Standalone scene split (`blender/kysucka_chata_exterier.blend` and `blender/kysucka_chata_interier.blend`), shared-envelope manifest, and basement handoff (`work/v18/stage1/`, `model/`):**
   - Write `model/shared_envelope_v18.json` for the 289 explicit shared mesh objects (`10_ENVELOPE`, `20_ROOF`, `30_GLAZING`, `40_ENTRY_DETAILS`, and the 24 `55_INTERIOR_V10` meshes with `v10_piece in {'REPLACEMENT', 'FRONT_GLAZING', 'GABLE_GLASS'}`), verifying the aggregate digest `8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50`.
   - Build `work/v18/stage1/kysucka_chata_exterier.blend` (opening at `Záber 01 | Chata a údolie`, frame 1) and `work/v18/stage1/kysucka_chata_interier.blend` (opening at `Záber 07 | Obývačka a krb`, frame 181, with new empty collection `56_BASEMENT_V18` linked via collection property to embedded text `V18 | Podklad pre pivnicu`) from frozen `work/v17/complete_3d/kysucka_chata_v17_komplet_3d.blend` (`8a733770...`).
   - Test batch pruning of only `90_VEGETATION_PROXY` (263 hidden mesh-only predecessors): retain the pruning if and only if zero incoming references exist and matched witness renders are pixel-identical; otherwise ship the full unpruned copies. Record both inherited V17 check counts (`5,363` objects / `248` images) and actual cold-open totals (`5,371` objects / `289` images before any `90_VEGETATION_PROXY` pruning) per the reconciled `MEASURED` critique.
   - Verify offline portability of each staged copy in `/tmp/opencode/v18_verify/` using `bwrap --unshare-net` with `R` masked (zero `bpy.data.libraries`, zero linked IDs, all reachable images packed, both arms of all `IsViewport` switches valid, shared-envelope digest `87288303...` identical in both files, and `/tmp/opencode/v18_verify/` cleaned after readback).
   - Render the Stage 1 matched comparison suite `work/v18/stage1/{source,exterier,interier}-{wide,gable,north,hero,gallery}.png` (960 × 540 @ 24 samples for `Záber 01` frame 1, `Záber 04` frame 91, `Záber 07` frame 181, `Záber 08` frame 211, plus 1:1 gable crop `[650,930) × [0,450)` from `Záber 03` frame 61).
   - Write `work/v18/stage1/{dependencies.json,portability.json,basement.json,cross_sections.csv,basement_plan.svg,cross_sections.svg,resources.json}` containing all measured ground-floor, corridor (`1.150 m`), stair/understair, fireplace, and slab-to-terrain cross-section data (including the `0.255 m` north sub-slab gap between `BASE_slab` `+0.200 m` and `V11_TERRAIN_NEAR` `-0.055 m`).
   - Promote the verified Stage 1 files to `blender/kysucka_chata_exterier.blend` and `blender/kysucka_chata_interier.blend` and verify their promoted SHA-256 hashes.

3. **Stage 2 — Right-valley Kysuce forest pilot and trail continuity proof (`work/v18/stage2/`, `scripts/v18_split_forest.py`, `model/parameters.json`):**
   - Copy the verified Stage 1 `blender/kysucka_chata_exterier.blend` to `work/v18/stage2/before.blend` (do **not** overwrite `blender/kysucka_chata_exterier.blend` or `blender/kysucka_chata_interier.blend` during Stage 2; both canonical files in `blender/` remain at their verified Stage 1 split hashes until Stage 2 is reviewed and Stage 3 is authorized).
   - Add `forest_realism_v18` to `model/parameters.json` (preserving all prior parameter sections unchanged) and implement `scripts/v18_split_forest.py` (`stage="stage2"`).
   - Build `work/v18/stage2/candidate.blend` applying the right-valley pilot (`01_report_00.md` §4, polygon `(-15,58)..(-23,64)`, seed `13718`):
     - Create eye-level witness camera `CAM_V18_FOREST_MARGIN` at `[-24, 100, 13.982899]` (`1.65 m` above ground `12.332899 m`) aiming at `[-41, 114, 17.408537]`, `32 mm`, horizontal `36 mm` sensor, `.03–600 m` clip, DOF off, under unchanged `V16_WORLD_MEADOW_BALANCE` and `V15_SUN_REFERENCE_KEY`.
     - Replace focal *Picea mariana* at `[-39.4190, 109.3753]` (`Z = 13.774797 m`) with the local Norway spruce adult master (`ABIES_LOD0` derivative with camera-side lowest obscuring dead/drooping branch components cleanly separated if needed so the trunk collar on forest soil is clearly visible in crop `[264,470) × [300,500)`), and selectively replace the remaining in-polygon *P. mariana* placements with verified Norway spruce forms (admitting `tevy Norway Spruce v1` LOD1 in the mid-distance stand mix if its matched crop shows clean card edges and useful crown variation, or local V11 Norway spruce render master otherwise).
     - Build the owned juvenile Norway spruce derivative from `ABIES_YOUNG` (`u' = 0.04 + 0.96 * ((u - 0.04)/0.96)^1.2` for `u > 0.04`, lower whorls broadened up to +17%) and place the two pilot half-height trees (`2` of `31` trees inside the pilot polygon) at `[-40.984, 116.188]` and `[-36.004, 116.845]` matched to `0.50` (`~5.127 m`) of the `10.254 m` adult Norway spruce comparator at `[-44.829, 116.349]`.
     - Regroup the scattered V17 broadleaves inside/adjacent to the pilot so pale trunks no longer stand isolated in bare meadow: move the birch at `[-33, 93]` to `[-48.5, 109.5]` and the birch at `[-61, 122]` toward the beech group at `[-57, 129.5]`, surrounded by irregular `shrub_01`, seedling/sapling, and sparse `grass_medium_01` understorey clusters and `Leaves Forest Ground` litter patches, keeping the sunlit gap at `[-32.5, 111.5]` open toward the deeper stand at `[-48, 132]`.
     - Apply the three interpenetrating layers (owned terrain material derivatives blending `Forest Ground 01` needle soil, moss, and 3D twigs/root detail under conifer crowns and `Leaves Forest Ground` under broadleaves; gap/margin seedlings, `shrub_01`, and sparse grass feathering into open meadow; grouped canopy and paired lightweight `IsViewport` working proxies). Preserve all 175 `V17_BOTANICAL_POINTS` and meadow outside the pilot masks.
     - On the adjacent gravel trail section `s = 93–124 m`, apply the owned material/mask derivative showing compacted grey-brown gravel, fine-soil transition, and irregular low verge while keeping the continuous passable center clear.
   - Verify Stage 2 second-apply idempotence, triangle-evaluated root support, crown and walking-corridor clearance, offline cold reopen of `work/v18/stage2/candidate.blend`, and working `IsViewport` branches.
   - Render the Stage 2 matched before/after comparison suite under `work/v18/stage2/` (serialized one-by-one on CachyOS, fixed 4-thread P0 CPU, seed 0, AgX/None, exposure 0, gamma 1, OIDN Accurate/High, logging wall time, peak RSS, and minimum available RAM):
     - `{before,after}-wide.png`: `CAM_V11_VALLEY_REVIEW` (`Záber 01`), `960 × 540`, **96 samples** (directly comparable to `V17_valley_960.png` and `B_v16_960.png`).
     - `{before,after}-right.png`: 1:1 right-valley sector crop `[712,960) × [0,244)` from `{before,after}-wide.png` (plus a 96-sample detailed border crop of that sector if needed to resolve crown/undergrowth layering clearly).
     - `{before,after}-forest.png`: `CAM_V18_FOREST_MARGIN`, `960 × 540`, **96 samples**.
     - `{before,after}-root.png`: close trunk-base & forest-soil crop `[264,470) × [300,500)` from `CAM_V18_FOREST_MARGIN` (at 96 samples).
     - `{before,after}-trail.png`: overhead full-route continuity witness with station and terrain-occlusion overlay (`s = 0..198.181 m` to `[42, 138.25, 1.157007]`, highlighting the terrain-wave line-of-sight occlusions at `s = 83.68–84.61 m` and `s = 113.18–124.03 m` and the `s = 93–124 m` pilot section).
   - Write `work/v18/stage2/{pilot.json,forest_inventory.csv,trail_stations.csv,resources.json}`, then **stop before Stage 3** and submit `01_report_01.md`.

## Repository gate and exact baseline

Working directory: `R = /home/agile/Projects/kysucka_moderna_chata`
Trace directory: `T = /home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18`
Exact baseline: `78534bd46020bb2bfc97eef69b05e583cba5a5e5` on `main`

Project repository gate:
- Standalone checkout at `R`, branch `main`, expected HEAD `78534bd46020bb2bfc97eef69b05e583cba5a5e5` (tracked working tree and index clean at start; untracked owner file `reference/01.png` with SHA-256 `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d` is classified under RF-12 as `unrelated-owner-work` and must remain untouched).
- Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `.ap` (gitlink = submodule HEAD).
- Meta repository: `/home/agile/meta`, branch `main`, HEAD `27595fe2af3263ef7c3d0f29bf6373b779c9b0b6`.

Immutable input hashes (verify before and after execution):
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
- `reference/01.png`: `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d`
- `work/v12/profile_03/isolated_config/userpref.blend`: `d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561`
- `/home/agile/.config/blender/5.3/config/userpref.blend`: `8c52b5cf0d5ac23a35c9496e442a37c69399203b47b32842dd76d05653c29c02`

Mandatory reading: governing WORKER spine (`.ap/AP.md` Semantic Authority + WORKER row, RF-03/RF-06/RF-12/RF-18, §8, §18); `.ap/AP_WORKER.md` Worker Session Target + Reporting; `.ap/PROMPT_CONTRACTS.md` Worker Report Header, Implementation Authority Record, Mutation Axes, Delivery Record; project `AGENTS.md`; `T/00_handout.md`; `T/00_notes.md`; and your accepted plan `T/01_report_00.md`.

## Execution route and resource/process guards

Canonical execution route: **isolated native Blender 5.3.0 CLI route** (`/home/agile/Applications/Blender/blender --background --disable-autoexec --threads 4`), explicitly activated for this task; live MCP (`tools.blender.*`) is prohibited.

- Run at most **one** owned background Blender child at a time, serialized sequentially.
- Launch with `nice -n 10`, `PYTHONPYCACHEPREFIX` inside the job's isolated runtime/temp directory, `PYTHONDONTWRITEBYTECODE=1`, `sys.dont_write_bytecode = True`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=4`, and process-local `BLENDER_USER_CONFIG`, `XDG_CACHE_HOME`, `TMPDIR`, `TMP`, `TEMP` initialized with a copy of `work/v12/profile_03/isolated_config/userpref.blend` (`d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561`). Any standard Python `__pycache__/*.pyc` files under `/home/agile/Applications/Blender/` or project `scripts/__pycache__` remain explicitly permitted as benign interpreter cache.
- Before every child launch, verify: no foreign background Blender is tampered with, any running owner GUI Blender process is left completely untouched, and system available RAM is **≥10 GiB**.
- Sample resources every ~1 s during execution: stop only your own child if own RSS exceeds **9 GiB**, or if system available RAM falls below **4.5 GiB** on two consecutive samples; use a **360 s** watchdog for `960 × 540` / scene-split jobs and a **900 s** watchdog for detailed crop/border jobs.
- Verify before and after every child that global `/home/agile/.config/blender/5.3/config/userpref.blend` (`8c52b5cf0d5ac23a35c9496e442a37c69399203b47b32842dd76d05653c29c02`) and all pinned input `.blend` files are unchanged.

## Authority and mutation axes

Changed-path allowlist:
- `blender/kysucka_chata_exterier.blend`
- `blender/kysucka_chata_interier.blend`
- `model/shared_envelope_v18.json`
- `model/parameters.json` (only adding/updating `forest_realism_v18`; all 20 prior top-level keys unchanged)
- `scripts/v18_split_forest.py`
- `assets/ASSET_MANIFEST.md` (appending the V18 asset section; all prior sections unchanged)
- `assets/models/tevy_norway_spruce_v1/{lod0,lod1,lod2}.glb` (limited to adopted LODs)
- `assets/textures/forest_v18/forrest_ground_01/forrest_ground_01_{diff_2k.jpg,nor_gl_2k.jpg,rough_2k.jpg,disp_2k.png}`
- `assets/textures/forest_v18/leaves_forest_ground/leaves_forest_ground_{diff_2k.jpg,nor_gl_2k.jpg,rough_2k.jpg,disp_2k.png}`
- `work/v18/stage0/raw/**` (the 11 pinned Stage 0 files)
- `work/v18/stage0/sidecars/lod{0,1,2}/{source.gltf,source.bin,image-00.ktx2,image-01.ktx2,image-02.ktx2,image-03.ktx2}`
- `work/v18/stage0/{normalized.blend,assets.json,resources.json,comparison-crown.png,comparison-root.png,comparison-bark.png,comparison-soil.png}`
- `work/v18/stage1/{kysucka_chata_exterier.blend,kysucka_chata_interier.blend,dependencies.json,portability.json,basement.json,cross_sections.csv,basement_plan.svg,cross_sections.svg,resources.json}`
- `work/v18/stage1/{source,exterier,interier}-{wide,gable,north,hero,gallery}.png`
- `work/v18/stage2/{before.blend,candidate.blend,pilot.json,forest_inventory.csv,trail_stations.csv,resources.json}`
- `work/v18/stage2/{before,after}-{wide,right,forest,root,trail}.png`
- Temporary sandbox directory `/tmp/opencode/v18_verify/**` (must be completely removed after readback before submitting the report)
- Direct-write terminal report `/home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/01_report_01.md`

Implementation boundaries:
- Positive authority: read access to `R`, `R/work/**`, and `/home/agile/meta/projects/kysucka_moderna_chata/00/**`; bounded Stage 0 HTTPS fetches strictly for the 11 SHA-256-pinned CC0 files listed in `01_report_00.md` §2; isolated headless Blender 5.3.0 execution and `bwrap --unshare-net` offline verification using `/tmp/opencode/v18_verify/` (cleaned before report); writes strictly to the Changed-path allowlist above and direct write of `T/01_report_01.md`.
- Negative authority: no modification of `work/v17/**`, `work/v16/**`, `work/v10/**`, or any existing `blender/kysucka_chata_*.blend` predecessor (`seed` through `v09_study`); no Stage 3 full-margin expansion or north trail connector build in this exchange (Stage 3 awaits visual review of the Stage 2 pilot); no live MCP calls (`tools.blender.*` prohibited); no GUI window launch; no touching global Blender preferences; no package/runtime installation; no Git stage, commit, or push in any repository; no 2D image retouch/post-processing; and never emit the project closure signal.

Repository mutation: `blender/kysucka_chata_exterier.blend`, `blender/kysucka_chata_interier.blend`, `model/shared_envelope_v18.json`, `model/parameters.json`, `scripts/v18_split_forest.py`, `assets/ASSET_MANIFEST.md`, `assets/models/tevy_norway_spruce_v1/**`, `assets/textures/forest_v18/**`, and untracked `work/v18/{stage0,stage1,stage2}/**` as listed in the Changed-path allowlist
Host/remote mutation: bounded Stage 0 HTTPS fetches of the 11 SHA-256-pinned CC0 files and temporary `/tmp/opencode/v18_verify` sandbox directory for isolated headless Blender 5.3.0 verification (must be removed before report; zero persistent host change)
Trace persistence: direct-write `/home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/01_report_01.md`

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
Downloadable prompt filename: 01_implementation_01.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18
Report filename: 01_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

## Validation and required evidence

Evidence tier: E2
Evidence tier basis: reversible scene split into standalone products, offline asset normalization, shared-envelope and basement cross-section verification, and isolated Stage 2 forest pilot build with matched CPU4 renders
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: cold-open offline `bwrap --unshare-net` portability, shared-envelope digest (`87288303...`), and `IsViewport` working-branch checks
Affected tests: Stage 0 asset pixel/alpha readback, Stage 1 matched comparison renders (`{source,exterier,interier}-{wide,gable,north,hero,gallery}.png`), Stage 2 pilot idempotence, triangle-evaluated root support, crown/corridor clearance, and matched before/after renders (`{before,after}-{wide,right,forest,root,trail}.png`)
New causal regression: Stage 1 shared-envelope digest and zero-library cold-open sandbox check + Stage 2 eye-level forest-margin witness (`CAM_V18_FOREST_MARGIN`) and overhead trail-occlusion overlay
Broad or full suite: not-used
Runtime or testbed: isolated headless Blender 5.3.0 CLI with MCP-disabled preferences and `bwrap --unshare-net`
Independent acceptance: not-required

Combined implementation envelope: allowed
Authorized implementation stages: (0) Stage 0 raw hash verification, KTX2-sidecar normalization, offline packed texture readback, asset promotion to `assets/`, and controlled single-tree/soil A/B renders; (1) Stage 1 scene split from `kysucka_chata_v17_komplet_3d.blend`, `model/shared_envelope_v18.json`, `bwrap --unshare-net` cold-open portability check, matched comparison renders, basement handoff package (`basement.json`, `cross_sections.csv`, `basement_plan.svg`, `cross_sections.svg`), and promotion to `blender/kysucka_chata_exterier.blend` and `blender/kysucka_chata_interier.blend`; (2) Stage 2 right-valley Kysuce forest pilot and trail diagnosis on `work/v18/stage2/candidate.blend` (leaving `blender/kysucka_chata_exterier.blend` at its Stage 1 hash), idempotence/support/clearance/cold-reopen checks, matched before/after pilot renders (`wide`, `right`, `forest`, `root`, `trail`), and terminal report `01_report_01.md`
Implementation stage gates: every failed gate stops the sequence; Stage 0 must pass before Stage 1, and Stage 1 must pass before Stage 2 begins
Rollback or recovery checkpoint: immutable `work/v17/complete_3d/kysucka_chata_v17_komplet_3d.blend` (`8a733770...`) and all prior `blender/` and `work/` files remain untouched; Stage 1 products in `blender/` remain untouched by Stage 2 pilot work in `work/v18/stage2/`
Activated stricter profile: none
Terminal implementation report point: one, at completion of Stage 2 pilot verification (before Stage 3)

Stopping conditions: failed repository/input/asset SHA-256 gate; foreign background Blender contention; own RSS >9 GiB or system available RAM <4.5 GiB; Stage 1 offline portability or shared-envelope digest mismatch; Stage 2 support/clearance/idempotence/cold-reopen failure; `/tmp/opencode/v18_verify` cleanup failure. Stop at the end of Stage 2 and report; do not proceed to Stage 3 in this grant.

Completion and report contract: begin `01_report_01.md` on line 1 with `### Report for ORCHESTRATOR_CHAT`; echo the coordinates (`kysucka-moderna-chata-split-and-forest-realism-v18`, `01`, `02`) once; include the compact core (`Status: PASS | PARTIAL | BLOCKED`, `Phase-qualified result: implementation-PASS | not-applicable`, `Start commit` / `End commit`, complete changed/created files and SHA-256 table including `blender/kysucka_chata_exterier.blend`, `blender/kysucka_chata_interier.blend`, `model/shared_envelope_v18.json`, `scripts/v18_split_forest.py`, `work/v18/stage2/candidate.blend`, and all Stage 0/1/2 renders and JSON/CSV/SVG outputs, validation summary with render wall times, peak RSS, minimum available RAM, cold-open/portability results, young-tree height ratios in the pilot, and trail continuity measurements, Git result = no writes, deviations/risks, one smallest next step, `Report justification: new-mutation`, authority-expiry statement, `Orchestration critique` `MEASURED` / `LEAD`, `Resolved Execution Issues / Near-Misses`, and `Pre-Existing Failure Classification`). Set `Logical-whole closure: not-closed`. Write `T/01_report_01.md` directly and read it back completely before returning your short completion notice.

Authority expiry: this terminal report, cancellation, or supersession ends this grant; retained context is convenience, not continuing authority.

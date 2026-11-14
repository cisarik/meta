# Implement realistic exterior timber and foreground rustic fence (v03)

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-realistic-timber-and-foreground-fence
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: Implementation
Task identity: BLENDER-MCP-REALISTIC-TIMBER-AND-FOREGROUND-FENCE-IMPLEMENTATION
Delivery route: manual Cooperator delivery
Continuity anchor: terminal PASS planning report projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/01_report_00.md (SHA-256 e8797b8cd1f7a1c4c80a5ac81e14995573f94449b3297b99215add5e8bca6c5c) from Worker session 01 / exchange 01 at project commit d67431d1678de511e06a8ad04cd632ae4899cdc4
Authority renewal: prior 01/01 planning authority expired at terminal report submission; this prompt grants complete new bounded implementation, official CC0 asset-download, live-MCP scene refinement/render/save, source-replay verification, Meta evidence persistence, and project commit/publication authority for exchange 01/02
Evidence posture: non-independent (same healthy Worker session 01 continuing from accepted 01/01 plan; retained context is convenience only and must be re-gated against current repository and live MCP state)
Reasoning recommendation: Standard/Medium — bounded execution of the accepted 4-part timber/fence technical plan with deterministic UV/shader/fence rules and source replay
Recommended context capacity: approximately 250k tokens
Implementation authority: explicit
Exact baseline: d67431d1678de511e06a8ad04cd632ae4899cdc4
Changed-path allowlist: AGENTS.md, README_SK.md, assets/ASSET_MANIFEST.md, assets/textures/wood/coated_pine_02/coated_pine_02_diff_2k.jpg, assets/textures/wood/coated_pine_02/coated_pine_02_nor_gl_2k.jpg, assets/textures/wood/coated_pine_02/coated_pine_02_rough_2k.jpg, assets/textures/wood/rough_wood/rough_wood_diff_2k.jpg, assets/textures/wood/rough_wood/rough_wood_nor_gl_2k.jpg, assets/textures/wood/rough_wood/rough_wood_rough_2k.jpg, blender/kysucka_chata_mcp_v03.blend, docs/OPERATIONS.md, model/parameters.json, scripts/build_scene.py, scripts/timber_fence_v03.py
Implementation boundaries: download the 6 official CC0 2K Poly Haven wood texture maps and record assets/ASSET_MANIFEST.md; save gitignored work/mcp-v03-before.blend; freshly render unchanged v02 baseline at 1448x1086 96-sample OIDN-denoised Cycles CPU to renders/before.png; implement scripts/timber_fence_v03.py and apply MAT_TIMBER_EXTERIOR (89 objects) and MAT_TIMBER_FENCE + rebuilt foreground fence (26 posts + continuous rails) on live v02 via MCP; render selected v03 at identical 1448x1086 96-sample OIDN-denoised Cycles CPU to renders/after.png and compose labelled renders/timber_details.png; pack textures and save active blender/kysucka_chata_mcp_v03.blend; sync model/parameters.json, scripts/build_scene.py, and narrow Slovak/English docs; verify cold CLI reopen of v03 and disposable source replay to work/v03_source_replay.blend; stage, commit, and non-force push the 14 tracked project paths to origin main; write Meta evidence/renders, reconcile ../00_RUN_MAP.md, and write/read back 01_report_01.md
Independence required: no

Evidence tier: E2
Evidence tier basis: cross-cutting reversible live-scene material/UV/fence refinement, CC0 PBR asset integration, source-replay verification, matched 1448x1086 denoised Cycles renders, and non-force Git publication
Authorized implementation stages: (1) repository/hash/live-MCP re-gating and before-checkpoint save; (2) official 2K CC0 Poly Haven texture download, MD5/SHA-256 verification, grain-axis inspection, and ASSET_MANIFEST.md creation; (3) fresh 1448x1086 96-sample denoised Cycles CPU baseline render of unchanged v02 to renders/before.png; (4) implementation of scripts/timber_fence_v03.py, model/parameters.json, and scripts/build_scene.py hook, live MCP application of MAT_TIMBER_EXTERIOR, MAT_TIMBER_FENCE, metric UVs, and foreground fence placement (Trial 1 / Trial 2), and separate MCP readback; (5) matched 1448x1086 96-sample denoised Cycles CPU render of v03 to renders/after.png, visual pixel inspection via look, and labelled renders/timber_details.png composition; (6) texture packing, canonical scene/viewport restoration, active blender/kysucka_chata_mcp_v03.blend save, cold CLI reopen check, and disposable source replay to work/v03_source_replay.blend; (7) narrow documentation updates, ap doctor check, explicit 14-path git stage/commit/non-force push to origin main, Meta evidence/run-map persistence, and terminal report 01_report_01.md write/readback
Combined implementation envelope: allowed
Implementation stage gates: stop on any failed baseline/hash/MCP precondition, download/hash mismatch, non-target fingerprint drift, render/denoiser failure, cold-reopen or source-replay tolerance failure, or pre-push origin/main parent mismatch
Independent acceptance: not-required
Rollback or recovery checkpoint: /Users/agile/Projects/kysucka_moderna_chata/work/mcp-v03-before.blend and preserved blender/kysucka_chata_mcp_v02.blend
Activated stricter profile: none
Terminal implementation report point: after public origin/main verification and complete readback of 01_report_01.md

## Goal and Accepted Plan Summary

Execute the accepted `01/01` implementation plan (`01_report_00.md`) in the same healthy Worker session (`01/02`) with Native planning mode `not-used` (OFF):

1. **Re-gate repository, hashes, and live Blender 5.2.3 LTS session**:
   - Confirm `P = /Users/agile/Projects/kysucka_moderna_chata` is on clean `main` at `d67431d1678de511e06a8ad04cd632ae4899cdc4` (`origin/main` and public `refs/heads/main` equal), `.ap` at `d7023cf037f6d17885c3ede5c04812c61640da50` (`./.ap/ap doctor` PASS), and all protected SHA-256 hashes match:
     - `blender/kysucka_chata_seed.blend`: `9fcea3fc25eeaec1e791b772c4d4ae4f825f103a139154ab45c2c420718226e0`
     - `blender/kysucka_chata_mcp_v01.blend`: `227edd9356a0e2917486351bce6e6fdbb62c58eacbfbb96101c1872d5235e4a8`
     - `blender/kysucka_chata_mcp_v02.blend`: `010f47a81a4fde2e936f401e87b8bc11af76a8e72d71811d68dd910da0b27249`
     - `reference/kysucka_chata_moderna.png`: `05bc3e72161e5945379c86da80450ffdf82ddce6dbdd9b9e77071aa79cdecc96`
     - `model/parameters.json`: `2d441b08d658e4aa4c8fccc5e71c76eb16666deeb4401cdd0b973c379901cada`
     - `scripts/build_scene.py`: `4310a6ed69e577157c2a605b5c2a7b0128ca62ab667f69ea72aece47563884c2`
   - Via MCP, confirm `blender/kysucka_chata_mcp_v02.blend` is open (`is_saved=True`, `is_dirty=False`, `mode='OBJECT'`, `is_job_running('RENDER')=False`, `656` objects, `13,438` mesh vertices, locked `CAM_A_REFERENCE` at `[21.5, -10.0, 1.25]`, target `[8.5, 2.5, 1.25]`, `35 mm`, `shift_y = 0.105`).
   - Capture in-memory preservation fingerprints of:
     - locked `CAM_A_REFERENCE`,
     - all excluded objects (`656 - 89 - 28 = 539` non-target objects, including all `77` excluded `MAT_WOOD_H` / `MAT_WOOD_V` consumers, roof, stone, glass, interior furniture/partitions/doors, fireplace/chimney, lights, world, vegetation/trees/shrubs, terrain, and path),
     - vertex coordinates, polygon topology, world transforms, and existing modifiers (`BEVEL`, `WEIGHTED_NORMAL`) of all `89` exterior timber objects (`CLADDING_front*` 35, `CLADDING_rear*` 33, `GABLE_timber*` 16, `SOFFIT_wood*` 2, `WOOD_BAY_post*` 2, `GABLE_other_proposed` 1),
     - original material node graphs (`MAT_WOOD_H`, `MAT_WOOD_V`, and all non-timber materials).
   - Before any setting or scene change, save `P/work/mcp-v03-before.blend` via MCP (`bpy.ops.wm.save_as_mainfile(filepath=..., copy=True, compress=True)`).
2. **Download and verify the 6 official 2K CC0 Poly Haven wood maps**:
   - Create `P/assets/textures/wood/coated_pine_02/` and `P/assets/textures/wood/rough_wood/` and download:
     - `https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/coated_pine_02/coated_pine_02_diff_2k.jpg` (`2,985,006` B, MD5 `9d2bb5797918490d00743efe737c1471`)
     - `https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/coated_pine_02/coated_pine_02_rough_2k.jpg` (`620,683` B, MD5 `44dd138d932b3f966e4be7ae21f81030`)
     - `https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/coated_pine_02/coated_pine_02_nor_gl_2k.jpg` (`1,418,403` B, MD5 `e4ca3043d18d35aee836fc26cfc3ac1e`)
     - `https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/rough_wood/rough_wood_diff_2k.jpg` (`2,223,327` B, MD5 `f5f9c55696f047ceaa49dc97c5aa5526`)
     - `https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/rough_wood/rough_wood_rough_2k.jpg` (`810,338` B, MD5 `832d6d549a8e76c16b9af2586f429d6c`)
     - `https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/rough_wood/rough_wood_nor_gl_2k.jpg` (`2,520,021` B, MD5 `62594f2d00eb246581b9d4fde30209f1`)
   - Verify exact byte sizes, MD5 checksums, and SHA-256 hashes. Inspect the dominant grain orientation of both diffuse maps (comparing horizontal vs vertical image gradients or visual inspection via `look(image=...)`) so that your metric UV mapping aligns the texture's actual wood grain direction with `u_m` (longitudinal axis of each board/post/rail/soffit), applying a 90° UV swap `(u, v) -> (v, u)` if the image grain runs along image V.
   - Write `P/assets/ASSET_MANIFEST.md` recording asset/page/license URLs (`https://polyhaven.com/a/coated_pine_02`, `https://polyhaven.com/a/rough_wood`, `https://polyhaven.com/license`), downloaded relative paths, map roles, color spaces, 2048×2048 resolution, physical scale (`1.05 m` and `0.50 m`), MD5, SHA-256, confirmed grain-axis orientation, and shader/UV usage (confirming no image files were modified on disk).
3. **Render matched `1448 × 1086` denoised baseline (`renders/before.png`) from unchanged `v02`**:
   - Create `M/renders/` and `M/evidence/` under `M = /Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence`.
   - Configure the common comparison render profile on unchanged `v02` (`1448 × 1086` at `100%`, `CYCLES`, `CPU`, `samples = 96`, `use_denoising = True`, `denoiser = 'OPENIMAGEDENOISE'`, `frame_current = 0`, `cycles.seed = 0`, `cycles.use_animated_seed = False`, `AgX`, look `None`, `exposure = 0.0`, `gamma = 1.0`, opaque film, 8 threads). *(Note: in Blender 5.2.3 LTS RNA, `scene.cycles.denoiser` is already `'OPENIMAGEDENOISE'`; check `scene.cycles.denoiser == 'OPENIMAGEDENOISE'` directly rather than `bl_rna.properties['denoiser'].enum_items`, which is dynamically populated and empty on static RNA inspection).*
   - Perform a separate MCP readback of the render profile and non-target fingerprints, then render unchanged `v02` to `M/renders/before.png` (`write_still=True`). Do NOT save over `v02`.
4. **Implement `scripts/timber_fence_v03.py`, `model/parameters.json`, and `scripts/build_scene.py`, and apply on live `v02` via MCP**:
   - Implement `P/scripts/timber_fence_v03.py` exposing `apply_v03(scene, parameters, project_root)` and `configure_comparison_render(scene)` as planned in `01_report_00.md`:
     - **`MAT_TIMBER_EXTERIOR`**: uses `coated_pine_02` maps (`sRGB` for diff, `Non-Color` for rough and `nor_gl`), explicit `ShaderNodeUVMap(uv_map='UVMap')`, warm honey/brown grading (`Object Info -> Random` brightness variation `0.94–1.06`), roughness remapped to `0.44–0.56` ± `0.02` clamped to `0.42–0.58`, tangent-space `ShaderNodeNormalMap` (`uv_map='UVMap'`, strength `~0.30`) fed into subtle `ShaderNodeBump` (distance `0.0002 m`, strength `0.08`), metallic `0.0`, coat `0.0`. Assigned to the exact **89 exterior timber objects** (`CLADDING_front*` 35, `CLADDING_rear*` 33, `GABLE_timber*` 16, `SOFFIT_wood*` 2, `WOOD_BAY_post*` 2, `GABLE_other_proposed` 1).
     - **`MAT_TIMBER_FENCE`**: uses `rough_wood` maps (`sRGB` for diff, `Non-Color` for rough and `nor_gl`), explicit `ShaderNodeUVMap(uv_map='UVMap')`, weathered desaturated grey/brown grading (`Object Info -> Random` brightness variation `0.90–1.10`), roughness remapped to `0.74–0.86` ± `0.02` clamped to `0.72–0.88`, tangent-space `ShaderNodeNormalMap` (`uv_map='UVMap'`, strength `~0.50`) fed into subtle `ShaderNodeBump` (distance `0.0007 m`, strength `0.12`), plus subtle procedural end-grain shading on upward/downward cap normals (`|normal.z| > 0.85` in local post space). Assigned only to rebuilt `FENCE_post_proxy*` and `FENCE_rail_proxy*`.
     - **Metric `UVMap` on all target meshes**: compute `u_m = dot(p, longitudinal_axis)`, `v_m = dot(p, transverse_axis)`, `UV = (u_m / tile_m + du, v_m / tile_m + dv)` (or swapped `(v_m / tile_m + dv, u_m / tile_m + du)` if the texture's wood grain runs along image V!), with `tile_m = 1.05` (`MAT_TIMBER_EXTERIOR`) and `tile_m = 0.50` (`MAT_TIMBER_FENCE`), and `du, dv` derived deterministically from two 64-bit chunks of `hashlib.sha256(obj.name.encode()).digest()`. Ensure `UVMap` is created on `GABLE_timber*`, `GABLE_other_proposed`, and `SOFFIT_wood*` as well as cladding, bay posts, and fence members, with zero degenerate visible faces.
     - **Foreground rustic fence (`FENCE_post_proxy*` + `FENCE_rail_proxy*`)**:
       - Evaluate Trial 1 (`(16.60, -8.62) -> (18.25, 1.00)`) first (and Trial 2 `(16.75, -8.70) -> (17.05, -7.20) -> (18.25, 1.00)` only if Trial 1 fails eligibility) using `random.Random(13703)` only.
       - 26 posts total (25 split stakes + 1 thicker anchor post at index 4, `s = 0.14`, section `0.16 × 0.13 m`, `Z_top = 0.62 m`; split stakes have foot datum `Z = -0.075 m` embedded in `-0.055 m` terrain, top `Z = 0.58 ± 0.04 m`, width `0.085 ± 0.015 m`, thickness `0.065 ± 0.010 m`, lean `<= 2°`, `0.003 m` 2-segment bevel + weighted normals; continuous lower and upper rails at `Z = 0.19 m` and `Z = 0.43 m`, section `0.055 × 0.065 m`, offset `0.020 m` toward camera, physically intersecting every leaning stake so rails and posts connect with zero air gaps).
     - **Global RNG isolation in `scripts/build_scene.py`**: keep the original fence loop and its 26 `random.uniform(...)` draws intact before tree generation; invoke `apply_v03(scene, P, ROOT)` after vegetation/world/camera construction (just before `bpy.ops.file.pack_all()` and `save_as_mainfile()`), asserting `random.getstate()` equality before and after `apply_v03` so all 38 background conifers and the apple tree remain 100% identical.
5. **Render matched `renders/after.png`, inspect pixels, and compose `renders/timber_details.png`**:
   - Perform a separate MCP readback of material assignments, UV bounds, fence world endpoints and camera UV projections, and preservation fingerprints.
   - Render `M/renders/after.png` under the exact same `1448 × 1086`, 96-sample, OIDN-denoised Cycles CPU profile.
   - Inspect `M/renders/before.png`, `M/renders/after.png`, and `P/reference/kysucka_chata_moderna.png` via `look(image=...)`. If grain orientation, normal strength, tint, or roughness needs one focused adjustment within scope, apply it in `scripts/timber_fence_v03.py` and `model/parameters.json`, re-apply via MCP, and re-render `M/renders/after.png`.
   - Compose `M/renders/timber_details.png` from the exact `1448 × 1086` `before.png` and `after.png` renders with native-pixel crops of the four regions (`Facade: (550, 619, 1000, 804)`, `Gable: (1042, 130, 1448, 673)`, `Soffit: (246, 550, 1000, 665)`, `Fence: (174, 793, 811, 1086)`), clearly labelled `Pred (v02)` / `Po (v03)` using macOS AppKit (`/usr/bin/osascript` or Python) with no AI retouching. Inspect `M/renders/timber_details.png` via `look(image=...)`.
6. **Save `blender/kysucka_chata_mcp_v03.blend`, verify cold CLI reopen, and verify disposable source replay**:
   - In live Blender via MCP: ensure all 6 wood texture images use portable relative paths (`//../assets/textures/wood/...`), call `bpy.ops.file.pack_all()` so all 6 wood textures and `REF_kysucka_chata_moderna` are packed in `v03`, restore canonical `scene.render.filepath = '//../work/camera_a.png'`, keep `1448 × 1086` at `100%`, `96` samples, `CYCLES` `CPU`, `use_denoising = True` (`OPENIMAGEDENOISE`), and Layout viewport in `CAMERA` + `RENDERED` (scene lights/world enabled, `16` preview samples), and save active `P/blender/kysucka_chata_mcp_v03.blend` (`copy=False, compress=True`).
   - Verify total size of `assets/` + `blender/kysucka_chata_mcp_v03.blend` is `< 80 MiB` and every tracked file is `< 90 MiB`.
   - Run cold CLI reopen check on `P/blender/kysucka_chata_mcp_v03.blend` using `/Applications/Blender.app/Contents/MacOS/Blender --background --disable-autoexec P/blender/kysucka_chata_mcp_v03.blend --python-exit-code 2 --python P/scripts/inspect_scene.py` plus read-only assertions verifying packed textures, relative paths, consumer counts, UV layers, fence projections, and preservation fingerprints.
   - Run disposable source replay in a separate CLI process:
     `/Applications/Blender.app/Contents/MacOS/Blender --background --factory-startup --python-exit-code 2 --python P/scripts/build_scene.py -- --output P/work/v03_source_replay.blend`
     and verify that `work/v03_source_replay.blend` agrees with saved `blender/kysucka_chata_mcp_v03.blend` within the stated tolerances (`1e-5 m` geometry/positions, `1e-6` UVs and scalar shader values, `1e-6 rad` rotations, identical consumer sets, and zero drift on excluded objects/trees). Also verify idempotence (`apply_v03` called a second time produces identical target state and object/material/image counts).
7. **Update documentation, publish project commit, and write Meta evidence + report**:
   - Narrowly update `P/AGENTS.md`, `P/docs/OPERATIONS.md`, and `P/README_SK.md` for `v03` (current working file `blender/kysucka_chata_mcp_v03.blend`, SHA-256 table, `assets/textures/wood/` + `assets/ASSET_MANIFEST.md`, `scripts/timber_fence_v03.py` source-replay notes, and `blender-mcp-live-v1` whole-03 activation), keeping the managed AP block and the entire `Closure and Git gates` section of `AGENTS.md` byte-identical.
   - Run `./.ap/ap doctor` (`PASS`).
   - Stage only the exact 14 tracked project paths, verify `git ls-remote origin refs/heads/main` still equals `d67431d1678de511e06a8ad04cd632ae4899cdc4`, commit with a clear subject (e.g. `feat: add PBR exterior timber and reposition foreground rustic fence in v03`), non-force push to `origin main`, and verify public `refs/heads/main` equals the new commit SHA.
   - Write `M/evidence/timber_fence_comparison.md` and `M/renders/render_metadata.json`, mechanically persist the Master run-map snapshot from `00_handout.md` to `/Users/agile/meta/projects/kysucka_moderna_chata/00/00_RUN_MAP.md` (after checking for any newer owner content), and write and fully read back your terminal report `M/01_report_01.md`.

## Execution Route and Authority (AP RF-16)

Execution route: **task-specific bounded deviation `blender-mcp-live-v1`** under AP RF-16, combined with `blender-local-v1` CLI cold verification and disposable source replay:
- **Activated live route**: `blender-mcp-live-v1` using Blender MCP tools (`get_addon_status`, `get_scene_info`, `execute_blender_code`, `look`) on the open Blender 5.2.3 LTS GUI session.
- **Activated CLI verification route**: `/Applications/Blender.app/Contents/MacOS/Blender --background` for read-only cold reopen of `v03` and factory-startup source replay into `work/v03_source_replay.blend`.

External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 00/03-realistic-timber-and-foreground-fence
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_implementation_01.md
Destination path: /Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence
Report filename: 01_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: /Users/agile/Projects/kysucka_moderna_chata/AGENTS.md, /Users/agile/Projects/kysucka_moderna_chata/README_SK.md, /Users/agile/Projects/kysucka_moderna_chata/assets/ASSET_MANIFEST.md, /Users/agile/Projects/kysucka_moderna_chata/assets/textures/wood/coated_pine_02/coated_pine_02_diff_2k.jpg, /Users/agile/Projects/kysucka_moderna_chata/assets/textures/wood/coated_pine_02/coated_pine_02_nor_gl_2k.jpg, /Users/agile/Projects/kysucka_moderna_chata/assets/textures/wood/coated_pine_02/coated_pine_02_rough_2k.jpg, /Users/agile/Projects/kysucka_moderna_chata/assets/textures/wood/rough_wood/rough_wood_diff_2k.jpg, /Users/agile/Projects/kysucka_moderna_chata/assets/textures/wood/rough_wood/rough_wood_nor_gl_2k.jpg, /Users/agile/Projects/kysucka_moderna_chata/assets/textures/wood/rough_wood/rough_wood_rough_2k.jpg, /Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v03.blend, /Users/agile/Projects/kysucka_moderna_chata/docs/OPERATIONS.md, /Users/agile/Projects/kysucka_moderna_chata/model/parameters.json, /Users/agile/Projects/kysucka_moderna_chata/scripts/build_scene.py, /Users/agile/Projects/kysucka_moderna_chata/scripts/timber_fence_v03.py (plus disposable gitignored /Users/agile/Projects/kysucka_moderna_chata/work/mcp-v03-before.blend and /Users/agile/Projects/kysucka_moderna_chata/work/v03_source_replay.blend)
Host/remote mutation: official CC0 2K texture downloads from dl.polyhaven.org; live Blender 5.2.3 LTS MCP checkpoint/material/UV/fence/render/pack/save operations producing blender/kysucka_chata_mcp_v03.blend; cold CLI reopen and factory-startup CLI source replay to work/v03_source_replay.blend; non-force git push of the single project commit to origin main (https://github.com/cisarik/kysucka_moderna_chata)
Trace persistence: direct-write /Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/renders/before.png, /Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/renders/after.png, /Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/renders/timber_details.png, /Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/renders/render_metadata.json, /Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/evidence/timber_fence_comparison.md, /Users/agile/meta/projects/kysucka_moderna_chata/00/03-realistic-timber-and-foreground-fence/01_report_01.md, /Users/agile/meta/projects/kysucka_moderna_chata/00/00_RUN_MAP.md

Positive authority:
- Create directories `P/assets/textures/wood/coated_pine_02`, `P/assets/textures/wood/rough_wood`, `M/renders`, and `M/evidence`.
- Download the 6 exact 2K JPG files from `https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/...` and write `P/assets/ASSET_MANIFEST.md`.
- Write/update the 14 allowed project files and disposable gitignored `P/work/mcp-v03-before.blend` and `P/work/v03_source_replay.blend`.
- Execute the authorized live Blender MCP operations, cold CLI reopen check, and disposable CLI source-replay check.
- Stage the exact 14 tracked project paths (`git add <explicit-paths>`), commit once on `main`, and push non-force (`git push origin main`) after verifying `origin/main` equals `d67431d1678de511e06a8ad04cd632ae4899cdc4`.
- Write the 6 Meta files under `M/`, mechanically update `/Users/agile/meta/projects/kysucka_moderna_chata/00/00_RUN_MAP.md` to the Master snapshot in `00_handout.md`, and read back `M/01_report_01.md` completely.

Negative authority:
- Never resave or modify `blender/kysucka_chata_seed.blend`, `blender/kysucka_chata_mcp_v01.blend`, `blender/kysucka_chata_mcp_v02.blend`, or `reference/kysucka_chata_moderna.png`.
- Never modify `CAM_A_REFERENCE`, building walls/openings/doors, roof, chimney/fireplace, interior furniture/partitions, glass, lights, world, vegetation (`SHRUB_proxy*`, `FLOWER_proxy*`, `APPLE_*`, `CONIFER_*`, `TREE_trunk_proxy*`), terrain, path, or the 77 excluded `MAT_WOOD_H` / `MAT_WOOD_V` consumers.
- Never regenerate CAD/PDF (`scripts/build_documents.py`) or modify `scripts/design.py` or `scripts/render_scene.py`.
- Never use `git add .`, `git add -A`, force-push, or perform any Git staging/commit/push in `/Users/agile/meta`.
- Never quote, print, or reproduce the literal project closure signal from `AGENTS.md`.

## Validation, Rollback, and Report Contract

Validation required before reporting `PASS`:
1. All 6 downloaded texture files match their expected byte sizes and MD5s; SHA-256 hashes are recorded in `assets/ASSET_MANIFEST.md`; `assets/` + `v03.blend` total `< 80 MiB` and every tracked file `< 90 MiB`.
2. Non-target preservation fingerprints match 100% across `v02` start, live `v03`, and cold CLI reopen of `v03`; all 89 exterior timber meshes retain exact vertex positions, polygon topology, transforms, and bevel/weighted-normal modifiers.
3. Both `renders/before.png` and `renders/after.png` are `1448 × 1086` PNGs rendered under identical 96-sample OIDN-denoised Cycles CPU settings; `renders/timber_details.png` shows the 4 labelled native-pixel before/after crops; all renders are visually inspected via `look(image=...)`.
4. Cold CLI reopen of `blender/kysucka_chata_mcp_v03.blend` and disposable factory-startup source replay to `work/v03_source_replay.blend` exit `0` and agree within stated tolerances (`1e-5 m` geometry, `1e-6` UV/shader scalars, `1e-6 rad` rotations, zero tree/RNG drift, idempotent `apply_v03`).
5. Live Blender 5.2.3 LTS ends on saved, clean (`is_saved=True, is_dirty=False`), idle (`is_job_running('RENDER')=False`) `blender/kysucka_chata_mcp_v03.blend`.
6. `./.ap/ap doctor` exits `0` (`PASS`), `git status --short` in project is empty after committing the 14 tracked files, and `git ls-remote origin refs/heads/main` matches the new commit SHA.

Begin `M/01_report_01.md` with `### Report for ORCHESTRATOR_CHAT`, echo this prompt's three coordinate fields (`Logical whole identity`, `Worker session ordinal`, `Worker exchange ordinal`) once, and include the compact core (`status: PASS`, `Phase-qualified result: implementation-PASS`, start/end commits, changed files and SHA-256 hashes, validation and publication results, note reminding Cooperator that `renders/render_metadata.json` needs `git add -f` in Meta, `Report justification: new-mutation`, `Logical-whole closure: not-closed`, `Orchestration critique`, `Resolved Execution Issues / Near-Misses`, `Pre-Existing Failure Classification`, and `Authority expiry`). Save `M/01_report_01.md`, read it back completely, and return a brief completion notice with its SHA-256.

# Implementation — Jelena grass and ground-cover realism (`v006`)

Persistent role identity: WORKER
Logical whole identity: jelena-grass-and-ground-cover-realism
Worker session ordinal: 01
Worker exchange ordinal: 04
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Fresh Implementation Worker
Phase: Implementation
Task identity: JELENA-GRASS-AND-GROUND-COVER-REALISM-IMPLEMENTATION-03
Delivery route: manual Cooperator delivery
Reasoning recommendation: Standard/Medium — the technical architecture, clump geometry, shader, post-distribution clearance math, and execution sequence are resolved in the accepted plan; downgrade after planning convergence.
Independence required: no
Implementation authority: explicit
Exact baseline: cisarik/jelena HEAD c83e2baf7d6c5d9d1be4b39c7656330e410c9c6e on main, with selected Option A working source Jelena/Jelena_Realistic_v005.blend (SHA-256 892d930bd70b6e608e99db2a812204307f7ecccf3ac80bf8e1ac94e4dce735b4) and preserved committed c83e2ba checkpoint .local/checkpoints/Jelena_Realistic_v005-before-edge-grass.blend (SHA-256 2399ce17ff1c332e7302bc5d623d687655eb2b72bc225fa2be88b0834583ddf8)
Changed-path allowlist: .local/checkpoints/Jelena_Realistic_v005-before-grass-v006.blend (local untracked checkpoint, never staged), Jelena/Jelena_Realistic_v006.blend, scripts/grass_ground_cover_v006.py, evidence/grass-006/camera-a-before.png, evidence/grass-006/camera-a-after.png, evidence/grass-006/overview-before.png, evidence/grass-006/overview-after.png, evidence/grass-006/grass-detail-before.png, evidence/grass-006/grass-detail-after.png, evidence/grass-006/access-clearance.png, evidence/grass-006/manifest.json, README.md
Implementation boundaries: scene-A grass and ground-cover realism in Jelena_Realistic_v006.blend only; preserve working v005 and all prior .blend files byte-for-byte; no Git commit or push in this exchange
Continuity anchor: blocked implementation report `/Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/01_report_02.md` (SHA-256 `da934dd8a6dc443fc69976ec0de7413af5888c1d2ca9e471b1f75db53d8d4cb6`) from Worker session `01` / exchange `03`, and accepted planning report `/Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/01_report_00.md` (SHA-256 `d29b57b861bcb92b6cf8ee17bc1b03fedab493b42f5d70c58f55f2c4198482b4`) from Worker session `01` / exchange `01`.
Authority renewal: prior authority expired at the submission of `01_report_02.md`. The Cooperator confirmed that the live dirty flag came from incidental UI selection (`Stolička • sedadlo.009`) with no unsaved owner work to keep, and reloaded the saved `v005` via `Súbor → Navrátiť`. The Orchestrator verified via direct read-only MCP query that `bpy.data.is_dirty` is now `False`, `filepath` is `/Users/agile/Projects/jelena/Jelena/Jelena_Realistic_v005.blend` (disk SHA-256 `892d930bd70b6e608e99db2a812204307f7ecccf3ac80bf8e1ac94e4dce735b4`), active scene `A • Chata pri lese` has `937` objects, and Scene B has `308` objects. This prompt grants complete new bounded implementation authority in the same healthy Worker session. Retained context is convenience only, not authority; re-gate repository and live Blender state before mutating and stop on any conflict with current repository or scene evidence.
Evidence posture: non-independent

## 1. Accepted Plan and Orchestrator Refinements

Your planning report `01_report_00.md` (`d29b57b861bcb92b6cf8ee17bc1b03fedab493b42f5d70c58f55f2c4198482b4`) is **accepted** with three operational refinements grounded in your `MEASURED` critique:

1. **Post-Distribution Clearance & Inside-Mask Rejection (`MEASURED` item 1)**:
   - As you measured, upstream face selection on `Lesná čistina` (`1.440 m` face diagonals) leaves roots inside projected access footprints.
   - Build the owned flat XY mask mesh (`Maska trávy v006 • A`, `hide_render = True`, `hide_viewport = True`, in `12a • Prototypy trávy v006 • A` or `11a • Pomocné • A`) from projected copies of `Lôžko • chodník`, both paver meshes (`Chodník • terasa`, `Chodník • vstup`), `Prechod • štrk`, `Parkovanie • štrk`, `Cesta • les`, visible terrace/entry steps (`.002`/`.003` in `06b`), and the cabin/terrace keep-out boxes, flattened to one horizontal Z plane without modifying source meshes.
   - Evaluate clearance **downstream of `Distribute Points on Faces`** on the distributed points before `Instance on Points`: remove all roots inside the projected mask (using vertical Raycast against the flat mask faces and/or `Geometry Proximity` `FACES` distance `d == 0`), force short variants (`0..2`) within `0.20 m` of finished surfaces, set `effective_xy_scale = min(s, (d - 0.008) / R)`, and delete roots where `effective_xy_scale < 0.45`.
   - Assert from the final evaluated instances that **zero** roots lie inside finished surfaces and every instance satisfies `R * effective_xy_scale + 0.008 <= d`.
2. **Deterministic 9-Variant `Pick Instance` Selection (`MEASURED` item 2)**:
   - Name the 9 prototypes in excluded scene-A collection `12a • Prototypy trávy v006 • A` with zero-padded prefixes (`Tráva v006 • 00 krátka A`, `01 krátka B`, `02 krátka C`, `03 hlavná A`, `04 hlavná B`, `05 hlavná C`, `06 vyššia A`, `07 vyššia B`, `08 vyššia C`) so `Collection Info` (`Separate Children = True`, `Reset Children = True`) orders indices `0..8` deterministically.
   - Enable `Pick Instance = True` on `Instance on Points` and drive `Instance Index` per point (`45%` short `0..2`, `50%` main `3..5`, `5%` accent `6..8` outside the `0.20 m` edge zone; `100%` short `0..2` inside `0.20 m`). Assert from `evaluated_geometry()` that all 9 variants are referenced with non-zero counts and `0` instances reference `Karta trávy A` or `Karta trávy B`.
3. **Git Read-Only Until Visual Review**:
   - Do **not** run `git add`, `git commit`, or `git push` in this exchange. Produce the checkpoint, `Jelena/Jelena_Realistic_v006.blend`, `scripts/grass_ground_cover_v006.py`, `evidence/grass-006/**`, and `README.md` on disk, verify all hashes and assertions, and submit `01_report_03.md` so the Orchestrator and Michal can inspect the rendered images before publication.

## 2. Authority, Mutation Axes, and Trace Delivery

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism
Trace project key: jelena
Trace logical-whole projection identity: jelena-grass-and-ground-cover-realism
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_implementation_03.md
Destination path: /Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism
Report filename: 01_report_03.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report
Repository mutation: .local/checkpoints/Jelena_Realistic_v005-before-grass-v006.blend, Jelena/Jelena_Realistic_v006.blend, scripts/grass_ground_cover_v006.py, evidence/grass-006/camera-a-before.png, evidence/grass-006/camera-a-after.png, evidence/grass-006/overview-before.png, evidence/grass-006/overview-after.png, evidence/grass-006/grass-detail-before.png, evidence/grass-006/grass-detail-after.png, evidence/grass-006/access-clearance.png, evidence/grass-006/manifest.json, README.md
Host/remote mutation: live Blender 5.2.3 LTS session on 127.0.0.1:9876 — Save As to Jelena/Jelena_Realistic_v006.blend, scene-A grass build/validation, and sequential single-still Cycles CPU renders to evidence/grass-006/
Trace persistence: direct-write /Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/01_report_03.md
```

```text
Evidence tier: E2
Evidence tier basis: reversible scene-A candidate creation (.blend + idempotent generator + matched visual evidence) with byte-verified local checkpoint and strict Scene-B/baseline preservation
Authorized implementation stages: (1) pre-mutation re-gate and checkpoint copy; (2) Save As Jelena_Realistic_v006.blend and preservation fingerprint capture; (3) temporary 1x reference census and matched before renders; (4) patch prototype build, render, and RSS/visual check; (5) staged 25%/50%/100% rollout and density calibration; (6) final sequential after/clearance renders, idempotence/clearance/preservation assertions, settings restoration, final save of v006, manifest and narrow README update, and terminal report
Combined implementation envelope: allowed
Implementation stage gates: stop immediately if source v005 hash or Scene-B fingerprint changes, if sampled RSS reaches 4.2 GiB (simplify) or 5.0 GiB (hard stop), if any clearance/preservation assertion fails, or if any before-v006 .blend hash changes
Rollback or recovery checkpoint: /Users/agile/Projects/jelena/.local/checkpoints/Jelena_Realistic_v005-before-grass-v006.blend (SHA-256 892d930bd70b6e608e99db2a812204307f7ecccf3ac80bf8e1ac94e4dce735b4) plus .local/checkpoints/Jelena_Realistic_v005-before-edge-grass.blend (SHA-256 2399ce17ff1c332e7302bc5d623d687655eb2b72bc225fa2be88b0834583ddf8)
Activated stricter profile: none
Terminal implementation report point: after Jelena_Realistic_v006.blend, scripts/grass_ground_cover_v006.py, evidence/grass-006/**, and README.md are saved and verified on disk, and 01_report_03.md is written and read back
```

- **Execution route**: local filesystem/shell operations in `/Users/agile/Projects/jelena` and live Blender operations through the `blender` MCP server (`get_addon_status`, `get_scene_info`, `execute_blender_code`).
- **Positive authority**:
  - Create `/Users/agile/Projects/jelena/.local/checkpoints/Jelena_Realistic_v005-before-grass-v006.blend` as a byte-for-byte copy of the current `Jelena/Jelena_Realistic_v005.blend` (`892d930b...`) and verify its SHA-256.
  - Switch the live Blender session to `/Users/agile/Projects/jelena/Jelena/Jelena_Realistic_v006.blend` via `bpy.ops.wm.save_as_mainfile(filepath="/Users/agile/Projects/jelena/Jelena/Jelena_Realistic_v006.blend")` before any scene mutation.
  - Write and run `/Users/agile/Projects/jelena/scripts/grass_ground_cover_v006.py` to build the `v006` grass prototypes, shader, mask, and Geometry Nodes graph in `Jelena_Realistic_v006.blend`.
  - Add scene-A review camera `J • Tráva • detail` at `(7.95, -5.25, 0.65)`, aim `(6.95, -3.75, -0.24)`, lens `55 mm`, zero shift, DOF off, in `07e • Kamery • hodnotenie • A`.
  - Render the 7 required PNG files sequentially (one still per MCP call) into `/Users/agile/Projects/jelena/evidence/grass-006/` and write `/Users/agile/Projects/jelena/evidence/grass-006/manifest.json`.
  - Update `/Users/agile/Projects/jelena/README.md` with the narrow version/Quick Start update from Section 6 of the accepted plan.
  - Write the complete terminal report to `/Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/01_report_03.md` if and only if that file is absent, and read it back completely.
- **Negative authority**:
  - Never save over `Jelena/Jelena_Realistic_v005.blend`, `Jelena/Jelena_Realistic_v004.blend`, `Jelena/Jelena_Realistic_v003.blend`, `Jelena/Jelena_Realistic_v002.blend`, `Jelena/Jelena_Realistic_v001.blend`, or `Jelena/Jelena.blend`.
  - Never revert, stage, or overwrite the 6 uncommitted `v005` working-tree files (`Jelena/Jelena_Realistic_v005.blend`, `evidence/access-005/overview.png`, `evidence/access-005/top-view.png`, `evidence/access-005/connection-detail.png`, `evidence/access-005/manifest.json`, `scripts/access_landscape_v005.py`) or the 6 existing `.local/checkpoints/` files.
  - Never modify trees, cabin, façade, roof, glass, terrace, furniture, steps, road/parking/path geometry or materials, `Lesná pôda`, `Kameň`, existing cameras (`A`–`I`), lighting/world settings, or Scene B (`B • Zariadená dispozícia`).
  - Never un-exclude any of the 9 excluded collections (`01a`, `02a`, `05a`, `05b`, `05c`, `06`, `07b`, `09`, `10a`) or create a new view layer.
  - Never realize the full grass scatter, apply modifiers, join all geometry, or run full-scene entrypoints of `vegetation_scene_a.py`, `conifer_detail.py`, or `access_landscape_v005.py`.
  - No Git writes (`git add`, `git commit`, `git push`, `git checkout`, `git restore`, `git clean`) in Jelena, `.ap`, or Meta.
  - No package installations, network calls, external assets, or background Blender instances.

## 3. Required Execution Sequence

Execute the accepted plan in order:

1. **Step 1 — Re-Gate & Checkpoint**:
   - Verify `HEAD` is `c83e2baf7d6c5d9d1be4b39c7656330e410c9c6e`, `.ap` is `d7023cf037f6d17885c3ede5c04812c61640da50`, `Jelena/Jelena_Realistic_v005.blend` on disk is `892d930bd70b6e608e99db2a812204307f7ecccf3ac80bf8e1ac94e4dce735b4`, `Jelena/Jelena_Realistic_v004.blend` is `00d1dbe65c15a7e86ae52480b4e8aa3cad5744cac9443a10e5a5b230ea9c76aa`, and live Blender has `Jelena_Realistic_v005.blend` open with `is_dirty == False`, active scene `A • Chata pri lese` (`937` objects), Scene B (`308` objects), and `Jelena_Realistic_v006.blend` absent.
   - Copy `Jelena/Jelena_Realistic_v005.blend` to `.local/checkpoints/Jelena_Realistic_v005-before-grass-v006.blend` and verify both SHA-256 hashes equal `892d930bd70b6e608e99db2a812204307f7ecccf3ac80bf8e1ac94e4dce735b4`.
2. **Step 2 — Save As `v006` & Fingerprint Capture**:
   - In live Blender, immediately `Save As` `/Users/agile/Projects/jelena/Jelena/Jelena_Realistic_v006.blend` and confirm `bpy.data.filepath` ends with `Jelena_Realistic_v006.blend`.
   - Capture preservation fingerprints for Scene B (308 objects, transforms, mesh/material/node-group users, world `Obloha nad lesom` 0.48, lights `2.2` / `610` / `65`), Scene A cameras `A`–`I`, lights, world `Obloha nad lesom • A`, `Kameň` (25 users), `Lesná pôda` (1 user), tree transforms, and the 9 excluded collections (`01a`: 210, `02a`: 38, `05a`: 171, `05b`: 20, `05c`: 3, `06`: 51, `07b`: 2, `09`: 8, `10a`: 2).
3. **Step 3 — 1× Reference Census, Camera `J`, and Matched Before Renders**:
   - In `v006` only, temporarily evaluate an owned copy of the old `Pokryv lesa` graph with `Matematika.001` set to `1.0` to record the exact `1×` reference root count both overall and on the common measurement support (`0.15 m` outside finished surfaces), then restore the exact working `14×` state for the before renders.
   - Add camera `J • Tráva • detail` in `07e • Kamery • hodnotenie • A` at `(7.95, -5.25, 0.65)`, aim `(6.95, -3.75, -0.24)`, lens `55 mm`, sensor `36 × 24 mm`, zero shift, DOF off.
   - Render sequentially (one still per MCP call, recording duration and sampled `ps` RSS in KiB for PID `14209`) at the matched recipe (`840 × 560`, Cycles CPU, 32 samples, adaptive threshold `0.01`, OIDN on, seed `0`, AgX / `None` / exposure `0.0` / gamma `1.0`, sRGB, PNG RGB 8-bit, frame `1`):
     - `evidence/grass-006/camera-a-before.png` (Camera A)
     - `evidence/grass-006/overview-before.png` (Camera D)
     - `evidence/grass-006/grass-detail-before.png` (Camera J)
4. **Step 4 — Script `scripts/grass_ground_cover_v006.py` & Patch Prototype**:
   - Write `/Users/agile/Projects/jelena/scripts/grass_ground_cover_v006.py` implementing:
     - The 9 deterministic 48-blade clump prototypes (`Tráva v006 • 00 krátka A` .. `08 vyššia C`) in excluded scene-A collection `12a • Prototypy trávy v006 • A` with curved/arched centrelines, width taper `(1 - t)^1.3`, central V-ridge fold, smooth normals, and longitudinal `t` UV / attribute.
     - Single-purpose material `Tráva • pokryv • A` (root/mid/tip ramp `(0.018, 0.035, 0.008)` -> `(0.055, 0.120, 0.018)` -> `(0.180, 0.245, 0.050)`, `Object Info -> Random` hue `±0.025` and value `0.88..1.12`, roughness `0.78`, IOR `1.45`, Specular IOR Level `0.25`, ~12% Translucent BSDF mix, opaque alpha).
     - Owned flat projected clearance mask (`Maska trávy v006 • A`, hidden from viewport and render) derived from actual copies of `Lôžko • chodník`, both paver meshes, `Prechod • štrk`, `Parkovanie • štrk`, `Cesta • les`, visible steps `.002/.003`, and cabin/terrace keep-out boxes.
     - Scene-A-only Geometry Nodes group `Pokryv lesa v006 • A` on `Pôda • pokryv` (retaining `Pokryv lesa` untouched for rollback) with world-space noise patchiness (`scale 0.65`, `detail 2`, point-domain probability thinning), post-distribution mask exclusion and `0.20 m` edge tapering (`effective_xy_scale = min(s, (d - 0.008) / R)`, discarding `< 0.45`), yaw-only rotation, Z scale `0.90..1.10`, and verified 9-variant `Pick Instance` indexing (`45%` short, `50%` main, `5%` accent; `100%` short within `0.20 m` of edges).
   - Run the **patch build** first (`x [5.0, 9.5], y [-6.0, -2.0]`), verify instance counts and sampled RSS, render a patch preview from Camera J, and visually inspect the image to confirm tapered/curved blades, natural root-to-tip colour, readable soil patches, and clean Path B / step edges. If up to two targeted shader/geometry refinements are needed for visual quality, apply them at the patch stage before full rollout.
5. **Step 5 — Staged Rollout (`25% -> 50% -> 100%`) & Density Calibration**:
   - Expand through `25%`, `50%`, and `100%` density stages while monitoring sampled `ps` RSS (`<= 4.2 GiB` soft gate, `<= 5.0 GiB` hard ceiling). Use the two ordered geometry simplifications from Section 5 of your plan only if required by the RSS/time budget.
   - Calibrate the global density coefficient (at most two deterministic adjustments) so common-support effective blade density lands in **`9.5×–10.5×`** of the `1×` reference (`~5M–6.5M` total rendered blades).
   - Run the full build twice in a row and assert idempotence (identical object/datablock/instance counts, zero `.001` duplicates).
6. **Step 6 — Final Sequential Evidence Renders, Inspection & Restoration**:
   - Render sequentially (one still per MCP call, recording per-render seconds and sampled `ps` RSS in KiB):
     - `evidence/grass-006/camera-a-after.png` (Camera A)
     - `evidence/grass-006/overview-after.png` (Camera D)
     - `evidence/grass-006/grass-detail-after.png` (Camera J, overwriting any patch preview)
     - `evidence/grass-006/access-clearance.png` (Camera G `G • Napojenie • detail`)
   - Directly inspect all 7 PNG images to verify visual quality, blade taper/curvature, natural green variation, readable soil patches, and clean paving/gravel/step margins without an exaggerated bare moat.
   - Restore saved render settings (`1260 × 840`, 80 samples, adaptive on, denoising off, PNG RGBA 8-bit, output `/tmp/`, active Camera A, frame 1), save `Jelena/Jelena_Realistic_v006.blend`, and verify `is_dirty == False`.
   - Re-verify all preservation fingerprints and confirm `Jelena_Realistic_v005.blend` (`892d930b...`), `.local/checkpoints/Jelena_Realistic_v005-before-grass-v006.blend` (`892d930b...`), `.local/checkpoints/Jelena_Realistic_v005-before-edge-grass.blend` (`2399ce17...`), and `Jelena_Realistic_v004.blend` (`00d1dbe6...`) remain byte-identical.
   - Write `evidence/grass-006/manifest.json` and apply the narrow `README.md` update.

## 4. Validation and Report Contract

```text
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: none
Affected tests: scripts/grass_ground_cover_v006.py read-only validation and assertion suite
New causal regression: scripts/grass_ground_cover_v006.py asserts 9-variant Pick Instance usage, post-distribution full-clump edge clearance (R * effective_xy_scale + 0.008 <= d), 9.5x-10.5x common-support blade ratio, idempotence across two consecutive runs, and Scene-B/excluded-collection preservation
Broad or full suite: not-used
Runtime or testbed: live Blender 5.2.3 LTS via local blender MCP
Independent acceptance: not-required
```

Stopping conditions:

- Stop and report `BLOCKED` or `PARTIAL` if any pre-mutation gate fails, if sampled `ps` RSS breaches `5.0 GiB` after the two authorized simplifications, if any clearance or Scene-B preservation assertion fails and cannot be resolved within scope, or if `01_report_03.md` already exists.

Completion and report contract:

- Begin `/Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/01_report_03.md` with `### Report for ORCHESTRATOR_CHAT` and echo the three coordinate fields from this prompt once.
- Report `status: PASS`, `Phase-qualified result: implementation-PASS`, `Start commit` and `End commit` = `c83e2baf7d6c5d9d1be4b39c7656330e410c9c6e`, `Report justification: new-mutation`, and `Logical-whole closure: not-closed`.
- Include: exact SHA-256 hashes of `Jelena_Realistic_v006.blend`, `scripts/grass_ground_cover_v006.py`, `README.md`, `manifest.json`, all 7 PNGs, and all verified checkpoints/baselines; the quantitative density table (common-support area, 1× reference clumps/blades, 14× spike state, v006 clumps/m², blades/clump, per-variant counts, total rendered blades, achieved ratio); clearance verification summary; per-render durations and sampled RSS in KiB (explicitly labelled sampled, not peak); visual inspection notes for each image; `Orchestration critique` (`MEASURED` / `LEAD`); `Resolved Execution Issues / Near-Misses`; `Pre-Existing Failure Classification`; and `Authority expiry`.
- Write the report to `/Users/agile/meta/projects/jelena/00/04-jelena-grass-and-ground-cover-realism/01_report_03.md`, read it back completely, and return status, path, and SHA-256.
- Authority expires upon submission of this terminal implementation report.

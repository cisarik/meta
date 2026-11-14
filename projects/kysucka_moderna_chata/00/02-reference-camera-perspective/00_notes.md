# 00_notes — kysucka-moderna-chata-reference-camera-perspective

Logical whole identity: kysucka-moderna-chata-reference-camera-perspective
Capability profile: Orchestrator
Orchestrator session scope: logical-whole
Development run identity: kysucka-moderna-chata-reference-visualization
Opened: 2026-11-14, Europe/Bratislava
Notes author: ORCHESTRATOR (this whole)
Status: closed — 3D camera perspective whole closed by Orchestrator (`01_closure.md`); visual project remains open for subsequent wholes

## AP Handout Revalidation Record

```text
Handout revalidation: projects/kysucka_moderna_chata/00/02-reference-camera-perspective/00_handout.md
Received handout status: provisional
Revalidated against: project commit f0fb0ea25fcd091ff05e5e3717c433c586cac4fa (origin https://github.com/cisarik/kysucka_moderna_chata, local HEAD and public main equal and clean); AP commit d7023cf037f6d17885c3ede5c04812c61640da50 (mode-160000 gitlink and clean detached .ap HEAD, ./.ap/ap doctor PASS stable); Meta commit 4db94c333340c6b77d06701d050de286c701dabc (origin https://github.com/cisarik/meta.git, local HEAD and public main equal); protected S00 and v01 SHA-256 values; live Blender 5.2.3 LTS session via Blender MCP tools
Usable facts: project main and public main are f0fb0ea25fcd091ff05e5e3717c433c586cac4fa; AP pin is d7023cf037f6d17885c3ede5c04812c61640da50; Meta HEAD and public main are 4db94c333340c6b77d06701d050de286c701dabc; blender/kysucka_chata_mcp_v01.blend (227edd9356a0e2917486351bce6e6fdbb62c58eacbfbb96101c1872d5235e4a8), blender/kysucka_chata_seed.blend (9fcea3fc25eeaec1e791b772c4d4ae4f825f103a139154ab45c2c420718226e0), reference/kysucka_chata_moderna.png (05bc3e72161e5945379c86da80450ffdf82ddce6dbdd9b9e77071aa79cdecc96), scripts/build_scene.py (4310a6ed69e577157c2a605b5c2a7b0128ca62ab667f69ea72aece47563884c2), model/parameters.json (90a3bf95c9c51ea407ae1d749b481795733e88c083c07415ed0f58f916c6cc7a), and predecessor renders/before.png (9a618128cf5e69f7af973a4acffbd036c125de6a5e0b03ce78836d23f05f4436) and renders/after.png (bf5e95c925446a7c6a317e117f07ce80e4ac28ab79e379976412c8a814017801) all match on disk
Stale facts and corrections: handout notes live/dirty state was unknown to Master -> directly verified via MCP that blender/kysucka_chata_mcp_v01.blend is active with is_saved=True, is_dirty=False, mode=OBJECT, active=APPLE_foliage_proxy.022, 656 objects, 13,438 vertices, and no running render job; handout notes predecessor before.png and renders/render_metadata.json were absent from public Meta 4db94c3 -> verified both files exist locally on disk with matching recorded SHA-256 hashes (before.png is untracked in Meta, while render_metadata.json is matched by Meta root .gitignore line 3 '*' which only un-ignores *.md and *.png so archiving JSON in Meta requires git add -f by the Cooperator)
Not revalidated: effective model/reasoning telemetry inside the separate manual Worker client session until reported by the Worker; Michal's subjective visual preference among camera candidates until rendered and reviewed
Handout disposition: adopted-with-corrections
```

## Orchestrator Read-Only Grounding (Repository + Live Blender MCP + Projective Analysis)

### 1. Repository and Trace State

- **Project repository**: `/Users/agile/Projects/kysucka_moderna_chata`, canonical origin `https://github.com/cisarik/kysucka_moderna_chata`, standalone checkout on `main` at `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa`, matching `origin/main` and public `refs/heads/main`. Worktree and index are clean.
- **AP submodule**: `.ap` at `d7023cf037f6d17885c3ede5c04812c61640da50`, clean detached HEAD matching gitlink; `./.ap/ap doctor` exits `0` (`resolved governing variant: stable`, `PASS`).
- **Verified SHA-256 anchors**:
  - `blender/kysucka_chata_seed.blend`: `9fcea3fc25eeaec1e791b772c4d4ae4f825f103a139154ab45c2c420718226e0`
  - `blender/kysucka_chata_mcp_v01.blend`: `227edd9356a0e2917486351bce6e6fdbb62c58eacbfbb96101c1872d5235e4a8`
  - `reference/kysucka_chata_moderna.png`: `05bc3e72161e5945379c86da80450ffdf82ddce6dbdd9b9e77071aa79cdecc96`
  - `model/parameters.json`: `90a3bf95c9c51ea407ae1d749b481795733e88c083c07415ed0f58f916c6cc7a`
  - `scripts/build_scene.py`: `4310a6ed69e577157c2a605b5c2a7b0128ca62ab667f69ea72aece47563884c2`
  - Predecessor `01-blender-mcp-first-reference-render/renders/before.png`: `9a618128cf5e69f7af973a4acffbd036c125de6a5e0b03ce78836d23f05f4436`
  - Predecessor `01-blender-mcp-first-reference-render/renders/after.png`: `bf5e95c925446a7c6a317e117f07ce80e4ac28ab79e379976412c8a814017801`
  - Opening handout `02-reference-camera-perspective/00_handout.md`: `f9f3a31c73e98fba558a32edb3b53e25575292f4d59571f412509f565deeee3f` (frozen on opening).
- **Meta repository**: `/Users/agile/meta`, canonical origin `https://github.com/cisarik/meta.git`, `HEAD` and public `refs/heads/main` at `4db94c333340c6b77d06701d050de286c701dabc`. Unrelated modified/untracked files exist under `projects/bookradar/`, `projects/jelena/`, `projects/kronika/`, and `projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/renders/before.png`. All unrelated and predecessor files are preserved untouched.

### 2. Live Blender MCP Observations (Read-Only)

The Orchestrator executed read-only MCP calls (`get_addon_status`, `get_scene_info`, read-only `execute_blender_code`, and `look(mode="camera", shading="solid", max_size=640)`):

- **Connected Blender**: `5.2.3 LTS`, addon `[1, 8]`, protocol `15` (expected `16`; native calls work), external asset libraries and generators `off`, `telemetry_consent = false`.
- **Active file & state**:
  - `bpy.data.filepath`: `/Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v01.blend`
  - `bpy.data.is_saved`: `True`, `bpy.data.is_dirty`: `False`, `bpy.app.is_job_running('RENDER')`: `False`
  - `active_object`: `APPLE_foliage_proxy.022`, `mode`: `OBJECT`, `object_count`: `656` (1 camera, 1 empty, 6 lights, 648 meshes), `mesh_vertices`: `13438`.
  - Layout 3D Viewport: `perspective = 'CAMERA'`, `shading = 'RENDERED'`, `use_scene_lights = True`, `use_scene_world = True`, `preview_samples = 16`. (Note: because the active viewport is in `RENDERED` shading with Cycles, `tools.blender.look(mode="camera")` requires `shading="solid"` or `image=...` so it does not fail on Cycles viewport capture; verified `is_dirty` remains `False` after `look(mode="camera", shading="solid")`).
- **Active Camera (`CAM_A_REFERENCE`) in `v01`**:
  - `location`: `[27.5, -15.5, 1.7]`, `target`: `[7.45, 3.15, 1.7]` (`rotation_euler = [1.570796, -0.0, 0.821558]`)
  - `lens`: `50.0` mm, `sensor_width`: `36.0` mm, `shift_x`: `0.0`, `shift_y`: `0.075`
  - Canonical render settings: `CYCLES`, `CPU`, `1448 x 1086` (`100%`), `96` samples, `//../work/camera_a.png`.

### 3. Projective Landmark & Perspective Analysis (`v01` vs `reference/kysucka_chata_moderna.png`)

Using `bpy_extras.object_utils.world_to_camera_view` (normalized top-left image coordinates `u = x/width`, `v = 1 - y/height`), the Orchestrator measured the 3D projections in `v01` against `model/reference_landmarks.json` and visual inspection of `reference/kysucka_chata_moderna.png`:

| Landmark / Control | 3D World Coord `(X, Y, Z)` | Reference `(u, v)` | `v01` (50 mm, `[27.5,-15.5,1.7]`, `shift_y=0.075`) | Discrepancy Diagnosis |
|---|---|---|---|---|
| `left_front_eave` | `(-0.55, -0.85, 2.40)` | `(0.1195, 0.5856)` | `(0.1187, 0.5575)` (`depth=30.52m`) | In `v01`, far left eave sits `2.8%` too high (`v=0.558` vs `0.586`) because 50 mm telephoto compresses near/far vertical scale. |
| `gable_peak` | `(14.95, 4.20, 7.45)` | `(0.8605, 0.0875)` | `(0.8611, 0.1290)` (`depth=22.61m`) | In `v01`, near gable apex sits `4.2%` too low (`v=0.129` vs `0.088`). Thus `left_front_eave.v - gable_peak.v` is only `0.4285` in `v01` vs **`0.4981`** in the reference (cannot be solved by `shift_y` alone). |
| `gable_near_base` | `(14.40, 0.15, 0.45)` | `(0.6996, 0.6897)` | `(0.6740, 0.7143)` (`depth=20.25m`) | In `v01`, the near gable corner is `2.6%` too far left (`u=0.674` vs `0.700`), making the entrance facade narrower and the glazed gable wider (`facade/gable width ratio = 1.97` in `v01` vs **`2.18`** in reference). |
| `gable_far_base` | `(14.40, 8.25, 0.45)` | `(0.9655, 0.6842)` | `(0.9564, 0.6898)` (`depth=25.77m`) | Matches reference closely (`du = -0.009, dv = +0.006`). |
| `chimney_top` | `(11.30, 3.20, 8.45)` | `(0.6526, 0.0994)` | `(0.6501, 0.0918)` (`depth=24.60m`) | Matches reference closely (`du = -0.003, dv = -0.008`). |
| `gable_front_eave` vs `gable_transom_near` | `(14.95, -0.85, 2.40)` vs `(14.455, 0.15, 3.18)` | `(0.6492, 0.4392)` | Eave fascia: `(0.6579, 0.5324)`; Transom/plate: `(0.6769, 0.4644)` | **Fixed-geometry note**: In the reference image, the roof eave meets the glazed gable near the horizontal transom (`Z = 3.18 m`), whereas in S00 the 45° roof extends over a `0.85 m` overhang down to `Z = 2.40 m`. Even on the fixed S00 eave (`Z = 2.40 m`), `v01` has an almost flat eave rise `eave_dv = left_front_eave.v - gable_front_eave.v = +0.0252` because `Z_cam = 1.70 m` is close to `Z_eave = 2.40 m` and the 50 mm lens is far away. |
| `entry_bottom` & `front_window_center` | `(7.875, -0.06, 0.45)` & `(5.15, -0.06, 1.925)` | Door: `(0.4931, 0.7127)`; Win: `(0.3591, 0.5976)` | Door: `(0.3850, 0.6930)`; Win: `(0.2976, 0.5845)` | **Fixed-geometry note**: Because `X = 14.4` is closer to the camera than `X = 0`, projective foreshortening always projects the physical midpoint (`X = 7.2 m`) left of the 2D facade midpoint. In S00, `D01` is centered at `X = 7.875 m` (`54.7%` of `14.4 m`), so it projects around `u ~ 0.37–0.41`; matching `u = 0.493` would require moving `D01` along `+X` in a later geometry whole. |
| `fireplace_front_center` vs `mullion_0.15` | `(11.30, 2.80, 1.40)` vs `(14.455, 0.15, 1.40)` | In reference, fireplace is visible in glass bay (`u ~ 0.79`) while chimney is at `u = 0.653` | Fireplace: `u = 0.6351`; `mullion_0.15`: `u = 0.6769` (`fp - m0 = -0.0418`) | **Parallax finding**: In S00, `FIREPLACE_stone` is vertically aligned under the chimney (`X = 11.3, Y = 3.2`), which is `3.1 m` left of the glazed gable (`X = 14.4`) and behind the solid front wooden wall! For a ray from `(xc, yc)` to `(11.3, 2.8)` to pass to the right of `(14.4, 0.15)`, the camera must swing toward `+X` until `(xc - 14.4)/(0.15 - yc) > 3.1/2.65 = 1.17` (which forces `gable_near_base.u < 0.62` and collapses the facade/gable width ratio to `< 1.30`). Conversely, moving the camera closer with a `32–35 mm` lens at `Z ~ 1.15–1.25 m` (`loc ~ [20.5..21.5, -9.0..-10.0, 1.15..1.25]`) matches the outer envelope (`left_front_eave.v - gable_peak.v ~ 0.485–0.497`, `facade/gable ratio ~ 2.20`, `eave_dv ~ +0.068..+0.083`), while proving that the reference's simultaneous chimney (`u=0.653`) and fireplace (`u=0.79`) placement is an AI perspective/interior-layout discrepancy. |

## Opening Routing Decisions — 01/01

- **Coordinates**:
  - `Logical whole identity`: `kysucka-moderna-chata-reference-camera-perspective`
  - `Worker session ordinal`: `01`
  - `Worker exchange ordinal`: `01`
  - `Worker session target`: `fresh-worker-session`
  - `Native planning mode`: `required`
  - `Worker session profile`: `Planner`
  - `Phase`: `planning`
  - `Delivery route`: `manual Cooperator delivery` (Orchestrator writes `01_planning_00.md` to Meta; Michal delivers to a fresh Worker session with Native Plan Mode ON).
  - `Reasoning recommendation`: `Standard/Medium` (approx. 250k tokens).
- **Execution route binding (AP RF-16)**:
  - Task-specific bounded activation of `blender-mcp-live-v1` departing from `blender-local-v1` per Master handout and Cooperator direction. During `01/01` planning, only read-only MCP observations (`get_addon_status`, `get_scene_info`, read-only `execute_blender_code`, optional `look(mode="camera", shading="solid")`) and read-only local repository/hash checks are permitted; no live-scene mutation, save, or render file write is authorized until `01/02` implementation.
- **Report persistence & P4 completion route**:
  - `Report persistence owner: assigned WORKER` with `Trace persistence: direct-write /Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective/01_report_00.md`.
  - If active Native Plan Mode blocks the direct file write, the P4 completion route applies: the Worker returns the complete standard report in-session (`status: PARTIAL` for missing file delivery only, with a decision-complete plan) and the Orchestrator persists the exact returned report bytes to `01_report_00.md` without another planning cycle.

## First Planner Report Reconciliation — 01/01

- **Report identity**: `projects/kysucka_moderna_chata/00/02-reference-camera-perspective/01_report_00.md`, SHA-256 `71e6552eb3e91f50253c5c41aad8119bebec3e51e18e434dd9c656c9cf1c7274`. Begins with `### Report for ORCHESTRATOR_CHAT`, echoes `01/01`, `status: PARTIAL` (due only to Native Plan Mode write block; resolved via P4 completion route on disk), `Phase-qualified result: not-applicable`, `Start commit` and `End commit` `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa`, `Report justification: new-evidence`, `Logical-whole closure: not-closed`.
- **Orchestration critique disposition (`01/01`)**:
  - `MEASURED`: C1 and C2 improve the outer envelope controls (`facade_to_gable_ratio`, `eave_dv`, `vertical_envelope_span`, and 5-landmark pixel RMSE `E`) while worsening `fireplace_parallax` and `fence_right.u` due to fixed S00 geometry (`FIREPLACE_stone` at `X=11.3, Y=3.2` and fence on `Y=-5.78`) -> confirmed; preserve as explicit measured residuals in `evidence/camera_comparison.md`, `renders/render_metadata.json`, and `01_closure.md`.
  - `LEAD`: `none`.
- **Accepted technical plan (`01/01`)**:
  1. **Comparison controls & landmarks**:
     - Six primary landmarks: `left_front_eave` `(-0.55,-0.85,2.40)`, `gable_front_eave` `(14.95,-0.85,2.40)`, `gable_peak` `(14.95,4.20,7.45)`, `gable_near_base` `(14.40,0.15,0.45)`, `gable_far_base` `(14.40,8.25,0.45)`, `chimney_top` `(11.30,3.20,8.45)`.
     - Three auxiliary probes: `fireplace_front_center` `(11.30,2.80,1.40)`, `mullion_0.15` `(14.455,0.15,1.40)`, `fence_right` `(16.80,-5.78,0.57)`.
     - Controls: `facade_to_gable_ratio`, `eave_dv`, `vertical_envelope_span`, `fireplace_parallax`, `fence_right.u`, and 5-point outer-envelope pixel RMSE `E = sqrt(mean((1448*du)^2 + (1086*dv)^2))` (excluding ambiguous `gable_front_eave`).
  2. **Three candidates & promotion rule**:
     - `v01` baseline: `location = [27.5, -15.5, 1.70]`, `target = [7.45, 3.15, 1.70]`, `lens = 50.0` mm, `shift_y = 0.075` (`E = 32.70 px`).
     - `cand_01_35mm_balanced`: `location = [21.5, -10.0, 1.25]`, `target = [8.5, 2.5, 1.25]`, `lens = 35.0` mm, `shift_y = 0.105` (`E = 29.11 px`, analytic favourite).
     - `cand_02_32mm_wide_low`: `location = [20.5, -9.0, 1.15]`, `target = [8.5, 2.5, 1.15]`, `lens = 32.0` mm, `shift_y = 0.115` (`E = 32.27 px`).
     - `cand_03_38mm_parallax`: `location = [25.5, -9.8, 1.25]`, `target = [7.8, 2.5, 1.25]`, `lens = 38.0` mm, `shift_y = 0.080` (`E = 74.00 px`, parallax trade-off control).
     - Render `renders/before.png`, `renders/candidate_01.png`, `renders/candidate_02.png`, `renders/candidate_03.png`, assemble the 2×2 labelled `renders/candidates_sheet.png` (`1280 × 1024`), apply the deterministic selection rule (`C1` analytic winner), and render `renders/after.png`.
  3. **Scene save, source sync, and publication**:
     - Save `work/mcp-v02-before.blend` (`copy=True, compress=True`) before camera changes; save chosen camera scene as active `/Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v02.blend` (`copy=False, compress=True`) with canonical `1448 × 1086`, 96 samples, `//../work/camera_a.png`, and `CAMERA` + `RENDERED` (16 preview samples) viewport.
     - Sync `model/parameters.json` (`camera.location`, `camera.target`, `camera.lens_mm`, `camera.shift_y`), narrowly update `AGENTS.md`, `docs/OPERATIONS.md`, and `README_SK.md` for `v02`, persist `/Users/agile/meta/projects/kysucka_moderna_chata/00/00_RUN_MAP.md`, validate via cold CLI `scripts/inspect_scene.py` and `./.ap/ap doctor`, and commit + non-force push the 5 tracked project files to `origin main`.

## Implementation Routing Decisions — 01/02

- **Coordinates**: `kysucka-moderna-chata-reference-camera-perspective`, session `01`, exchange `02` (`01_implementation_01.md` + `01_report_01.md`).
- **Session target & mode**: `current-worker-session` (same healthy Worker session that produced `01_report_00.md`), `Native planning mode: not-used` (OFF), profile `Fresh Implementation Worker` (operating as current-session implementation continuation under AP §3 / PROMPT_CONTRACTS), `Reasoning recommendation: Standard/Medium`.
- **Direct persistence**: Orchestrator writes `01_implementation_01.md` to Meta; Worker directly writes `renders/before.png`, `renders/candidate_01.png`, `renders/candidate_02.png`, `renders/candidate_03.png`, `renders/candidates_sheet.png`, `renders/after.png`, `renders/render_metadata.json`, `evidence/camera_comparison.md`, `/Users/agile/meta/projects/kysucka_moderna_chata/00/00_RUN_MAP.md`, and `01_report_01.md`, then reads back its report.

## Implementation Report Reconciliation, Direct Orchestrator Verification, and Closure — 01/02

- **Report identity**: `projects/kysucka_moderna_chata/00/02-reference-camera-perspective/01_report_01.md`, SHA-256 `e480ecaa827bb4906c7b87433816734993c2db182e16e57086f6000c7312f9be`. Written directly by the `01/02` Worker and read back. Echoes `01/02`, `status: PASS`, `Phase-qualified result: implementation-PASS` (with `publication-PASS` in its publication section), `Start commit: f0fb0ea25fcd091ff05e5e3717c433c586cac4fa`, `End commit: d67431d1678de511e06a8ad04cd632ae4899cdc4`, `Report justification: new-mutation`, `Logical-whole closure: not-closed`.
- **Direct Orchestrator MCP verification of live Blender 5.2.3 LTS session**:
  - `get_scene_info`, read-only `execute_blender_code`, and `look(image=".../renders/after.png")` executed directly by the Orchestrator after `01_report_01.md`:
  - `bpy.data.filepath`: `/Users/agile/Projects/kysucka_moderna_chata/blender/kysucka_chata_mcp_v02.blend`
  - `is_saved`: `True`, `is_dirty`: `False`, `is_job_running('RENDER')`: `False`
  - `objects`: `656`, `mesh_vertices`: `13438`, non-camera scene fingerprints unchanged (`combined = e27e1212796b96a4f33e6fad8ee9de354d86f65d740c4b7c537b45c540e26ef6`).
  - `CAM_A_REFERENCE`: `location = [21.5, -10.0, 1.25]`, `target = [8.5, 2.5, 1.25]`, `rotation_euler = [1.570796, -0.0, 0.805004]`, `lens_mm = 35.0`, `sensor_width_mm = 36.0`, `shift_x = 0.0`, `shift_y = 0.105`, matching `model/parameters.json` (`max_euler_diff_vs_json = 0.0`).
  - Canonical saved scene settings: `engine = 'CYCLES'`, `device = 'CPU'`, `resolution = [1448, 1086, 100]`, `cycles.samples = 96`, `cycles.preview_samples = 16`, `filepath = '//../work/camera_a.png'`.
  - Layout 3D Viewport: `perspective = 'CAMERA'`, `shading = 'RENDERED'`, `use_scene_lights = True`, `use_scene_world = True`, `use_scene_lights_render = True`, `use_scene_world_render = True`.
- **Direct Orchestrator visual inspection of rendered images**:
  - Inspected `reference/kysucka_chata_moderna.png`, `renders/before.png`, `renders/candidates_sheet.png` (`1280 × 1024` 2×2 sheet of `v01`, `C1`, `C2`, `C3`), and `renders/after.png` (`640 × 480`, 32 samples Cycles CPU).
  - Confirmed `cand_01_35mm_balanced` (`C1`, 35 mm at `[21.5, -10.0, 1.25]`, target `[8.5, 2.5, 1.25]`, `shift_y = 0.105`) improves outer-envelope RMSE (`32.70 -> 29.11 px`), brings `facade_to_gable_ratio` from `1.9661` to `2.2069` (vs `2.1818` reference), increases `vertical_envelope_span` from `0.4285` to `0.4848` (vs `0.4982` reference), and increases front eave upward rise `eave_dv` 2.7x from `+0.0252` to `+0.0677`.
- **Direct Orchestrator verification of repository, cold CLI reopen, and public Git state**:
  - Commit `d67431d1678de511e06a8ad04cd632ae4899cdc4` (`feat: calibrate 3D camera perspective in mcp_v02 working scene`), parent `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa`, clean worktree/index, public `refs/heads/main` verified via `git ls-remote origin refs/heads/main` = `d67431d1678de511e06a8ad04cd632ae4899cdc4`.
  - `./.ap/ap doctor`: `PASS` (`stable`).
  - Cold CLI `scripts/inspect_scene.py` on `blender/kysucka_chata_mcp_v02.blend`: exit `0`, matching camera and scene invariants; live MCP connection verified intact afterward.
  - Preserved hashes verified: `seed` (`9fcea3fc25eeaec1e791b772c4d4ae4f825f103a139154ab45c2c420718226e0`), `v01` (`227edd9356a0e2917486351bce6e6fdbb62c58eacbfbb96101c1872d5235e4a8`), `reference` (`05bc3e72161e5945379c86da80450ffdf82ddce6dbdd9b9e77071aa79cdecc96`), `scripts/build_scene.py` (`4310a6ed69e577157c2a605b5c2a7b0128ca62ab667f69ea72aece47563884c2`).
- **Orchestration critique disposition (`01/02`)**:
  - `MEASURED`: C1 improves outer-envelope perspective relationships while fireplace and fence probes remain fixed-model residuals -> confirmed and recorded in `01_closure.md`.
  - `LEAD`: `none`.
- **Cooperator feedback and brainstorming classification**:
  - Michal confirmed report completion and recorded his residual observation and next-whole priority: *"report vygenerovany, dalsi do residual moj brainstorming: plot je inak umiestneny ako na predlohe prvej chcem realisticke drevo aj drevo fasady potrebujem realisticke drevo."*
  - Classified under AP (`RF-01`, `§13`, `§16`):
    1. **Camera perspective whole (`02`)**: accepted for closure (`01_closure.md`).
    2. **Confirmed Cooperator residual observation**: foreground fence placement/orientation in S00 (`Y = -5.78`, `X = -1.5..16.8`) differs from the reference image.
    3. **Cooperator priority for next logical whole (`future-logical-whole`)**: realistic wood material/shader calibration (`MAT_WOOD_H`, `MAT_WOOD_V`, and fence wood) and/or foreground fence alignment, handed back to the Master Chat Orchestrator in `01_closure.md`.
- **Closure decision**: All required preceding results (`implementation-PASS`, `acceptance-PASS`, `publication-PASS`), Cooperator-owned decisions, residual-risk disposition, upgrade-ledger reconciliation (none declared), and no-active-mutation / no-active-render-job conditions are satisfied. This `00_notes.md` file is frozen at closure, and `01_closure.md` is emitted with `CELOK UZAVRETÝ ORCHESTRÁTOROM`.



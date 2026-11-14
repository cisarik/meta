# 01_closure — kysucka-moderna-chata-reference-camera-perspective

Closure signal: CELOK UZAVRETÝ ORCHESTRÁTOROM
Closure status: closed — 3D camera perspective calibration whole (`v02`); overall visual project remains open for subsequent wholes
Closed: 2026-11-14, Europe/Bratislava
Author: ORCHESTRATOR (this whole)
Access profile: Orchestrator
Orchestrator session scope: logical-whole
Development run identity: kysucka-moderna-chata-reference-visualization
Closed scope: bounded 3-candidate 3D camera perspective comparison on fixed S00/v01 geometry, promotion of `cand_01_35mm_balanced` (`location = [21.5, -10.0, 1.25]`, `target = [8.5, 2.5, 1.25]`, `lens = 35 mm`, `shift_y = 0.105`), saved and cold-reopenable working scene `blender/kysucka_chata_mcp_v02.blend`, comparable 4:3 Cycles CPU renders (`renders/before.png`, `renders/candidate_01..03.png`, `renders/candidates_sheet.png`, `renders/after.png`), `evidence/camera_comparison.md`, `renders/render_metadata.json`, mechanical persistence of Master's `00_RUN_MAP.md` snapshot, and narrow source/documentation publication

```text
Phase-qualified result: publication-PASS
Result artifact or commit: d67431d1678de511e06a8ad04cd632ae4899cdc4
Result evidence: live MCP read/change/readback on Blender 5.2.3 LTS across v01 baseline and 3 camera candidates, saved and cold-reopened blender/kysucka_chata_mcp_v02.blend, 640x480 4:3 Cycles before/candidate/after renders and 1280x1024 labelled sheet, ./.ap/ap doctor PASS, and direct public origin/main readback
Logical-whole closure: closed-by-ORCHESTRATOR
Required preceding results: satisfied
Cooperator-owned decisions: satisfied
Residual-risk disposition: satisfied
Upgrade-ledger reconciliation: complete
Active mutation: none
Closure actor: ORCHESTRATOR
```

## 1. Whole Identity and Delivered Outcomes

Logical whole identity: `kysucka-moderna-chata-reference-camera-perspective`

All required outcomes of the provisional handout (`00_handout.md`) were delivered and independently verified by this whole's Orchestrator:

1. **Bounded 3D camera perspective comparison on unchanged non-camera scene state**:
   - Starting from the preserved `blender/kysucka_chata_mcp_v01.blend` baseline (`[27.5, -15.5, 1.70]`, target `[7.45, 3.15, 1.70]`, `50 mm`, `shift_y = 0.075`), evaluated three purposeful 3D camera candidates at identical `640 × 480` 32-sample Cycles CPU settings (`AgX`, look `None`, exposure `0.0`, gamma `1.0`, denoising `false`, frame `0`, seed `0`):
     - `cand_01_35mm_balanced` (`C1`): `location = [21.5, -10.0, 1.25]`, `target = [8.5, 2.5, 1.25]`, `lens = 35.0 mm`, `shift_y = 0.105`
     - `cand_02_32mm_wide_low` (`C2`): `location = [20.5, -9.0, 1.15]`, `target = [8.5, 2.5, 1.15]`, `lens = 32.0 mm`, `shift_y = 0.115`
     - `cand_03_38mm_parallax` (`C3`): `location = [25.5, -9.8, 1.25]`, `target = [7.8, 2.5, 1.25]`, `lens = 38.0 mm`, `shift_y = 0.080`
   - Promoted **`cand_01_35mm_balanced` (`C1`)** by the predeclared deterministic selection rule: lowest 5-point outer-envelope RMSE (`E = 29.11 px` vs `32.70 px` in `v01`), closest entrance-facade-to-glazed-gable apparent width ratio (`2.2069` vs `2.1818` in reference; `v01` was `1.9661`), improved vertical envelope span (`0.4848` vs `0.4982` in reference; `v01` was `0.4285`), and a **2.7× steeper** front roof eave upward convergence (`eave_dv = +0.0677` vs `+0.0252` in `v01`).
   - Verified via SHA-256 scene fingerprints (`combined = e27e1212796b96a4f33e6fad8ee9de354d86f65d740c4b7c537b45c540e26ef6`) that all non-camera object transforms, 656 objects, 13,438 mesh vertices, modifiers, materials, glass, lights, and world nodes remained 100% unchanged throughout baseline, candidates, saved `v02`, and cold CLI reopen.
2. **Saved and cold-reopenable working scene `blender/kysucka_chata_mcp_v02.blend` synced with `model/parameters.json`**:
   - Saved as the active file in the live Blender 5.2.3 LTS session (`is_saved = True`, `is_dirty = False`, canonical `1448 × 1086` at `100%`, `96` samples, `//../work/camera_a.png`, Layout viewport in `CAMERA` + `RENDERED` with scene lights/world enabled and `16` preview samples) and verified in a separate cold CLI process (`scripts/inspect_scene.py`, exit `0`).
   - Updated only `camera.location`, `camera.target`, `camera.lens_mm`, and `camera.shift_y` in `model/parameters.json`; verified exact agreement (`0.0 rad` Euler difference) with the existing generator formula `(Vector(cp['target']) - cam.location).to_track_quat('-Z', 'Y').to_euler()` in `scripts/build_scene.py`.
3. **Comparable 4:3 Cycles renders, labelled candidate sheet, comparison evidence, and run-map persistence**:
   - Produced `renders/before.png`, `renders/candidate_01.png`, `renders/candidate_02.png`, `renders/candidate_03.png`, the `1280 × 1024` 2×2 labelled comparison sheet `renders/candidates_sheet.png`, `renders/after.png`, `renders/render_metadata.json`, and `evidence/camera_comparison.md`, and mechanically persisted Master's run-map snapshot at `projects/kysucka_moderna_chata/00/00_RUN_MAP.md`.

## 2. Project Repository and Public Publication Result

| Item | Result |
|---|---|
| Baseline commit | `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa` (`feat: create MCP working scene and refine camera framing`) |
| Final project commit | `d67431d1678de511e06a8ad04cd632ae4899cdc4` |
| Commit subject | `feat: calibrate 3D camera perspective in mcp_v02 working scene` |
| Parent commit | `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa` |
| Pinned AP gitlink (`.ap`) | `d7023cf037f6d17885c3ede5c04812c61640da50` (mode `160000`, clean detached HEAD) |
| `./.ap/ap doctor` | `PASS` (`resolved governing variant: stable`) |
| Public `refs/heads/main` | `d67431d1678de511e06a8ad04cd632ae4899cdc4` (verified independently by Orchestrator via `git ls-remote origin refs/heads/main`) |
| Project worktree / index | Clean (`git status --short` empty; checkpoints in `work/` and `.blend1` remain gitignored) |

Changed tracked project paths (exact 5-file allowlist):

```text
AGENTS.md
README_SK.md
blender/kysucka_chata_mcp_v02.blend
docs/OPERATIONS.md
model/parameters.json
```

The managed AP block and the entire `Closure and Git gates` section in `AGENTS.md` remain byte-identical.

## 3. Why Perspective Is Closer and Where It Still Differs (Measured Controls & Residuals)

### Landmark & Control Summary (top-left UV: `u = x/width`, `v = 1 - y/height`)

| Control / Witness | Reference | `v01` (`before.png`, 50 mm) | `C1` (`after.png`, 35 mm, **chosen v02**) | `C2` (32 mm) | `C3` (38 mm parallax) |
|---|---:|---:|---:|---:|---:|
| `left_front_eave` `(-0.55,-0.85,2.40)` | `(0.1195, 0.5856)` | `(0.1187, 0.5575)` | **`(0.1202, 0.5730)`** | `(0.1297, 0.5822)` | `(0.2006, 0.5456)` |
| `gable_front_eave` `(14.95,-0.85,2.40)` | `(0.6492, 0.4392)`* | `(0.6579, 0.5324)` | **`(0.6807, 0.5053)`** | `(0.6884, 0.4997)` | `(0.6019, 0.4891)` |
| `gable_peak` `(14.95,4.20,7.45)` | `(0.8605, 0.0875)` | `(0.8611, 0.1290)` | **`(0.8802, 0.0881)`** | `(0.8849, 0.0851)` | `(0.8471, 0.0827)` |
| `gable_near_base` `(14.40,0.15,0.45)` | `(0.6996, 0.6897)` | `(0.6740, 0.7143)` | **`(0.6916, 0.7253)`** | `(0.6975, 0.7306)` | `(0.6310, 0.6828)` |
| `gable_far_base` `(14.40,8.25,0.45)` | `(0.9655, 0.6842)` | `(0.9564, 0.6898)` | **`(0.9506, 0.6984)`** | `(0.9479, 0.7041)` | `(0.9615, 0.6647)` |
| `chimney_top` `(11.30,3.20,8.45)` | `(0.6526, 0.0994)` | `(0.6501, 0.0918)` | **`(0.6441, 0.0744)`** | `(0.6440, 0.0797)` | `(0.6423, 0.0756)` |
| `facade_to_gable_ratio` | `2.1818` | `1.9661` | **`2.2069`** | `2.2678` | `1.3026` |
| `eave_dv` (`left.v - gable_eave.v`) | `0.1464`* | `0.0252` | **`0.0677`** | `0.0825` | `0.0565` |
| `vertical_envelope_span` (`left.v - peak.v`) | `0.4982` | `0.4285` | **`0.4848`** | `0.4971` | `0.4629` |
| `fireplace_parallax` (`fp.u - m0.u`) | `> 0` (visible) | `-0.0418` | **`-0.0661`** | `-0.0721` | `-0.0081` |
| `fence_right.u` `(16.8,-5.78,0.57)` | `> 0.90` | `0.4836` | **`0.4668`** | `0.4573` | `0.3140` |
| 5-point envelope RMSE `E` (`1448×1086` px) | `0.00` | `32.70 px` | **`29.11 px`** | `32.27 px` | `74.00 px` |

### Why `v02` (`C1`) Is Closer to the Reference

- **Eliminates telephoto depth compression**: Moving from a `50 mm` lens at `[27.5, -15.5, 1.70]` (`~25 m` distance) to a `35 mm` lens at `[21.5, -10.0, 1.25]` (`~14.5 m` distance to gable peak, `target = [8.5, 2.5, 1.25]`, `shift_y = 0.105`) increases near/far perspective expansion so `left_front_eave.v` (`0.5730` vs `0.5856` ref) and `gable_peak.v` (`0.0881` vs `0.0875` ref) match simultaneously (`vertical_envelope_span` improves from `0.4285` to `0.4848`).
- **Restores long roof eave rise**: Lowering the camera eye height from `Z = 1.70 m` to `Z = 1.25 m` (while keeping `target.z = 1.25 m` so verticals remain strictly upright) increases the eave's height above the horizon and raises `eave_dv` 2.7× (`+0.0252 -> +0.0677`).
- **Matches entrance-facade vs glazed-gable width balance**: Shifting the viewing azimuth slightly toward the entrance facade brings `gable_near_base.u` from `0.6740` to `0.6916` (vs `0.6996` ref) and `facade_to_gable_ratio` from `1.9661` to `2.2069` (within `1.1%` of the reference's `2.1818`).

### Where `v02` Still Differs (Fixed S00 Model Residuals)

1. **Foreground picket fence geometry (`Y = -5.78`, `X = -1.5..16.8`)**: As Michal also observed, the S00 fence runs parallel to the front wall and terminates at `X = 16.8` (`fence_right.u = 0.4668` in `v02` vs `0.4836` in `v01`), whereas in the reference image the fence runs diagonally across the entire lower foreground.
2. **Interior fireplace vs exterior chimney alignment (`X = 11.3, Y = 3.2`)**: Because S00 places `FIREPLACE_stone` directly beneath `CHIMNEY_shaft` (`3.1 m` behind the glazed gable plane `X = 14.4`, behind the solid front wall), any camera that matches the reference's `2.18 : 1` facade-to-gable width ratio projects the fireplace behind the front wall (`fireplace_parallax = -0.0661`), whereas swinging the camera toward `+X` (`C3`) to bring the fireplace toward the corner mullion (`-0.0081`) collapses `facade_to_gable_ratio` to `1.3026` (`E = 74.00 px`).
3. **Overhanging eave (`Z = 2.40 m`) vs gable transom (`Z = 3.18 m`) and entry door X-position (`X = 7.875 m`)**: These remain fixed S00 architectural hypotheses outside camera calibration.
4. **Unchanged non-camera visual elements**: Procedural wood/stone/roof materials, proxy vegetation, `WORLD_procedural_sky` (`Background Strength = 0.26`), and 32-sample Cycles interior noise were intentionally held fixed for this camera comparison.

## 4. Exact File and Artifact SHA-256 Hashes

### Project and Checkpoint Files (relative to `/Users/agile/Projects/kysucka_moderna_chata`)

| Path | Role / Status | SHA-256 |
|---|---|---|
| `blender/kysucka_chata_seed.blend` | Preserved S00 seed (unchanged) | `9fcea3fc25eeaec1e791b772c4d4ae4f825f103a139154ab45c2c420718226e0` |
| `blender/kysucka_chata_mcp_v01.blend` | Preserved v01 scene (unchanged) | `227edd9356a0e2917486351bce6e6fdbb62c58eacbfbb96101c1872d5235e4a8` |
| `reference/kysucka_chata_moderna.png` | Preserved 1448 × 1086 visual target (unchanged) | `05bc3e72161e5945379c86da80450ffdf82ddce6dbdd9b9e77071aa79cdecc96` |
| `scripts/build_scene.py` | Preserved procedural scene builder (unchanged) | `4310a6ed69e577157c2a605b5c2a7b0128ca62ab667f69ea72aece47563884c2` |
| `blender/kysucka_chata_mcp_v02.blend` | New active working scene (committed) | `010f47a81a4fde2e936f401e87b8bc11af76a8e72d71811d68dd910da0b27249` |
| `model/parameters.json` | Updated camera `location`, `target`, `lens_mm`, `shift_y` (committed) | `2d441b08d658e4aa4c8fccc5e71c76eb16666deeb4401cdd0b973c379901cada` |
| `AGENTS.md` | Narrow MCP v02 route & hash update (committed) | `3184e475b04dd10abc186855bf0c1687b73c941db70ea5ddf6a129216672e172` |
| `docs/OPERATIONS.md` | Narrow Slovak v02 operations update (committed) | `d10b86ff0b47444d6371697cc23570e3ba67c0b1408109232279e4e12ffca204` |
| `README_SK.md` | Narrow Slovak v02 opening instructions (committed) | `4169e36d413ce0e54e8199f90d326ed765178b01859cf5d634e04fb01c497641` |
| `work/mcp-v02-before.blend` | Gitignored pre-comparison v02 baseline checkpoint | `2b94a34e2fb958d716612a5358beb13a13791bed7eef7659adedc7c18cfe2d09` |

### Meta Trace and Render Artifacts (relative to `projects/kysucka_moderna_chata/00/02-reference-camera-perspective/`)

| File | Role | SHA-256 |
|---|---|---|
| `00_handout.md` | Frozen provisional handout from Master | `f9f3a31c73e98fba558a32edb3b53e25575292f4d59571f412509f565deeee3f` |
| `00_notes.md` | Frozen per-whole Orchestrator notes | `bd55300638aeccd09064c284b2e620a82a5a94e0deb8267460b1519b33430392` |
| `01_planning_00.md` | `01/01` Planner prompt | `247cfa216b31cf62d40411e5b46469a2cc708d963d65195acc6840931430453a` |
| `01_report_00.md` | `01/01` Planner terminal report | `71e6552eb3e91f50253c5c41aad8119bebec3e51e18e434dd9c656c9cf1c7274` |
| `01_implementation_01.md` | `01/02` Implementation prompt | `297c343dc5aa39dbdffcfe810a80b92ba4cf35e44174851271f76a0a0efc0e83` |
| `01_report_01.md` | `01/02` Implementation terminal report | `e480ecaa827bb4906c7b87433816734993c2db182e16e57086f6000c7312f9be` |
| `renders/before.png` | `640 × 480` 4:3 Cycles CPU 32-sample baseline render (`v01` 50 mm) | `b27eb2c0d65e593405da855cc23e035b112dc3ec0b111147e293df07d5ef1ed8` |
| `renders/candidate_01.png` | `640 × 480` 4:3 Cycles CPU 32-sample render (`C1` 35 mm, chosen) | `0ca02ea8aa96f4180ca9ff1fdbcf9a5955655e2d1fa5bc0e909001803f0c6037` |
| `renders/candidate_02.png` | `640 × 480` 4:3 Cycles CPU 32-sample render (`C2` 32 mm) | `28b7965562ca0453d6f0891b76cb85605ccf8f5e1b12dddf5f1c62829a5c2cb6` |
| `renders/candidate_03.png` | `640 × 480` 4:3 Cycles CPU 32-sample render (`C3` 38 mm parallax) | `93d098ddd7678a40af099bbba5680162cc19339ce31d8646d305d6ab5f7a83a3` |
| `renders/candidates_sheet.png` | `1280 × 1024` 2×2 labelled comparison sheet (`v01`, `C1`, `C2`, `C3`) | `4a35c1613aa58d545021604bfc3dc0fa1c5c8d4903a1c4491dd708ef7d1c9164` |
| `renders/after.png` | `640 × 480` 4:3 Cycles CPU 32-sample final render (`v02` / `C1` 35 mm) | `a29ccb86bec5dc3beb077f924e46386576e6cb80109e437977059a41ff09d815` |
| `renders/render_metadata.json` | Full camera/projection/render/fingerprint/hash/cold-reopen metadata | `eb9f66762b297fd3028f27d5e3733e1ba55874a40bef44b1e338496a49cc80a9` |
| `evidence/camera_comparison.md` | Camera comparison tables, MCP receipts, selection, and residuals | `ca6588422e4cdb6822b12c47a9aac6e39a3c6438e7f4eb3c23ffbb1e5bf0d277` |
| `../00_RUN_MAP.md` | Mechanically persisted Master run-map snapshot | `09d75c155b983ed9d9ff7e492a8ff88751acde49a8fb516ee1d3cb903e78d6de` |

*(Note for Cooperator Meta archival: `/Users/agile/meta/.gitignore` line 3 `*` ignores `*.json` while un-ignoring `*.md` and `*.png`; use `git add -f` when staging `renders/render_metadata.json` in `cisarik/meta`.)*

## 5. Cooperator Feedback and Brainstorming Input for Master

Michal's verbatim response on 2026-11-14:

> *"report vygenerovany, dalsi do residual moj brainstorming: plot je inak umiestneny ako na predlohe prvej chcem realisticke drevo aj drevo fasady potrebujem realisticke drevo."*

| Item | Classification | Disposition |
|---|---|---|
| 1. Camera perspective calibration (`blender/kysucka_chata_mcp_v02.blend`, `renders/before.png`, `renders/candidates_sheet.png`, `renders/after.png`) | **PASS** (camera-whole scope) | Directly verified via MCP and cold CLI reopen by Orchestrator; accepted for closure of whole `02`. |
| 2. *"plot je inak umiestneny ako na predlohe"* (foreground fence placement differs from reference) | **Cooperator observation / fixed-model geometry residual** | Recorded in `evidence/camera_comparison.md` and Section 3 above (`FENCE_post_proxy` / `FENCE_rail_proxy` on `Y = -5.78`, `X = -1.5..16.8` vs the reference's diagonal foreground fence spanning to the right edge). |
| 3. *"prvej chcem realisticke drevo aj drevo fasady potrebujem realisticke drevo"* (priority request for realistic wood on the fence and facade cladding) | **Cooperator priority for next logical whole (`future-logical-whole`)** | Handed to Master Chat Orchestrator below as Michal's primary selection input for whole `03`. |

## 6. Expired Grants and Active Job State

- **Expired Worker grants**:
  - `01/01` (`01_planning_00.md` -> `01_report_00.md`): terminal `PARTIAL` (file write blocked by Native Plan Mode; resolved via P4 completion route; plan accepted); authority expired.
  - `01/02` (`01_implementation_01.md` -> `01_report_01.md`): terminal `PASS` (`implementation-PASS` and `publication-PASS`); authority expired.
  - Task-specific `blender-mcp-live-v1` mutation authority for whole `02` is now expired.
  - No active Worker, no parallel stream, no uncommitted project mutation, and **no running render job** (`bpy.app.is_job_running('RENDER') == False`, `is_saved == True`, `is_dirty == False`).

## 7. Run-Map Update Input and Recommendation to Master

The Master-supplied snapshot was mechanically persisted unchanged to `projects/kysucka_moderna_chata/00/00_RUN_MAP.md` (`09d75c155b983ed9d9ff7e492a8ff88751acde49a8fb516ee1d3cb903e78d6de`). With the closure of this whole `02`, the reconciled run-map evidence for Master is:

```text
Run entry: 02 | kysucka-moderna-chata-reference-camera-perspective | closed | depends on: kysucka-moderna-chata-blender-mcp-first-reference-render | handout: projects/kysucka_moderna_chata/00/02-reference-camera-perspective/00_handout.md | evidence: public commit d67431d1678de511e06a8ad04cd632ae4899cdc4, working scene blender/kysucka_chata_mcp_v02.blend (35 mm at [21.5,-10.0,1.25], target [8.5,2.5,1.25], shift_y 0.105), 3-candidate MCP comparison (candidates_sheet.png, before.png, after.png), and measured fixed-model residuals completed and closed
```

**Recommendation to Master for the next bounded visual whole (`03`) based on Michal's explicit priority**:
Scope **realistic wood material/shader upgrade (and optional foreground fence placement alignment)** on top of `blender/kysucka_chata_mcp_v02.blend` (`d67431d1678de511e06a8ad04cd632ae4899cdc4`), addressing Michal's stated priority: *"plot je inak umiestneny ako na predlohe prvej chcem realisticke drevo aj drevo fasady potrebujem realisticke drevo"* (`MAT_WOOD_H` horizontal facade cladding, `MAT_WOOD_V` vertical gable/soffit/fence wood, and foreground fence placement/material realism).

## Closure Statement

CELOK UZAVRETÝ ORCHESTRÁTOROM

The logical whole `kysucka-moderna-chata-reference-camera-perspective` is closed on verified live Blender MCP evidence, the saved and cold-reopenable working scene `blender/kysucka_chata_mcp_v02.blend`, the comparable 4:3 Cycles renders (`before.png`, `candidate_01..03.png`, `candidates_sheet.png`, `after.png`), public commit `d67431d1678de511e06a8ad04cd632ae4899cdc4`, and Michal's feedback.

### Report for ORCHESTRATOR_CHAT

Logical whole identity: kysucka-moderna-chata-reference-camera-perspective  
Worker session ordinal: 01  
Worker exchange ordinal: 01  
Persistent role identity: WORKER  
Worker session target: fresh-worker-session  
Native planning mode: required  
Worker session profile: Planner  
Phase: planning  
Task identity: BLENDER-MCP-REFERENCE-CAMERA-PERSPECTIVE-PLAN  
status: PARTIAL  
Phase-qualified result: not-applicable  
Start commit: f0fb0ea25fcd091ff05e5e3717c433c586cac4fa  
End commit: f0fb0ea25fcd091ff05e5e3717c433c586cac4fa  
Report justification: new-evidence  
Logical-whole closure: not-closed

# v02 camera perspective implementation plan

The technical plan is complete. Native Plan Mode prohibits file writes, so `01_report_00.md` remains absent; this complete report is supplied through the authorized P4 completion route. No files or live scene data were changed.

## 1. Perspective discrepancies and comparison controls

Repository identity, clean `main`, baseline, AP pin and all five applicable protected hashes match the grant. `./.ap/ap doctor` passed. Meta HEAD remains `4db94c333340c6b77d06701d050de286c701dabc`; unrelated owner work is preserved.

Direct MCP observations confirmed Blender **5.2.3 LTS**, the exact open v01 path, 656 objects, 13,438 mesh vertices, saved state, no running render, and `is_dirty=False` before and after inspection. The existing protocol 15/16 warning did not prevent native calls.

Use the following **six primary landmark correspondences**. Coordinates are metres; UV uses the top-left origin. Reference annotations retain their ±15 px uncertainty.

| Landmark | World XYZ | Reference UV | v01 UV | C1 UV | C2 UV | C3 UV |
|---|---|---|---|---|---|---|
| `left_front_eave` | `(-0.55,-0.85,2.40)` | (.1195,.5856) | (.1187,.5575) | (.1202,.5730) | (.1297,.5822) | (.2006,.5456) |
| `gable_front_eave` | `(14.95,-0.85,2.40)` | (.6492,.4392) | (.6579,.5324) | (.6807,.5053) | (.6884,.4997) | (.6019,.4891) |
| `gable_peak` | `(14.95,4.20,7.45)` | (.8605,.0875) | (.8611,.1290) | (.8802,.0881) | (.8849,.0851) | (.8471,.0827) |
| `gable_near_base` | `(14.40,0.15,0.45)` | (.6996,.6897) | (.6740,.7143) | (.6916,.7253) | (.6975,.7306) | (.6310,.6828) |
| `gable_far_base` | `(14.40,8.25,0.45)` | (.9655,.6842) | (.9564,.6898) | (.9506,.6984) | (.9479,.7041) | (.9615,.6647) |
| `chimney_top` | `(11.30,3.20,8.45)` | (.6526,.0994) | (.6501,.0918) | (.6441,.0744) | (.6440,.0797) | (.6423,.0756) |

Use three auxiliary probes for the required parallax and fence controls; these are excluded from reference landmark fitting.

| Probe | World XYZ | v01 UV | C1 UV | C2 UV | C3 UV |
|---|---|---|---|---|---|
| `fireplace_front_center` | `(11.30,2.80,1.40)` | (.6351,.6228) | (.6293,.6280) | (.6293,.6333) | (.6256,.5955) |
| `mullion_0.15` | `(14.455,0.15,1.40)` | (.6769,.6275) | (.6953,.6239) | (.7014,.6256) | (.6337,.5924) |
| `fence_right` | `(16.80,-5.78,0.57)` | (.4836,.7448) | (.4668,.7796) | (.4573,.7936) | (.3140,.7081) |

Define `facade_to_gable_ratio = (near.u − left.u)/(far.u − near.u)`. The other controls use the formulas specified in the grant.

| Control | Reference | v01 | C1 | C2 | C3 |
|---|---:|---:|---:|---:|---:|
| `facade_to_gable_ratio` | 2.1818 | 1.9661 | 2.2069 | 2.2678 | 1.3026 |
| `eave_dv` | .1464* | .0252 | .0677 | .0825 | .0565 |
| `vertical_envelope_span` | .4982 | .4285 | .4848 | .4971 | .4629 |
| `fireplace_parallax` | visible, positive; approximate | −.0418 | −.0661 | −.0721 | −.0081 |
| `fence_right.u` | fence continues beyond right edge; endpoint unknown | .4836 | .4668 | .4573 | .3140 |

The reference ratio above comes directly from stored landmark coordinates. Analytic projection reproduces Blender’s baseline `world_to_camera_view` results within `4.2e-7` UV; candidate values are predictions, not rendered acceptance evidence.

Camera-solvable targets are near/far scale, facade/gable width ratio, vertical envelope and eave convergence. Preserve these fixed S00 hypotheses:

- The nominal overhanging eave is at Z=2.40, while the transom is at Z=3.18. The reference eave correspondence marked `*` is ambiguous and cannot serve as an exact registration gate.
- D01 remains at X=7.875; its reference placement is a geometry residual outside this task.
- Fireplace and chimney remain aligned at X=11.3, Y=3.2, behind the glazed gable plane.
- The fence remains on Y=−5.78. C1/C2 predict worse fireplace parallax and fence coverage; disclose these trade-offs with any promoted camera.

## 2. Three candidates and selection rule

All cameras use `PERSP`, 36 mm sensor width, existing `AUTO` sensor fit, `shift_x=0`, square pixels and a level target (`target.z=location.z`).

| ID | Location | Target | Lens | `shift_y` | Purpose |
|---|---|---|---:|---:|---|
| v01 | `[27.5,-15.5,1.70]` | `[7.45,3.15,1.70]` | 50 mm | .075 | Preserved baseline |
| `cand_01_35mm_balanced` | `[21.5,-10.0,1.25]` | `[8.5,2.5,1.25]` | 35 mm | .105 | Balanced outer envelope and facade ratio |
| `cand_02_32mm_wide_low` | `[20.5,-9.0,1.15]` | `[8.5,2.5,1.15]` | 32 mm | .115 | Stronger convergence and near-reference vertical span |
| `cand_03_38mm_parallax` | `[25.5,-9.8,1.25]` | `[7.8,2.5,1.25]` | 38 mm | .080 | Measure fireplace-parallax versus facade-ratio trade-off |

Render a fresh v01 baseline, all three candidates, then the selected camera once more as `after.png`: **five renders maximum**. Use identical **640×480, 100%, Cycles CPU, 32 samples, denoising off, frame 0, seed 0, animated seed off, AgX, look None, exposure 0, gamma 1**. Preserve all other inherited render settings.

Calculate envelope error:

`E = sqrt(mean((1448·du)² + (1086·dv)²))`

Use the five primary landmarks excluding ambiguous `gable_front_eave`. Predicted E values are **32.70 px baseline, 29.11 C1, 32.27 C2, 74.00 C3**.

Promotion rule:

1. Require unchanged non-camera scene state, successful render/readback, all five envelope landmarks within frame, and an unclipped chimney cap.
2. Require lower E and smaller absolute errors in facade ratio, vertical span and `eave_dv` than v01.
3. Among eligible candidates, find minimum E. Treat candidates within 15 reference pixels of that minimum as tied; break ties by smaller facade-ratio error, then vertical-span error, then candidate number.
4. Report fireplace/fence changes and edge cropping explicitly. These diagnostics do not override the envelope selection rule.

**C1 is the analytic favourite.** Actual rendered comparison and MCP readback must confirm eligibility.

If none qualifies, restore v01, leave `after.png` and v02 uncreated, retain comparison evidence, and return a no-promotion result. The next Master decision is to retain v01 and dispose of the measured residuals; no additional camera variants or geometry changes follow automatically.

## 3. Implementation scope, validation and rollback

Define:

- `P = /Users/agile/Projects/kysucka_moderna_chata`
- `M = /Users/agile/meta/projects/kysucka_moderna_chata/00/02-reference-camera-perspective`

**Proposed implementation mutation axes, requiring the renewed grant:**

- Repository mutation: only `P/blender/kysucka_chata_mcp_v02.blend`, `P/model/parameters.json`, `P/AGENTS.md`, `P/docs/OPERATIONS.md`, `P/README_SK.md`.
- Host mutation: live `CAM_A_REFERENCE` location/orientation/lens/shift, temporary matched render settings, canonical viewport restoration, and MCP checkpoint/render/save operations described here.
- Trace persistence: `M/renders/before.png`, `after.png`, `candidate_01.png`, `candidate_02.png`, `candidate_03.png`, `candidates_sheet.png`, `render_metadata.json`; `M/evidence/camera_comparison.md`; `M/01_report_01.md`; and `/Users/agile/meta/projects/kysucka_moderna_chata/00/00_RUN_MAP.md`.

Implementation sequence:

1. Recheck root, origin, baseline, clean state, AP pin, protected hashes, exact live v01 path and idle render state. Refuse output/checkpoint collisions or unsafe symlink destinations.
2. If dirty, preserve owner state through MCP as `P/work/mcp-v02-owner-checkpoint.blend` using `copy=True, compress=True`, then stop for baseline reconciliation. Otherwise require Object mode and save `P/work/mcp-v02-before.blend` with the same copy options.
3. Capture a compact in-memory signature of non-camera object transforms, mesh/topology/modifiers, material assignments/shaders, world and lights. Compare after camera work; retain counts as supplementary checks. No full inventory artifact is needed.
4. Render the fresh baseline from unchanged v01 at shift .075. Apply each fixed candidate through MCP, perform separate readback, calculate actual projected controls, and render its PNG.
5. Create a labelled **1280×1024, 2×2 sheet**: baseline/C1/C2/C3, each original 640×480 render beneath a 32 px label band. Use existing macOS AppKit through `/usr/bin/osascript`; its availability was verified. No dependency installation is required.
6. Select by the stated rule, render `after.png`, and inspect the PNGs through MCP `look(image=...)`. For camera viewport inspection use `shading="solid"`.
7. Restore **1448×1086, 100%, 96 samples, Cycles CPU, denoising off, `//../work/camera_a.png`**. Restore viewport `CAMERA` + `RENDERED`, scene lights/world enabled, 16 preview samples. Save the chosen scene once as active v02; never save over v01 or seed.
8. Sync only accepted camera fields in JSON: location, target, lens and shift; keep sensor width 36 and canonical resolution. Verify the existing generator formula `(Vector(cp['target']) - cam.location).to_track_quat('-Z', 'Y').to_euler()` against the saved orientation and projections. Use `1e-5` tolerance for camera/projection agreement; leave scripts unchanged.
9. Make narrow v02 working-file/camera/hash/route documentation updates. Preserve historical initialization/v01 anchors, the managed AP block and the entire existing `Closure and Git gates` section. Human-facing documentation and comparison notes are Slovak; the formal Worker report is English.
10. Mechanically persist the exact Master run-map snapshot from `00_handout.md`, after checking for owner changes. Do not rewrite frozen predecessor files or invent updated statuses.

Validation and acceptance:

- Cold-open v02 in a separate process using `/Applications/Blender.app/Contents/MacOS/Blender --background --disable-autoexec P/blender/kysucka_chata_mcp_v02.blend --python-exit-code 2 --python P/scripts/inspect_scene.py`, substituting the absolute root. Add read-only assertions for JSON camera agreement and canonical saved settings; perform no save or render there.
- Require successful cold reopen, separate final MCP readback, matching non-camera signature, preserved seed/v01/reference/generator hashes, exact changed-path allowlist, and `./.ap/ap doctor` PASS. Final GUI state must be saved, clean, active v02 with no running render.
- Metadata records input/output scene hashes, camera parameters/matrix, all projected controls and scores, actual preview versus saved settings, Cycles CPU classification, invariant checks and PNG hashes. The comparison note records MCP read/change/readback, selection and residuals.
- Cover normal promotion, no eligible candidate, dirty-owner/checkpoint collision, render failure and reopen mismatch. On failure restore preview settings in `finally`; restore the original camera or safely reopen verified v01 through MCP. Revert only task-authored JSON/documentation changes. Preserve checkpoints and failed artifacts with failure status; perform no cleanup or forced reopen over owner work.

Git fetch/staging/commit/publication remain unauthorized unless explicitly granted in the implementation prompt. Meta Git remains Cooperator-owned. Visual acceptance remains with Michal and the Orchestrator.

Changed files: none.  
Validation performed: repository/AP/hash checks, `ap doctor`, direct read-only MCP verification, analytic projection comparison, reference/baseline image inspection, destination absence checks and AppKit capability check. No renders or saves were executed.  
Git result: no fetch, staging, commit or push.  
Persistence limitation: `M/01_report_00.md` was not written or read back because Native Plan Mode forbids writes.

Smallest next step: ORCHESTRATOR persists this exact report through the P4 completion route, reconciles it, then issues the complete current-session implementation grant with Native planning mode `not-used`.

Orchestration critique:  
MEASURED: C1/C2 improve envelope controls while worsening fireplace parallax and fence coverage; preserve these as explicit comparison residuals.  
LEAD: none.

Resolved Execution Issues / Near-Misses: none.  
Pre-Existing Failure Classification: none; the known nonfatal add-on protocol warning remains unchanged.  
Authority expiry: this terminal report ends the planning grant; no implementation or autonomous continuation is authorized.

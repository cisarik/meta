# Camera perspective comparison — v02

Logical whole: kysucka-moderna-chata-reference-camera-perspective
Worker execution: session 01, exchange 02; non-independent implementation.
Input project commit: f0fb0ea25fcd091ff05e5e3717c433c586cac4fa
AP pin: d7023cf037f6d17885c3ede5c04812c61640da50
Route: task-specific blender-mcp-live-v1, with read-only CLI cold verification.

## Result and deterministic selection

Promoted `cand_01_35mm_balanced` to `blender/kysucka_chata_mcp_v02.blend`. The envelope RMSE decreases from 32.696457 to 29.110122 reference pixels (10.97%). The facade/gable ratio changes from 1.966083 to 2.206878 against 2.181820 in the approximate reference annotation. The vertical envelope expands from 0.428542 to 0.484817 against 0.498158.

C1 and C2 pass all accepted eligibility checks: identical non-camera fingerprints; successful matched renders/readbacks; five envelope witnesses and the chimney cap inside frame; lower E and smaller ratio/span/eave-control errors than v01. C3 fails E and facade-ratio improvement. C1/C2 are within the accepted 15 px E tie band, and C1 wins the facade-ratio tie-break. No fourth candidate or geometry adjustment was tried. Subjective visual acceptance remains pending.

The annotation uncertainty is 15 pixels at 1448 × 1086. Numerical projection precision does not imply accepted physical dimensions or strict image registration.

## Camera parameters and comparison profile

| Camera | Location | Target | Lens mm | shift_y |
|---|---|---|---:|---:|
| v01 | [27.5,-15.5,1.7] | [7.45,3.15,1.7] | 50 | 0.075 |
| cand_01_35mm_balanced | [21.5,-10,1.25] | [8.5,2.5,1.25] | 35 | 0.105 |
| cand_02_32mm_wide_low | [20.5,-9,1.15] | [8.5,2.5,1.15] | 32 | 0.115 |
| cand_03_38mm_parallax | [25.5,-9.8,1.25] | [7.8,2.5,1.25] | 38 | 0.08 |

All use PERSP, AUTO sensor fit at 4:3, 36 mm sensor width, shift_x=0 and target.z=location.z. Orientation uses the existing generator expression:
`(Vector(cp['target']) - cam.location).to_track_quat('-Z', 'Y').to_euler()`.

Every rendered PNG uses Cycles CPU, 640 × 480 at 100%, square pixels, 32 maximum samples, denoising off, frame 0, seed 0, animated seed off, AgX, look None, exposure 0, gamma 1 and opaque film. Inherited adaptive sampling remains enabled (threshold 0.01, min samples 0); max bounces 8, transmission bounces 6, fixed 8 threads. These settings are identical across the five renders. Cycles preferences expose METAL, while scene.cycles.device is CPU; this run uses CPU and makes no Metal acceleration claim.

| Render | Cycles CPU seconds | Dimensions |
|---|---:|---|
| renders/before.png | 5.865 | 640 × 480 |
| renders/candidate_01.png | 13.016 | 640 × 480 |
| renders/candidate_02.png | 11.556 | 640 × 480 |
| renders/candidate_03.png | 12.171 | 640 × 480 |
| renders/after.png | 12.717 | 640 × 480 |

The 1280 × 1024 sheet has baseline/C1 above C2/C3, each 640 × 480 image beneath a 32 px label band. It was composed with existing macOS AppKit; source PNGs remain untouched.

## Measured projections

Top-left UV is `(world_to_camera_view.x, 1-world_to_camera_view.y)`. The first six rows are primary correspondences; the last three are diagnostic probes. E uses the five primary points excluding ambiguous gable_front_eave:
`sqrt(mean((1448*du)^2 + (1086*dv)^2))`.

| Witness | World XYZ, metres | Reference UV | v01 UV | C1 UV | C2 UV | C3 UV |
|---|---|---|---|---|---|---|
| left_front_eave | [-0.55,-0.85,2.4] | (0.119475, 0.585635) | (0.118715, 0.557521) | (0.120166, 0.572959) | (0.129699, 0.582234) | (0.200615, 0.545589) |
| gable_front_eave | [14.95,-0.85,2.4] | (0.649171, 0.439227) | (0.657915, 0.532369) | (0.680655, 0.505255) | (0.688367, 0.499749) | (0.601885, 0.489135) |
| gable_peak | [14.95,4.2,7.45] | (0.860497, 0.087477) | (0.861064, 0.128979) | (0.880246, 0.088142) | (0.884921, 0.085102) | (0.847117, 0.082673) |
| gable_near_base | [14.4,0.15,0.45] | (0.699586, 0.689687) | (0.673991, 0.714307) | (0.691628, 0.725332) | (0.697531, 0.730615) | (0.631044, 0.682777) |
| gable_far_base | [14.4,8.25,0.45] | (0.965470, 0.684162) | (0.956418, 0.689834) | (0.950574, 0.698368) | (0.947922, 0.704108) | (0.961472, 0.664657) |
| chimney_top | [11.3,3.2,8.45] | (0.652624, 0.099448) | (0.650124, 0.091828) | (0.644069, 0.074396) | (0.643952, 0.079738) | (0.642301, 0.075553) |
| fireplace_front_center | [11.3,2.8,1.4] | auxiliary, not fitted | (0.635082, 0.622838) | (0.629253, 0.628015) | (0.629306, 0.633322) | (0.625632, 0.595468) |
| mullion_0.15 | [14.455,0.15,1.4] | auxiliary, not fitted | (0.676912, 0.627488) | (0.695315, 0.623948) | (0.701427, 0.625630) | (0.633692, 0.592352) |
| fence_right | [16.8,-5.78,0.57] | auxiliary, not fitted | (0.483617, 0.744769) | (0.466781, 0.779633) | (0.457318, 0.793641) | (0.313956, 0.708065) |

| Control | Reference | v01 | C1 | C2 | C3 |
|---|---:|---:|---:|---:|---:|
| facade_to_gable_ratio | 2.181820 | 1.966083 | 2.206878 | 2.267778 | 1.302645 |
| eave_dv | 0.146408 | 0.025153 | 0.067704 | 0.082485 | 0.056454 |
| vertical_envelope_span | 0.498158 | 0.428542 | 0.484817 | 0.497133 | 0.462916 |
| fireplace_parallax | positive; approximate | -0.041829 | -0.066061 | -0.072121 | -0.008060 |
| fence_right_u | endpoint unknown | 0.483617 | 0.466781 | 0.457318 | 0.313956 |
| outer_envelope_rmse_reference_px | 0; ranking only | 32.696457 | 29.110122 | 32.265731 | 74.004556 |

## Visual findings and residuals

- MCP look inspected the reference, fresh baseline, corrected comparison sheet and after PNG. C1 gives the long eave a stronger rise and increases near-gable vertical scale while retaining useful chimney/ridge headroom. The far right roof/fascia remains near or cropped by the image edge; the selected envelope witnesses and chimney cap remain inside.
- The nominal S00 overhanging eave lies at Z=2.40, whereas the transom is at Z=3.18. Reference gable_front_eave correspondence is ambiguous. This physical height difference remains a fixed-model hypothesis.
- D01 remains at X=7.875. Its apparent position is still left of the annotated reference door; no opening was moved.
- Fireplace and chimney remain aligned at X=11.3, Y=3.2. C1 worsens the fireplace-front probe relative to the first mullion from −0.041829 to −0.066061. C3 reduces this gap to −0.008060 but makes the facade ratio and envelope worse. This probe is a parallax diagnostic, not a complete occlusion test or proof that every possible camera is impossible.
- The fence stays on Y=−5.78. Its right rail endpoint moves from u=0.483617 to 0.466781 in C1; none of these candidates makes it span the reference's lower-right frame.
- Proxy vegetation, grey/tan sky, material appearance and low-sample interior noise are unchanged. These images support a bounded camera choice; broader visualization acceptance is not claimed.

## Preservation, source agreement and persistence

| Non-camera group | SHA-256, identical at start, candidates, saved GUI and cold reopen |
|---|---|
| combined | e27e1212796b96a4f33e6fad8ee9de354d86f65d740c4b7c537b45c540e26ef6 |
| lights | 20c34805feacaaa25192354c3cd793b6ff5f01210feae1936376e9e4104bc4cf |
| materials | d71a7f0b67b3c8f695e4c817b0bfe1a640b64cbaed8514ff2e5373f04aa3a755 |
| non_camera_objects_geometry_modifiers | 0981d3f1d2731a1a8828bffa625d034bc201c5768b37b26b5984898b7009782c |
| worlds | 43d2b066edc22e98abae123ddf0676c708e604bad6834a8bcab0ca296fc8784f |

Fingerprints serialize non-camera object world/basis transforms, parent/data identities, visibility, mesh coordinates/edges/polygons, modifiers, constraints and material slots; writable scalar material/light/world RNA properties; shader node properties, input defaults, links and color ramps. Runtime readonly caches are excluded. The full helper source and observed receipts are retained in render_metadata.json.

The baseline checkpoint was saved via MCP with copy=True/compress=True at `work/mcp-v02-before.blend` after setting the required cheap preview profile and before camera changes. The original seed and v01 were never resaved. V02 was saved as the active mainfile with copy=False/compress=True.

Only camera.location, camera.target, camera.lens_mm and camera.shift_y changed in model/parameters.json. The generator orientation agrees with the saved camera with maximum absolute Euler error 0 radians (tolerance 1e-5). No generator was run or modified.

Saved v02 settings are 1448 × 1086, 100%, 96 samples, CPU, denoising off, and `//../work/camera_a.png`. The live Layout viewport is CAMERA/RENDERED, all scene light/world flags enabled, preview_samples=16. It is saved, clean and idle. Separate cold CLI observation verifies the same camera, settings, packed 1448 × 1086 reference, 656 objects, 13,438 vertices and identical non-camera fingerprints.

PNG CRC/decompression and dimensions passed for all six PNG artifacts. Fresh baseline decoded RGBA bytes equal the predecessor after.png; final after.png decoded RGBA bytes equal candidate_01.png. Container SHA-256 values differ, with date/time/render-time metadata present; exact file and decoded-pixel hashes are recorded separately.

The managed AP block and entire Closure and Git gates section remain byte-identical. Project changes are limited to the five granted paths. Master run-map content is copied verbatim from the handout and current grant, preserving its provisional entry for this whole. No Meta Git writes, installs, downloads or external generators were used. Project publication receipts belong to the terminal report.

## MCP receipts and verification issues

Ordered tool receipts, actual camera readbacks, projections, render timings, fingerprint groups and code excerpts are in render_metadata.json. Each candidate followed camera change → separate readback/projection/fingerprint check → render. Winner promotion likewise used a separate readback before after.png. A further MCP readback after cold CLI confirmed the live connection and JSON agreement.

Resolved issues, with their first failures preserved:
1. The first read-only fingerprint helper assumed StringProperty has is_array. It raised AttributeError before any scene mutation; guarded access fixed serialization.
2. The first AppKit sheet was blank because a JavaScript assignment did not bind the native drawing context. MCP visual inspection caught it; explicit NSGraphicsContext.setCurrentContext produced the verified sheet.
3. An extra initial cold assertion required RENDERED shading in background mode and exited 2. A focused cold probe observed CAMERA/SOLID with scene light/world flags preserved. The final CLI validates saved scene data and camera flags; rendered shading is verified through live MCP. Final cold verification exits 0. No scene change or resave was needed.

The existing add-on protocol 15/16 warning and use_nodes deprecation warnings did not prevent supported operations and required no installation. Remaining limitations are the explicitly measured visual residuals and pending Cooperator/Orchestrator acceptance.

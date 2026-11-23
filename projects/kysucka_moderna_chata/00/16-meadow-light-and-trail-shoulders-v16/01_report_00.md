
# V16 — Golden meadow accents, readable forest shadows, and irregular trail shoulders

```text
Logical whole identity: kysucka-moderna-chata-meadow-light-and-trail-shoulders-v16
Worker session ordinal: 01
Worker exchange ordinal: 01
Status: PASS
Phase-qualified result: not-applicable
Logical-whole closure: not-closed
Start commit: 78534bd46020bb2bfc97eef69b05e583cba5a5e5
End commit: 78534bd46020bb2bfc97eef69b05e583cba5a5e5
Changed files: none
Git result: no writes, commits, or publication; project and AP working trees clean
Report justification: new-evidence
```

## 1. Summary and verified baseline

Implement one editable V16 candidate from immutable [V15 C](work/v15/reference_01/checkpoints/candidate_exterior_v15_tonal.blend), using owned material copies, coordinated terrain/trail masks, and a small additional shoulder population. Preserve the existing meadow distribution and geometry, all forest placements, cottage, garden, camera, interior, and packed images.

Project root `R` is `/home/agile/Projects/kysucka_moderna_chata`. The verified input is 433,603,200 bytes, SHA-256:

`15870b192662714a40ae7772a120e554acd9c3317e6ebfa1be54d4ac907d5bf2`

The physical root, `main`, expected commit, local backup origin, and AP gitlink/submodule HEAD match the grant. The canonical GitHub identity is corroborated by local project documentation and LFS configuration; public branch equality was outside this planning check.

All nine supplied input hashes matched before and after inspection. The actual A/B/C/reference images and required recipes, reports, AP anchors, and trace records were inspected.

One isolated Blender 5.3.0 process completed successfully:

| Observation | Measured result |
|---|---:|
| Inspection duration | 8.70 s |
| Peak sampled process RSS | 2.00 GiB |
| Minimum sampled system available RAM | 16.44 GiB |
| Other Blender process | Owner GUI PID 2452, start_ticks 12233 |
| Scene saves / renders | 0 / 0 |
| Global preference/startup/recovery stat/SHA witnesses | Unchanged |

`/tmp/opencode/v16_plan_inspect` was completely removed. The V16 output directory and report destination remain absent. No live MCP tool was called.

## 2. Measured scene and shader inventory

The saved scene contains **5,952 objects, 3,013 meshes, and 95 materials**.

| Owner | Measured state |
|---|---|
| `V11_TERRAIN_NEAR` → `V13_V11_TERRAIN_NEAR_MESH` | 34,263 vertices; 67,918 faces. Slot 4, `MAT_V11_CONTINUOUS_MEADOW_FINAL`, serves 10,816 faces; slot 5, `MAT_V13_ECOLOGICAL_MEADOW`, serves 57,102. |
| `V11_TERRAIN_FAR` → `V13_V11_TERRAIN_FAR_MESH` | 45,843 vertices; 91,101 faces. Ecological slot 5 serves 88,638 faces; the remaining 2,463 use retained slot 1. |
| `V11_TERRAIN_EXTENSION` → `V13_V11_TERRAIN_EXTENSION_MESH` | 40,719 vertices; 79,776 faces, all using ecological slot 2. |
| Terrain fields | `v13_ecology` and `v13_exterior_weight` are POINT floats. Near terrain has 5,568 exact-zero exterior weights protecting the original core. Geometry, UVs, shell flags and corner normals are explicitly stored. |
| `V07_TRAIL` → `V07_TRAIL_MESH` | Closed mesh; 25,612 vertices, 47,846 faces, 51,220 triangles. Its top has 12,806 vertices and 22,236 faces. Material: `MAT_V07_GRAVEL`; no modifiers. |
| `V07_GATE_TRANSITION` | Separate concrete connector: 12 vertices, 14 faces, 20 triangles. |
| `V07_SHOULDER_POINTS` | 60,552 points, hidden in viewport and render. Its former restoration strip extends to 1.15 m; this does not establish the requested shoulder-width zone. |
| Existing details | `V07_STONES_POINTS`: 300 active instances; `V07_LITTER_POINTS`: 600. Core retains 196 shoulder-derived points in `V11_CORE_GRASS_V07_SHOULDER_POINTS`. |
| Exterior meadow | 29,000 points in 52 `V13_MEADOW_CLOUD_*` meshes, using `V13_MEADOW_IsViewport`. Stored attributes include `prototype`, `rotation`, `scale`, and `ecology`. |
| Meadow libraries | `V13_MASTER_MEADOW_RENDER`: 48 forms, 4,324–10,201 triangles each; total library 342,288 triangles. Unscaled form heights span 0.160–0.410 m. `V13_MASTER_MEADOW_WORK` contains 3,043 triangles across 48 forms. |
| Forest | 6,200 placements in 126 active `V11_FOREST_*` clouds, using `V12_WRAP_V11_FOREST_GN`. |

The four meadow materials are:

- `MAT_V09_MAT_V08_MAT_V06_GREEN`
- `MAT_V09_MAT_V08_MAT_V06_OLIVE`
- `MAT_V09_MAT_V08_MAT_V06_THATCH`
- `MAT_V09_MAT_V08_MAT_V06_MEADOW_CARD`

Each has 208 mesh users across predecessor, core, and exterior libraries. V16 must copy these materials and bind the copies only to its exterior render masters. Preserve the atlas alpha, normal, roughness, UVs, and existing 0.12 translucency mix.

`MAT_V13_ECOLOGICAL_MEADOW` combines the preserved substrate with ecology-driven green/dry colors, 0.40 image multiplication, and a six-metre exterior transition. Its inherited bump uses strength 0.22 and distance 0.026 m. Although `MAT_V07_SHOULDER` remains in terrain slots, no active terrain face uses it.

The retained route has **1,105 samples**, length **198.180813 m**, maximum sample interval **0.199971 m**, and widths **1.12–2.10 m**, ending at `[42,138.25]`. Across every gravel top vertex, measured gravel-to-active-terrain separation is **0.014999866–0.015000343 m**.

The active world is `V15_WORLD_REFERENCE_LIGHT`. Camera rays use capped Kloofendal clouds; other rays use capped Qwantani. C values are fill strength 0.73, tint `[1,.90,.70]`, clouds strength 2.35, tint `[1,.77,.49]`. The active key is `V15_SUN_REFERENCE_KEY`: energy 2.8, color `[1,.88,.69]`, azimuth 285°, elevation 17.6°, diameter 2°. Its measured source vector is approximately `[.246704,-.920712,.302370]`.

All five existing working-library checks passed through `_working_branch`: forest, core lawn, core meadow, predecessor exterior meadow, and V13 meadow. All **87 file images are packed**, use relative paths, and resolve to existing targets.

## 3. Implementation changes and fixed defaults

**Recipe and ownership**

Create import-safe `apply_v16(scene, config, ROOT) -> dict`. The recipe performs explicit in-memory changes; drivers own loading, saving, rendering, and receipts. Use isolated seed **13716**, configuration hashing, and a stored V16 summary. A repeated application with the same configuration must verify and return the existing result without duplication.

Copy the three active terrain meshes and trail mesh into V16-owned derivatives. Preserve all original geometry buffers, UVs, normals, existing attributes, face material indices, and transforms; add only V16 mask/coordinate attributes and replace the required material bindings. Retain predecessor meshes and world, adding fake users only where needed for retention.

Create `V16_MASTER_MEADOW_RENDER` with 48 linked mesh objects and object-level overrides for four owned material copies. Clone the meadow GN group and change only its render-library reference. Preserve its existing IsViewport TRUE arm, working library, stride eight, and point attributes. The 29,000 placements and all existing master geometry remain exact.

**Golden accents and meadow texture**

Use one shared shader field based on world XY coordinates:

- Noise lengths: **18 m, 3 m, and 0.28 m**; Detail 2, Roughness 0.5.
- Warm-patch field: `F = smoothstep(.36,.68,.65*N18 + .35*N3)`.
- Sun-facing factor: `D = smoothstep(.18,.62,dot(normalized_unbumped_normal, key_source_vector))`.
- Terrain golden mix: `0.38*D*F`, gated by the existing exterior weight. Golden linear RGB: **`[.30,.255,.065]`**.
- Meadow golden mix: `(0.08 + 0.22*D)*F`, applied consistently to the existing diffuse and translucent color branches. Golden linear RGB: **`[.38,.32,.075]`**.
- Shared three-metre brightness multiplier: **0.86–1.14**. Additional meadow micro multiplier: **0.88–1.14**; terrain micro multiplier: **0.94–1.06**.
- Meadow roughness modulation: ±0.04, clamped to **0.62–0.94**.
- Exterior terrain micro-bump: strength **0.15**, distance **0.008 m**, chained with the retained normal treatment.

Keep emission at zero and preserve atlas transparency. Existing tuft positions, rotations, scales, heights and basal envelopes remain unchanged. Actual Cycles lighting supplies occlusion and cast shadows; the sun-facing tint is an albedo treatment.

**Forest-shadow balance**

Copy the C world to `V16_WORLD_MEADOW_BALANCE` and change only the fill:

| Control | V16 default |
|---|---:|
| Fill strength | **0.92** |
| Fill linear tint | **`[1,.94,.80]`** |
| Fill saturation / cap / azimuth | Retain **0.58 / 2.35 / 39.052734375°** |
| Camera-cloud branch | Retain C exactly |
| Key light | Retain C exactly |
| Forest materials and interior lights | Preserve exactly |

This raises shaded illumination between B and C while retaining C’s stronger key and cloud appearance. The chosen forest crop’s median encoded luma is 24.63 in C and 32.99 in B. Its high-frequency RMS is nearly equal in both; the measured deficit is primarily dark tonal placement.

**Irregular trail and shared shoulder masks**

Treat **0.45–0.75 m as the width of each shoulder**, measured outward from the effective gravel edge. Preserve the closed trail geometry and terrain support. Produce irregular effective width through coordinated opaque surface blending and low vegetation.

Reconstruct only the retained route’s XY/station/width queries; use the actual C triangles for support. For side `σ`:

- `h(s) = existing_width(s)/2`.
- `a(s) = smoothstep(1,4,s) * [1-smoothstep(L-3,L,s)]`.
- Effective edge: `Eσ(s) = h(s) - a(s)*(.02 + .04*Nedgeσ(s))`.
- Shoulder width: `Wσ(s) = .45 + .30*Nwidthσ(s)`.

Use V13’s integer-lattice hash with quintic interpolation and `iy=0`. Edge wavelengths are **2.7/8.5 m**, weights **.65/.35**; shoulder wavelengths **4.5/13 m**, weights **.70/.30**. Set salts to `13716 + 100*side_index + 10*channel + octave`, with left/right indices 0/1 and edge/width channels 0/1.

Store station, signed lateral coordinate, half-width, both edge values, both shoulder widths, and the active/protection mask on the derived terrain/trail meshes. Compute absolute lateral distance in the shader after interpolation.

Use the same surface-blend group on gravel and terrain:

- For `d = abs(lateral)-Eσ ≤ 0`, retain gravel.
- Over **0–0.12 m**, blend gravel into worn loam, linear RGB **`[.115,.095,.040]`**, roughness **0.96**.
- From **0.12 m to Wσ**, blend loam into the local V16 substrate.
- Retain the existing three packed gravel maps and three-metre route UV scale. Bake matching route UVs onto the terrain halo.
- Preserve the central corridor `abs(lateral) ≤ h(s)-.08` as gravel. Its minimum width is **0.96 m**.
- Protect the enclosed garden, paving, concrete transition and gate geometry. Use a 0.10 m exclusion around the transition and garden boundary; fade treatment at route endpoints.

Add eight source-derived low-tuft masters from complete connected components of V13 low forms. Heights: **0.06–0.14 m**; render limit **192 triangles/master**. Scatter on a jittered **0.20 m** lattice, with density rising smoothly from **6 to 24 tufts/m²** across the shoulder. Hard cap: **6,000**, selected by global deterministic rank if necessary.

Every full transformed tuft hull must clear the effective gravel edge by **0.02 m**, the protected travelled core, and existing obstacle masks. Support roots on the actual visible terrain/gravel surface. Reject envelopes crossing an unresolved gravel-height step; try scale refinements **0.75**, then **0.5**, before rejection.

New shoulder vegetation receives its own IsViewport switch, off-scene libraries, working stride four, and working masters capped at **24 triangles**. Maximum additional working cost is therefore **36,000 triangles**.

## 4. Validation, visual criteria, and resource envelope

Run three serialized native jobs: **build/save**, **fresh-input replay without saving**, then **cold reopen/render**. Each job uses the canonical CLI, `--background --disable-autoexec --threads 4`, nice +10, isolated configuration/temp directories, the exact prepared MCP-disabled preferences, disabled persistence, and bytecode writing disabled.

Before every child, verify the exact owner GUI identity, absence of foreign background Blender, immutable hashes, clean Git/AP state, and **≥12 GiB available RAM**. Sample resources every second. Stop only the owned child on RSS exceeding **8 GiB**, available RAM falling below **6 GiB**, or process-identity divergence; use 7 GiB as an early-stop threshold. Preserve the first failure.

**Preservation and portability**

- Snapshot all predecessor objects, meshes, materials, node groups, lights, worlds, images, camera and saved UI. Enumerate allowed binding/retention changes explicitly.
- Prove exact terrain/trail geometry, UVs, normals and existing attributes; exact 29,000 meadow records and 6,200 forest records; unchanged protected cottage/garden/interior data.
- Prove idempotence, fresh replay equality, and cold semantic equality.
- Verify all 87 packed image hashes, colorspaces, relative strings and resolved targets. Keep the candidate at the same directory depth as C, including the exact Qwantani string `//../../../v14/assets/qwantani_sunset_puresky_2k.hdr`.
- Re-run `_working_branch` for every existing working library and the new shoulder library. Verify off-scene render masters and both switch arms. Headless checks establish branch/cost preservation; they do not measure a new orbit FPS.

**Actual support and clearance**

Reuse validated predecessor support only after proving unchanged geometry and placement buffers. For every new tuft, exhaustively test the transformed basal envelope against clipped actual surface triangles, then check basal vertices after float32 storage. Allow maximum root exposure **1 mm**, maximum burial **18 mm**, and refine support spans above **5 mm**.

Test full body hulls against the actual emitted core/shoulder masks, including interpolated attributes. Require zero core, paving, garden, gate, post or protected-trunk intersections. Verify shoulder-width bounds within **2 μm numerical tolerance** and report accepted/rejected populations.

**Matched render**

Preserve the exact saved `CAM_V11_VALLEY_REVIEW` matrix and optics: position `[62,-27,12]`, 35 mm, sensor 36 mm, zero shifts. Use CPU4, 96 samples, 960×540, adaptive 0.01, OIDN Accurate/High with GPU denoising off, frame/seed zero, AgX/None, exposure zero and gamma one.

Native render time must remain **below 157.5 s**. Apply a 240 s whole-child watchdog to the cold/render job. Fully decode the PNG, verify opaque alpha and dimensions, and rehash the unchanged candidate after rendering.

**Image measurements and review**

Use fixed 960×540 crop boxes:

| Crop | Pixels `(x0,y0,x1,y1)` |
|---|---|
| Front meadow | `(288,448,672,518)` |
| Left / right slopes | `(29,157,192,243)` / `(758,178,902,248)` |
| Shaded left forest | `(10,8,126,52)` |
| Cottage shadow / adjacent lit grass | `(551,276,567,288)` / `(628,276,644,288)` |
| Sky | `(413,3,605,24)` |
| Front / right / upper trail | `(280,378,550,413)` / `(640,265,710,343)` / `(720,145,825,220)` |

Record RGB means, encoded-luma percentiles/std, Gaussian high-pass RMS at σ=1.5 px, clipping, and golden-pixel fraction. Define golden pixels as `R/G>.99`, `G/B>1.35`, and luma above 80.

Measured baseline and proposed review thresholds:

| Metric | C | B | Reference¹ | V16 criterion |
|---|---:|---:|---:|---|
| Front meadow luma std | 8.85 | 9.50 | 20.57 | 10.2–16 |
| Front high-pass RMS | 5.74 | 5.75 | 13.31 | ≥6.3 |
| Left / right slope luma std | 4.57 / 6.45 | 5.77 / 7.59 | 21.24 / 20.21 | ≥5.5 / ≥7.8 |
| Forest median luma | 24.63 | 32.99 | 34.49 | 28–33; p5 ≥18 |
| Cottage shadow/lit median ratio | .633 | .753 | — | .60–.71 |

¹ Reference resized only in memory; its framing differs, so these are appearance comparisons.

Require increased golden fraction in all three meadow/slope crops, retained dark-green regions, sky mean RGB within one encoded level of C, and no new sky clipping. Compare projected trail-edge profiles and 1:1 crops: front-edge transition width should increase by at least 25%, with visible irregular shoulders and a continuous clear core.

These measurements guide the single visual review. Direct pixel inspection must also reject yellow blotches, contour bands, exposed uniform gravel rims, floating tufts, or broken meadow continuity.

## 5. Deliverables, assumptions, and disposition

All implementation writes require the renewed grant and remain under `work/v16/meadow_trail_01/`:

- `source/meadow_trail_v16.py`
- `source/meadow_trail_v16.json`
- `checkpoints/candidate_exterior_v16.blend`
- `renders/B_v16_960.png`
- `worker/**` — isolated drivers and supervisor
- `proofs/**` — preservation, replay, support, portability, resource and crop evidence
- `runtime/**` — isolated prepared configuration and temporary runtime data

Reserve one separately authorized correction using `source/meadow_trail_v16_c01.{py,json}`, `checkpoints/candidate_exterior_v16_c01.blend`, `renders/C_v16_c01_960.png`, and `c01_*` receipts/runtime paths. Preserve the first candidate and render. Keeping both checkpoints in the same directory preserves image-path depth.

Defaults are shader-led meadow refinement, unchanged existing tuft geometry, per-side shoulder widths, and effective trail-width variation over supported retained geometry. Initial delivery contains one native 960×540 render. UHD, architecture, interior changes, GUI benchmarking, asset downloads and Git publication remain outside this slice.

Risks: the selected shader/light values are proposed defaults requiring rendered inspection; the reference has different framing and richer landscape structure. Existing trail geometry retains its approximately 15 mm physical lip, which must be visually concealed by the coordinated blend and supported low cover.

**Smallest next step:** Orchestrator disposition of this plan, followed by a complete implementation prompt targeting the current Worker session with `Native planning mode: not-used`.

**Report delivery:** Complete text is returned here for the named Orchestrator relay to `/home/agile/meta/projects/kysucka_moderna_chata/00/16-meadow-light-and-trail-shoulders-v16/01_report_00.md`. No report file was written.

**Orchestration critique**  
MEASURED: The active terrain does not use its retained shoulder-material slot, and the original shoulder cloud is hidden. V16 must address active terrain, gravel and population masks together.  
LEAD: None.

**Resolved Execution Issues / Near-Misses:** No scene-inspection or resource failure. Verbose legacy provenance output was reduced to bounded summaries without another Blender launch.

**Pre-Existing Failure Classification:** No prerequisite failure. The documented meadow, shadow and shoulder appearance gaps remain the intended correction targets.

**Authority expiry:** Submission of this terminal planning report expires the current grant. Implementation requires the complete renewed authority described above.


# V17 implementation plan — meadow plants, broadleaf margins, and front-loop gravel

Build one local candidate from `work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend`, SHA-256 `5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1`. Keep the selected B palette, camera, cottage, glazing, garden, orchard, and route geometry. The pilot covers the close hillside, a 15 m section of the front loop, and the right forest margin. Full V17 extends that treatment to the measured front loop and adds three asymmetric broadleaf groups and one open-slope birch.

## 1. V16 B scene audit

The saved scene has 5,084 linked objects, 87 packed file images, and zero external Blender libraries. `V11_FOREST` has 126 active point clouds. `V13_MEADOW_CLOUDS` carries 29,000 points in 52 clouds, using the 48 `V16_MASTER_MEADOW_RENDER` masters and `MAT_V16_GREEN`, `MAT_V16_OLIVE`, `MAT_V16_THATCH`, and `MAT_V16_MEADOW_CARD`. The eight `V16_MASTER_SHOULDER_RENDER` masters are 6–14 cm tall. `V16_SHOULDER_POINTS` has 2,903 points overall and 558 in the front-loop interval, split 285 meadow-side and 273 garden-side.

| Off-scene working library | Masters | Triangles per master | `IsViewport` True consumer |
|---|---:|---:|---|
| `V12_WORK_CORE_LAWN` | 48 | 54–64 | `V12_WRAP_V11_CORE_LAWN_GN` |
| `V12_WORK_CORE_MEADOW` | 96 | 51–64 | `V12_WRAP_V11_CORE_MEADOW_GN` |
| `V12_WORK_EXTERIOR_MEADOW` | 16 | 62–64 | `V12_WRAP_V11_MEADOW_GN` |
| `V12_WORK_FOREST` | 6 | 5,400–6,300 | `V12_WRAP_V11_FOREST_GN` |
| `V13_MASTER_MEADOW_WORK` | 48 | 61–64 | `V16_MEADOW_IsViewport` and its retained `V13_MEADOW_IsViewport` predecessor |
| `V16_MASTER_SHOULDER_WORK` | 8 | 21–24 | `V16_SHOULDER_IsViewport` |

All six links independently passed the check from Collection Info through Instance on Points to the True input of a switch driven by `IsViewport`. Preserve every branch graph and master. The forest wrapper has no point stride, so removing the four named records from owned cloud copies preserves the working representation of every surviving tree.

| V11 cohort | Count | Height min / median / max, m | Vertical scale min / median / max |
|---|---:|---:|---:|
| Young | 1,220 | 1.504 / 4.006 / 6.491 | .157 / .417 / .676 |
| Middle | 1,717 | 7.005 / 11.297 / 16.000 | .637 / 1.163 / 1.666 |
| Mature | 3,263 | 13.000 / 18.341 / 23.997 | 1.169 / 1.898 / 2.498 |

All 6,200 render points matched the saved registry and its float32 scales. The separately linked `V04_YOUNG_00`, `01`, and `02` are visible at `(-8,0)`, `(-13.5,4.5)`, and `(13,13.5)`, with heights 2.10, 3.00, and 2.30 m. Preserve them. `V04_YOUNG_03` is hidden. Its archived V06 replacement is a point at `(10,19.25,0.889166)` in the predecessor lineage. The nearest active V11 root to that XY is 48.46 m away. The audit found no separately named V06, V07, or V08 young spruce objects.

**Front loop.** Use stations `5 ≤ s ≤ 44 m` for the V17 treatment. The route uses its existing 1,105 samples over 198.180813 m from the gate to the north boundary at `(42,138.25)`. Negative lateral is the meadow side here. The archived `edge_left` and `width_left` consequently refer to the negative side. UV below is normalized from the top left of `CAM_V11_VALLEY_REVIEW`. Z is the gravel top at the centerline.

| s, m | Center XYZ, m | h | B edge left / right, m | B shoulder left / right, m | Center UV |
|---:|---|---:|---|---|---|
| 5 | `(8.93277,-13.05352,.17475)` | .63370 | .58305 / .59261 | .58925 / .71791 | .155 / .659 |
| 7.5 | `(10.81001,-14.70010,.38789)` | .63781 | .59298 / .60129 | .58425 / .69860 | .133 / .671 |
| 16 | `(18.86752,-15.08175,.48605)` | .64925 | .59508 / .59918 | .58028 / .52168 | .171 / .730 |
| 24 | `(22.79127,-8.83559,.02860)` | .65462 | .60968 / .62528 | .54818 / .57262 | .337 / .744 |
| 30 | `(23.00076,-2.84138,.03273)` | .65444 | .60753 / .61120 | .58731 / .57337 | .453 / .711 |
| 36 | `(22.59411,3.14333,.10138)` | .65062 | .60639 / .60099 | .58320 / .58893 | .546 / .677 |
| 42 | `(21.99029,9.11282,.18350)` | .64365 | .60576 / .60889 | .54897 / .58172 | .624 / .645 |
| 44 | `(21.89181,11.11017,.20197)` | .64077 | .60197 / .60822 | .61682 / .63330 | .649 / .636 |

At `s=30`, the gravel top 6 mm inside the negative and positive lips is respectively `(23.6491,-2.8286,.0198)` and `(22.3524,-2.8542,.0197)`. At 50 mm outside, the corresponding terrain Z is `.0027` and `.0060` m. At `s=24`, the two top heights 6 mm inside are both `.0156` m, and the terrain 50 mm outside is `−.0011` and `.0010` m. Across the entire audited front interval, all 795 gravel boundary vertices have exact XY matches on the terrain, 560 on `V11_TERRAIN_NEAR` and 235 on `V11_TERRAIN_FAR`. The stored V16 route attributes agree exactly at those vertices. Lip height is `14.999986–15.000015 mm`.

| Front-loop surface sample | Intersected triangles / source vertices | Clipped XY area | Triangles / m² |
|---|---:|---:|---:|
| `V07_TRAIL` top, s 5–44 | 4,451 / 2,632 | 50.591 m² | 87.98 |
| `V11_TERRAIN_NEAR`, s 5–44, within `h+.75 m` | 8,878 / 4,795 | 76.279 m² | 116.39 |
| `V11_TERRAIN_FAR`, same band | 3,537 / 1,918 | 32.858 m² | 107.64 |
| Pilot gravel top, s 21–36 | 1,710 / 1,020 | 19.614 m² | 87.18 |
| Pilot near terrain, within `h+.75 m` | 4,646 / 2,495 | 42.109 m² | 110.33 |

The active trail shader is `MAT_V16_V07_GRAVEL`. B begins changing gravel 20–60 mm inward from the lip, while its grass transition starts 120 mm beyond that origin. The lip therefore retains gravel dominance, and the B tufts stop off the gravel. C01 demonstrated the shared-substrate and separate gravel-root technique. Its archived polarity-independent front-edge width was 4.23 px versus 2.78 px for B, with the outer brightness polarity reversed. Use the lip technique with B’s substrate. [V16 B](</home/agile/Projects/kysucka_moderna_chata/work/v16/meadow_trail_01/renders/B_v16_960.png>) · [C01 comparison](</home/agile/Projects/kysucka_moderna_chata/work/v16/meadow_trail_01/renders/C_v16_c01_960.png>) · [Edge measurements](</home/agile/Projects/kysucka_moderna_chata/work/v16/meadow_trail_01/proofs/c01_edge_polarity.json>)

## 2. Target zones, pilot, and fixed low witness

**A — close hillside.** Recompute the five surveyed XY vertices by casting the listed main-camera rays onto the audited near hillside. Use their convex hull unioned with the buffered pilot footprint below. Keep roots at main-camera `u=.16–.86`, `v=.75–.985`, and depth `≤22 m`. The depth filter keeps the close hillside separate from the opposite ground visible through the same frame band.

| Main UV | Terrain XYZ, m | Closest route s, m |
|---|---|---:|
| `.16,.800` | `(46.733929,-22.973505,7.314148)` | 20.079 |
| `.35,.770` | `(47.269444,-19.940622,7.207313)` | 20.702 |
| `.86,.770` | `(52.996902,-13.885490,7.584684)` | 23.062 |
| `.86,.975` | `(56.051716,-18.232145,7.800160)` | 21.741 |
| `.16,.975` | `(51.494843,-24.279903,7.667785)` | 20.225 |

**B — meadow beside the fence loop.** Use `7.5 ≤ s ≤ 42` and `−(h+1.35) ≤ lateral ≤ −(h+.12)`. At `s=7.5` the strip runs from `(10.3628,-15.3119)` to `(9.6368,-16.3048)`, at `s=24` from `(23.5623,-8.9100)` to `(24.7866,-9.0283)`, and at `s=42` from `(22.7511,9.1783)` to `(23.9766,9.2837)`. Their main-camera UV ranges are `.094–.118/.664–.671`, `.343–.353/.753–.776`, and `.634–.651/.650–.662` respectively. Use the trail field in section 5 for the two shoulders closer to the lip.

**C — forest margins.** For each of the R, L, and D groups in section 4, the understorey domain is the convex hull of the listed roots buffered by 5 m. Keep the meadow-facing half, defined by the side of the hull’s centroid toward the valley axis. Keep foliage root footprints outside trunk and corridor masks. The three group envelopes project to R `u=.762–.847, v=.090–.232`, L `.121–.219, .096–.197`, and D `.709–.781, .081–.164`. Use basal cover and seed-bearing grasses here. Reserve individual flower heads for A and B.

**Pilot footprint.** Use the convex hull of these four anchors buffered by `.65 m`, with A’s projection and depth filters. Include B and both shoulders only at `s=21–36`, and group R with its C understorey. Force one supported white head at each of the first and third anchors, a yellow head at the second, and an arching seed stem at the fourth before adding the seeded clusters.

| Pilot anchor XYZ, m | Main UV | Low witness UV at ground + .36 m |
|---|---|---|
| `(46.689899,-19.693404,6.981531)` | `.348,.774` | `.674,.716` |
| `(45.643211,-20.053246,6.648271)` | `.306,.787` | `.386,.797` |
| `(45.766047,-19.150921,6.536287)` | `.354,.786` | `.564,.764` |
| `(44.895369,-19.543401,6.280423)` | `.316,.795` | `.381,.810` |

Create `CAM_V17_LOW_DETAIL` at `(48,-21.75,8.070608535)`, looking at `(33.871910472,-7.882651524,5.225659935)` via `to_track_quat('-Z','Y')`. Use 28 mm, horizontal 36 × 24 mm sensor, 16:9, zero shifts, clips `.03–450 m`, and depth of field off. Evaluated ground at the eye is `7.390608535 m`, giving a `.680 m` eye height. The negative shoulder at `s=30` projects to `(.413,.659)` at 31.44 m camera depth. R3’s crown witness projects to `(.617,.196)` with a clear ray against terrain, cottage and fence bounds, and retained conifer crown cylinders. Keep the low pose fixed for both predecessors and all candidates.

## 3. Botanical masters and population

**Asset selection.** The prior isolated test verified direct meshopt geometry decode and an embedded KTX2 failure with `0 × 0` images. Externalizing image buffer views to KTX2 sidecars and importing the local `.gltf` with stock `import_ktx_texture=True`, `import_pack_images=True`, and `merge_vertices=False` produced readable packed OpenEXR with working color, alpha, and normals. Its tiny native preview resolved both flower forms and the LOD1 crown profiles. [Prior asset probe](</home/agile/meta/projects/kysucka_moderna_chata/00/17-meadow-wildflowers-and-broadleaf-edges-v17/01_report_00.md>) · [tevy format documentation](https://tevy.dev/docs)

| Source | Verified geometry and V17 use |
|---|---|
| tevy Wildflower Patch v1 LOD0, CC0 | 3,860 triangles, 118.9 × 114.3 × 53.5 cm. Separate white heads measuring 5.1–7.4 cm across, yellow heads measuring 3.1–4.0 cm across, and low green leaf components. |
| Poly Haven Dandelion 01 1K Blend, CC0, Rico Cilliers and Rob Tuytel | `dandelion_01_a_LOD2` and `dandelion_01_b_LOD2`, 629 and 619 triangles, 15.9 and 11.3 cm high. Use their basal foliage. The prior exchange verified geometry and map readback. |
| Local Grass Medium 01, Shrub 01, Periwinkle Plant | Verified heights 14.5–32.3, 29.4–37.2, and 20.6–39.7 cm respectively. Select `V04_MASTER_GRASS_MEDIUM_01_1` and `_2` and `V16_SHOULDER_00` through `_07` as blade sources. Keep shrub and periwinkle libraries available as baseline assets. |

[Wildflower Patch](https://tevy.dev/models/wildflower-patch) · [Dandelion 01](https://polyhaven.com/a/dandelion_01) · [Local asset manifest](</home/agile/Projects/kysucka_moderna_chata/assets/ASSET_MANIFEST.md>)

- **Flower masters.** Weld only for component detection at `10 µm`; copy the original faces and UVs. Select eight-triangle caps by first polygon index. White IDs are `2380, 2436, 2492, 2548, 2604, 2660, 2716, 2772`. Yellow IDs are `2828, 2878, 2928, 2978, 3028, 3078, 3128, 3178`. Attach each cap at its centroid to a tapered five-sided curved stem. White terminal heights are `.27, .31, .35, .39 m` and yellow `.18, .22, .26, .30 m`, cycling in ID order. Keep the source cutout and normal. Multiply yellow RGB by `.82` in an owned material.
- **Basal masters.** From the tevy mesh, select the first six whole non-flowering green components in polygon order with horizontal span `.025–.16 m` and top `≤.15 m` above the source ground. Verify classification from alpha-covered atlas samples, rejecting white, yellow, or pink parts. Use three source leaves per clover-like cluster, yawed at `0°, 117°, 247°` with radial offsets `.020, .026, .018 m`. For each dandelion LOD2 object retain connected basal foliage with top `≤.075 m` above its mesh base. Bake transforms and root at the basal centroid. Use the dandelion forms on one in eight accepted basal placements, alternating `a` and `b`. Preserve their UVs and material dependencies.
- **Stems and seedheads.** Use physical arch geometry. A stem of height `H` follows cubic controls `(0,0,0)`, `(.01,0,.39H)`, `(.07,0,.82H)`, and `(.13,0,H)`. Use ten segments, five sides, and radius `.0014–.00055 m`. Make three six-spikelet tiers across the terminal 4–7 cm, with 4–9 mm tapered spikelets. Cycle nominal `H=.26,.34,.42,.48 m`. Use linear RGB `(.102,.078,.035)` on dry stems and `(.240,.145,.054)` at seedheads, roughness `.76–.88`, with three owned brightness variants `.88, 1, 1.09`. The frozen world fill is `.92` with tint `(1,.94,.80)` and the V15 key sun is `2.8`. Warm highlights come from these lit forms and the existing exposure.
- **Scattering.** Use seed `13717` and keyed BLAKE2b uniforms over layer and integer cell coordinates. Generate cluster centers on a 1.2 m grid, jitter each axis by ±`.54 m`, keep with probability `.45`, and accept in hash order with `.90 m` minimum center separation. Insert the four pilot centers first. Give each center randomized yaw and ellipse radii `.45–1.10 m` and `.28–.65 m`. Let `C` be the maximum of `(1−q²)²` inside these ellipses, where `q` is normalized elliptical radius. On `.20 m` jittered candidate cells, accept with probability `λ × .04`, using independent keys by layer.

| Zone | Basal λ/m² | Seed stem λ/m² | White λ/m² | Yellow λ/m² |
|---|---:|---:|---:|---:|
| A | `.65+3.4C` | `.45+3.0C` | `.55C²` | `.24C²` |
| B | `.45+2.3C` | `.20+1.35C` | `.24C²` | `.10C²` |
| C | `.12+.65C` | `.10+.70C` | 0 | 0 |

Add yaw uniformly over one turn, scale `.82–1.12`, and bend by `4–17°` about the local root axis. Use accepted components rather than whole atlas patches, with `.12 m` minimum separation between flower roots. Retain the existing low cover and all 52 V13 clouds. Suppress a new basal or stem candidate if it is within `.14 m` of a V13 root or overlaps an accepted trail-edge root footprint. Select the lowest hashes at combined A/B/C caps of 500 basal, 350 seed, 52 white, and 24 yellow placements, counting forced pilot witnesses first.

Store position, prototype, rotation, and scale on owned point meshes. Use `V17_BOTANICAL_IsViewport` with whole leaf or stem components capped at 32 triangles per proxy. Retain every other basal and stem point in the working arm, with all pilot and flower points represented by their simple proxies. The render arm uses linked full masters.

## 4. Broadleaf placement and clearances

Use tevy v1 LOD1 for render, European Beech at 17,674 triangles and Silver Birch at 11,108. Their measured unscaled leaf envelopes are `16.14 × 18.30 m` and `10.97 × 11.07 m`. Use the verified LOD2 geometry in `V17_BROADLEAF_IsViewport` as the working proxies, with simple owned solid bark and crown colors. The eight placements total 108,562 render triangles and 44,354 working triangles before instancing. Preserve authored trunk centers, crown asymmetry, and underside root geometry. [European Beech](https://tevy.dev/models/european-beech) · [Silver Birch](https://tevy.dev/models/silver-birch)

| ID | Species | XY, m | Terrain Z, m | Closest s, m | Scale / yaw | Scaled crown width XY, m | V11 action |
|---|---|---|---:|---:|---|---|---|
| R1 | Beech | `(-60.69144,133.50793)` | 19.41421 | 149.22 | `.46 / 32°` | `7.43 × 8.42` | Replace `V11_TREE_01610` |
| R2 | Birch | `(-66.30013,142.67116)` | 22.22815 | 150.24 | `.49 / −27°` | `5.37 × 5.42` | Replace `V11_TREE_02456` |
| R3 | Birch | `(-61,122)` | 15.83949 | 146.08 | `.40 / 72°` | `4.39 × 4.43` | Complement R1 and R2 |
| L1 | Beech | `(-106.59949,26.90979)` | 18.90422 | 76.77 | `.33 / −22°` | `5.33 × 6.04` | Replace `V11_TREE_01307` |
| L2 | Birch | `(-103.25,16.75)` | 19.52643 | 74.91 | `.43 / 51°` | `4.71 × 4.76` | Complement L1 |
| D1 | Beech | `(-122.10011,174.11145)` | 27.83711 | 150.57 | `.45 / 61°` | `7.26 × 8.24` | Replace `V11_TREE_03274` |
| D2 | Birch | `(-111,178)` | 31.25922 | 151.20 | `.42 / −43°` | `4.61 × 4.65` | Complement D1 |
| O1 | Birch | `(-33,93)` | 10.57744 | 121.35 | `.50 / 18°` | `5.48 × 5.53` | Open-slope specimen |

For replacements use the exact stored float32 XY from the registry. Check source cloud and index before filtering. In table order the four source rows are `V11_FOREST_-001_+002:14`, `V11_FOREST_-002_+002:6`, `V11_FOREST_-002_+000:2`, and `V11_FOREST_-002_+002:8`. Retain original meshes with fake users and bind owned filtered copies on the three touched clouds. Verify 6,196 surviving V11 points and eight new broadleaves. This preserves the entire young conifer cohort.

Clearances below are conservative lower bounds against the scaled and yawed source envelopes and measured V16 geometry. For XY obstacles use the envelope’s circumscribed disk. Trail clearance is to the centerline expanded by `1.05 m`, its maximum half-width. The protected valley strip is ±42 m from `(7.2,5)` along `(-.82284904,.56826003)`. Glazing gaps are between projected boxes in the main frame.

| ID | Cottage, m | Fence / garden, m | Apple, m | Trail, m | Valley strip, m | Glazing UV gap |
|---|---:|---:|---:|---:|---:|---:|
| R1 | 132.07 | 119.47 / 119.56 | 137.60 | 73.75 | 19.29 | .336 |
| R2 | 144.76 | 132.04 / 132.14 | 150.22 | 84.60 | 25.64 | .357 |
| R3 | 124.66 | 111.63 / 111.73 | 129.88 | 72.94 | 12.36 | .288 |
| L1 | 103.21 | 87.39 / 87.48 | 99.99 | 104.25 | .43 | .288 |
| L2 | 99.49 | 84.27 / 84.35 | 95.45 | 102.70 | 7.70 | .334 |
| D1 | 198.97 | 184.43 / 184.53 | 202.87 | 146.70 | 17.93 | .300 |
| D2 | 198.25 | 184.20 / 184.30 | 202.64 | 141.24 | 29.86 | .352 |
| O1 | 85.76 | 74.44 / 74.52 | 92.01 | 34.24 | 3.61 | .270 |

The eight envelopes all remain at least 43.99 m west of the east-facing glazing plane and have a positive projected gap from the cottage, fence, and orchard. The smallest crown gap between new trees is 1.00 m, and between a new tree and a retained V11 envelope 1.87 m. Terrain rays toward the sun are open at the surveyed crown witnesses. `V11_TREE_03495` overlaps the projected middle of R1 and R2 under the conservative cylindrical test. Left-offset crown rays are open and R3 is fully clear at the sampled offsets. Keep that spruce and judge the resulting silhouettes in the pilot.

Seat the upright trees on actual terrain triangles. For each basal bark footprint compute the minimum of `ground_z(x,y) − scaled_local_z` over the clipped support triangles. Set origin Z to the smaller of the table’s evaluated center height and that minimum minus `.012 m`. Test the full transformed basal ring after float32 storage. Stop the placement if seating needs more than `.25 m` downward shift or any basal bark exceeds `.42 m` burial. Recheck both LOD envelopes, tree-to-tree gaps, and projection before saving.

## 5. Shared trail field, shader, and support

Use the existing `V07_TRAIL` top and wall and the front faces of both V11 terrain carriers. Copy the meshes and material graphs that receive V17 attributes or shaders. Preserve all coordinates, topology, UVs, normals, and indices. Compute the new fields once per world XY and write the same float32 values to corresponding vertices of both surfaces. Audit the stored values at all matched lip vertices.

Let `S(a,b,x)` be cubic smoothstep. On a triangle, evaluate its barycentric `s`, `lateral`, `h`, and `p`, where `p` is the signed XY distance to the actual traced gravel lip, negative on the gravel. Store `p=0` at each lip vertex. Use `C=.480 m` for the protected half-core. Bake per-side `E` and `W` from these station functions before interpolation.

```text
I− = .101 + .026 sin(τs/3.70+.59) + .013 sin(τs/1.21+1.30)
          + .009 sin(τs/7.46+.60)
I+ = .072 + .019 sin(τs/4.60+1.90) + .009 sin(τs/1.62+.37)
          + .008 sin(τs/8.60+2.71)
Eσ = max(.500, h−Iσ)
W− = .59 + .065 sin(τs/6.30+.80) + .025 sin(τs/2.12+.50)
W+ = .53 + .048 sin(τs/5.40+1.30) + .023 sin(τs/1.89+2.40)

d = abs(lateral)−Eσ
F = S(−.020,.045,d)
G = max(S(.015,max(.035,h−Eσ),d), S(−.025,0,p))
K = A(s) × S(.480,.500,abs(lateral)) × (1−S(Wσ−.08,Wσ,p))
Afull = S(5,7.5,s) × (1−S(42,44,s))
Apilot = S(21,23,s) × (1−S(34,36,s))
```

Choose `σ` from signed lateral after interpolation. The shader blends `gravel → fines` by `F`, then this mix into the same B terrain substrate by `G`. Blend that result over the original slot by `K`. This gives exactly the original core for `|lateral|≤.480 m` and full shared substrate at `p=0` on both carriers in the unfaded interval. Use the original B gravel PBR in the gravel branch. For the fines, use the same gravel diffuse at `.30 m` repetition mixed 56% toward linear `(.086,.069,.040)`, roughness `.94`, and bump distance `.004 m`. Extract the B ecological color, roughness, and normal inputs upstream of its shoulder overlay. Feed both carriers the same ground height, ecology, exterior weight, and terrain normal sampled from the original terrain triangles. This also keeps the lip wall on the same texture basis. The scope of this shader is the front band defined by `K`.

Place edge details from the **same stored field**, sampled on the actual top and terrain triangles. Jitter `.13 m` cells and use priority hashes, with these acceptance densities per m² weighted by `A(s)`:

- Terrain tufts and low leaves use `4+6G` where `.012 ≤ p ≤ Wσ−.035` and `d≥.020`. Use whole 4–11 cm forms from the shoulder masters, with stronger clustering on the meadow side.
- Gravel-edge blades use `3.2G` where `−.070 ≤ p ≤ −.008` and `d≥.025`. Use single 3–8 cm arching blades with a narrow basal footprint and yaw toward the verge. The blade can cross the lip above the surface.
- Pebbles use `4F(1−G)` within `−.09 ≤ p ≤ .11`, with `d≥.010`. Use copies of `V07_STONES_MASTER_0` through `_2` scaled to 1.8–4.0 cm long. Cap new terrain tufts, gravel blades, and pebbles at 420, 100, and 140 respectively. Keep the existing V16 shoulder points and reject new roots within `.08 m` of them.

For every new placement, clip its complete basal footprint against the actual carrier triangles. Require complete coverage on one carrier. For a gravel root require the entire footprint to stay at least 6 mm inside the top perimeter. Solve origin height as `min(ground_z−transformed_base_z)−.002 m` over the clipped footprint extrema. Recheck stored geometry for exposure `≤1 mm` and burial `≤18 mm`. Try scale factors `1, .85, .70` in order, then reject the placement. Test the full projected body against `|lateral|≤.480 m`, the hard obstacle masks, and the actual lip. Any overhanging blade must clear the gravel top by at least 1 mm where it crosses the lip. No V17 root or body enters the protected core. Give the edge population its own `IsViewport` True arm with every fourth point represented by complete components of at most 24 triangles.

## 6. Execution, render pairs, and acceptance

Implement `apply_v17(scene, config, project_root, *, stage)` in `source/nature_detail_v17.py`, with `stage` exactly `pilot` or `full`. Store seed, baseline hash, asset hashes, coordinates, field constants, and render presets in `source/nature_detail_v17.json`. The module imports without scene effects. Compute and validate the owned changes before saving. Record the baseline, recipe, config, normalized asset, and semantic hashes on the candidate. A repeated call verifies the actual result against the recorded semantic hash and returns it. Reject ownership or hash mismatches. A full build starts from fresh B.

1. **Stage 0 — normalize assets.** Verify the raw content against the pinned hashes below. For each tevy GLB check header, chunk lengths, image buffer bounds, and KTX2 magic. Retain the BIN chunk and meshopt declarations, extract each image to a local KTX2 sidecar, set image `uri`, and import through the tested stock `.gltf` path. Append only the two dandelion LOD2 objects and their dependencies. Pack the normalized library with the selected color, alpha, and normal images. Cold-reopen and verify dimensions, alpha range, finite nonconstant pixels, material roles, and decoded pixel hashes. Record author or publisher, URL, license, version, raw and normalized hashes, and modifications in `assets/ASSET_MANIFEST.md`. Stage 0 binds any reused local source and preserves the existing asset credits.

   | Pinned input | SHA-256 |
   |---|---|
   | Wildflower Patch v1 LOD0 | `8fd2262da4a62e4d16c97f4bfd24c0aff1498f08fa34c3245cee13a40aefc096` |
   | European Beech v1 LOD1 / LOD2 | `20be1b2801f72cebeb3d5b91a5b275e7645de54d160771e881ea9061b8e726c3` / `f52e44fc1de7bcd31c1eb6a2cdcd509e5fae18d7ab2162f89d1bdbe17eac5f00` |
   | Silver Birch v1 LOD1 / LOD2 | `ba9ccd03ba2d0ad21f82eb6fd9934712822946b6c869069a17f3d5580b7ddedc` / `a6ae6b4384feeb955fdd5e23d21fa5d1feb821ddda1dd1d95892b82a1728bb92` |
   | Dandelion 01 1K Blend | `9751bb96fe8a10f19cd04c736e1417825f71aa7fbf1cb632e8c5ebc08f77a3d4` |

2. **Stage 1 — pilot.** Build the specified pilot from B. Render the main frame and the fixed low view. Compare both against the matched B views before expansion. The low view must resolve the two white anchors, the yellow anchor, and curved seed stems. The `s=30` cross-section must show a continuous gravel core, an irregular fine edge, and supported leaves or blades crossing the lip. The main frame must retain the B slope palette and show at least R3’s distinct crown. Judge the two overlapping R crowns with the complete group in context. Check geometry and stored masks before evaluating pixels.
3. **Stage 2 — full candidate.** Build from pristine B using the full masks and all eight broadleaves. Save `checkpoints/candidate_exterior_v17.blend` with the original main camera and original render profile active. Compare a second application, a fresh-input replay, and a separate offline cold reopen by semantic hashes. Run the six existing branch checks and the new branch checks, exhaustive changed-footprint support checks, trail continuity and core masking, four exact replacement checks, and the clearance table. Compare protected camera, cottage, interior, orchard, fence, paving, sky, lights, existing packed image bytes, and all point attributes outside the authorized replacements. Only the new asset inputs and normalized library are required during building. The cold candidate must resolve its images locally. If a reproducible visual defect remains, use at most one recorded correction from B. Limit it to the smallest implicated parameter in the pilot treatment, and repeat the affected pair and all final gates. A further failure returns `PARTIAL` for disposition.

**Render suite.** Serialize on CachyOS under isolated Blender 5.3.0 with the currently verified owner GUI identity and at least 12 GiB available at each launch. Use CPU with four fixed threads, 96 samples, threshold `.01`, adaptive minimum `0`, seed and frame `0`, CPU OIDN Accurate/High, AgX None, exposure `0`, and gamma `1`. Log wall time and peak RSS for each job. The measured B frame took 118.83 s at 4.38 GiB peak RSS. Include observed candidate costs for each photo size. Use:

- `CAM_V11_VALLEY_REVIEW` at `960 × 540`, with original camera matrix, 35 mm horizontal fit, zero shifts, and `.1–2400 m` clips. Reuse the verified native `B_v16_960.png` as B.
- Exact main-camera 1:1 border from a `5760 × 3240` render, using top-left pixel rectangle `[504,2000,5184,3240)` for both scenes. At the 22 m A-zone depth limit, an untilted 5.1 cm head spans roughly 13 px and a 3.1 cm head roughly 8 px before foreshortening. Use the same native border and PNG settings in both jobs.
- Fixed `CAM_V17_LOW_DETAIL` at `3200 × 1800` for B, pilot, and full V17. Inspect the native pixels at the four botanical anchors, the `s=30` transect, and R3. Compute edge profiles on both sides at `s=16,24,30,36,42`, using absolute 10–90% transition widths and recording polarity separately. Visual review checks differentiated stems and heads, an irregular two-sided gravel transition, and a connected clear core through the gate and to the north boundary.

**Exact write allowlist for the future grant.** All paths below are relative to `work/v17/nature_detail_01/`. Braces enumerate allowed names. `runtime/` contains disposable job directories only. Reuse the B main PNG from its immutable original location.

```text
source/nature_detail_v17.{py,json}
assets/ASSET_MANIFEST.md
assets/v17_masters.blend
assets/raw/{wildflower-patch-v1-lod0,european-beech-v1-lod1,european-beech-v1-lod2,silver-birch-v1-lod1,silver-birch-v1-lod2}.glb
assets/raw/dandelion/dandelion_01_1k.blend
assets/raw/dandelion/textures/dandelion_01_{alpha_1k.png,nor_gl_1k.exr,diff_1k.jpg,mask_1k.png,rough_1k.exr}
checkpoints/{pilot_v17,candidate_exterior_v17}.blend
renders/{pilot_valley_960,pilot_low,B_foreground,V17_foreground,B_low,V17_low,V17_valley_960}.png
proofs/{assets,preflight,pilot,full,idempotence,replay,cold,support,clearance,render_metrics,visual_review}.json
proofs/artifacts.sha256
proofs/{assets,pilot,full,replay,cold,pilot_valley_960,pilot_low,B_foreground,V17_foreground,B_low,V17_low,V17_valley_960}.log
runtime/{assets,pilot,full,replay,cold,pilot_valley_960,pilot_low,B_foreground,V17_foreground,B_low,V17_low,V17_valley_960}/**
before_c01/checkpoints/{pilot_v17,candidate_exterior_v17}.blend
before_c01/renders/{pilot_valley_960,pilot_low,V17_foreground,V17_low,V17_valley_960}.png
before_c01/proofs/{config,render_metrics,visual_review}.json
```

Use `before_c01/` only for evidence that exists when the single correction is made. Review the final candidate and render pairs with Michal for visual acceptance. This terminal report expires the current planning authority. An accepted plan requires the separate explicit implementation grant before any implementation writes.

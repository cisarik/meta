# V18 standalone Blender scenes, Kysuce forest, and trail continuation

Logical whole identity: `kysucka-moderna-chata-split-and-forest-realism-v18`  
Worker session ordinal: `01`  
Worker exchange ordinal: `01`  
Status: `PASS`  
Phase-qualified result: `not-applicable`  
Start commit: `78534bd46020bb2bfc97eef69b05e583cba5a5e5`  
End commit: `78534bd46020bb2bfc97eef69b05e583cba5a5e5`  
Changed files: `none`  
Git result: `no writes`  
Logical-whole closure: `not-closed`  
Report justification: `new-evidence`

Release the interior and exterior as independently portable copies of the complete V17 scene. Deliver the measured basement handoff with the interior at Stage 1. Use the right-valley pilot to select the forest treatment before expanding it. Michal confirmed that Stage 3 includes building the missing trail continuation to the actual north boundary of V17.

## 1. Verified source and dependencies

| Readback | Complete V17, the split source | V17 exterior checkpoint |
|---|---|---|
| Absolute path | `/home/agile/Projects/kysucka_moderna_chata/work/v17/complete_3d/kysucka_chata_v17_komplet_3d.blend` | `/home/agile/Projects/kysucka_moderna_chata/work/v17/nature_detail_01/checkpoints/candidate_exterior_v17.blend` |
| SHA-256 | `8a733770f3f4b96922dce76d662e81b281d2047affee5adceac849fb8948113e` | `f2e0942b63c25ec813b64ad483ea535d4a44b5e0c3a9f6dcfc0eebf7cb3ec4be` |
| File size | 716,141,423 B, approximately 683 MiB | 481,097,097 B |
| Scene inventory | 5,371 scene objects, 36 cameras, 289 packed file images, zero libraries | 5,089 scene objects, 21 cameras, 110 packed file images, zero libraries |
| Interior | `55_INTERIOR_V10` has 151 objects, including 124 mesh objects using 114 distinct meshes, 21 lights and six cameras. The 86 entries in `v10_hide_registry` are hidden for render and viewport. Twelve original partition meshes still render. | All 73 `50_INTERIOR_PROXY` objects are render-enabled. `55_INTERIOR_V10` and the hide registry are absent. |
| Forest | 6,196 V11 conifers, eight V17 broadleaves, and 3,157 `V10_HILL_FORESTS` trees in 122 clouds. Total 9,361. | 6,196 V11 conifers and eight V17 broadleaves. Total 6,204. |
| Saved review | Frame 1, `Záber 01`, 1920 × 1080. Eight camera markers and the three named V17 workspaces. | Frame 0, `CAM_V11_VALLEY_REVIEW`, 960 × 540. Zero markers. |
| Working branches | `V17 PREVIEW Ihličnany` and `V17 PREVIEW Listnáče` feed viewport switches. Terrain, trail and visible building meshes also have viewport-only material modifiers. | `V12_WORK_FOREST` and the original `V17_*_WORK` collections feed the corresponding switches. |

The complete scene descends from `kysucka_chata_mcp_v10.blend` (`8628822a730d6a1f574126b81fb6a9ee7d109c1f8a254f1331215461526cab70`). The assembly appended the V10 study and placed **3,006 conifers and 151 broadleaves** with seed `1372010`. Those placements account for the additional large crowns and scattered slope trees in `render_valley.png`. The 248-image build check counts inherited images. The saved complete file contains those 248 plus 41 preview images. [V10 assembly receipt](/home/agile/Projects/kysucka_moderna_chata/work/v10/complete_scene/assembly.json) · [V17 build receipt](/home/agile/Projects/kysucka_moderna_chata/work/v17/complete_3d/build.json)

For the three V11 terrain meshes and `V07_TRAIL`, vertex coordinates, topology, attributes, material bindings and render transforms agree between the two scenes. The four V17 clouds agree at **297,566 ground-cover, 175 botanical, eight broadleaf and 243 trail-edge points**. All 39 common node-group fingerprints, 133 common material graph fingerprints and 110 original packed image payloads agree. The complete scene swaps the working arm of the conifer and broadleaf switches. The original render collections remain bound. The two wide PNGs use different sample counts, so the Stage 1 visual gate uses fresh matched renders from the complete scene. [V17 preparation](/home/agile/Projects/kysucka_moderna_chata/work/v17/complete_3d/prepare.py) · [V17 exterior render](/home/agile/Projects/kysucka_moderna_chata/work/v17/nature_detail_01/renders/V17_valley_960.png) · [Complete render](/home/agile/Projects/kysucka_moderna_chata/work/v17/complete_3d/render_valley.png)

The original envelope, roof, glazing and entry collection members have matching mesh data and transforms after evaluation. The complete scene initially returned unevaluated world matrices for 22 hidden predecessors. Their `matrix_basis` and world matrices after temporary evaluation matched the exterior checkpoint. The visible differences at the south corner and gable follow the V10 wall, cladding and glazing replacements.

### Collection dependency map

Counts are total objects, render-enabled objects and reachable packed images in the complete scene. Image counts overlap across rows. Dependencies include hidden collections and both arms of Geometry Nodes. The split audit must also walk incoming ID references before removing anything.

| Root | Total / render / images | Dependencies and split disposition |
|---|---:|---|
| `00_REFERENCE` | 1 / 0 / 1 | Reference image empty. Retain its packed image and camera background bindings. |
| `00 \| Kamery V17` | 8 / 8 / 1 | Eight named camera clones, timeline markers and C1 background. Keep together. |
| `10_ENVELOPE` | 107 / 86 / 4 | Slab, walls, cladding, gables, timber maps and working material groups. Keep V10 replacement links and hidden predecessors. Walls and cladding cast shadows. |
| `20_ROOF` | 31 / 31 / 4 | Roof, soffits, chimney, material slots and bevel/solidify/working modifiers. Retain shadow and reflection geometry. |
| `30_GLAZING` | 34 / 32 / 0 | Pane and mullion meshes, transmission shaders and working bindings. Two original panes are hidden and replaced from `55_INTERIOR_V10`. |
| `40_ENTRY_DETAILS` | 93 / 93 / 4 | Entry openings, door, exterior fixtures, joinery and paving, shared materials, emissive surfaces and working material groups. |
| `50_INTERIOR_PROXY` | 73 / 12 / 0 | Twelve active `PARTITION_proposed` meshes through `.011`. The other 61 are registry predecessors. |
| `55_INTERIOR_V10` | 151 / 151 / 178 | Structure, furniture, lights, cameras and replacements. Includes native Auto Smooth groups, V17 working material groups and 146 reachable materials. Retain full interior transport through glass, reflections and shadows. |
| `60_LIGHTS` | 6 / 2 / 0 | Two active `SCONCE_wash` lights. Preserve color, energy, ray flags and hidden predecessors. |
| `70_SITE` | 47 / 46 / 6 | Near-house site and paving details, bed/fence materials and timber maps. |
| `80_CAMERAS` | 1 / 1 / 1 | Locked `CAM_A_REFERENCE` and its packed background. |
| `90_VEGETATION_PROXY` | 263 / 0 / 0 | Mesh-only hidden predecessors, five materials, zero outgoing object or collection dependencies. The sole proposed pruning trial. |
| `95_LANDSCAPE_V04` | 1,717 / 200 / 72 | Orchard, young trees, planting and edge grass, plus hidden hill and forest predecessors. Linked meshes and shared material/image users cross generations. |
| `96_SITE_V05` | 1,793 / 417 / 63 | Garden perimeter, fence, gate, paving and cameras. Historical lawn and meadow clouds refer to the three `V05_MASTER_*` vegetation collections. |
| `97_VEGETATION_V06` | 179 / 5 / 60 | Five active cameras. Retained terrain and vegetation use `V06_MASTER_FOREST`, `V06_MASTER_LAWN` and `V06_MASTER_MEADOW`. |
| `98_VEGETATION_V08` | 228 / 0 / 57 | Historical forest, lawn and meadow render/view master pairs. Preserve the `IsViewport` groups and reused tree/ground sources. |
| `99_EXTERIOR_V11` | 203 / 150 / 65 | All three terrain carriers, 6,196 conifers and core vegetation. Conifers use `V11_MASTER_FOREST_RENDER` and `V17 PREVIEW Ihličnany`. Core uses `V09_MASTER_LAWN_RENDER`, `V09_MASTER_MEADOW_RENDER` and the V12 working pairs. The retained exterior-meadow group also reaches `V11_MASTER_MEADOW_RENDER` and `V12_WORK_EXTERIOR_MEADOW`. |
| `99_NATURE_STUDY_V09` | 173 / 0 / 4 | Historical study grass and light, with V08 working and V09 render master dependencies. |
| `V07_ROOT` | 78 / 8 / 64 | Four cameras, `V07_GATE_TRANSITION`, gravel, litter and stones. Live detail groups use `V07_MASTER_STONES` and `V07_MASTER_LITTER`. Retained forest and shoulder groups reach `V07_MASTER_FOREST` and `V06_MASTER_MEADOW`. |
| `V10_HILL_FORESTS` | 122 / 122 / 63 | Shared V11 conifer and V17 beech/birch render masters and both V17 preview collections. |
| `V13_COHERENT_EXTERIOR_MEADOW` | 52 / 52 / 4 | `V16_MEADOW_IsViewport` switches between `V16_MASTER_MEADOW_RENDER` and `V13_MASTER_MEADOW_WORK`. |
| `V16_SHOULDERS` | 1 / 1 / 0 | `V16_SHOULDER_IsViewport` and its render/work master pair. |
| `V17_NATURE_DETAIL` | 5 / 5 / 20 | Detail camera and four clouds. Keep render/work pairs for ground cover, botanicals and trail edge, the broadleaf render master, and the V17 broadleaf preview master. |

The scene root also owns `CAM_V09_ENVIRONMENT_STUDY`, `CAM_V11_VALLEY_REVIEW`, `CAM_LANDSCAPE_FOREST_REVIEW`, the inactive V14 sun and active `V15_SUN_REFERENCE_KEY`. The active sun has energy 2.8, angular diameter 2° and color `[1, .88, .69]`. Preserve it with `V16_WORLD_MEADOW_BALANCE` and both packed HDR images it references. Preserve camera bindings, parent and constraint targets, ray visibility, indirect transport, material and modifier socket references, text records and fake users.

### Camera readback

Positions and forward directions below are rounded for display. Record the full world matrices, DOF, fit, lens, sensor and clips in Stage 1. The 21 inherited cameras fingerprint identically between the two scenes. Sensor size is 36 × 24 mm throughout. Shifts are zero except C1 `shift_y=.105` and V07 overview `shift_y=−.215`.

| Camera | World position | Forward direction | Lens mm |
|---|---|---|---:|
| `CAM_A_REFERENCE` | 21.5, −10, 1.25 | −.7208, .6931, 0 | 35 |
| `CAM_V05_LAWN_DETAIL` | 11, −6, .24 | −.4032, .9071, −.1209 | 55 |
| `CAM_V05_MEADOW_DETAIL` | 23, −6, .65 | .6991, .6991, −.1503 | 50 |
| `CAM_V05_ORBIT_NE` | 42, 38, 24 | −.6954, −.6084, −.3824 | 35 |
| `CAM_V05_ORBIT_NW` | −40, 38, 24 | .7127, −.5939, −.3733 | 35 |
| `CAM_V05_ORBIT_SE` | 42, −34, 24 | −.6807, .6297, −.3744 | 35 |
| `CAM_V05_ORBIT_SW` | −40, −34, 24 | .6984, .6152, −.3658 | 35 |
| `CAM_V05_OVERVIEW` | 52, −60, 58 | −.5042, .6353, −.5849 | 35 |
| `CAM_V05_VALLEY_INSIDE` | 12.2, 3.2, 2 | .9999, 0, −.0123 | 30 |
| `CAM_V06_EXTERIOR` | 14.65, 3.2, 1.9698 | .9999, 0, −.0123 | 30 |
| `CAM_V06_FOREST` | −18, 18, 3.8995 | −.6686, .5730, .4740 | 35 |
| `CAM_V06_LAWN` | −10, 7, .185 | −.4838, .8708, −.0871 | 55 |
| `CAM_V06_MEADOW` | −20, 8, 2.8036 | −.6595, .6595, .3608 | 50 |
| `CAM_V06_NW` | −36, 34, 54 | .5316, −.4337, −.7275 | 35 |
| `CAM_V09_ENVIRONMENT_STUDY` | 62, −27, 12 | −.8154, .5633, −.1334 | 35 |
| `CAM_V11_VALLEY_REVIEW` | 62, −27, 12 | −.8154, .5633, −.1334 | 35 |
| `CAM_V17_LOW_DETAIL` | 48, −21.75, 8.0706 | −.7064, .6934, −.1422 | 28 |
| `V07_CAM_AGE` | 10, 24, 4.5457 | −.6166, .7871, .0170 | 45 |
| `V07_CAM_GATE` | 11, −14, 1.9824 | −.4147, .8758, −.2471 | 45 |
| `V07_CAM_OVERVIEW` | 160, −180, 175 | −.3465, .7591, −.5511 | 50 |
| `V07_CAM_WALKING` | 2.6436, 36.3735, 6.081 | −.0752, .9961, .0464 | 35 |
| `CAM_LANDSCAPE_FOREST_REVIEW` | 108.1612, −232.4339, 184 | −.5962, .7318, −.3301 | 31 |
| `CAM_V10_ENTRY` | 8.72, 3.925, 1.62 | .9959, .0781, −.0458 | 16 |
| `CAM_V10_GALLERY` | 8.7, 2.6, 4.85 | .7575, .2956, −.5820 | 16 |
| `CAM_V10_HERO` | 14.05, 4.5, 1.5 | −.6802, −.7300, .0664 | 14 |
| `CAM_V10_PANO` | 13, 4.15, 1.62 | 1, 0, 0 | PANO |
| `CAM_V10_PLAN` | 11.55, 4.2, 14 | 0, 0, −1 | ORTHO 9.2 m |
| `CAM_V10_SOFA` | 10.45, 1.05, 1.58 | .7360, .6675, −.1130 | 18 |

C1 clips are `.1–500 m`. V05/V06 and V07 cameras clip at `.1–1000 m`. V09, V11, V17 low and the V10 hill review clip at `.1–600`, `.1–2400`, `.03–450` and `.15–2400 m` respectively. V10 interior clips are `.05–500 m`. V09, V11, V17 low and V07 use horizontal fit. The other named source cameras use automatic fit.

| Frame | V17 marker camera | Source or exact aim |
|---:|---|---|
| 1 | `Záber 01 \| Chata a údolie` | `CAM_V11_VALLEY_REVIEW` |
| 31 | `Záber 02 \| Lúka od chodníka` | `CAM_V17_LOW_DETAIL` |
| 61 | `Záber 03 \| Priečelie a terasa` | `CAM_A_REFERENCE` |
| 91 | `Záber 04 \| Severná strana` | `[−.7,27.5,5.4]` toward `[7.2,4.4,2.55]`, 41 mm |
| 121 | `Záber 05 \| Západná strana` | `[−19,1.3,5.1]` toward `[7.1,4.2,2.8]`, 37 mm |
| 151 | `Záber 06 \| Kopce a lesy` | `[136,−205,154]` toward `[−134,84,10]`, 30 mm |
| 181 | `Záber 07 \| Obývačka a krb` | `CAM_V10_HERO` |
| 211 | `Záber 08 \| Jedáleň a galéria` | `CAM_V10_GALLERY` |

The three new V17 poses use horizontal fit and `.045–2300 m` clipping. The five clones inherit their source optics.

## 2. Stage 0 asset locks and comparison

Outbound HTTPS and stock Blender 5.3.0 import both worked. The three pinned CC0 GLBs imported through `.gltf` sidecars with `import_ktx_texture=True`, `import_pack_images=True` and `merge_vertices=False`. The packed fixture cold-opened with the network, project directory and raw asset directory masked. All **20 tested images** retained their packed byte hashes, decoded pixel ranges and color spaces. [tevy Norway Spruce v1](https://tevy.dev/models/norway-spruce) · [Forest Ground 01](https://polyhaven.com/a/forrest_ground_01) · [Leaves Forest Ground](https://polyhaven.com/a/leaves_forest_ground)

| tevy LOD | Triangles | Blender X × Y × Z, m | SHA-256 | Raw file |
|---|---:|---|---|---|
| 0 | 41,432 | 9.9908 × 9.0768 × 20.5949 | `63d364cdec9bbcef366c25ed0397d17f3cff57d3e62cf8aff2ce06fc987fbbf7` | [lod0.glb](https://tevy.dev/models/norway-spruce/v1/lod0.glb) |
| 1 | 14,282 | 10.3013 × 9.8986 × 20.5990 | `1a99b9b1d8c5307337c204e4db26cecaf6493e4c2e11f51f6254d822dd1e6d07` | [lod1.glb](https://tevy.dev/models/norway-spruce/v1/lod1.glb) |
| 2 | 2,520 | 10.0028 × 9.9660 × 20.2723 | `2dbb026f880470e94924e9eb99acba144a7486ecc27908487235a1558b91285f` | [lod2.glb](https://tevy.dev/models/norway-spruce/v1/lod2.glb) |

| Poly Haven 2K map | SHA-256 | Raw file |
|---|---|---|
| Forest diffuse | `e4d557ff61a0b42712a58e8a2e91c6010738977d4e172b7af47abd7d406ae735` | [JPG](https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/forrest_ground_01/forrest_ground_01_diff_2k.jpg) |
| Forest OpenGL normal | `aa23fa930c6303490f842f7c016c19d838263e8e4538d42508a9332e3fd76b69` | [JPG](https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/forrest_ground_01/forrest_ground_01_nor_gl_2k.jpg) |
| Forest roughness | `e09258c7f055156a7607f1b21dccf38c7efd847e7d030271d5ffcc4a722df37d` | [JPG](https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/forrest_ground_01/forrest_ground_01_rough_2k.jpg) |
| Forest height | `1d8cb8bbe9039ee2cd22068d457617a1748170405aacd49d33fcf637e08bb12b` | [PNG](https://dl.polyhaven.org/file/ph-assets/Textures/png/2k/forrest_ground_01/forrest_ground_01_disp_2k.png) |
| Leaves diffuse | `bda0ffc30570af7c067a3d6922cb1c7f31ada4fcece24b8f2cc4c5dde742e22c` | [JPG](https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/leaves_forest_ground/leaves_forest_ground_diff_2k.jpg) |
| Leaves OpenGL normal | `2713002b4a75b8b47b983c75d3f388d79f0775f305ca14884eae6a277b8f48bd` | [JPG](https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/leaves_forest_ground/leaves_forest_ground_nor_gl_2k.jpg) |
| Leaves roughness | `a08b1aaba9ca87924abfbe65a1c6be03c6cc7fcfcf140dc784ccf35205c307f0` | [JPG](https://dl.polyhaven.org/file/ph-assets/Textures/jpg/2k/leaves_forest_ground/leaves_forest_ground_rough_2k.jpg) |
| Leaves height | `38294b4ce4c1f6c99611876cb972f7973ecf65ae5be0ed406a11b705699411bd` | [PNG](https://dl.polyhaven.org/file/ph-assets/Textures/png/2k/leaves_forest_ground/leaves_forest_ground_disp_2k.png) |

- **Normalize.** Verify each raw SHA-256. Preserve `EXT_meshopt_compression` and quantization. Copy the GLB binary chunk to `source.bin`, extract each KTX2 image buffer view to `image-NN.ktx2`, and replace its `bufferView` with a relative URI using the V17 procedure. Record derived hashes, triangle counts, world-space dimensions, alpha and packed image hashes. Keep bark, branches and needle-card roles through import. Bake transforms into local masters and normalize the planting collar. Use the trunk ring around original local `Z=0` for tevy. The lowest root tip alone left the broader flare visibly raised in the planning fixture. [V17 sidecar procedure](/home/agile/Projects/kysucka_moderna_chata/work/v17/nature_detail_01/source/nature_detail_v17.py:160)
- **Repeat a controlled A/B.** Match the adult height to `ABIES_LOD0` at 9.5862 m, then compare the same silhouette, backlit needle detail, bark/root close-up and planted base with the frozen world and sun. The local control gave finer backlit needles and a narrow, smooth flare. tevy gave stronger bark texture, distinct drooping branch tiers and a wider root flare. Its lowest sprays covered the trunk in the full-tree crop, and broad alpha cards were conspicuous nearby. The imported cutoff was `.5`, with 81.6%, 75.2% and 66.7% of needle-color texels below cutoff in LODs 0–2. Use local `ABIES_LOD0` for the focal adult. Admit tevy LOD1 to the mid-distance mix when the matched crop shows useful crown variation and clean card edges. Use the local V11 Norway spruce render master for that role if the crop fails. Keep LOD2 for distant substitution only after a silhouette check.
- **Set soil and understory.** Start Forest Ground at 2.00 m per repeat and Leaves Forest Ground at 1.26 m. Use sRGB diffuse, Non-Color normal/roughness/height, tangent OpenGL normal and height as bump. Both packed 2048² sets rendered. The leaf surface reads warmer and more distinct, so use it in patches beneath broadleaf crowns. Keep true 3D twigs, moss and root flare near the eye-level witness. [Forest Ground scale and credits](https://polyhaven.com/a/forrest_ground_01) · [Leaves Forest Ground scale and credits](https://polyhaven.com/a/leaves_forest_ground)
- **Reuse the local masters.** `ABIES_LOD0/LOD1/YOUNG` have 84,240/21,000/84,240 triangles and approximately 9.59/9.61/9.59 m source heights. `MARIANA_LOD0/LOD1` have 69,701/18,000 triangles and approximately 11.22/11.23 m heights. Use `shrub_01` at its `.294–.372 m` source heights and `grass_medium_01` for sparse feathering at `.145–.323 m`. Preserve the existing periwinkle garden use. The local V17 library supplies beech and birch LOD1/2, the 3,860-triangle wildflower patch and two 619/629-triangle dandelions. Preserve their existing attribution. Document *Picea mariana* as the historical North American visual proxy and prioritize *Picea abies* and grouped broadleaves in readable margins. [Local asset manifest](/home/agile/Projects/kysucka_moderna_chata/assets/ASSET_MANIFEST.md) · [CHKO Kysuce](https://chkokysuce.sopsr.sk/priroda/opis-uzemia/) · [US Forest Service black spruce range](https://research.fs.usda.gov/silvics/black-spruce)

## 3. Stage 1 split and basement handoff

### Products and ownership

- Independently open the frozen complete V17 for each output. Stage under `work/v18/stage1/`. Promote to `blender/kysucka_chata_exterier.blend` and `blender/kysucka_chata_interier.blend` after both offline gates pass. Exterior opens at `Záber 01`, frame 1. Interior opens at `Záber 07`, frame 181. Both keep the V17 workspaces and all marker cameras.
- Exterior owns the landscape, trail, garden and exterior visualization. Keep the complete V10 scene contribution at Stage 1, including lights, emission, partitions, furnishings and glazing interactions. Interior owns future disposition. Keep full `55_INTERIOR_V10`, its supporting partitions, envelope, near terrain, garden, orchard and the entire current horizon and forest for window views and indirect light.
- The first build of each copy retains all active objects and both working branches. For pruning, test only the 263 hidden members of `90_VEGETATION_PROXY` as a batch. Require zero incoming references from retained objects, node trees, modifiers, drivers or collections, followed by pixel-identical matched witnesses. Remove only that root and its proven unshared zero-user IDs on success. If either check fails, ship the full copy. Keep the other collections in the dependency table. This sets a reproducible fidelity-first split with a measurable pruning boundary.
- Write `model/shared_envelope_v18.json`. The exact 289-member selection is all meshes in `10_ENVELOPE`, `20_ROOF`, `30_GLAZING` and `40_ENTRY_DETAILS`, plus the 24 `55_INTERIOR_V10` meshes whose `v10_piece` is `REPLACEMENT`, `FRONT_GLAZING` or `GABLE_GLASS`. Include `BASE_slab`, the exterior chimney, original openings and panes, `V10_REPL_*`, `V10_FRONT_GLAZING_*` and `V10_GLASS_*`. Expand membership into sorted, explicit object names. For each row store collection, mesh ID, parent, render flags, material slots, evaluated world matrix, local vertex SHA-256, topology SHA-256 and world-matrix SHA-256. Use little-endian float32 for vertex and matrix hashes and row-major ordering for the 4 × 4 matrix. Resolve hidden transforms in an isolated audit pass. Record source hash, metres, `+X` from wood bay to glazed gable, `+Y` toward the north/rear facade, `+Z` up, slab underside `+.200`, slab top `+.450`, and actual interior finish `+.451`. Embed the manifest digest in both products.
- The measured aggregate SHA-256 of compact UTF-8 JSON rows `[name, vertex_sha256, matrix_sha256]` is `8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50`. `BASE_slab` has world translation `[7.2,4.2,.325]` and identity rotation/scale. Its vertex digest is `b363ad9a5dffae272a45c0652b7cb6ffe72e6b0ddded30e97e3fe56c3080c53c`. The chimney shaft center is `[11.3,3.2,7.225]`. Use the manifest as the basis for any later explicit transfer of shared geometry between products.

### Measured handoff

`BASE_slab` spans `X 0–14.40`, `Y 0–8.40`, `Z +.200–+.450 m`. The wood bay occupies `X 0–2.40`; the closed west wall occupies `X 2.40–2.70`. The side walls begin on the slab top. The grey band is the exposed slab edge. The north shadow has a measured **.255 m open space** below that edge. The under-slab envelope inventory found only `BASE_slab` at or below `+.200 m` within the footprint. Seven rays from `Záber 04` reached the mid-gap across `X 1.2–13.3` without hitting the slab or terrain. They project along the dark band. [North render](/home/agile/Projects/kysucka_moderna_chata/work/v17/complete_3d/render_north.png)

| Facade | Along-edge section | Perpendicular section | Measured terrain |
|---|---|---|---:|
| North | `Y=8.40`, `X=0–14.40` | Outward to `Y=11.40` | `−.055 m` |
| South | `Y=0`, `X=0–14.40` | Outward to `Y=−3.00` | `−.055 m` |
| West | `X=0`, `Y=0–8.40` | Outward to `X=−3.00` | `−.055 m` |
| East | `X=14.40`, `Y=0–8.40` | Outward to `X=17.40` | `−.055 m` |

Measured on the active top triangles at the facade and offsets `.05`, `.15`, `.50`, `1`, `2` and `3 m`, with along-edge sampling at 10 mm. Use sections at `X=1.2, 2.55, 7.2, 11.3 m` and `Y=2.10, 3.925, 6.30 m` to show the bay, wall, corridor, fireplace and less-exposed flanks. Record the slab bevel separately from the flat underside.

| Ground-floor feature | World-space evidence, metres |
|---|---|
| Corridor and east opening | Clear band `Y=3.35–4.50`, width `1.150`. Corridor `X=2.70–8.65`, opening through `X=8.65–8.80`. Finish `+.451`. Under gallery/platform underside at `+3.050`, headroom `2.599`. Under the first tread past `Y=4.40`, headroom `2.574` at `Y=4.425–4.50`. |
| Service and back rooms | Bath/WC `X=2.70–5.15`, technical `5.30–6.65`, entry `6.80–8.65`, each `Y=.30–3.20`. North rooms `X=2.70–5.65` and `5.80–8.65`, both `Y=4.65–8.10`. Retain the measured partitions and opening geometry as the visualization basis. |
| Stair and gallery | Lower flight `X=9.80–10.75`, `Y=6.02–7.10`. Landing `X=8.80–10.75`, `Y=7.10–8.10`, top `+1.32569`. Upper flight `X=8.80–9.75`, `Y=4.40–7.10`. Top platform `X=8.80–9.75`, `Y=3.35–4.40`, top `+3.250`. Rise `2.799 m` over 16 risers of `.17494`, with `.270` going and `.950` flight width. |
| Stair headroom | Sampled over three positions across each flight. Minimum `3.089` lower and `2.852` upper. The rear landing reaches `1.924` beneath a rafter near `[10.275,8.09]`. At `X=9.275`, under-flight clearance at `Y=5.0 / 5.25 / 5.5 / 6.0` is `2.224 / 2.049 / 1.874 / 1.699`. Map the rail and landing edge in the handoff. |
| Understairs and fireplace | Cabinet `X=8.82–9.71`, `Y=5.30–7.08`, `Z=.451–1.898`. Fireplace breast and hearth bound `X=10.65–12.60`, `Y=2.75–3.65`; breast rises to `+6.70`. Preserve both exclusion volumes for the later study. |
| West and north approach levels | Existing land `−.055` at the measured flanks, `.506 m` below interior finish. Record visibility from `Záber 04` and `Záber 05` for the future side-entry option. |

Create `56_BASEMENT_V18` in the interior and link its handoff name through a collection property to an embedded `V18 | Podklad pre pivnicu` text. Deliver Slovak-labeled dimensioned plan and X/Y sections together with machine-readable measurements. Mark the west service/corridor study area, the stair/cabinet and fireplace exclusions, the north shadow gap and the west/north approach levels. Stage 1 hands off the measured existing geometry before any basement design. [V10 design basis](/home/agile/meta/projects/kysucka_moderna_chata/00/10-interior-living-space/evidence/design_basis_v10.md) · [Interior render](/home/agile/Projects/kysucka_moderna_chata/work/v17/complete_3d/render_interior.png)

## 4. Stage 2 right-valley forest and trail diagnosis

### Pilot coordinates and design

Use this inclusive world XY polygon in metres:

```text
(-15,58) (-9,63) (-12,86) (-18,105) (-23,122) (-35,143)
(-68,148) (-72,123) (-58,108) (-44,98) (-31,81) (-23,64)
```

Its bounds in the V11 valley basis are station `46.289–143.139 m`, right lateral `30.996–89.573 m`, using origin `(7.2,5)`, normalized forward `(-.822849,.568260)` and right `(forward_y,−forward_x)`. There are 31 source trees inside, including 26 conifers and five broadleaves. Use the wide `CAM_V11_VALLEY_REVIEW` crop `[712,960) × [0,244)` at 960 × 540, with pixel origin at the upper left. The adjacent gravel treatment runs from V07 station `s=93` to `124 m`. The visual target is grouped meadow-to-forest transitions with visible gaps and depth. [Concept reference](/home/agile/Projects/kysucka_moderna_chata/reference/01.png) · [V16 baseline](/home/agile/Projects/kysucka_moderna_chata/work/v16/meadow_trail_01/renders/B_v16_960.png)

Set `CAM_V18_FOREST_MARGIN` to **`[-24,100,13.982899]` toward `[-41,114,17.408537]`**, 32 mm, horizontal 36 mm sensor, zero shifts, `.03–600 m` clips and DOF off. The ground at the eye is `12.332899 m`, so eye height is 1.65 m. Use `-Z` track and `+Y` up. Keep the saved sun and world.

- **Adult and soil.** Replace the focal *P. mariana* at `[-39.4190,109.3753]` with a local Norway spruce at the same XY. Ground there is `13.774797`. Use the local adult master with a clear view of the bark collar from the witness. Selectively remove separable camera-side lowest dead or drooping branch components on an owned copy if they cover the collar. Maintain the adjoining crown and verify its branch joins. Use the adult at `[-44.829,116.349]` for the juvenile height comparison. The focal base projects near `(356,410)` in the witness. Use crop `[264,470) × [300,500)` for close evaluation.
- **Ecotone and depth.** Use the two existing juvenile positions at `[-40.984,116.188]` and `[-36.004,116.845]`. Place the broadleaf group around the V17 birch currently at `[-33,93]` by moving it to `[-48.5,109.5]`, with irregular shrub and litter patches. Bring the isolated birch at `[-61,122]` toward the beech group, with `[-57,129.5]` as the first support-tested root. Keep a sun gap at `[-32.5,111.5]` and a deeper stand witness toward `[-48,132]`. Terrain rays from the proposed camera reached all these anchors, and terrain rays toward the sun cleared the gap. Stage 2 checks actual foliage and trunk occlusion in the matched render.
- **Three layers.** Use owned material derivatives on the existing terrain carriers. Keep their vertex coordinates in the pilot. Fade conifer soil, sparse moss and twig/root detail according to crown footprints. Mix leaf litter in patches around the broadleaf groups. Add small groups of spruce juveniles, low shrubs and sparse grass in gaps, thinning toward open meadow. Regroup the scattered broadleaves with nearby adult crowns and understory, and replace the four in-polygon *P. mariana* selectively with verified Norway spruce forms at existing heights and IDs. Use irregular crown spacing to preserve the open valley and at least two visible stand depths. Preserve the 175 botanical points and the meadow outside the pilot masks.
- **Support and preview.** Sample the actual top triangles under each transformed root footprint, including triangle crossings. Check contact, slope, exposed root, burial, crown projection clearance from trail/fence and low branch clearance. Reuse the V11 clearance parameters for retained paths and garden. Keep render meshes instanced. Give every new prototype a paired lightweight working master with stable instance index, `IsViewport` selection and packed compact materials. Reuse the approximate 136–214-triangle V17 tree proxy range for recognizable working crowns.

### Existing forest inventory and V18 cohort

Values show combined complete-scene counts and min/median/max over active placements. World heights use the transformed vertex range with the stored Euler rotation and XYZ scale. Source height is the actual render prototype.

| Index and source | Count | Source height m | Z scale min / median / max | World height m min / median / max |
|---|---:|---:|---|---|
| V11 `000` Abies LOD0 | 1,210 | 9.607 | .543 / 1.554 / 2.494 | 5.217 / 14.933 / 23.958 |
| V11 `001` Abies LOD1 | 2,080 | 9.606 | .545 / 1.587 / 2.498 | 5.231 / 15.249 / 24.002 |
| V11 `002` Abies LOD1 | 1,654 | 9.606 | .547 / 1.592 / 2.498 | 5.253 / 15.292 / 23.999 |
| V11 `003` Abies LOD0 | 1,508 | 9.607 | .542 / 1.575 / 2.491 | 5.207 / 15.134 / 23.934 |
| V11 `004` Abies Young | 1,782 | 9.601 | .157 / .538 / 2.473 | 1.504 / 5.168 / 23.744 |
| V11 `005` Mariana LOD1 | 968 | 11.244 | .464 / 1.372 / 2.131 | 5.213 / 15.427 / 23.959 |
| V17 beech LOD1 | 60 | 24.468 | .213 / .498 / .955 | 5.211 / 12.178 / 23.370 |
| V17 birch LOD1 | 99 | 18.042 | .290 / .678 / 1.296 | 5.234 / 12.237 / 23.385 |

The 1,220 V11 `004` placements are `1.504–6.490 m`, or `.095–.411` of the measured 15.782 m median of Norway spruce adult forms at least 9 m tall. The 562 hill-layer `004` placements are `5.234–23.744 m`, or `.332–1.504` of that same comparator. Twenty-eight hill-layer `004` placements fall in `.45–.55`. A height-only count using the equivalent same-species adult medians is 461 Norway spruces, 70 black spruces, three beeches and eight birches. This demonstrates why the `Young` label and half-height ratio require separate measurements.

- Pilot target is **two of 31 trees**. Use the two specified roots and match their actual world heights to `.50` of the 10.254 m Norway spruce comparator, approximately `5.127 m` each. Stage 3 target is **468 of 9,361 active trees, 4.9995%**, including the two pilot trees, using one-for-one replacement and retaining the population count.
- Build the juvenile form from an owned `ABIES_YOUNG` derivative. Retain the root and material/UV bands. Below mid-crown, redistribute normalized crown height with `u′=.04+.96*((u−.04)/.96)^1.2` for `u>.04` and broaden the lower whorls smoothly by up to 17%. Verify that lower foliage coverage visibly increases at matched height. Use the same form in the render and reduced working LODs. Record each selected stable source ID, comparator ID, source height, scale, actual height and ratio. Accept `.45–.55` on every cohort row. Count incidental short adult forms in the height histogram as observed.
- For Stage 3 use seed `13718` and stable source object/point IDs. Favor existing young-form roots, then convert eligible Norway spruce adult-form placements one-for-one. Select groups of two to four around a same-species adult at least 9 m tall, with the nearest eligible adult as comparator and the same stand as priority. Keep 35 qualifying juveniles in the readable margin mask, including the pilot group, and allocate the remaining 433 across 96 m occupied stand cells by population-weighted largest remainder. Take paired or larger groups in adjacent cells when a cell’s quota is one. Re-run terrain, clearance and visibility checks before counting a placement.

### Existing trail proof

The approach is centered at `X=7.875`. Paving is `+.110 m` with 50 mm joints. The last paving slab meets `V07_GATE_TRANSITION` at `Y=−8.175`. The bevel leads to `s=0` at `[7.875,−8.393592,0]`. The 1,105 stations cover **198.180813 m XY and approximately 200.6168 m graded**, with a maximum station interval of `.199971 m`. Four stations land on the threshold, 1,100 on gravel by vertical ray, and the last is the exact mesh edge vertex `[42,138.25,1.157007]`. The terrain at that vertex is `1.142007 m`. The gravel top has one connected component with 22,236 triangles. The closed sheet has 51,220 triangles and every edge has two incident faces. The sampled gravel top clearance is `.01499987–.01500034 m`.

| Valley-camera witness | Measured result |
|---|---|
| `s=83.6766–84.6091 m`, near pixels `(708–714,228)` | `V11_TERRAIN_NEAR` intercepts the camera rays before the gravel. |
| `s=113.1815–124.0314 m`, near pixels `(888–959,156–148)` | `V11_TERRAIN_FAR` intercepts the rays. At `s≈117.0493`, gravel at `[2.0393,73.3542,11.0882]` remains 15 mm above support and the terrain intercept is 10.665 m closer to the camera. |
| Past `s=124.2204 m` | The centerline leaves the 960-pixel wide frame. It continues to the exact old mesh endpoint. |
| Active gravel shader | `V17_MAT_V16_V07_GRAVEL` connects an opaque Principled surface with alpha `1`, transmission `0` and no displacement connection. The V17 material blend is zero at these upper-bend stations. Its local fines/grass blend changes material inputs. |

Use an overhead station overlay to prove the occluded bends. Keep their existing supported geometry. For `s=93–124`, add the compacted grey-brown gravel, fine-soil transition and irregular low verge through an owned material/mask derivative, keeping the continuous center visible in the overhead and walking checks. Verify the gate in its open position in a diagnostic copy using its measured hinge axis. The product retains the saved closed pose and the recorded 5 mm leaf clearance. Use a clear walking envelope at least `1.0 m` wide and `2.2 m` tall beyond the gate, with the short existing bevel reported separately.

## 5. Stage 3 readable margins, north continuation, and release gates

### Expansion and connector

- Apply the accepted pilot treatment to the two readable V11 margins. Use the V11 basis above. The measured mask has `32<t<420 m`, camera depth `0<d≤390 m`, projected X `−20<pixel_x<980` at 960 pixels, and `M(t)−20≤|l|≤M(t)+65 m`. Here `M=55+17 sin(t/87)+11 sin(t/29+.6)`, with `7 sin(t/53+1.8)` added on the negative-lateral side. It contains 704 baseline trees. Include the pilot polygon in the retained treatment. Use the three-layer composition and the cohort rules above. Preserve distant silhouettes with the existing instanced masters, applying further changes only for the registered in-stand cohorts and the proved route clearance.
- **Continue to the actual boundary.** V11’s terrain reaches `Y=644.75 m`. The old exit is the inner terrain seam. The straight continuation measured approximately 48% immediately north of the seam and reaches 86.3% farther on. A root-avoiding centerline feasibility probe found a **538.428 m XY / 541.609 m graded** continuation to `[44,644.75]`, on a true boundary edge with original ground `Z≈2.017673`. Its maximum longitudinal grade is **29.1%**. Its largest sampled center cut is `.939 m` and fill `.429 m`. This is the design basis for the new section. Its width, exact excavated surface and full walking envelope are Stage 3 acceptance measurements.
- **Reproduce the alignment.** Preserve the seam profile across `X=41.398663–42.601337`. Start the new ground center at `[42,138.25,1.142007]` and use `[42,140.25,1.724]`, `[42,142.25,2.306]` for the joining ramp. Search on 2 m XY cells in `X=−138…182`, `Y=142.25…644.25`, plus the true north edge row. Use 0.10 m design elevation levels and neighbors `(di,dj)` with `di=−2…2`, `dj=−1…2`, `0<|di|+|dj|≤3`. Start the search at level `2.30 m` and restore `2.306 m` at the ramp join. Require segment grade `≤.298` and center cut/fill within `±1.00 m` at samples spaced `≤.50 m`. Exclude centerline segments within `.95+max(.30,.045×world_height)` metres of a current trunk. Rank by length plus grade, cut/fill, lateral displacement and root-cell cost, using the forward distance to the edge as the heuristic and lexical grid indices for equal costs. Per-metre cost is `1+1.6×grade²+.10×mean_abs_cut_fill²+.0006×abs(x−42)`, plus `.6` per trunk in the destination cell and `.064` for a non-forward step. The measured route starts its turns near `[46,144.25]`, climbs through `[64,178.25]`, passes `[62,246.25]` and `[46,306.25]`, then approaches the boundary near `X=44`.
- **Build a supported connection.** Use the reproducible centerline as the alignment and carry a nominal 1.25 m gravel width, a 15 mm supported gravel layer and an irregular `.45–.75 m` verge. Use an owned derivative of the extension carrier and join tangent along the old gravel seam. Preserve the old vertices, material fields and UVs. Remove the internal end cap only in the owned joined trail mesh, and match the old terminal edge vertices exactly. Blend local grading back to unchanged terrain in a strip no farther than 2.5 m from the center. Adjust the last design level to the actual north edge height. Round bends only when the actual triangle-sampled profile remains within the grade and cut/fill bounds. Audit at `≤.20 m` spacing, at triangle crossings, across the strip, and at both seams. Test actual trunks and low branches against the swept walking envelope. For a collision, add the offending footprint to the search exclusion and regenerate the alignment before modifying any trees. Reserve the proved route mask before cohort placement.
- **Verify the whole route.** Require a single continuous supported top from the gate threshold through the former edge to the true scene perimeter, an opaque gravel center, a clear walking envelope and continuous cover outside the bounded verge. Keep the overhead with stations, terrain-hit overlays, the old join and the new edge. Re-render `Záber 06` for the extension’s effect on the forest and horizon. A failed connector gate leaves the accepted Stage 1 interior and last verified exterior available.

### Acceptance and implementation paths

- **Blender route.** Use `/home/agile/Applications/Blender/blender` 5.3.0, build `02f0899d78e3`, with `--background --disable-autoexec --threads 4`, `nice -n 10`, isolated MCP-disabled preferences and independent cache/temp paths. For cold verification copy each product alone into a different directory, mask `R` and use `bwrap --unshare-net`. Require zero `bpy.data.libraries`, zero linked IDs and packed bytes for all reachable render and working assets. Verify both arms of the geometry switches on representative instances, plus markers, startup frame and workspace. This sandbox route passed on the asset fixture.
- **Stage 1 comparison.** Render the frozen source and both cold products with identical Cycles CPU settings. Use 960 × 540 at 24 samples for `Záber 01`, `Záber 03`, `Záber 04`, `Záber 07` and `Záber 08`. Save the 1:1 gable crop `[650,930) × [0,450)` from frame 61 and the window/reflective regions from the interior frames. Require exact shared-envelope, light/world and protected render-branch digests. Any pruning requires identical decoded RGB pixels in all comparison images. Release both copies and the basement packet at this gate.
- **Stage 2 and 3 comparison.** Use fixed four-thread P0 CPU, seed 0, AgX/None, exposure 0, gamma 1 and OIDN Accurate/High. Render the 960 × 540 valley, specified right crop, 960 × 540 forest witness, specified trunk crop and overhead route witness before commissioning a 3200 × 1800 render. Use 24 samples for the first matched review, then 96 samples for a disputed small crop. Log wall time, peak RSS, available RAM and actual device. The archived complete valley render took approximately 2:51 at 960 × 540. Planning inventory peaked at approximately 5.65 GiB RSS. A full-resolution exterior render follows approval of the fast evidence. Stage 3 also requires cold exterior replay, unchanged interior product hash, the 468-tree registry, support and clearance receipts, and an asset provenance update.
- **Reproducibility.** Use one `scripts/v18_split_forest.py` entry point with stage, explicit input scene and output directory. Add only `forest_realism_v18` to `model/parameters.json`. Store source hash, seed, placement IDs, masks, asset pins and route thresholds there. Keep each accepted predecessor locally with its hash and replay from the complete V17 source. Use staged paths on the project filesystem and promote only verified products. A pre-existing product name requires matching its authorized predecessor hash before replacement.

| Area | Exact proposed implementation write allowlist |
|---|---|
| Canonical products and source | `blender/kysucka_chata_exterier.blend`, `blender/kysucka_chata_interier.blend`, `model/shared_envelope_v18.json`, `model/parameters.json`, `scripts/v18_split_forest.py`, `assets/ASSET_MANIFEST.md` |
| Adopted inputs | `assets/models/tevy_norway_spruce_v1/lod0.glb`, `lod1.glb`, `lod2.glb` under that directory, limited to adopted LODs. `assets/textures/forest_v18/<asset>/<asset>_<role>_2k.<ext>` for the two exact Poly Haven asset IDs and eight role/extension pairs in the Stage 0 table. |
| Stage 0 staging | `work/v18/stage0/raw/` for the eleven pinned downloads, `sidecars/lod{0,1,2}/source.{gltf,bin}` and `image-{00,01,02,03}.ktx2` in each LOD directory, `normalized.blend`, `assets.json`, `comparison-{crown,root,bark,soil}.png`, `resources.json` |
| Stage 1 evidence | `work/v18/stage1/{kysucka_chata_exterier.blend,kysucka_chata_interier.blend,dependencies.json,portability.json,basement.json,cross_sections.csv,basement_plan.svg,cross_sections.svg,resources.json}` and `{source,exterier,interier}-{wide,gable,north,hero,gallery}.png` |
| Stage 2 evidence | `work/v18/stage2/{before.blend,candidate.blend,pilot.json,forest_inventory.csv,trail_stations.csv,resources.json}` and `{before,after}-{wide,right,forest,root,trail}.png` |
| Stage 3 evidence | `work/v18/stage3/{before.blend,candidate.blend,release.json,cohort.csv,connector.csv,trail_stations.csv,resources.json,overhead.svg}` and `{before,after}-{wide,right,forest,root,trail,hills}.png`, plus `valley_3200.png` if approved |
| Isolated verification | `/tmp/opencode/v18_verify/` for per-product cold copies and isolated preferences, cache and process logs. Clean it after readback. |

### Report disposition

**Validation summary.** The project root, local origin and clean tracked `main` matched the grant. The AP gitlink and checkout were both `d7023cf037f6d17885c3ede5c04812c61640da50`. Meta was `27595fe2af3263ef7c3d0f29bf6373b779c9b0b6`. Both frozen scenes opened in separate headless processes. All six pinned input scenes, both preference files, all five pinned project renders and `reference/01.png` passed SHA-256 readback after cleanup. The owner reference remains `unrelated-owner-work`. Available RAM met the 10 GiB pre/post gate. The observed owner GUI process stayed present through the final gate, with zero foreign background processes at cleanup. `/tmp/opencode/v18_plan_inspect` was verified absent.

**Resolved Execution Issues / Near-Misses.** Poly Haven returned case-sensitive map role names and the corrected fetch verified all eight byte pins. The spatial JSON serialization retry completed with the same source. Blender recorded temporary append provenance before saving the disposable fixture, and cold reopen established zero library IDs. The command runner rejected forced recursive removal. An ownership-checked file inventory and individual unlink/rmdir operations removed all 77 temporary entries.

**Pre-Existing Failure Classification.**

- Pre-existing claim: `asserted`
- Comparison baseline commit: `78534bd46020bb2bfc97eef69b05e583cba5a5e5`
- Baseline predates: `whole-logical-whole`
- Test identity: `V07_TRAIL` gravel endpoint against the active V17 terrain perimeter
- Failure signature: gravel ends at `Y=138.25 m`, while the active north perimeter lies at `Y=644.75 m`
- Topically related to touched behavior: `yes`
- Superseded by accepted authority: Michal’s decision to include the continuation in V18
- Regression exclusion evidence: the frozen complete scene and exterior checkpoint have identical trail and terrain geometry and unchanged byte hashes
- Closure impact: `blocks-closure` until Stage 3 verifies the connection

Orchestration critique:  
MEASURED: The V17 preparation receipt labels its inherited inventory as `objects` and `packed_images`. Stage 1 should record both inherited checks and actual cold-open totals so the gate can distinguish the two.  
LEAD: The proposed forest witness clears the terrain at all four subject anchors. The cheapest remaining check is the matched 960-pixel render with native foliage to confirm ground-level visibility and light through the gap.

**Smallest next step.** Accept the decision-complete plan and issue the explicit Stage 0–1 implementation grant in execution mode. Stage 2 pilot approval gates Stage 3 expansion.

**Authority expiry.** This terminal report ends the planning grant. Repository mutation and trace persistence are `none`. Manual relay of this complete report is assigned to the Orchestrator at `/home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/01_report_00.md`.

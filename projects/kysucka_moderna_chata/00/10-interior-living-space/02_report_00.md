### Report for ORCHESTRATOR_CHAT

Logical whole identity: kysucka-moderna-chata-interior-living-space  
Worker session ordinal: 02  
Worker exchange ordinal: 01  
Persistent role identity: WORKER  
Worker session profile: Planner  
Task identity: INTERIOR-V10-PLAN-R1  

**Capability handshake:** file read, search, image read, shell (`sha256sum`, `git rev-parse`, `git status -sb`, `python3`, `free -h`); network **not used**; Blender/MCP **not called**; file write **not used**. Session **read-only**.

**Evidence tier:** E0  
**Validation ladder:** not-used  
**Independent acceptance:** not-required  

**status:** PASS  
**Phase-qualified result:** not-applicable  
**Start commit:** `ebfdf66f5afc0c05343adf4ed49dffb03eb874ef` (observed)  
**End commit:** `ebfdf66f5afc0c05343adf4ed49dffb03eb874ef`  
**Changed files:** none  
**tests/validation:** prompt hash; seven JSON sections gate; source hashes; C1 ray arithmetic (`python3`); image review; reference hashes  
**Git result:** no writes  
**Report justification:** new-evidence  
**Logical-whole closure:** not-closed  

**Deviations:** Prompt expected HEAD `f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c`; observed `ebfdf66f5afc0c05343adf4ed49dffb03eb874ef` (`main...origin/main [ahead 1]`). Seven frozen JSON sections **MATCH** `work/v09/baseline/model/parameters.json`; planning uses baseline geometry, not HEAD identity alone.  
**Risks:** Concurrent V09 owns GUI/MCP and `nature_study_v09` append; RAM guard ≥12 GiB; `MAT_GLASS` roughness 0.07; gallery/stair headroom sensitive to exact `roof_z(y)` at west bays; front glazing deferred from exterior mutation until integration grant.  
**Missing evidence:** Per-pixel C1 frustum with `shift_y=0.105` and mullion occlusion; exact post-hide mesh bounds in saved blends — **Blender witness** in implementation slice 3.  
**Smallest next step:** Cooperator approves decisions §14 defaults; Orchestrator issues implementation grant slice 1 (`work/v10/**`, `model/interior_v10.json`, `scripts/interior_v10.py` only).  

**Authority expiry:** This terminal report ends INTERIOR-V10-PLAN-R1 planning authority. No implementation.

**Orchestration critique:**  
MEASURED: C1 axis ray at gable plane x=14.4 m gives y=−3.17 m (below glass); fireplace/sofa center rays cross gable at y=−0.81 / −2.47 m — confirms Orchestrator correction vs prior plan.  
LEAD: Prior plan ranked fireplace/sofa as C1-primary; corrected wedge is dining/kitchen/rear-roof through upper gable pane.

**Resolved Execution Issues / Near-Misses:** none introduced here  
**Pre-Existing Failure Classification:** V09 concurrent session; V08 GPU reset history; glass 0.07 blur — carry forward

**Preserved inventory (from sources; implementation Worker has no prior report):**

| Item | Value | Source |
|---|---|---|
| Room 07 rect | x∈[8.8,14.1], y∈[0.3,8.1], F=+0.450 m | `work/v09/baseline/model/parameters.json` L168–176, L17 |
| Roof | E=+3.250 m, R=+7.450 m, 45° | JSON L19–20; `design.roof_z` L12–13 |
| Chimney axis | (11.3, 3.2), 0.8×0.8 m | JSON L26–31; `build_scene.py` L214–228 |
| Gable glass | x≈L+0.012, y∈[0.15,8.25], upper y∈[1.35,7.05] | JSON L33–38; `build_scene.py` L169–174 |
| Corridor partition | x∈[8.65,8.8]; opening y∈[3.35,4.5] | JSON L235–251, L137–144 |
| D04 | x=7.1, y=3.2, w=1.1 m | JSON L269–272 |
| Proxies | `50_INTERIOR_PROXY` | `build_scene.py` L29, L250–272 |
| C1 | [21.5,−10,1.25]→[8.5,2.5,1.25], 35 mm, shift_y 0.105 | JSON L290–309 |

---

## 1. Visibility

### 1.1 Orchestrator ray arithmetic (verified)

Camera **C**=(21.5,−10,1.25), target **T**=(8.5,2.5,1.25). For world point **P**=(px,py), parametric ray at gable plane x_g=**14.4 m**:

`t_g = (14.4 − 21.5)/(px − 21.5)`; `y_g = −10 + t_g·(py + 10)` (z≈1.25 on horizontal sight lines).

| Point | (px,py) | y at x=14.4 m | x at front y=0 | Gable visible? |
|---|---|---|---|---|
| Fireplace | (11.3, 3.2) | **−0.81** | 13.77 | **No** (y<0.15) |
| Sofa centre | (10.8, 1.35) | **−2.47** | 12.07 | **No** |
| Dining centre | (12.55, 6.35) | **+2.97** | 16.03 (off wall) | **Yes** (0.15–8.25) |
| Kitchen centre | (10.9, 7.75) | **+1.89** | 15.53 | **Yes** |
| Camera axis | (8.5, 2.5) | **−3.17** | — | **No** |

**Fact:** Lower gable y∈[0.15,8.25]; front wall plane y≈0 blocks rays with y_g<0.15 before x_g.

**Inference (gable wedge, plan view):** Ray through gable front glass edge (y=0.15) meets rear wall y=8.1 at **x≈8.84 m** (prompt); visible deep triangle: rear wall x∈[8.84,14.4], dining band y≈5.6–7.2, kitchen run, upper-pane roof soffit timbers — matches `previews/v08/after_C1.png`.

**C1 sees today (named objects, priority):** `G01_lower_glass`/`G02_upper_glass`, `GABLE_mullion_*`, `GABLE_timber_*`, `DINING_table`, `CHAIR_*`, `KITCHEN_proxy`/`KITCHEN_worktop`, `PENDANT_ring_proxy`, rear `W04` frame, `roof_z` soffit — **not** `FIREPLACE_stone`/`SOFA_*` as primary centrelines.

**Blender check (slice 3):** mesh ray cast from `CAM_A_REFERENCE` through mullion solids; export hit list to `work/v10/evidence/c1_hits.json`.

### 1.2 After planned front glazing (study + integration)

Planned aperture **W07_FRONT**: x∈[10.05,14.012], y=0 face, sill z=0.50 m, head z=3.20 m (plate zone), mullions per §4.

| Effect | Objects newly readable from C1 at z≈1.25 | Still blocked on axis |
|---|---|---|
| Front glass strip | Forecourt paving, `BENCH_seat`, lower `CLADDING_front` gap, meadow/fence silhoette at y∈[0.15,2.5] | Fireplace, sofa (rays remain y_g<0.15 at x=14.4) |
| Combined gable+front | Dining/kitchen unchanged; adds ground-level exterior depth left of hearth | Hearth/TV stack not in C1 centreline wedge |

**Integration-only:** cutting `CLADDING_front_*` / `WALL_front_*` for x∈[10.05,14.012] — hidden, not deleted (`build_scene.py` L122–153).

---

## 2. Gallery

### 2.1 Slab geometry

| Quantity | Value | Derivation |
|---|---|---|
| Plan extent | x∈[2.7,8.55], y∈[0.3,8.1] | Covers rooms 01–06 rects (JSON L100–166); stops 0.10 m before partition face x=8.65 |
| Corridor void | x∈[2.7,8.55], y∈[3.35,4.5] open | Clear D04 corridor; bridge only at stair landing |
| FF elevation | **+2.70 m** | Below `roof_z(6)−2.1 m` guard; see below |
| Slab thickness | **0.20 m** | Underside **+2.50 m** → bedrooms 01–03 ceiling |
| Edge beam | 0.24×0.18 m GLT along x=8.55, y∈[0.3,8.1] | Bears gallery + railing toward room 07 |

**Partition interface:** Gallery bears on existing `PARTITION_proposed` tops (hidden); add owned `V10_GALLERY_support_*` pads at x=8.55, not editing partition meshes.

### 2.2 Headroom map (`roof_z(y)=7.45−|y−4.2|`, `design.py` L12–13)

| y (m) | roof_z | Clear above FF 2.70 m (m) | Usable gallery strip |
|---|---|---|---|
| 0.3 | 3.55 | 0.85 | Low edge only; railing + walk 0.9 m |
| 2.0 | 5.45 | 2.75 | Full walk |
| 4.2 | 7.45 | 4.75 | Ridge; recessed spots only |
| 6.0 | 5.65 | 2.95 | Bedrooms 05–06 |
| 8.1 | 3.55 | 0.85 | Rear edge walk |

**Usable walk band:** y∈[1.2,7.2] with ≥2.10 m clear; y∈[0.3,1.0] and [7.2,8.1] marked low-edge (reference plants only).

### 2.3 Railing toward room 07

| Param | Value | Reference |
|---|---|---|
| Height | 1.10 m above FF (rail top 3.80 m) | concept_00 cable gallery |
| Posts | 0.040 m square @ 1.2 m spacing along x=8.55 | steel `metal_plate_02` |
| Infill | 3× cable Ø0.006 m, 0.09 m spacing | procedural |
| Top rail | 0.08×0.05 m timber `oak_veneer_01` | — |

**Room 07 view:** Seated sightline from (10.6,1.6,1.05) sees railing sillhouette + underside cladding (`raw_plank_wall`) + stair upper flight — **not** bedroom interiors (partition face).

---

## 3. Stair

### 3.1 Position (panorama: stair left; hero: stair right of hearth — both along partition)

| Stage | Footprint | Notes |
|---|---|---|
| Foot | (8.45, 1.65) | 0.15 m inside room 07, west of D04 swing zone |
| Run 1 | Along +Y, centreline x=8.45 | Toward corridor opening |
| Landing | (8.45, 3.95) size **1.25×1.00 m**, z=+1.50 m | Below opening y∈[3.35,4.5] |
| Run 2 | Turn −X toward gallery | Arrives gallery FF at **(7.55, 4.25, 2.70)** |

### 3.2 Rise / goings (plausible domestic)

| Quantity | Value | Arithmetic |
|---|---|---|
| Total rise | **2.25 m** | 2.70 − (F+0.025) = 2.70 − 0.475 |
| Risers | **15** @ **0.150 m** | 15×0.15=2.25 |
| Goings | **0.280 m** | 2×0.28+0.15≈0.71 m/side comfort |
| Width | **1.00 m** clear | Treads 1.05 m total |
| Stringers | 0.045 m laminated oak sides | procedural + `stair_planks` |
| Tread thickness | 0.040 m | Cantilevered boxes |

**Flights:** Run1: 7 risers, run 1.96 m; landing; Run2: 8 risers, run 2.24 m.

### 3.3 Headroom along walking line

Min roof at (8.45,3.5)=`roof_z(3.5)`=6.95 m; at tread z=1.5 m → **5.45 m** clear (>>2.10 m). **Blender check:** sample 20 points along polyline, assert clearance ≥2.05 m.

### 3.4 Corridor / door / kitchen clearance

| Constraint | Requirement | Proposed |
|---|---|---|
| Corridor opening | y∈[3.35,4.5], width 1.15 m | Landing centre y=3.95 inside opening |
| D04 swing | x=7.1, w=1.1 m, swing −1 | Stair foot y=1.65 > 1.0 m south of door |
| Circulation | ≥0.85 m to kitchen | Kitchen run starts y=7.0; stair run 1 ends x=8.45 leaves path x>9.0 |
| Gallery arrival | (7.55,4.25) | Opens to gallery walk toward rooms 05–06 |

### 3.5 Lit-step detail

Warm **2700 K** strip: `AREA` 8 W per tread underside, size 0.8×0.02 m, emissive nose `V10_MAT_TREAD_GLOW` (duplicate `MAT_LED`); synced to fire dimmer group.

### 3.6 Railing

Same cable/post spec as gallery; 1.10 m on open sides; wall-side bracket on partition face (hidden proxy partition remains).

---

## 4. Glazed front corner

### 4.1 Opening (study = interior glass shell; integration = envelope cut)

| Param | Value | Match gable profile |
|---|---|---|
| X span | **[10.05, 14.012] m** | Aligns `BENCH_seat` / entry zone |
| Sill z | **0.50 m** (F+0.05) | Above `FLOOR_interior` |
| Head z | **3.20 m** | Just below plate E=3.25 |
| Frame | 0.065 m `MAT_FRAME` analogue → `V10_MAT_FRAME` | `mullion_width` 0.075 JSON L34 |
| Vertical mullions X | 10.05, 12.075, 13.043, 14.012 | 3 bays |
| Horizontal rails z | 1.15, 2.65, 3.18 | Echo gable transom |
| Corner post | x=14.012, y=0, mates `G01_lower_glass` | shared dark post mesh |

### 4.2 Intersected sources (`build_scene.py`)

| Object | Lines | Handling |
|---|---|---|
| `WALL_front_*_*` core strips | L122–136 | Hide; `V10_W07_GLASS_*` in front |
| `CLADDING_front_*` | L137–153 | Hide x∈[10.05,14.1]; retain in file |
| `BASE_slab` edge | L119 | No change |
| `BENCH_seat`, `BENCH_support_*` | L235–237 | **Keep visible** through glass (exterior read) |
| `WALL_DECOR_proxy` | L236 | Hide render; retained |
| `SCONCE_*` (x=6.95,8.78) | L233–234 | Outside span — unchanged |
| `LED_eave` front segment | L212 | Hide segment x∈[10,14]; retained |
| `FIREWOOD_log` bay | L240–243 | Outside x<10 — unchanged |

**C1 effect:** Adds foreground exterior horizontal band; does **not** bring fireplace into centreline (§1).

---

## 5. Fireplace

### 5.1 Recommended synthesis (panorama-led + concept_00 fire read)

| Element | Spec | Chimney lock |
|---|---|---|
| Stack | 1.45×0.55 m plan stone to z=5.20 m, `stacked_stone_wall` 2K, tile 2 m | Centre (11.3, 3.2) |
| Insert | Black steel 0.85×0.62×0.72 m, corner glass 3-sided 4 mm `V10_MAT_GLASS_FIRE` | Firebox centre (11.3, 3.05, 0.95) |
| Hearth bench | Stone slab 1.60×0.55×0.42 m, top z=0.88 m | On axis |
| Breast | Steel panels + stone to `CHIMNEY_shaft` | Reuse shaft L217 unchanged |
| Log store | Niche 0.55×0.40×0.55 m right of stack, procedural logs | concept_00 shelf zone |
| TV wall | Plane 1.65×0.92 m @ (12.05, 3.15, 1.65) | Panorama |
| Fire light | Area 60 W warm inside box + emissive logs 8 W | Supersedes `FIRE_proxy` visibility |

**Alternative (Cooperator D1):** Full concept_00 — peninsula glass only on stone bench, no stacked stone TV wall; lighter C1 silhouette.

**Proxies:** Hide `FIREPLACE_stone`, `FIREPLACE_recess`, `FIRE_proxy` — do not delete.

---

## 6. Layout and furniture

### 6.1 Zoning (plan, stair in place)

| Zone | XY | Min circulation |
|---|---|---|
| Living | x 9.0–12.0, y 0.8–3.8 | 0.85 m to stair foot |
| Hearth/TV | x 11.0–12.8, y 2.6–4.0 | — |
| Dining | x 11.8–13.4, y 5.2–7.2 | 0.90 m around table |
| Kitchen | x 9.0–13.2, y 7.0–8.0 | 0.85 m work aisle |
| Work/music | x 13.0–14.0, y 1.0–3.5 | 0.75 m desk depth |
| Doors | D05/D06 glimpses at x≈4.4/6.65 | Closed leaves procedural |

### 6.2 Furniture table

| Piece | Centre (x,y,z) | Rot°Z | Size L×D×H (m) | Asset |
|---|---|---|---|---|
| Sofa L (assembly) | (10.45,1.35,F) | 0 | 2.73×0.93×0.82 | `sofa_03` + chaise procedural 1.05×0.93 |
| Ottoman/pouf | (9.85,2.05,F) | 15 | 0.88×0.62×0.62 | `Ottoman_01` |
| Coffee table | (10.05,2.65,F) | 0 | 1.20×0.60×0.39 | `modern_coffee_table_01` |
| Rug | (10.2,2.1,F+.01) | 0 | Ø2.40×0.02 | procedural weave `rough_linen` |
| Throw | on sofa | — | — | procedural `knitted_fleece` |
| Pillows | sofa | — | — | `throw_pillows_01` scaled |
| Arc floor lamp | (9.55,1.05,F) | 0 | procedural arch H=1.75 | procedural |
| Side stump | (11.65,0.95,F) | 0 | 0.55×0.45×0.57 | `tree_stump_01` scaled |
| Dining table | (12.50,6.35,F) | 0 | 2.00×0.95×0.76 | procedural (catalogue 2.26 m long) |
| Chairs ×6 | grid per build L259–264 | — | 0.43×0.58×0.97 | `dining_chair_02` |
| Kitchen run | (10.9,7.55,F) | 0 | 3.60×0.60×0.92 | procedural matte fronts |
| Worktop | (10.9,7.48,F) | 0 | 3.70×0.65×0.04 | procedural stone |
| Pendant rings | (12.55,6.35,2.85) | 0 | Ø1.10×0.03 | procedural emissive |
| Desk | (13.35,2.40,F) | −15 | 1.40×0.70×0.75 | procedural |
| Office chair | (13.15,2.05,F) | 10 | 0.82×0.99×1.02 | `modern_arm_chair_01` |
| Guitars/keyboard | (13.45,3.10,F) | — | procedural stands | procedural |
| Plants ×4 | see refs | — | — | `potted_plant_01`, `_02` |
| Picture | (8.95,2.85,1.45) | 90 | 0.59×0.84 | `hanging_picture_frame_02` |
| Vases/books | shelves | — | — | shortlist decorative |

---

## 7. Surfaces

| Surface | Texture ID | Res | Scale (m) | Notes |
|---|---|---|---|---|
| Floor | `plank_flooring_03` | 2K | 2.25 | UV metric along +X |
| Ceiling boards | `oak_veneer_01` | 2K | 1.83 | Under `roof_z` following rafters procedural 0.24 m |
| Walls plaster | `white_plaster_02` | 1K | 1.0 | Upper zones |
| Timber wainscot | `raw_plank_wall` | 2K | 1.87 | Hearth + TV wall to 2.4 m |
| Gallery soffit | `brown_planks_09` | 1K | 1.0 | Underside slab |
| Stair treads | `stair_planks` | 2K | 1.2 | — |
| Kitchen fronts | `painted_metal_shutter` | 2K | 2.0 | rough 0.35 |
| Worktop | `slate_floor_03` | 2K | 2.0 | — |
| Hearth stone | `stacked_stone_wall` | 2K | 2.0 | — |
| Sofa fabric | `wool_boucle` | 1K | 0.31 | — |
| Rug | procedural + `dirty_carpet` blend | 1K | 0.6 | — |
| Steel rails | `metal_plate_02` | 1K | 2.0 | — |

---

## 8. Lighting

| Light | Type | Position / target | K | Power (W) | Status |
|---|---|---|---|---|---|
| `SUN_key` | SUN | unchanged | ~5500 | 2.0 | keep `build_scene.py` L325–326 |
| `FILL_front` | AREA | unchanged | ~6500 | 280 | keep L327 |
| World Nishita | background | unchanged | — | 0.26 | keep L322–324 |
| `V10_FIRE_KEY` | AREA | (11.3,2.95,0.9)→hearth | 2700 | 60 | new |
| `V10_PENDANT` | mesh emission | rings z=2.85 | 2700 | 120 | supersedes `PENDANT_ring_proxy` light read |
| `V10_SPOT_*` | SPOT ×6 between rafters | y=4.2 band | 3000 | 15 each | new |
| `V10_STAIR_*` | AREA ×15 | tread noses | 2700 | 8 each | new |
| `V10_SHELF_LED` | AREA strip | fireplace niche | 2700 | 25 | concept_00 |
| `V10_LAMP_ARC` | POINT | lamp head | 2700 | 8 | new |
| `INTERIOR_warm` | AREA | (12,4.8,3.2) | warm | 200 | **hide**; replace mood |
| `DINING_downlight` | AREA | table | warm | 110 | **retire** after spots |

**Looks:** Day = sun + fill + low fire; Dusk = fire + stair + pendant + spots, sun energy ×0.35 (parameter in `interior_v10.json`, not world).

---

## 9. Cameras (C1 untouched)

| ID | Location | Target | Lens (mm) | Role |
|---|---|---|---|---|
| `V10_CAM_HERO` | (11.2, 2.45, 1.62) | (11.3, 3.15, 0.95) | 32 | concept_00: gable left, hearth centre, stair right |
| `V10_CAM_PANO` | (11.5, 4.2, 1.68) | (11.5, 4.2, 1.68) | 0 | **Equirect** 2048×1024 evidence |
| `V10_CAM_SEAT` | (10.55, 1.55, 1.02) | (11.2, 2.9, 0.85) | 40 | Seated living |
| `V10_CAM_GABLE_IN` | (13.05, 3.8, 1.55) | (10.8, 2.2, 0.9) | 28 | Valley through glass |
| `V10_CAM_DINING` | (11.9, 5.9, 1.62) | (12.5, 6.35, 0.92) | 35 | Table/kitchen |

**Equirect:** **Worthwhile** for layout QA vs `interior_concept_01_panorama`; not sole acceptance. C1 `CAM_A_REFERENCE` byte-frozen.

---

## 10. Technical route

| Decision | Choice | Proof |
|---|---|---|
| Study input | **Open** `blender/kysucka_chata_mcp_v03.blend` (15 MB), CLI save-as `work/v10/study/interior_study_base.blend` | Faster than full rebuild; has PBR timber, C1, lights, no forest (`prompt` L238–240) |
| Not rebuild | Full `build_scene.py` → v08 omit not needed for slice 1–2 | v03 cottage core witness equals envelope code path |
| Cottage equality vs `v08_view` | Export name+matrix for collections `10_ENVELOPE`…`60_LIGHTS` from both; SHA-256 JSON diff | Implementation step 0 |
| Parameter file | **`model/interior_v10.json`** only | No `parameters.json` edit while V09 active |
| Module | **`scripts/interior_v10.py`** `apply_v10(scene, P_int, ROOT, *, components=None)` | Pattern `vegetation_v08.py` L677–692 |
| Seed | **13710** | `random.getstate()` assert |
| Collections | `55_INTERIOR_V10` (+ `56_GALLERY_V10`, `57_STAIR_V10`, `58_GLAZING_V10_STUDY`) | — |
| Naming | Prefix **`V10_`**; materials **`V10_MAT_*`** | — |
| Hidden tracking | `V10_replaces` JSON on scene: `{original_name, hide_state}` | — |
| Idempotence | Second `apply_v10` → zero delta object count | — |
| Protected witnesses | C1 matrix, G01/G02 verts, chimney, partitions, no `nature_study_v09` | Automated script |
| Integration (later grant) | Append `interior_v10` to `parameters.json`; hook after `apply_v08`; save `kysucka_chata_mcp_v10.blend`; apply **front glazing** envelope cut; link exterior glass | Preconditions: V09 closed, ≥12 GiB, no shared MCP |

---

## 11. Glass

**Mechanism (study):** Duplicate interior-facing meshes for gable + study front glass with owned **`V10_MAT_GLASS_VIEW`** (roughness **0.03**, IOR 1.45); exterior `MAT_GLASS` slots on `G01`/`G02` unchanged. Optional compositor Z-mask pass for stills. **Reason:** JSON `MAT_GLASS` roughness 0.07 (`parameters.json` L351) blurs interior; study must judge hearth/sofa via `V10_CAM_*`, C1 via A/B crop with view material on **duplicate** faces only.

**Front corner in study:** `V10_W07_GLASS_STUDY` plane 0.02 m in front of hidden cladding; full envelope cut only at integration (`prompt` L46–47).

---

## 12. Slices, resources, evidence

| Slice | Delivers | Check |
|---|---|---|
| **S1 Structure** | Gallery slab, stair, surfaces clay/PBR pilots, hide map | Idempotence; headroom script; Solid screenshot |
| **S2 Furniture** | CC0 downloads to `assets/models/interior/`, assembly | Manifest SHA; bbox vs table §6 |
| **S3 Lights+renders** | Full rig, glass view mats, cameras, C1 crop A/B | P0 CPU 8t 96 spp if RAM≥12 GiB |

| Resource | Value |
|---|---|
| Process RSS S1 | 1.5–3 GiB |
| S2 | +1–2 GiB |
| S3 render | 4–8 GiB peak |
| Pilot | 800×600, 32 spp, ~3–8 min |
| Hero | 1448×1086, 96 spp, ~25–45 min serial |
| GPU | **Forbidden** |
| Downloads | ~80–120 MB → `assets/textures/interior/`, `assets/models/interior/` |
| Evidence | `work/v10/evidence/*.png`, `interior_v10_summary.json`, `sha256.txt`, `c1_gable_crop_{before,after}.png`, cold-open log |
| Replay | CLI reopen study blend + `apply_v10` stdout |
| Recovery | `work/v10/checkpoint_pre_{slice}.blend`; stop if RAM<12 GiB before render; V09 MCP conflict → abort save |

---

## 13. Grant boundary

### Allowlist (implementation, V09 active)

`scripts/interior_v10.py`, `scripts/build_interior_study.py` (optional), `model/interior_v10.json`, `work/v10/**`, `assets/textures/interior/**`, `assets/models/interior/**`, Meta `00/10-interior-living-space/**` (Orchestrator write)

### Forbidden until integration

`model/parameters.json`, `scripts/build_scene.py`, `scripts/nature_study_v09.py`, `AGENTS.md`, `README_SK.md`, `docs/OPERATIONS.md`, `work/v09/**`, overwrite `blender/kysucka_chata_mcp_v08*.blend`, live MCP/GUI, GPU render, `git write`, driver/prefs

### Commands

Allowed: background Blender **isolated** `--disable-autoexec`, single owner, CPU only; `sha256sum`; asset download Poly Haven only; serialized renders after `free` guard  
Forbidden: shared MCP PID 9404; `git add`; OPTIX stress

---

## 14. Open Cooperator decisions

| # | Decision | Options | Default | Consequence |
|---|---|---|---|---|
| D1 | Fireplace character | A stacked stone + TV (§5.1); B concept_00 glass peninsula dominant | **A** | A matches panorama layout |
| D2 | Front bench | Keep `BENCH_seat` visible; remove/hide | **Keep** | Visible through new glass |
| D3 | Front glass span | A x∈[10.05,14.0]; B full room front x∈[8.8,14.0] | **A** | B needs more cladding hide |
| D4 | Gallery FF | 2.65 / **2.70** / 2.75 m | **2.70** | Affects riser count |
| D5 | Work corner depth | Full music (§6); desk only | **Full** if approved | Instruments need x>13 |
| D6 | Glass study | A `V10_MAT_GLASS_VIEW` duplicate; C interior cams only | **A** | C1 A/B needs A |
| D7 | Equirect render | Yes 2048×1024 / No | **Yes** | QA vs panorama |
| D8 | Sofa | `sofa_03`+procedural chaise; full procedural | **Catalogue hybrid** | Only catalogue path |

### Follow-on wholes

1. V10 integration + front envelope glazing cut  
2. Rooms 01–06 furnish  
3. Global glass/optics (`MAT_GLASS` policy)  
4. Door hardware D02–D06  
5. Bathroom/technical rooms 02–03

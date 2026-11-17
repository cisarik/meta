### Report for ORCHESTRATOR_CHAT

Logical whole identity: kysucka-moderna-chata-interior-living-space  
Worker session ordinal: 01  
Worker exchange ordinal: 01  
Persistent role identity: WORKER  
Worker session target: fresh-worker-session  
Native planning mode: required  
Worker session profile: Planner  
Phase: planning  
Task identity: INTERIOR-V10-PLAN  

**Capability handshake:** file read, search, image read, shell (read-only: `sha256sum`, `git rev-parse`, `python3` JSON/math), network **not used** (no catalogue fetch this session), write **not observed / not used**; session **read-only**. Blender/MCP **not called**.

**Evidence tier:** E0 — read-only repository planning.

**Validation ladder:** not-used  
**Independent acceptance:** not-required

**Repository gate (verified):**

| Check | Result | Source |
|---|---|---|
| Project root | `/home/agile/Projects/kysucka_moderna_chata` | prompt L113 |
| HEAD | `f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c` | `git rev-parse HEAD` |
| Prompt SHA-256 | `db31e843fb3a98adb32660dea2ff2927ee760a6a486856e57195ac52a33f716e` (323 lines) | `sha256sum` |
| AP gitlink | `d7023cf037f6d17885c3ede5c04812c61640da50` | prompt L121–122 / AGENTS.md |
| `scripts/build_scene.py` | `c83e2bd2f584231e5df7719998ecec64d201e1dc01a6f49457e0a4b1904cc369` | `sha256sum` (matches prompt L129) |
| `reference/kysucka_chata_moderna.png` | `05bc3e72161e5945379c86da80450ffdf82ddce6dbdd9b9e77071aa79cdecc96` | `sha256sum` |
| `previews/v08/after_C1.png` | `17c7cc0715b1c3e74678a702a845d33c4f6f982de041baf259176c1cc665d81f` | `sha256sum` |
| JSON sections gate | `building`, `openings`, `rooms`, `partitions`, `interior_doors`, `camera`, `materials` all **MATCH** `work/v09/baseline/model/parameters.json` | `python3` diff |
| RAM available | **~14 GiB** `available` | `free -h` |

**status:** PASS  
**Phase-qualified result:** not-applicable  
**Start commit:** `f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c`  
**End commit:** `f3439b18dc1c2f6f44b6f1d5642ad8c4c44b9c2c`  
**Changed files:** none  
**tests/validation:** planning evidence only (hashes, JSON gate, geometry math, image review)  
**Git result:** no writes  
**Report justification:** new-evidence  
**Logical-whole closure:** not-closed  

**Deviations:** none from prompt.  
**Risks:** active V09 whole owns live Blender GUI and `model/parameters.json` append — interior work must stay disjoint until integration grant. Hardware-reset history (AGENTS.md V08) — no GPU stress without grant.  
**Missing evidence:** exact per-pixel C1 frustum with `shift_y=0.105` and mullion occlusion requires Blender ray cast (not run). Network catalogue identifiers not verified live (preflight step proposed).  
**Smallest next step:** Cooperator approves plan + decisions table; Orchestrator issues implementation grant with `work/v10/**` + `model/interior_v10.json` only (V09 settled or path fully disjoint).

**Authority expiry:** This terminal report ends INTERIOR-V10-PLAN planning authority. No implementation.

**Orchestration critique:**  
MEASURED: none  
LEAD: none  

**Resolved Execution Issues / Near-Misses:** none  
**Pre-Existing Failure Classification:** open visualization gaps (glass roughness 0.07, interior proxies); unrelated deferred V07 shoulder; V09 concurrent session — carry forward, not introduced here.

---

## 1. Measured inventory

### 1.1 Room 07 envelope (fact from JSON + `design.py`)

| Quantity | Value | Source |
|---|---|---|
| Room id / name | `07` Obyvacka / jedalen / kuchyna | `work/v09/baseline/model/parameters.json` L168–176 |
| Floor rect XY | x ∈ [8.8, 14.1], y ∈ [0.3, 8.1] m | same |
| Net floor area | 5.3 × 7.8 = **41.34 m²** | `design.metrics()` pattern L16–17 |
| Floor datum | F = **+0.450 m** | JSON `building.floor_z` L17 |
| Wall plate | E = **+3.250 m** (façade/cladding reference) | JSON L19 |
| Ridge | R = **+7.450 m** | JSON L20 |
| Open volume | no flat ceiling; underside follows `roof_z(y)` | `design.roof_z` L12–13; `build_scene.py` L185–191 |
| `roof_z(0.3)` ≈ `roof_z(8.1)` | **~3.55 m** at short walls | computed: R − (W/2 − 0.3)×(R−E)/(W/2) |
| `roof_z(4.2)` (axis) | **7.45 m** | ridge |
| Glazed gable plane | x ≈ **L = 14.4 m** (glass at L+0.012) | `build_scene.py` L169–179 |
| Corridor boundary | partition strip x ∈ [8.65, 8.8] | JSON `partitions` L246–250 |
| Door D04 | x=7.1, y=3.2, w=1.1 m | JSON L269–272 |
| Rear W04 (kitchen) | x=10.4–12.2, sill +1.1 m → z 1.55–2.65 | JSON L90–98 |

**Inference:** Room 07 clear height at centerline ~7 m; at north/south edges of room ~3.55 m below ridge line.

**Blender-only:** exact interior face normals after v08 merge; proxy hide state in saved blend.

### 1.2 Surfaces bounding room 07 (from `build_scene.py`)

| Role | Objects / mechanism | Material slot | Lines |
|---|---|---|---|
| Floor finish | `FLOOR_interior` cube (wood) | `MAT_FLOOR` | L120 |
| Inner leaf rear/front walls | `WALL_*` cubes, `inside` | `MAT_INTERIOR_PLASTER` | L122–136 |
| Wood bay inner edge | `WALL_left_closed` x=2.55 (out of 07) | inside | L121 |
| Corridor partitions | `PARTITION_proposed` for JSON partitions | inside | L267–268 |
| Roof underside | `SOFFIT_wood_*`, `ROOF_underlay_*` inner faces | `MAT_WOOD_V` / roof | L185–190 |
| Gable inner lining | `GABLE_timber_*` | `MAT_WOOD_V` | L180–183 |
| Glazed gable | `G01_lower_glass`, `G02_upper_glass` | `MAT_GLASS` | L169–174 |
| Chimney mass (visual) | `FIREPLACE_stone`, `FIREPLACE_recess`, `FIRE_proxy`×6 | stone/dark/fire | L223–228 |
| Exterior chimney shaft | `CHIMNEY_*` (penetrates volume) | stone | L215–222 |

Protected envelope/glazing not to move (prompt L69–72).

### 1.3 Existing interior proxies, lights, materials (fact)

**Collection:** `50_INTERIOR_PROXY` (`build_scene.py` L29).

| Name | Center (x,y,z) | Size / notes | Mat | L |
|---|---|---|---|---|
| `FIREPLACE_stone` | (11.3, 3.2, 1.7) | 0.8×0.8×2.5 | stone | 223 |
| `FIREPLACE_recess` | (11.3, 2.79, 1.2) | 0.63×0.03×0.8 | dark | 224 |
| `FIRE_proxy` ×6 | cy−0.44, z~1.04 | cones | fire emissive | 225–228 |
| `SOFA_base` | (10.8, 1.35, F+.26) | 3.0×1.0×0.42 | fabric | 251 |
| `SOFA_back` | (10.8, 0.94, F+.60) | 3×0.2×0.75 | fabric | 252 |
| `SOFA_arm` ×2 | x=9.45/12.15 | 0.23×0.95×0.62 | fabric | 253 |
| `COFFEE_table` | (10.0, 2.7, F+.42) | 1.4×0.7×0.07 | wood H | 254–255 |
| `DINING_table` | (12.55, 6.35, F+.76) | 1.1×2.0×0.09 | wood H | 256–258 |
| `CHAIR_*` | 6 seats grid | ~0.43×0.45 | wood | 259–264 |
| `KITCHEN_proxy` | (10.9, 7.75, F+.45) | 3.7×0.58×0.9 | plaster | 265 |
| `KITCHEN_worktop` | (10.9, 7.73, F+.92) | 3.8×0.65×0.055 | stone | 266 |
| `PENDANT_ring_proxy` | (12.55, 6.35, 3.0) | torus R=.60 | led | 270–272 |

**Lights (`60_LIGHTS`):**

| Name | Loc → target | Power | Color | L |
|---|---|---|---|---|
| `INTERIOR_warm` | (12, 4.8, 3.2)→(13.9, 3.4, 1.3) | 200 | warm | 273 |
| `DINING_downlight` | (12.5, 6.35, 3.1)→(12.5, 6.35, 0.5) | 110 | warm | 274 |
| (+ seed exterior) | `SUN_key`, `FILL_front` | — | — | L325–327 |

**Shared materials used by interior:** `MAT_INTERIOR_PLASTER`, `MAT_FLOOR`, `MAT_FABRIC`, `MAT_WOOD_H/V`, `MAT_STONE`, `MAT_GLASS` (roughness **0.07** JSON L351–352), `MAT_LED`, `MAT_FIRE_PROXY`.

### 1.4 Reference vs C1 (observation)

| Cue | Reference `kysucka_chata_moderna.png` | C1 `previews/v08/after_C1.png` | Mapping |
|---|---|---|---|
| Timber-lined volume | strong horizontal wood | flat beige boxes | needs V10 lining |
| Fireplace / fire | stone + visible flame | grey box + emissive cones | refine stone + fire read |
| Sofa | upholstered L-shape | fabric boxes | replace proxy |
| Dining + ring pendant | table, chairs, halo light | visible but crude; glass blur | y≈6.35 zone |
| Kitchen run | rear counter | grey `KITCHEN_proxy` | y≈7.75 |
| Warm light | linear + practicals | `INTERIOR_warm` + downlight | extend, keep world |

---

## 2. Cameras: C1 sightline and interior review poses

### 2.1 C1 (unchanged — fact)

| Param | Value | Source |
|---|---|---|
| Name | `CAM_A_REFERENCE` | JSON L291 |
| Location | [21.5, −10.0, 1.25] | JSON L292–296 |
| Target | [8.5, 2.5, 1.25] | JSON L297–300 |
| Lens / sensor | 35 mm / 36 mm | JSON L302–303 |
| shift_y | **0.105** | JSON L309; `build_scene.py` L329 |
| Resolution | 1448×1086 | JSON L304–307 |

### 2.2 Gable glazing aperture (fact)

| Pane | y range (m) | z range (m) | Source |
|---|---|---|---|
| Lower `G01` | 0.15 – 8.25 | 0.45 – 3.18 | JSON L35–38, L33; `build_scene.py` L170–171 |
| Upper `G02` | 1.35 – 7.05 | 3.18 – roof−0.18 | JSON L37–38; L173–174 |
| Mullions Y | 0.15, 2.175, 4.2, 6.225, 8.25 | full height | JSON L39–44 |

### 2.3 Sightline wedge (computed + inference)

**Fact (central ray at gable plane x=14.012 m):** parameter s=(21.5−14.012)/(21.5−8.5)=0.577 → **y≈−2.79 m, z=1.25 m** (below glass y_min); principal axis does **not** pierce glazed area.

**Fact (35 mm HFOV ≈ 54°, half-angle at gable Δx≈7.5 m):** frustum y at gable ≈ **[−6.6, +1.0] m**; z ≈ **[−1.2, +3.7] m** (sensor height 24 mm assumed, Blender default).

**Inference:** Intersection with lower glass at z≈1.25 m gives y≈**[0.15, 1.0] m** (south strip only) — insufficient alone for dining at y=6.35. **`shift_y=0.105`** and full 3D wedge through **upper pane** + depth into room bring **fireplace (11.3, 3.2)**, **sofa band (y~1–2)**, **dining (12.55, 6.35)**, **pendant (z=3.0)** into frame — consistent with reference and `after_C1.png`.

**Objects in C1 readability wedge (proposal aligned to target + image):**

| Priority | Object(s) | Approx position | Reference role |
|---|---|---|---|
| P1 | Fireplace stack + hearth | (11.3, 3.2) | left-center glass |
| P1 | Sofa group | (10.8, 1.35) | fore portico side |
| P2 | Coffee table | (10.0, 2.7) | mid |
| P2 | Dining table + chairs | (12.55, 6.35) | upper glass / deep |
| P2 | `PENDANT_ring_proxy` | (12.55, 6.35, 3.0) | halo |
| P3 | Kitchen run | (10.9, 7.75) | edge / rear |
| P3 | Timber lining / floor | surfaces | tone read |

**Blender verify:** mesh ray cast from C1 through G01/G02 mullion solids → per-pixel depth list.

### 2.4 Proposed interior review cameras (owned, C1 untouched)

| Id | Location (m) | Target (m) | Lens (mm) | Purpose |
|---|---|---|---|---|
| `CAM_V10_HEARTH` | (11.0, 2.8, 1.65) | (11.3, 3.2, 1.1) | 32 | fireplace, sofa, coffee |
| `CAM_V10_GABLE_IN` | (13.2, 4.2, 1.65) | (10.5, 2.5, 1.1) | 28 | reverse: room → valley through glass |
| `CAM_V10_DINING` | (11.8, 5.8, 1.65) | (12.55, 6.35, 0.95) | 35 | table, pendant, kitchen |
| `CAM_V10_SEAT` | (10.6, 1.6, 1.05) | (11.3, 3.0, 0.9) | 40 | seated living |

Collection: `80_CAMERAS`; names prefixed `V10_`; hide render by default except when selected.

---

## 3. Design concept — room 07

### 3.1 Zoning (open plan, one roof)

| Zone | XY anchor (m) | Function |
|---|---|---|
| Living | x 9.2–11.8, y 0.8–3.8 | sofa, coffee, hearth |
| Dining | x 11.8–13.4, y 5.2–7.2 | table 6 places |
| Kitchen | x 9.0–13.2, y 7.0–8.0 | run + worktop (W04 above) |

Clearances: **≥0.85 m** circulation to D04 zone (not furnishing 01–06); **≥1.0 m** between sofa front and coffee table.

### 3.2 Furniture list (metres, replace proxies; hide originals)

| Piece | Proposed center | Size (L×D×H) | Notes |
|---|---|---|---|
| Sofa 3-seat + chaise | (10.7, 1.5, F) | 2.8×1.05×0.82 | faces fireplace |
| Coffee table | (10.0, 2.65, F) | 1.2×0.65×0.40 | wood top, metal legs |
| Dining table | (12.5, 6.35, F) | 2.0×0.95×0.76 | aligns proxy |
| Chairs ×6 | existing grid ±0.05 | 0.45×0.48×0.88 | procedural |
| Kitchen base | (10.9, 7.55, F) | 3.6×0.60×0.92 | fronts W04 wall |
| Worktop | (10.9, 7.48, F+.92) | 3.7×0.65×0.04 | stone top |
| Hearth / mantle | (11.3, 3.2, F) | 0.9×0.35×1.35 | stone + firebox |
| Ring pendant | (12.55, 6.35, 2.85) | Ø1.1 ring | emissive + metal |
| Table lamp (optional) | (10.2, 2.9, F+.55) | 0.15×0.15×0.45 | sofa side |

### 3.3 Surfaces

| Surface | Treatment | Notes |
|---|---|---|
| Floor | warm oak boards, MAT_FLOOR PBR | UV metric 1.2 m planks |
| Walls (inner) | horizontal timber to 2.4 m + plaster above OR full-height timber on fireplace wall | owned `V10_MAT_WALL_*` |
| Roof underside | dark stained boards following soffit | matches reference soffit |
| Gable lining | vertical boards between timbers | link to exterior `GABLE_timber` |
| Fireplace | light limestone + dark firebox | reuse `MAT_STONE` maps |
| Kitchen | matte fronts + stone worktop | dark slim handles |

### 3.4 Lighting mood

| Light | Type | Intent |
|---|---|---|
| `V10_FIRE` | area + emissive logs | hearth read through glass |
| `V10_PENDANT` | mesh ring 2700 K | dining focal |
| `V10_LINEAR` | area strips at wall plate | reference eave warmth echo |
| `V10_LAMP` | point 40 W equiv | sofa corner |
| Keep | `SUN_key`, `FILL_front`, world Nishita | `build_scene.py` L322–327 |
| Retire visibility | proxy `DINING_downlight` | supersede with owned rig |

Exterior LED beams on fascia remain unchanged.

---

## 4. Asset route

**Network:** not used this session — identifiers below are **proposed**; **Step 0 preflight** = read-only catalogue lookup + manifest draft before download grant.

| Element | Primary CC0 | Licence | Res | Real size | ~DL | Fallback procedural |
|---|---|---|---|---|---|---|
| Floor oak | Poly Haven `wood_floor` or AmbientCG `WoodFloor051` | CC0 | 1K–2K | 2×2 m tile | ~3×2 MB | `build_scene` noise wood |
| Wall timber | PH `laminate_floor_02` / `brown_planks_03` | CC0 | 2K | 1×1 m | ~8 MB | MAT_WOOD_H procedural |
| Stone hearth | PH `granite_01` or `concrete_floor_02` | CC0 | 2K | 2×2 m | ~6 MB | `MAT_STONE` |
| Fabric sofa | PH none ideal → AmbientCG fabric or procedural | CC0 | 1K | — | TBD | cube + noise |
| Metal black | PH `metal_plate` | CC0 | 1K | 1×1 m | ~2 MB | MAT_FRAME |
| Pendant | **procedural** torus + emission | — | — | Ø1.1 m | 0 | keep topology from L270 |

**Manifest pattern:** `assets/ASSET_MANIFEST.md` + JSON section in **`model/interior_v10.json`** (not `parameters.json` during V09).

---

## 5. Technical route and V09 coexistence

### 5.1 Parameters while V09 contends

| Store | Path | Owner |
|---|---|---|
| Frozen envelope | `work/v09/baseline/model/parameters.json` | witness |
| Interior draft | **`model/interior_v10.json`** | V10 whole |
| Integration | append `interior_v10` section later | post-V09 grant |

### 5.2 Study scene input

**Recommended:** CLI `build_scene.py --output work/v10/study/interior_study.blend` **only after** grant adds hook skip flag OR dedicated `scripts/build_interior_study.py` importing envelope+interior block from `build_scene.py` (lines 1–274) **without** v03–v08 imports (L349–379).

**Why geometrically identical to cottage core in v08_view:** same seven JSON sections + same `build_scene` envelope/interior/proxy code path; no vegetation modules → cottage-only shell matches protected interior coordinates (witness diff hashes of envelope objects).

### 5.3 Module API (pattern `vegetation_v08.py` L677–698)

```text
apply_v10(scene, P_interior, ROOT, *, components=None) -> dict
```

- Seed **13710** (deterministic RNG restore assert).
- Collection **`55_INTERIOR_V10`** (new); subcollections `FURN`, `SURF`, `LIGHTS`.
- Materials **`V10_MAT_*`** only; do not mutate `MAT_WOOD_H` shared slots on exterior.
- Proxies: `hide_render=True`, `hide_viewport=True`, `V10_proxy_preserved` custom prop; **no delete**.
- Idempotence: second call counts unchanged; `scene['interior_v10_summary']` JSON.
- Components: `components={"surfaces"|"furniture"|"lights"|"all"}` for pilots.

### 5.4 Protected witness checks (post-implementation)

| Witness | Check |
|---|---|
| C1 matrix | `CAM_A_REFERENCE` location/target/lens/shift byte-equal baseline |
| Gable meshes | vertex count G01/G02 unchanged |
| Chimney JSON | (11.3, 3.2) unchanged |
| Partitions | 13 partition rects unchanged |
| Exterior collections | no new objects in `10_ENVELOPE`/`30_GLAZING` |

### 5.5 Integration (later grant)

**Preconditions:** V09 settled; `nature_study_v09` merge agreed; ≥12 GiB free for CPU render; no concurrent MCP on same blend.

1. Append `interior_v10` to `model/parameters.json`.  
2. Add `from interior_v10 import apply_v10` after `apply_v08` in `build_scene.py`.  
3. Replay to `blender/kysucka_chata_mcp_v10.blend` (new file; v08 preserved).  
4. Cold CLI reopen + `inspect_scene.py`.

---

## 6. Glass and C1 readability

| Option | Mechanism | Invasion |
|---|---|---|
| **A (recommended default)** | Owned duplicate materials `V10_MAT_GLASS_VIEW` on **interior-facing** glass duplicate faces or light-path override pass; roughness **0.02–0.04** for study + C1 A/B only | no change to exterior `MAT_GLASS` slot on G01/G02 |
| B | Global `MAT_GLASS` roughness 0.07→0.04 | **rejected** — affects all glazing |
| C | No glass change; judge from `CAM_V10_*` only | acceptable fallback |

**Evaluation:** C1 crop gable 600 px wide before/after + interior `CAM_V10_GABLE_IN`.

---

## 7. Resources, pilots, evidence

| Stage | Scene | RSS estimate | Render | Guard |
|---|---|---|---|---|
| Study open | cottage only + V10 | 1–3 GiB | none | OK while V09 runs |
| Pilot render | study | 3–5 GiB CPU | 800×600, 32 spp, OIDN | start if **≥12 GiB** available (V09 rule) |
| C1 evidence | full v10 (later) | 8–15 GiB | P0 1448×1086 96 CPU | serialize; one job at a time |

**Order:** (1) study build + idempotence, (2) `CAM_V10_HEARTH` + `CAM_V10_DINING` P0-low, (3) one full candidate, (4) ≤1 correction (glass or pendant).

**Evidence set:**

| Artifact | Path |
|---|---|
| Interior PNGs ×3 cameras | `work/v10/evidence/` |
| C1 crop before/after | `work/v10/evidence/c1_gable_crop_{before,after}.png` |
| JSON summary | `work/v10/evidence/interior_v10_summary.json` |
| SHA-256 manifest | `work/v10/evidence/sha256.txt` |
| Replay log | CLI stdout `INTERIOR_V10` + idempotence PASS |

**Stop rules:** RAM <12 GiB → no new CPU render; V09 GUI conflict → stop saves; witness fail → rollback to `work/v10/checkpoint_pre_v10.blend`.

**Recovery:** preserve `work/v06`/`v08` paths untouched; V10 checkpoints only under `work/v10/`.

---

## 8. Proposed implementation grant boundary

### 8.1 Allowlist (phase 1 — study, V09 active)

| Path | Action |
|---|---|
| `scripts/interior_v10.py` | create |
| `scripts/build_interior_study.py` | create (optional wrapper) |
| `model/interior_v10.json` | create |
| `work/v10/**` | checkpoints, evidence, downloads |
| `assets/textures/interior/**` | after preflight + download grant |
| Meta `00/10-interior-living-space/*` | Orchestrator trace |

### 8.2 Forbidden until integration grant

`model/parameters.json`, `scripts/build_scene.py`, `scripts/nature_study_v09.py`, `AGENTS.md`, `README_SK.md`, `docs/OPERATIONS.md`, `work/v09/**`, any `blender/kysucka_chata_mcp_v08*.blend` overwrite, Blender MCP/GUI, GPU renders, `git write`.

### 8.3 Commands

| Allowed | Forbidden |
|---|---|
| Background Blender **study only**, `--disable-autoexec`, single process | Live MCP, GUI blend shared with V09 |
| `sha256sum`, read-only git | `git add`, commit, push |
| CPU Cycles study renders serialized | OPTIX stress |

### 8.4 Cooperator decisions before grant (see table)

---

## 9. Follow-on wholes

| Order | Whole | Evidence needed |
|---|---|---|
| 1 | **V10 integration** into full scene + builder hook | witness PASS + C1 crop |
| 2 | Rooms **01–06** furnishing | plan slices per room rect |
| 3 | **Glass / optics** whole (global readability) | C1 A/B if option A insufficient |
| 4 | **Interior doors/hardware** D02–D06 | corridor views |
| 5 | **Bathroom/tech** 02–03 | out of scope V10 |

Rooms 01–06 inventory (names only): 01 Zádverie, 02 Technická, 03 Kúpeľňa, 04 Chodba, 05–06 Izby — no design in V10.

---

## Cooperator decisions

| # | Decision | Options | Recommended default | Consequence |
|---|---|---|---|---|
| D1 | Wall lining scope | A full-height timber fireplace wall only; B timber wainscot 2.4 m all walls | **A** | A faster, matches reference focal; B more work |
| D2 | Glass C1 pilot | A owned lower-roughness view pass; C interior cameras only | **A** | A enables C1 acceptance; C defers exterior read |
| D3 | Asset depth | A CC0 2K PBR floor/stone; B full procedural | **A** with procedural fallback | A needs preflight download grant |
| D4 | Pendant | A ring only; B ring + diffuser disc | **A** | matches reference halo |
| D5 | Kitchen extent | A wall run 3.6 m; B + island 1.2 m | **A** | B needs space check y>7 |
| D6 | Integration timing | A after V09 close; B parallel study only | **B now, A later** | respects concurrent V09 |
| D7 | Table lamp | include optional lamp | **Yes** | reference warmth near sofa |

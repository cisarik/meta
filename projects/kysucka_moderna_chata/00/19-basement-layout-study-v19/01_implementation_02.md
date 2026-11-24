# V19 implementation (01/03) — build Variant A interior basement study and deliver high-craft showcase renders and regression proofs

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-basement-layout-study-v19
Worker session ordinal: 01
Worker exchange ordinal: 03
Implementation authority: explicit
Native planning mode: not-used
Worker session target: current-worker-session
Worker session profile: Fresh Implementation Worker
Phase: implementation
Task identity: BASEMENT-LAYOUT-V19-IMPL — implement the Cooperator-selected Variant A interior basement and staircase study in `work/v19/kysucka_chata_interier_pivnica_v19.blend`, verify continuous passage, slab/envelope diff, cold portability, and fixed-camera regression, and deliver showcase architectural renders of the stair entry and B1 basement
Delivery route: manual Cooperator delivery
Continuity anchor: accepted terminal PASS planning report `projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/01_report_01.md` (SHA-256 `8f1f7f5766b591ad4ce24ecc3a9406773b6b9d61e21c3fd657cc46add44d04d5`) from Worker session 01 / exchange 02
Authority renewal: prior planning authority expired at `01_report_01.md`; this prompt completes the Plan-to-Execution Gate (`Native planning mode: not-used`) and grants explicit bounded implementation authority in the same healthy Worker session
Why current session: same healthy Worker session that authored the accepted Variant A plan and verified all scene coordinates, envelope hashes, and ray clearances; independence not required
Retained context: convenience, not authority
Evidence posture: non-independent
Re-gate: independently re-verify repository checkout, clean tracked working tree, AP pin, and all pinned input hashes before any write; stop on conflict with current repository evidence
Reasoning recommendation: High — named risks: exact bevel-preserving boolean/bmesh slab cut and metric UV/normal preservation on `BASE_slab_V19_STUDY`, continuous 3D walking-cylinder and simultaneous door/corridor clearance verification, zero light-bleed or geometry regression in fixed living-room/gallery/window cameras, and high-craft photorealistic Cycles interior lighting and detailing in B1 and the stair entry
Recommended context capacity: approximately 250k tokens
Independence required: no

Exact baseline: `f600c7a8e69a23a029559872652302ac299c2aea` on branch `main` at `/home/agile/Projects/kysucka_moderna_chata` (with standalone interior scene `blender/kysucka_chata_interier.blend` at SHA-256 `c607cb21fbdb289b49f05596004b403e7dd5f96a64e900ce42ed8485f6a30449`)
Changed-path allowlist:
- `/home/agile/Projects/kysucka_moderna_chata/work/v19/**`
- `/home/agile/meta/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/01_report_02.md`
- `/home/agile/meta/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/evidence/**`
- `/home/agile/meta/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/renders/**`
Implementation boundaries:
- Positive: create and populate `/home/agile/Projects/kysucka_moderna_chata/work/v19/**` (including deterministic build script `work/v19/build_basement_v19.py`, candidate scene `work/v19/kysucka_chata_interier_pivnica_v19.blend`, slab/envelope diff `work/v19/slab_envelope_diff.json`, walking/clearance proof `work/v19/walk_clearance_v19.json`, cold-portability proof `work/v19/cold_portability_v19.json`, updated SVGs, and renders), copy final SVGs/JSON receipts and PNG renders to `/home/agile/meta/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/{evidence,renders}/`, and write the terminal report to `/home/agile/meta/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/01_report_02.md`; use temporary `/tmp/opencode/v19_impl` for isolated config and cold-open sandbox verification (cleaned completely before finishing).
- Negative: do not modify `blender/kysucka_chata_interier.blend`, `blender/kysucka_chata_exterier.blend`, `work/v18/**`, or any tracked file in `/home/agile/Projects/kysucka_moderna_chata`; do not overwrite `00_handout.md`, `00_notes.md`, `01_planning_00.md`, `01_report_00.md`, `01_planning_01.md`, or `01_report_01.md` in Meta; do not call live MCP (`tools.blender.*` prohibited); do not touch or signal any running owner GUI Blender process; do not modify global `/home/agile/.config/blender/5.3/config/userpref.blend`; do not perform any Git stage, commit, or push in any repository.

## Cooperator decision and visual excellence mandate

Michal approved **Variant A (interior entry from the service zone)** from `01_report_01.md` and issued an explicit visual quality directive:
> *"Ano variant A suhlasim mas moju plnu doveru, konaj autonomne.. Clielom je ohurit, ukazat prekrasnu vizualizaciu, daj do toho maximum a nerob ziadne chyby"*

Therefore, your implementation must combine **strict geometric fidelity** to the accepted Variant A specification in `01_report_01.md` (§2 & §4) with **showcase architectural visualization craft** inside collection `56_BASEMENT_V19`, using the rich packed PBR materials and 3D assets already present inside `blender/kysucka_chata_interier.blend` (`c607cb21...`). Do not deliver a bare grey schematic box.

## Sources, identity, and repository gate

Working directory: `R = /home/agile/Projects/kysucka_moderna_chata`
Trace directory: `T = /home/agile/meta/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19`

Repository identity and baseline:
- Project checkout: standalone checkout at `R`, branch `main`, expected HEAD `f600c7a8e69a23a029559872652302ac299c2aea` (tracked working tree and index clean; `work/` is gitignored).
- Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `.ap` (gitlink = submodule HEAD).
- Meta repository: `/home/agile/meta`, branch `main`, HEAD `cffbe078c285f2b47a1062531fe6a2119bcb8b43` (or later Cooperator Meta archival commit on `main`; untracked trace files under `projects/kysucka_moderna_chata/00/**` are expected and permitted).

Verified immutable input hashes (must match before and after your run):
- `blender/kysucka_chata_interier.blend`: `c607cb21fbdb289b49f05596004b403e7dd5f96a64e900ce42ed8485f6a30449`
- `work/v18/recovery/kysucka_chata_exterier_doladeny.blend`: `5e8ada70e99c70a3be0a7eea9b18306b422e4ef3a141a63b51b237b7957e3a24`
- `model/shared_envelope_v18.json`: `e58959a22b2d1879828fe87cff645ec3f7ed99a28ec12ae66bfce01c4f6045b8` (289-object `aggregate_sha256`: `8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50`)
- `work/v18/stage1/basement.json`: `4f2a87459c4ffffd8c80acdd80159f3a1b351271e6ef19a7b3f6550ec0c81a2a`
- `work/v18/stage1/basement_plan.svg`: `62bba44d676415cebd8e4669b58f09b0087ed37df5a411e62e8578c6f1169f93`
- `work/v18/stage1/cross_sections.csv`: `28940be9935bd08ad897777291c6437ba432590683cd5a59a9bcb6364f591bb4`
- `work/v18/stage1/cross_sections.svg`: `49b1d04d9f977148da1019302c0ca0d4b7ac4601a2a8de8d737f521ab946d4f7`
- Isolated MCP-disabled preferences `work/v12/profile_03/isolated_config/userpref.blend`: `d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561`
- Current global `/home/agile/.config/blender/5.3/config/userpref.blend`: `ae7a8626c3f41081ac7dde07f2ddcf2ab7d09c807a16ae2bdd5f6d233f88a9c0` (record before probe and confirm unchanged after probe; leave any running owner GUI Blender process such as `PID 25973` completely untouched).

Mandatory reading:
- Governing WORKER spine: `.ap/AP.md` Semantic Authority + WORKER row, RF-03/RF-06/RF-12/RF-18, §8, §18; `.ap/AP_WORKER.md` Worker Session Target and Reporting; `.ap/PROMPT_CONTRACTS.md` Worker Report Header, Implementation Authority Record, Plan-to-Execution Gate, Worker Exchange Identity, Mutation Axes Record, Cooperator Delivery and Trace Destination Record.
- Project `AGENTS.md`, `docs/OPERATIONS.md`, `model/shared_envelope_v18.json`, `T/00_handout.md`, `T/00_notes.md`, and `T/01_report_01.md`.

## Technical & visual specification for Variant A (`work/v19/kysucka_chata_interier_pivnica_v19.blend`)

Write a clean, deterministic, idempotent builder script `work/v19/build_basement_v19.py` and run it in isolated headless Blender 5.3.0 (`/home/agile/Applications/Blender/blender --background --factory-startup --disable-autoexec --threads 4` with `nice -n 10` and isolated environment in `/tmp/opencode/v19_impl`) to produce `work/v19/kysucka_chata_interier_pivnica_v19.blend` from `blender/kysucka_chata_interier.blend`:

### 1. Collection ownership, labeled study derivatives, and exact diff (`work/v19/slab_envelope_diff.json`)

- Retain `56_BASEMENT_V18` and embedded text `V18 | Podklad pre pivnicu` untouched.
- Create collection **`56_BASEMENT_V19`** linked to the scene root to own all new V19 basement study objects, lights, cameras, and labeled study copies.
- **Preservation of original `BASE_slab`, `V10_FLOOR_oak`, `V11_TERRAIN_NEAR`, and service partitions:**
  - Do not destructively overwrite the mesh data of `BASE_slab`, `V10_FLOOR_oak`, `V11_TERRAIN_NEAR`, or the modified `PARTITION_proposed*` objects. Keep the original objects in their original collections with 100% unchanged mesh data and transforms, set `hide_viewport = True` and `hide_render = True` on the superseded originals (recording them in a custom scene property `v19_hide_registry` for full reversibility), and place the labeled active study copies inside `56_BASEMENT_V19`:
    - `BASE_slab_V19_STUDY`: derived from the evaluated `BASE_slab` mesh **after** its bevel/weighted-normal modifiers so that the exterior 25 mm bevel, exterior face coordinates (`X=0, X=14.40, Y=0, Y=8.40`), normals, UVs, and `MAT_CONCRETE` material remain 100% identical to the original evaluated `BASE_slab`, while cutting only the internal stairwell opening **`X = 3.830..7.100 m`, `Y = 2.480..3.340 m`, `Z = +0.200..+0.450 m`** (`3.270 × 0.860 m = 2.8122 m²`).
    - `V10_FLOOR_oak_V19_STUDY`: derived from `V10_FLOOR_oak` (`Z = +0.451 m`, `V10_MAT_OAK_FLOOR`) with the matching internal cutout `X = 3.830..7.100 m, Y = 2.480..3.340 m` and planar UV continuity on all remaining floor faces.
    - `V11_TERRAIN_NEAR_V19_STUDY`: derived from `V11_TERRAIN_NEAR` by clipping/depressing only the internal sub-slab footprint `X = 2.700..7.400 m, Y = 2.480..5.700 m` (so the flat terrain sheet at `Z = -0.055 m` does not slice through the stairwell and B1 basement room), while keeping 100% of vertices, triangles, normals, UVs, and `MAT_V18_VALLEY_TERRAIN_4K` material bindings outside `X = 2.700..7.400, Y = 2.480..5.700 m` (including the south sub-slab terrain strip `Y = 0.000..2.480 m`) identical.
- Write **`work/v19/slab_envelope_diff.json`** (and copy to `T/evidence/slab_envelope_diff.json`) containing:
  - Verification that all 289 original objects in `model/shared_envelope_v18.json` (with `BASE_slab` evaluated from its preserved original mesh/object) still hash to `8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50` (`0` mismatches across all 289 objects);
  - Exact vertex/triangle/bounds/UV/normal diff between evaluated original `BASE_slab` (`56` vertices, `108` triangles), `V10_FLOOR_oak` (`4` vertices, `2` triangles), and `V11_TERRAIN_NEAR` vs their `*_V19_STUDY` copies, proving zero exterior perimeter vertex/normal change;
  - Re-verification of the bevel-aware exterior shadow-gap sightline test from `Záber 03`, `Záber 04`, and `Záber 05` confirming that no ray entering the `0.255 m` gap sees any V19 cut or sub-slab wall (`Y ≥ 2.480 m > 2.460 m`).

### 2. Ground-floor service-zone repartitioning, pocket door, and staircase (`56_BASEMENT_V19`)

Implement the exact Variant A ground-floor layout from `01_report_01.md` §2:
- **Top landing & vestibule connection:**
  - Top landing `X = 7.160..8.260 m`, `Y = 2.450..3.350 m`, `Z = +0.451 m` (`1.100 × 0.900 m`), accessed directly from `04 Chodba` (`Y = 3.350..4.500 m`) and `01 Zádverie` through the preserved `1.100 m` corridor opening (`X = 7.100..8.200 m`).
- **Top sliding pocket door (`V19_DOOR_TOP_POCKET`):**
  - Threshold at `X = 7.100 m`, `Z = +0.451 m`, clear opening `Y = 2.530..3.320 m` (`0.790 m` wide × `2.180 m` high, lintel `Z = +2.631 m`).
  - Model an architectural oak-and-black-steel pocket door leaf (`30 mm` thick, `V10_MAT_OAK` panel with recessed vertical grooves, `V10_MAT_STEEL_BLACK` edge trim and flush pull handle, overhead track at `X = 7.080 m`) and pocket wall cavity (`X = 7.040..7.100 m`, `Y = 1.510..2.480 m`).
  - Place the active visible door leaf in its **open/parked position** (`Y = 1.550..2.420 m`, or store a shape key / custom property / hidden closed-pose witness mesh `V19_DOOR_TOP_CLOSED_WITNESS` at `Y = 2.470..3.340 m`) so that the showcase entry camera `CAM_V19_STAIR_ENTRY` looks directly from the top landing down the illuminated oak staircase, while your clearance script tests the full translation sweep `Y = 1.550..3.340 m`.
- **Service-zone partitions and compact bath/utility fixtures:**
  - Replace only the affected southern corridor / service partitions (`PARTITION_proposed`, `PARTITION_proposed.001`, `.002`, `.003`, `.004`) with clean `56_BASEMENT_V19` plaster/timber study walls (`V10_MAT_PLASTER`) forming:
    - Stair shaft walls: north separator `X = 3.830..7.100 m, Y = 3.340..3.350 m` (rising from B1 up to `+3.050 m` with a clean oak/steel floor-opening trim collar), south shaft/pocket wall `X = 3.750..7.100 m, Y = 2.380..2.480 m`;
    - Western service access spur from `04 Chodba` (`X = 2.780..3.680 m` opening at `Y = 3.200..3.350 m` into the `1.050 m` spur `X = 2.700..3.750 m, Y = 1.580..3.350 m`) turning east along the `0.800 m` aisle `X = 3.750..5.150 m, Y = 1.580..2.380 m`;
    - Compact wet room `03 Kúpeľňa / WC` (`X = 2.700..5.150 m, Y = 0.300..1.500 m = 2.94 m²`) with double-pocket door opening `X = 3.470..4.370 m` at `Y = 1.500..1.580 m`, ceramic WC (`X = 2.700..3.300, Y = 0.770..1.140 m`), washbasin (`X = 3.820..4.120, Y = 0.300..0.580 m`), and flush glass/stone shower zone (`X = 4.300..5.150, Y = 0.300..1.500 m`);
    - Utility room `02 Technická miestnosť` (`X = 5.300..6.650 m, Y = 0.300..2.380 m = 2.81 m²`) with doorway `Y = 1.580..2.380 m` through `X = 5.150..5.300 m` and compact heat-pump/boiler cabinet (`X = 5.600..6.200, Y = 0.360..1.010 m`).
- **Architectural staircase (`V19_STAIR_*`):**
  - Straight flight descending west along centerline `Y = 2.925 m`, clear width `0.810 m` (`Y = 2.520..3.330 m`).
  - **14 risers** of `h = 2.701 / 14 = 0.192928571 m` and **13 treads** of `g = 0.240 m` (`2h + g = 0.625857 m`, pitch `38.8°`, total horizontal run `3.120 m` from `X = 7.100 m` down to the 14th riser at `X = 3.980 m, Z = -2.250 m`).
  - Craft the stair with high visual detail:
    - Thick solid oak treads (`42 mm` thickness, `255 mm` tread depth with `15 mm` rounded bullnose overhang and bevelled edges, using `V10_MAT_OAK` with proper metric UVs along the wood grain) and recessed dark oak/plaster risers;
    - Under-tread recessed warm linear LED diffuser strips (`V10_MAT_LED_WARM`) tucked beneath each tread nosing so every step casts a warm architectural glow onto the oak tread below;
    - Matte black steel side stringers (`V10_MAT_STEEL_BLACK`) along `Y = 2.480..2.520 m` and `Y = 3.330..3.340 m` and a continuous wall-mounted oak-and-black-steel handrail along the north wall (`Y = 3.300..3.335 m`, `0.900 m` above the stair pitch line, keeping the full `0.810 m` clear width below/beside the rail profile);
    - Treat the north stairwell wall descending into B1 as a featured natural Kysuce stone wall (`V10_MAT_STONE` with metric UVs) and the south stairwell wall in warm plaster (`V10_MAT_PLASTER`) with oak trim around the slab soffit transition.

### 3. B1 basement architecture, custom wine/pantry shelving, 3D props, and lighting (`56_BASEMENT_V19`)

Build the B1 level (`Z = -2.250 m` finished floor to `Z = +0.140 m` finished ceiling soffit, `2.390 m` clear height; structural floor slab `Z = -2.450..-2.250 m`, perimeter walls `0.200 m` thick within gross footprint `X = 2.700..7.400 m, Y = 2.280..5.700 m = 16.07 m²`):
- **Lower landing (`X = 2.900..3.980 m, Y = 2.480..3.460 m`, `1.080 × 0.980 m` at `Z = -2.250 m`) & B1 doorway:**
  - Dividing partition between the stairwell and the B1 storage cellar at `Y = 3.460..3.600 m` (`0.140 m` thick, oak-and-stone framed portal).
  - Rough opening `X = 2.920..3.940 m`, threshold at `Y = 3.600 m, Z = -2.250 m`, clear opening `X = 2.950..3.890 m` (`0.940 m` wide × `2.180 m` high, lintel `Z = -0.070 m`).
  - Glazed oak-and-black-steel cellar door (`V19_DOOR_B1_STORE`, vertical hinge at `(3.910, 3.600)`, leaf length `0.960 m` with clear glass center panel `V10_MAT_GLASS_CLEAR` framed in `V10_MAT_OAK` and `V10_MAT_STEEL_BLACK`), modeled **open at 90° (`+Y` into the store along `X = 3.910, Y = 3.600..4.560 m`)** so there is a continuous unobstructed view and walk path between the B1 store and the lower stair landing!
  - Under-stair enclosed volume (`X = 3.980..7.200 m, Y = 2.480..3.460 m`) finished cleanly with flush oak storage cabinet doors (`V10_MAT_OAK` + `V10_MAT_STEEL_BLACK` pulls) beneath the sloping stair soffit.
- **B1 main cellar & storage room (`X = 2.900..7.200 m, Y = 3.600..5.500 m`, `4.300 × 1.900 m = 8.17 m²`):**
  - **Floor:** large-format honed stone slabs (`V10_MAT_STONE_SLAB` with subtle bevelled tile joints at `0.60 × 0.60 m` grid and metric UVs) at `Z = -2.250 m`.
  - **Perimeter walls:** rich Kysuce stone masonry (`V10_MAT_STONE` with metric box/planar UVs) on the north (`Y = 5.500 m`), east (`X = 7.200 m`), and west (`X = 2.900 m`) walls, and warm lime plaster (`V10_MAT_PLASTER`) with oak wainscoting/trim on the south partition wall (`Y = 3.600 m`).
  - **Ceiling:** timber lining (`V10_MAT_TIMBER_LINING` at `Z = +0.140..+0.200 m`) with exposed rhythmic transverse oak ceiling beams (`V10_MAT_TIMBER_BEAM`, `0.12 × 0.14 m` every `0.85 m` along `X`, bottom at `Z = +0.040 m` outside the door swing / or flush coffers above `+0.140 m` so clear room height is `≥ 2.390 m` everywhere in the walk path) and warm hidden perimeter LED cove strips (`V10_MAT_LED_WARM`).
  - **Bespoke oak-and-steel cellar shelving, wine rack & pantry display (`X = 4.350..7.100 m, Y = 5.080..5.480 m` along the north wall, and an east end return `X = 6.750..7.180 m, Y = 3.750..5.080 m` — completely clear of the door swing `X = 2.950..3.910, Y = 3.600..4.560 m` and the `0.700 m` walking path):**
    - Frame in matte black steel (`V10_MAT_STEEL_BLACK`, `25 × 25 mm` uprights) with `35 mm` solid oak shelves (`V10_MAT_OAK`), a central diamond/horizontal oak wine-bottle rack section, lower slatted oak crate bays, and integrated warm under-shelf LED strips (`V10_MAT_LED_WARM`).
    - Populate the shelves richly with existing packed scene assets (linked/duplicated mesh data with varied transforms so file size stays compact) plus clean procedural bottles/jars:
      - Row of dark-glass wine bottles (`V10_MAT_GLASS_BLACK` / deep green-amber glass with foil caps and paper labels `V10_MAT_PAPER`) resting horizontally in the oak wine rack and standing on the oak tasting counter;
      - Wicker storage baskets (`V10_HEARTH_BASKET_00/01` mesh data) on the lower shelves;
      - Slatted oak storage crates filled with red/golden apples (instancing the packed `food_apple_01` mesh from `V04_ORCHARD`);
      - Ceramic vessels and stoneware jars (`V10_SHELF_VASE_A`, `V10_SHELF_VASE_B`, `V10_KITCHEN_VASE`), brass pots (`V10_KITCHEN_POT_00/01`), wooden bowls (`V10_DECOR_BOWL`), and wooden lanterns (`V10_HEARTH_LANTERN_00/01`) on the shelves and lower landing console.
- **Architectural lighting design (`56_BASEMENT_V19`) — warm, dramatic, zero light-bleed into living zone:**
  - Place warm 2700K–3000K Cycles `AREA` and `POINT` / `SPOT` lights inside `56_BASEMENT_V19`:
    1. Soft warm ceiling rectangular area lights along the B1 cellar centerline and shelf front (`Z ≈ +0.08 m`, warm color `(1.0, 0.86, 0.70)`), balanced with linear area lights behind the shelving and along the stone wall cove to bring out the 3D stone texture, oak grain, glass reflections, and ceramic/brass highlights;
    2. Stepped warm staircase lighting along the descent (`X = 7.0..3.5 m, Y = 2.925 m`) and over the lower landing (`X = 3.45, Y = 2.95, Z = -0.10 m`) so the view from B1 looking toward the doorway and stairs shows warm light cascading down the oak treads;
    3. A controlled top-landing soffit downlight (`X = 7.65, Y = 2.90, Z = +2.98 m`, directed downward into the top landing and upper stairs with narrow spread/baffle) so `CAM_V19_STAIR_ENTRY` is beautifully lit while zero stray light reaches the living room (`X > 8.80 m`).

### 4. Showcase cameras, updated SVG plans/section, walk-envelope proof, and fixed-camera regression suite

1. **Two V19 showcase camera renders (`1920 × 1080`, Cycles, 128 samples, OIDN Accurate/High, seed 0, AgX/None):**
   - **`CAM_V19_STAIR_ENTRY` (`záber nástupu`):** positioned at the vestibule/corridor entry to the top landing (start from the planned `(8.10, 3.18, 2.05)` → `(6.65, 2.925, 0.55)`, 22 mm, or fine-tune within the top landing / corridor mouth so the frame shows the oak floor transition, the open oak pocket door and frame, the stone & plaster stairwell, the black-steel/oak handrail, and at least 10–12 illuminated oak treads descending into the warm B1 landing below). Render to `work/v19/renders/zaber_nastupu_v19.png` and copy to `T/renders/zaber_nastupu_v19.png`.
   - **`CAM_V19_B1_CELLAR` (`záber z B1`):** positioned inside the B1 cellar (start from `(6.90, 5.00, -0.62)` → `(3.35, 3.62, -1.12)`, 22–24 mm, or fine-tune inside the east end of B1 around `(6.95, 4.45, -0.85)` aiming slightly west-northwest so the wide composition simultaneously showcases the stone walls, timber-beamed ceiling, honed stone floor, the illuminated oak-and-steel shelving stocked with wine bottles, baskets, apple crates, ceramics, and brass vessels on the right, AND the open glazed oak doorway at `Y = 3.600 m` revealing the lower landing and the warm lit oak staircase rising up to the ground floor on the left!). Render to `work/v19/renders/zaber_b1_pivnica_v19.png` and copy to `T/renders/zaber_b1_pivnica_v19.png`.
   - **Mandatory visual quality check:** After rendering both `1920 × 1080` PNGs, inspect their pixel luminance histograms and visually read back the actual PNG images. If either image is underexposed, overexposed, clipped by a wall/door, or visually flat, adjust the camera framing or light energies in `build_basement_v19.py`, re-save `kysucka_chata_interier_pivnica_v19.blend`, and re-render before running the final cold-open and regression suite.
2. **Updated scaled SVG drawings from the actual built 3D scene (`work/v19/` and `T/evidence/`):**
   - `podorys_prizemia_v19.svg` (updated Ground-Floor Plan showing the built Variant A stairs, pocket door, service spur, compact bath/utility fixtures, simultaneous corridor walk path, and camera markers `CAM_V19_STAIR_ENTRY`);
   - `podorys_b1_v19.svg` (updated B1 Plan showing the built B1 stone perimeter walls, lower landing, open B1 door, under-stair cabinets, north/east oak-and-steel wine/pantry shelving, continuous walk path, and camera marker `CAM_V19_B1_CELLAR`);
   - `rez_aa_v19.svg` (updated scaled Cross-Section A–A along `Y = 2.925 m` through the built 14-riser oak stair, `BASE_slab_V19_STUDY`, `+0.451 m` floor, `-0.055 m` terrain, `0.255 m` gap, `+0.140 m` B1 timber ceiling, `-2.250 m` B1 stone floor, `2.180 m` door lintels, and `2.197 m` head-reach lip clearance).
3. **Continuous 3D walking-passage and simultaneous corridor proof (`work/v19/walk_clearance_v19.json` and `T/evidence/walk_clearance_v19.json`):**
   - Programmatically sweep the `0.700 m` diameter × `2.100 m` tall upright walking cylinder (sampled at `≤ 0.05 m` steps) against all active evaluated scene triangles in `work/v19/kysucka_chata_interier_pivnica_v19.blend` along:
     - **Path 1 (Basement descent):** from ground-floor corridor `(7.650, 3.925, +0.451)` → top landing `(7.650, 2.925, +0.451)` → through the open top pocket door at `X = 7.100 m` → down all 14 stair risers along `Y = 2.925 m` to the last step (`X = 3.980 m, Z = -2.250 m`) → B1 lower landing `(3.450, 2.925, -2.250)` → north through the open B1 store door (`Y = 3.600 m`) → inside the B1 cellar along `Y = 4.350 m` to `X = 6.200 m`. Record minimum horizontal clearance, minimum vertical headroom at every riser/tread (including the `0.350 m` forward head-reach envelope at the `X = 3.830 m` slab lip: verify `≥ 2.197 m` to `+0.140 m` ceiling and `≥ 2.180 m` at both door lintels), and confirm zero mesh collisions.
     - **Path 2 (Simultaneous main corridor passage):** from `01 Zádverie` `(7.650, 1.500, +0.451)` through the `1.100 m` portal → `04 Chodba` (`Y = 3.925 m`) → east portal into `07 Obývačka` (`X = 10.250 m`) and into `05 Izba 1` and `06 Izba 2`, tested simultaneously with the top pocket door in its closed pose, open pose, and across its full travel sweep `Y = 1.550..3.340 m`.
     - **Path 3 (Service spur passage):** from `04 Chodba` through `X = 3.230 m` down the `1.050 m` spur and `0.800 m` aisle into `03 Kúpeľňa / WC` and `02 Technická miestnosť`.
4. **Fixed-camera comparison renders (`Záber 07`, `Záber 08`, `CAM_V10_ENTRY`, `CAM_V05_VALLEY_INSIDE`):**
   - Using identical render settings (`960 × 540` or `1920 × 1080`, Cycles, 96 samples, OIDN Accurate/High, seed 0, AgX/None, removing timeline marker camera-rebinding in the temporary render session when overriding the active camera at frame 181/211), render matched pairs from the untouched predecessor `blender/kysucka_chata_interier.blend` (`before_*`) and from `work/v19/kysucka_chata_interier_pivnica_v19.blend` (`after_*`) for:
     - `Záber 07 | Obývačka a krb` (frame 181 — living room and fireplace)
     - `Záber 08 | Jedáleň a galéria` (frame 211 — dining and gallery)
     - `CAM_V10_ENTRY` (frame 181 — view from corridor portal through living space and gable window)
     - `CAM_V05_VALLEY_INSIDE` (frame 181 — interior view through glazing to exterior valley)
   - Compute per-pair mean absolute RGB difference and maximum channel difference, and assemble a labeled side-by-side comparison contact sheet `work/v19/renders/porovnanie_fixnych_kamier_v19.png` (and copy to `T/renders/porovnanie_fixnych_kamier_v19.png`).
5. **Cold-open offline portability verification (`work/v19/cold_portability_v19.json` and `T/evidence/cold_portability_v19.json`):**
   - Test `work/v19/kysucka_chata_interier_pivnica_v19.blend` in a separate cold Blender process (copying the `.blend` alone into `/tmp/opencode/v19_impl/cold/` with `--factory-startup --disable-autoexec` and `bwrap --unshare-net` if available), verifying:
     - `0` external `bpy.data.libraries` and `0` linked IDs;
     - All packed images present and readable;
     - Saved startup frame `181` and active camera `Záber 07 | Obývačka a krb` preserved;
     - Collection `56_BASEMENT_V19`, `56_BASEMENT_V18`, text `V18 | Podklad pre pivnicu`, and all 289 shared-envelope records verified;
     - Re-running `build_basement_v19.py` on the saved candidate is idempotent (zero duplicate objects/materials/lights).

## Authority and mutation axes

Repository mutation: `/home/agile/Projects/kysucka_moderna_chata/work/v19/**` only (gitignored working directory; zero tracked repository file changes)
Host/remote mutation: bounded temporary `/tmp/opencode/v19_impl` directory for isolated headless Blender 5.3.0 config and cold-open verification only (must be removed completely before report; benign Python `__pycache__/*.pyc` interpreter cache permitted)
Trace persistence: direct-write `/home/agile/meta/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/01_report_02.md`, `/home/agile/meta/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/evidence/**`, and `/home/agile/meta/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/renders/**`

External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 19-basement-layout-study-v19
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_implementation_02.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19
Report filename: 01_report_02.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Evidence tier: E2
Evidence tier basis: reversible working-copy 3D interior/basement implementation with labeled slab/floor/terrain study derivatives, cold-open portability check, 3D walking-cylinder clearance proof, showcase renders, and fixed-camera regression comparison
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: V18 289-object shared-envelope verifier and bevel-aware shadow-gap ray test
Affected tests: 3D walking-cylinder & simultaneous corridor passability check, slab/floor/terrain derivative diff check, fixed-camera regression comparison (`Záber 07`, `Záber 08`, `CAM_V10_ENTRY`, `CAM_V05_VALLEY_INSIDE`), and cold-open offline portability test
New causal regression: `work/v19/build_basement_v19.py` embedded verification suite — proves continuous 0.70 × 2.10 m passage from ground floor to B1, zero exterior slab bevel/normal change, and idempotent rebuild
Broad or full suite: not-used
Runtime or testbed: isolated headless Blender 5.3.0 CLI (`/home/agile/Applications/Blender/blender --background --factory-startup --disable-autoexec`)
Independent acceptance: not-required

Stopping conditions: failed repository or pinned predecessor hash gate (`blender/kysucka_chata_interier.blend` must remain `c607cb21...`); modification of any tracked project file or predecessor `.blend`; tampering with owner GUI Blender (`PID 25973`); unresolved mesh collision along the walking path; exterior slab edge or bevel mutation; temporary `/tmp/opencode/v19_impl` cleanup failure.

Completion and report contract:
- First finalize all files under `work/v19/**` and copy the SVG drawings, JSON verification receipts (`slab_envelope_diff.json`, `walk_clearance_v19.json`, `cold_portability_v19.json`), and PNG renders (`zaber_nastupu_v19.png`, `zaber_b1_pivnica_v19.png`, `porovnanie_fixnych_kamier_v19.png`) into `T/evidence/` and `T/renders/`.
- Write the complete terminal report to `/home/agile/meta/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/01_report_02.md` (if and only if that file does not already exist) and read it back completely before your completion notice.
- Begin `01_report_02.md` on line 1 with `### Report for ORCHESTRATOR_CHAT`; echo the coordinates (`kysucka-moderna-chata-basement-layout-study-v19`, `01`, `03`) once; include the compact core (`Status: PASS | PARTIAL | BLOCKED`, `Phase-qualified result: implementation-PASS`, `Start commit` / `End commit`, complete table of created files with byte sizes, SHA-256 hashes, and PNG dimensions, slab/envelope diff summary, walking-clearance summary, fixed-camera comparison metrics, cold-open and resource metrics, Git result = no writes, deviations/risks, one smallest next step, `Report justification: new-mutation`, authority-expiry statement, `Orchestration critique` `MEASURED` / `LEAD`, `Resolved Execution Issues / Near-Misses`, and `Pre-Existing Failure Classification`). Set `Logical-whole closure: not-closed`.

Authority expiry: this terminal implementation report, cancellation, or supersession ends this grant; retained context is convenience, not continuing authority.

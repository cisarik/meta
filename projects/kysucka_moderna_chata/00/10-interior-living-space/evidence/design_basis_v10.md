# V10 interior — Orchestrator design basis

Author: ORCHESTRATOR, 2026-11-17. This is the Orchestrator's decision after
the single targeted plan revision (`02_report_00.md`). It replaces the
spatial parts of that plan and keeps its technical route. It is a
visualization design, not architectural or structural dimensioning. Values
are metres in model coordinates: X along the house toward the glazed gable,
Y from the entrance facade to the rear, Z up.

Every binding value is a parameter of `model/interior_v10.json`, so Michal
(COOPERATOR) can change it after seeing the layout pilot.

## 1. Source facts (verified in the repository)

| Fact | Value | Source |
|---|---|---|
| Floor / wall plate / ridge | +0.45 / +3.25 / +7.45 | `model/parameters.json::building` |
| Roof | `roof_z(y) = 7.45 − |y − 4.2|` | `scripts/design.py` L12–13 |
| Room 07 (inner faces) | x 8.8–14.1, y 0.3–8.1 | `rooms[6].rect` |
| Rooms 01–06 | x 2.7–8.65, y 0.3–8.1 | `rooms[0..5]` |
| Partition toward room 07 | x 8.65–8.8, y 0.3–3.35 and y 4.5–8.1; open at y 3.35–4.5 (corridor) | `partitions[10..11]` |
| Partition height | z 0.45–3.05 (centre F+1.3, height 2.6) | `scripts/build_scene.py` L267–268 |
| Chimney | axis (11.3, 3.2), 0.8 × 0.8, existing shaft starts at roof | `building.chimney`, L215–217 |
| Gable glass | plane x ≈ 14.41, lower pane y 0.15–8.25, z 0.45–3.18; transom at 3.18 | L170–179 |
| Front wall | core y 0–0.3 as long strips `WALL_front_j_k`; cladding boards `CLADDING_front_*` centred y = −0.018, 0.06 thick, 0.22 m courses | L122–153 |
| Front openings | D01 x 7.25–8.5; W01 x 4.15–6.15 | `openings` |
| Entry pier, sconce | x 8.78 (pier 8.54–9.02) | L231–234 |
| Bench | x 10.25–12.35, y −0.695…−0.045 | L235, L237 |
| Round ornament | centre (11.3, −0.10, 2.10), radius 0.42 | L236 |
| Kitchen window W04 | rear wall, x 10.4–12.2, z 1.55–2.65 | `openings` |
| C1 | (21.5, −10, 1.25) → (8.5, 2.5, 1.25), 35 mm | `camera` |

## 2. What was wrong in the revised plan

| Plan value | Finding |
|---|---|
| Gallery floor +2.70, slab underside +2.50 | Cuts the 3.05 m partitions and leaves rooms 01–06 a 2.05 m clear height. |
| "Usable band y 1.2–7.2 with ≥ 2.10 m" | At y 1.2 the clear height above +2.70 is 4.45 − 2.70 = 1.75 m. Arithmetic error. |
| Slab void over the corridor | Splits the gallery along the ridge, where headroom is best. No reason given. |
| Stair centreline x = 8.45 | That is inside room 01 (x 6.8–8.65), not room 07. The landing at +1.50 in the corridor opening blocks the only way into room 07. |
| Front glazing x 10.05–14.01 | Covers the bench and removes the ornament; the exterior reference shows a narrow glazed corner beside them. |
| "Fireplace still hidden from C1 after front glazing" | False. The ray to (11.3, 3.2) crosses the front wall at x = 13.77, inside any glazing that reaches the corner. |
| Hero camera 0.7 m from the firebox | Cannot show gable, fireplace and stair together. |

Kept from the plan: study scene from the preserved v03 scene; module
`scripts/interior_v10.py`, parameters in `model/interior_v10.json`, seed
13710, `V10_` naming, hidden originals tracked and never deleted, owned clear
glass duplicates, CPU-only serialized jobs, the three slices, the texture and
model identifiers of `polyhaven_catalogue_shortlist.md`.

## 3. Binding structure

### 3.1 Gallery

| Item | Value | Arithmetic |
|---|---|---|
| Slab | x 2.7–8.8, y 0.3–8.1, top **+3.25**, 0.20 thick | underside 3.05 = partition tops; top = wall plate |
| Rooms 01–06 clear height | 2.60 m | 3.05 − 0.45 |
| Edge toward room 07 | x = 8.8, visible edge beam about 0.12 × 0.30 | — |
| Clear height above gallery floor | `roof_z(y) − 0.20 − 3.25` | 0.20 = ceiling lining allowance |
| Standing band (≥ 2.0 m) | **y 2.2–6.2** | needs roof_z ≥ 5.45 → \|y − 4.2\| ≤ 2.0 |
| Low zones | y 0.3–2.2 and 6.2–8.1 | 0.1 m at the walls, 2.0 m at the band edge |
| Railing | along x = 8.8 for y 0.3–8.1 except the stair arrival y 3.35–4.40; 1.05 m high; dark steel posts about every 1.1 m, flat steel top rail, 5 horizontal cables | references |
| Furnishing | sparse: rug, one armchair or daybed, low shelf, plant, floor lamp, inside the standing band near the edge | visible from room 07 |

### 3.2 Stair (dog-leg in the north-west corner of room 07)

Total rise 3.25 − 0.45 = 2.80 m = **16 risers × 0.175 m**; going **0.27 m**
(2 × 0.175 + 0.27 = 0.62). Clear width 0.95 m per flight.

| Part | Footprint | Levels |
|---|---|---|
| Lower flight, walking toward +Y | x 9.80–10.75, y 6.02–7.10 | 5 risers, 4 goings (1.08 m); first riser at y 6.02; arrives at +1.325 |
| Half landing | x 8.80–10.75, y 7.10–8.10 | +1.325 |
| Upper flight, walking toward −Y | x 8.80–9.75, y 7.10–4.40 | 11 risers, 10 goings (2.70 m); arrives at +3.25 |
| Top platform | x 8.80–9.75, y 3.35–4.40, 0.20 thick | +3.25; underside 3.05, so the corridor opening keeps 2.60 m |

Checks done by the Orchestrator (repeat them in the scene):

- Headroom on the walking line (roof_z − 0.20 − tread level): lower flight
  ≥ 3.3 m, landing 3.03 m at y 7.1, 2.53 m at y 7.6, 2.12 m at y 8.0, upper
  flight ≥ 2.99 m.
- Under the upper flight the clear height falls from 2.48 m at y 4.5 to
  2.12 m at y 5.0 and 1.78 m at y 5.5. Treat x 8.8–9.75, y 5.3–7.1 as a
  non-walking zone and fill it (low cabinet, bench, plant or firewood).
- The foot is approached from the south: keep x 9.7–10.85, y 5.1–6.02 free.
- Arrival onto the gallery is in the middle of the standing band.

Build: closed or cut timber stringers, solid oak-look treads about 0.05 m
thick with a warm light strip under each nosing, the same steel and cable
railing on open sides (east side of both flights and landing, east and south
side of the top platform). Emission strips plus a few real lights, not one
lamp per tread.

### 3.3 Glazed front corner

| Item | Value |
|---|---|
| Opening | **x 12.75–14.25**, z 0.45–3.18, in the front wall |
| Frame | dark, same section family as the gable (about 0.075 wide); jamb at 12.75, corner post 14.25–14.40 meeting the gable mullion at y 0.15, sill and head rails; **no** intermediate mullion |
| Glass | one pane in the wall plane, owned clear glass |
| Unchanged | bench, ornament, entry pier, sconces, eave light, plinth, porch paving |

Handling of existing objects in the study scene: every `WALL_front_*` and
`CLADDING_front_*` object whose X range intersects 12.75–14.25 within z
0.45–3.25 is hidden and retained; an owned duplicate is trimmed to the
remaining parts so that materials and UVs stay identical. Record each
original in the hide registry.

C1 through this pane (x at the front wall = 21.5 + (px − 21.5)·10/(py + 10)):
at depth y 1.0 it shows x 11.9–13.5, at y 1.9 x 11.1–12.9, at y 3.2
x 9.95–11.9. So the south-east corner of the chimney breast, the coffee
table area and the east end of the seating are visible, as in the exterior
reference. Through the gable C1 keeps seeing the dining table, the kitchen,
the rear wall and now the stair landing (ray to (9.8, 7.6) crosses the gable
at y 0.68).

### 3.4 Fireplace (synthesis of both references)

| Part | Value |
|---|---|
| Chimney breast | stacked grey stone, plan x 10.65–11.95, y 2.75–3.65 (contains the 0.8 × 0.8 chimney), floor to roof lining |
| Firebox | black steel insert in the **south-east corner**, glass on the south face x 11.30–11.95 and the east face y 2.75–3.30, z 0.90–1.50; dark steel frame and a black steel band above it |
| Hearth bench | stone, top +0.87, along the east face x 11.95–12.60, y 2.75–3.65; open log store under it |
| Log niche | in the south face, x 10.75–11.20, z 0.90–2.05, 0.40 deep, stacked split logs, warm light strip |
| Fire | emissive flames and embers plus one warm light inside the firebox |
| C1 check | (11.8, 2.85) crosses the front wall at x 13.95 → inside the pane |

Alternative for Michal: a wider breast with a timber-slat TV wall
(panorama) or a free-standing black steel body (first image).

## 4. Zones and starting layout (not binding)

Positions are a starting point. The implementation adjusts them with a
collision check and a top view, and reports what it moved.

| Zone | Area | Content |
|---|---|---|
| Living | south, x 8.9–14.0, y 0.4–2.75 | corner sofa: 2.8 m run with its back to the front wall (about x 9.0–11.8, y 0.4–1.35) and a short return or pouf at the west end; low timber table about 1.1 × 0.6 between sofa and breast with ≥ 0.40 m on both sides; round woven rug Ø 2.4; armchair, side table and arc floor lamp in the glazed south-east corner (about x 12.3–13.6, y 0.7–2.2); plant |
| Dining | north-east, about x 11.3–13.5, y 4.5–6.3 | table 2.0 × 0.95 along X, six chairs, double ring pendant above |
| Kitchen | rear wall, x 10.85–14.0, y 7.45–8.1 | base run with worktop under W04, tall unit at the east or west end, wall units only where the roof allows |
| Stair corner | north-west | §3.2; filled under-stair zone |
| Walls | partition south part, front wall | framed pictures, shelf; closed door leaf not needed (corridor is an opening) |

Clear routes, each ≥ 0.80 m wide: corridor opening → living zone past the
west side of the breast; corridor opening → stair foot; corridor opening →
kitchen aisle; kitchen aisle along the whole run (≥ 1.0 m).

A TV is not placed by default (open decision). The work and music corner of
the panorama is left out: the room has no free wall for it once the stair
is in.

## 5. Surfaces, light, cameras

- Floor: oak planks along X. Partition and front wall inside: light plaster
  with timber panelling where it helps. Roof underside: boarded timber
  lining with exposed rafters about 0.08 × 0.18 every 0.9 m along X,
  straight, plus a ridge beam. Gallery underside: boards. Stone as §3.4.
  Slice 1 uses plain owned procedural materials in the right tones; CC0
  textures come in slice 2.
- Light: fire; warm strips on stair, log niche and under the gallery edge;
  ring pendant over the dining table; small spots between rafters; arc
  lamp. Existing `INTERIOR_warm` and `DINING_downlight` are hidden in the
  study scene and retained. Two looks from one parameter set: day and dusk.
- Cameras (all owned, C1 untouched):
  `CAM_V10_HERO` — from the north-east, about (13.4, 6.9, 1.55) toward
  (10.5, 2.6, 1.3), 18 mm: gable left, fireplace centre, stair right;
  `CAM_V10_SOFA` — seated in the living zone toward fire and gable;
  `CAM_V10_ENTRY` — standing in the corridor opening looking east;
  `CAM_V10_GALLERY` — from the gallery edge down into the room;
  `CAM_V10_PLAN` — orthographic top view with roof and gallery hidden;
  `CAM_V10_PANO` — equirectangular at about (11.9, 4.6, 1.6).

## 6. Open decisions for Michal (defaults already applied)

| # | Question | Default |
|---|---|---|
| D1 | Fireplace character | stone breast with black steel corner firebox |
| D2 | Front glazing width | narrow corner x 12.75–14.25, bench and ornament stay |
| D3 | TV | none |
| D4 | Work and music corner | none |
| D5 | Gallery use | sparse lounge furnishing |
| D6 | Clear glass on the gable in the full scene | decide at integration |

## Amendment 1 — finished floor level (2026-11-17, 21:06)

Found by Worker session 03 and confirmed in `scripts/build_scene.py` L120:
the proxy `FLOOR_interior` is 0.044 thick with its centre at F + 0.022, so
its top is at +0.494, while the declared floor datum
(`building.floor_z`, door sills, entry steps, lower edge of the gable
glass) is +0.45.

Decision: the datum **+0.45 stays** and every level in this file stays as
written. `FLOOR_interior` joins the proxies that give way: it is hidden and
retained, and an owned floor finish covers the same XY extent (the whole
interior, rooms 01–06 included) with its top between +0.450 and +0.455.
The stair rise is measured from the actual top of that owned finish, in 16
equal risers.

## Amendment 2 — after the layout pilot (2026-11-17, about 22:17; an earlier draft of this heading said 22:35, which was a wrong estimate)

Measured by Worker session 04 (`04_report_00.md`) and decided afterwards.

- **Cooperator decisions on the pilot images:** the layout stands; the
  fireplace keeps its built shape and receives real grey stacked stone; the
  glazed front corner stays x 12.75–14.25 with bench and ornament. The
  layout positions built in slice 1 (report 04/01, table "Layout positions
  changed") replace the starting values of §4.
- **Gallery standing band.** The roof shell underside is at roof_z − 0.17,
  so the lining sits at roof_z − 0.20 and the exposed rafters project
  0.113 m below it. Rafters stay. The band with ≥ 2.0 m under the rafters
  is **y 2.31–6.09**; that is the standing band from now on (§3.1 said
  y 2.2–6.2, which holds only between rafters).
- Accepted as built: finish top +0.451 and the resulting 1 mm offsets;
  front opening head inside the roof thickness; edge beam only south of
  the stair arrival; free stair-foot approach strip x 9.80–10.85.

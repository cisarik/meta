### Report for ORCHESTRATOR_CHAT

Logical whole identity: kysucka-moderna-chata-basement-layout-study-v19  
Worker session ordinal: 01  
Worker exchange ordinal: 02  
Persistent role identity: WORKER  
Worker session target: current-worker-session  
Native planning mode: required  
Worker session profile: Planner  
Phase: planning  
Task identity: BASEMENT-LAYOUT-V19-PLAN  
Status: PASS  
Phase-qualified result: not-applicable  
Start commit: `f600c7a8e69a23a029559872652302ac299c2aea`  
End commit: `f600c7a8e69a23a029559872652302ac299c2aea`  
Report justification: new-evidence  
Logical-whole closure: not-closed

# V19 basement access and layout study

**Recommend Variant A, with a straight stair descending west from the vestibule side of the service zone.** Its pocket door preserves the full **1.150 m** main corridor and the existing **1.100 m** vestibule portal. The study retains a **2.94 m²** wet room, a **2.81 m²** utility room and both existing bedrooms. The tradeoff is a **0.810 m** clear stair with a **0.790 m** door opening. Variant B offers a gentler **1.050 m** stair and preserves the ground-floor rooms in full. Its route from the front door is about **34.17 m** around the orchard and its west entry removes **1.20 m** of the visible slab edge.

## 1. Verified baseline and study assumptions

The isolated Blender 5.3.0 readback opened `blender/kysucka_chata_interier.blend` at frame 181 on `Záber 07 | Obývačka a krb`. It found 1,288 scene objects, 262 packed images and zero external Blender libraries. The 420,066,660-byte file matched SHA-256 `c607cb21fbdb289b49f05596004b403e7dd5f96a64e900ce42ed8485f6a30449`.

The canonical V18 verifier recomputed all **289 envelope records with zero mismatches** and aggregate SHA-256 `8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50`, matching the scene property and manifest. The linked `56_BASEMENT_V18` survey collection is empty and references `V18 | Podklad pre pivnicu`. The embedded JSON payload matched the local survey byte for byte. `BASE_slab`, `WALL_left_closed`, the wood-bay posts, rack and logs are in the envelope. `V10_FLOOR_oak`, `PORCH_paving`, the terrain and the internal partitions are outside that inventory. [V18 envelope manifest](/home/agile/Projects/kysucka_moderna_chata/model/shared_envelope_v18.json)

All coordinates below are in world metres, with `+X` east, `+Y` north and `+Z` up. Areas use unrounded dimensions.

| Existing element | Direct scene readback |
|---|---|
| `BASE_slab` | `X 0–14.400`, `Y 0–8.400`, `Z +0.200–+0.450`. Thickness **0.250 m**. Its evaluated 25 mm edge bevel leaves the flat west and north faces at `Z +0.225–+0.425`. |
| `V10_FLOOR_oak` | `X 2.460–14.400`, `Y 0–8.400`, `Z +0.451`. |
| `V11_TERRAIN_NEAR` | **−0.055 m** at all 36,192 V18 perimeter stations, with zero difference from the survey. The gap to the flat underside is **0.255 m**. The grade to interior finish difference is **0.506 m**. |
| `V10_GALLERY_slab` | `X 2.700–8.800`, `Y 0.300–8.100`, `Z +3.050–+3.250`. **2.599 m** clear over the corridor and its tested route to the living zone. |
| Wood bay and west wall | Bay `X 0–2.400`, `Y 0–8.400` at `+0.450`. `WALL_left_closed` occupies `X 2.400–2.700`, `Z +0.450–+3.250`. The west gable rises to `+7.450`. |
| Wood and posts | The 80 logs span `X 0.229476–2.120561`, `Y 0.220–0.920`, `Z +0.493017–+1.931958`. With the rack, the union is `X 0.229476–2.150`, `Y 0.050–1.050`, `Z +0.450–+1.931958`. The two posts occupy `X 0.030–0.210` and `2.190–2.370`, both `Y −0.020–0.180`. |
| Windows and entry | W01 assembly `X 4.150–6.150`, `Y −0.135–−0.035`, `Z +1.350–+2.500`. W02 and W03 span `X 3.450–4.850` and `6.550–7.950`. `D01_leaf` spans `X 7.250–8.500`, `Y −0.105–−0.015`, `Z +0.450–+2.750`. |
| Living-zone exclusions | Gallery stair `X 8.800–10.785`, `Y 3.350–8.100`, `Z +0.451–+4.300`. Cabinet `X 8.820–9.710`, `Y 5.300–7.080`, `Z +0.451–+1.898`. Fireplace `X 10.650–12.600`, `Y 2.750–3.650`, `Z +0.451–+6.700`. |

| Ground-floor zone | Clear `X` | Clear `Y` | Baseline access |
|---|---:|---:|---|
| 01 Zádverie | 6.800–8.650 | 0.300–3.200 | D01 and corridor opening `X 7.100–8.200` |
| 02 Technická miestnosť | 5.300–6.650 | 0.300–3.200 | Corridor opening `X 5.450–6.250` |
| 03 Kúpeľňa / WC | 2.700–5.150 | 0.300–3.200 | Corridor opening `X 4.100–5.000` |
| 04 Chodba | 2.700–8.650 | 3.350–4.500 | East portal through `X 8.650–8.800` |
| 05 Izba 1 | 2.700–5.650 | 4.650–8.100 | Corridor opening `X 4.400–5.300` |
| 06 Izba 2 | 5.800–8.650 | 4.650–8.100 | Corridor opening `X 6.650–7.550` |
| 07 Denná zóna | 8.800–14.100 | 0.300–8.100 | East portal from 04 |

The two proposals use B1 for occasional access to dry storage and shelving. Both assume a **−2.250 m** finished floor, a **+0.140 m** finished ceiling under the **+0.200 m** slab underside, and **2.390 m** clear standing height in the store. The visualization uses a 0.200 m floor assembly and 0.200 m perimeter walls, with a 0.300 m west passage wall in B. The walking witness uses a 0.700 m plan diameter and 2.100 m upright height. It follows the tread support elevations and separately checks the head’s reach up to 0.350 m ahead of the support point. These are visualization assumptions for Michal’s review. Structural, waterproofing and code design remain outside the study.

## 2. Variant A · Vstup zvnútra zo zázemia

### Access, levels and clearances

The existing 02 bay is **1.350 × 2.900 m**. A straight run needs **3.120 m** before landings. A U-stair needs at least two clear flight widths plus a divider, and an L-stair requires adjacent room space for its turn and approach. A trial L layout in the southwest service corner also put its excavation within direct sightlines from the low southern camera. The proposed straight stair uses the **combined north strip of the service rooms**, with its top landing reached from 04 through the existing 01 portal.

| Element | Variant A coordinates and geometry |
|---|---|
| Route to the stair | From 04 at `(7.650, 3.925, +0.451)`, go south to `(7.650, 2.925, +0.451)` and turn west. Clear top landing `X 7.160–8.260`, `Y 2.450–3.350`, `Z +0.451`, **1.100 × 0.900 m**. |
| Upper threshold and door | Threshold at `X 7.100`, `Z +0.451`. Clear opening `Y 2.530–3.320`, **0.790 × 2.180 m**, lintel `Z +2.631`. A 30 mm leaf on a track at `X 7.080` translates **−0.920 m along Y**. Closed leaf `Y 2.470–3.340`, parked `Y 1.550–2.420`. Pocket `X 7.040–7.100`, `Y 1.510–2.480`. The slider has no hinge or swing arc. Its complete sweep stays at `X ≤ 7.100`, `Y ≤ 3.340`. |
| Slab and oak opening | Rectangle `X 3.830–7.100`, `Y 2.480–3.340` through `BASE_slab` and `V10_FLOOR_oak`. **2.8122 m²**, with **0.70305 m³** nominal slab removal before edge details. The north separator fits in `Y 3.340–3.350`. |
| Flight | Descends west on centreline `Y 2.925`. Clear after rail and lining `Y 2.520–3.330`, **0.810 m**. **14 risers** of `2.701/14 = 0.192928571 m` and 13 goings of **0.240 m**. `2h + g = 0.625857 m`, pitch **38.8°**, run **3.120 m**. Riser `i` is at `X = 7.100 − (i−1) × 0.240`, with the following support at `Z = +0.451 − i × h`. One straight flight. |
| Last riser and standing zone | Last riser `X 3.980`, `Z −2.250`. Standing rectangle `X 2.900–3.980`, `Y 2.480–3.460`, **1.080 × 0.980 m**. Turn north at `X 3.450` to the store. |
| Store door | Threshold `Y 3.600`, `Z −2.250`, through a partition at `Y 3.460–3.600`. Rough opening `X 2.920–3.940`. Hinge `(3.910, 3.600)` with vertical axis, leaf 0.960 m long, swings **+Y** into the store. The open passage is `X 2.950–3.890`, **0.940 m**. Lintel **2.180 m** above the threshold. |
| B1 footprint and store | Gross `X 2.700–7.400`, `Y 2.280–5.700`, **16.07 m²**. Clear store `X 2.900–7.200`, `Y 3.600–5.500`, **4.300 × 1.900 m = 8.17 m²**. The space under the flight is outside the storage area. Shelf footprint `X 4.550–6.700`, `Y 5.100–5.500`. |

The controlling passage height is **2.180 m at both door lintels**. At the west slab lip `X 3.830`, the forward head reach can first engage the lip at a support position 0.350 m east, `X 4.180`. That lies on tread 13, whose top is **−2.057071 m**. Clearance there is **2.257 m** to the structural slab and **2.197 m** to the proposed B1 soffit. The floor immediately below the lip is the B1 landing, with **2.390 m** clear. The measured gallery underside supplies **2.599 m** above the top landing.

### Simultaneous passage and room function

The pocket door stays south of the corridor and west of the 01 portal throughout its travel. The whole `Y 3.350–4.500` band remains **1.150 m** wide. The path from 01 at `X 7.650` occupies `X 7.300–8.000` at the portal, inside `7.100–8.200` and at least **0.200 m** from the door sweep. In the main corridor its centre is `Y 3.925` and its sides are `Y 3.575–4.275`. Triangle clipping of the existing scene along that route found no hard geometry through the east portal to `X 10.250`, or at the branches to 05 and 06 centred on `X 4.850` and `7.100`.

Old direct mouths to 02 and 03 become the north side of the stair enclosure. Their new access branches west from 04 through `X 2.780–3.680` into the **1.050 m** spur at `X 2.700–3.750`. At `Y 1.980` the path turns east along the **0.800 m** aisle `Y 1.580–2.380`. The 0.700 m witness has 50 mm each side in that aisle. The new 03 portal spans `X 3.470–4.370` through `Y 1.500–1.580`. Two pocket leaves park left and right inside the wall. The 02 portal spans `Y 1.580–2.380` through `X 5.150–5.300`. The existing triangle check at the new spur and technical portal found exactly the intended internal partition blockers there.

| Zone | Before | After A | Loss | Function in the study |
|---|---:|---:|---:|---|
| 01 Zádverie | 5.37 m² | 5.07 m² | 0.30 m² | Original entry route and 1.100 m corridor portal. Loss covers the shaft strip and pocket footprint outside that strip. |
| 02 Technická miestnosť | 3.92 m² | 2.81 m² | 1.11 m² | `X 5.300–6.650`, `Y 0.300–2.380`. A 0.600 × 0.650 m appliance at `X 5.600–6.200`, `Y 0.360–1.010` leaves a 0.900 m deep standing zone in front. |
| 03 Kúpeľňa / WC | 7.11 m² | 2.94 m² | 4.17 m² | `X 2.700–5.150`, `Y 0.300–1.500`. WC at west, 0.300 × 0.280 m basin at `X 3.820–4.120`, `Y 0.300–0.580`, and flush **0.850 × 1.200 m** shower at `X 4.300–5.150`. A 0.700 m path fits from the new door to the wet room. |
| 04 Chodba | 6.84 m² | 6.84 m² | 0.00 m² | Full band and east portal. |
| 05 Izba 1 | 10.18 m² | 10.18 m² | 0.00 m² | Existing room and opening. |
| 06 Izba 2 | 9.83 m² | 9.83 m² | 0.00 m² | Existing room and opening. |

The fixtures are fit envelopes for a compact wet room and one utility appliance or stack. They make the room functions testable without assuming a specific appliance or plumbing layout. A has no physical overlap with W01, the gallery stair, the cabinet or the fireplace. The W01 assembly is south of `Y −0.035`, while the slab opening starts at `Y 2.480`.

### Visible plinth and envelope

A removes **0.00 m** of the exterior slab edge. The 288 other envelope objects have zero planned edits. The labelled slab derivative changes the internal surface around the opening while preserving the outside bevel, normals, UVs and material. The ground surface cut and all new geometry in the under-slab air gap are limited to `X 2.700–7.400`, `Y 2.480–5.700`. The south wall thickening at `Y 2.280–2.480` stays below grade and retains the terrain surface above it.

For the fixed north, west and low south cameras, a conservative ray entering the 0.255 m shadow gap at the top of the flat underside reaches the original grade before the proposed work. The reach includes a 25 mm inward allowance for the slab bevel.

| Direct sightline | Maximum reach from edge | First A intervention |
|---|---:|---:|
| `Záber 04`, north | 0.963 m | 2.700 m |
| `Záber 05`, west | 1.015 m | 2.700 m |
| `Záber 03`, south | 2.460 m | 2.480 m |
| `Záber 03`, east | 1.755 m | 7.000 m |

The same test clears the other V18 exterior marker cameras. This establishes **zero direct plinth, silhouette or facade-surface change** for A, including the open shadow band in the designated views. Appearance through the existing glass and indirect light are raster regression checks for the implementation exchange.

### Pôdorys prízemia — Variant A

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 536" role="img" font-family="sans-serif" font-size="14" fill="#223640">
  <title>Pôdorys prízemia · Variant A</title>
  <defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#a6432d"/></marker></defs>
  <rect width="800" height="536" fill="#fcfbf7"/>
  <text x="24" y="28" font-size="18" font-weight="700">Pôdorys prízemia · Variant A</text>
  <g transform="translate(56 447) scale(48 -48)" stroke="#223640" stroke-width=".022">
    <rect width="14.4" height="8.4" fill="#e7e4dc"/>
    <rect width="2.4" height="8.4" fill="#e4d9c6"/>
    <rect x="2.4" width=".3" height="8.4" fill="#9baab0"/>
    <path d="M0 -.65H6.7V0H0ZM6.7 -1.05H9.05V0H6.7Z" fill="#e7e4dc"/>
    <g fill="#f8f4ea">
      <rect x="6.8" y=".3" width="1.85" height="2.9"/>
      <rect x="5.3" y=".3" width="1.35" height="2.08"/>
      <rect x="2.7" y=".3" width="2.45" height="1.20"/>
      <rect x="2.7" y="4.65" width="2.95" height="3.45"/>
      <rect x="5.8" y="4.65" width="2.85" height="3.45"/>
      <rect x="8.8" y=".3" width="5.3" height="7.8"/>
    </g>
    <rect x="2.7" y="3.35" width="5.95" height="1.15" fill="#d1e4e0"/>
    <path d="M2.70 1.58H5.15V2.38H3.75V3.35H2.70Z" fill="#d1e4e0"/>
    <rect x="3.83" y="2.48" width="3.27" height=".86" fill="#e7b2a4" stroke="#a6432d"/>
    <rect x="7.16" y="2.45" width="1.10" height=".90" fill="#efdcc6"/>
    <path d="M3.75 2.38H7.10V2.48H3.75ZM3.83 3.34H7.10V3.35H3.83Z" fill="#9baab0"/>
    <path d="M2.78 3.35H3.68M7.10 3.20H8.20M7.10 3.35H8.20M4.40 4.50H5.30M4.40 4.65H5.30M6.65 4.50H7.55M6.65 4.65H7.55M8.65 3.35V4.50M8.80 3.35V4.50M3.47 1.50H4.37M5.15 1.58V2.38M5.30 1.58V2.38" stroke="#fcfbf7" stroke-width=".10"/>
    <path d="M7.25 -.06H8.50" stroke-width=".055"/>
    <path d="M4.15 -.06H6.15M3.45 8.46H4.85M6.55 8.46H7.95" stroke="#46949a" stroke-width=".075"/>
    <path d="M2.7 .77H3.3V1.14H2.7ZM3.82 .3H4.12V.58H3.82ZM5.60 .36H6.20V1.01H5.60Z" fill="#ded8c5"/>
    <rect x="4.30" y=".30" width=".85" height="1.20" fill="#d1e4e0"/>
    <path d="M8.8 3.35H10.785V8.1H8.8ZM10.65 2.75H12.60V3.65H10.65Z" fill="#50636a33" stroke-dasharray=".08 .07"/>
    <rect x="8.82" y="5.30" width=".89" height="1.78" fill="#50636a44"/>
    <path d="M7.10 2.48v.86m-.24 -.86v.86m-.24 -.86v.86m-.24 -.86v.86m-.24 -.86v.86m-.24 -.86v.86m-.24 -.86v.86m-.24 -.86v.86m-.24 -.86v.86m-.24 -.86v.86m-.24 -.86v.86m-.24 -.86v.86m-.24 -.86v.86m-.24 -.86v.86" stroke="#ba7665"/>
    <path d="M6.85 2.925H4.12M7.24 2.80V1.60" fill="none" stroke="#a6432d" stroke-width=".035" marker-end="url(#a)"/>
    <path d="M7.08 2.47V3.34" stroke="#a6432d" stroke-width=".045"/>
    <path d="M7.08 1.55V2.42" stroke="#a6432d" stroke-width=".045" stroke-dasharray=".07 .05"/>
    <path d="M7.65 2.87V3.925H10.25M7.65 3.925H3.23V1.98H5.66M3.92 1.98V.96M4.85 3.925V5.12M7.10 3.925V5.12" fill="none" stroke="#236c59" stroke-width=".065" stroke-linecap="round"/>
  </g>
  <text x="75" y="64">↑ Y · sever</text><text x="50" y="53" text-anchor="end">8,40</text><text x="50" y="290" text-anchor="end">3,35</text>
  <g text-anchor="middle" font-weight="700">
    <text x="432" y="368">01</text><text x="343" y="382">02</text><text x="242" y="399">03</text><text x="328" y="253">04</text>
    <text x="256" y="148">05</text><text x="403" y="148">06</text><text x="608" y="245">07</text>
  </g>
  <text x="56" y="469">0</text><text x="180" y="469">2,70</text><text x="470" y="469">8,80</text><text x="747" y="469" text-anchor="end">14,40 X</text>
  <text x="56" y="496">Zelená · súbežný priechod. Červená · otvor, zostup a pohyb posuvu.</text>
  <text x="56" y="520">Chodba Y = 3,350–4,500 m · čistá šírka 1,150 m</text>
  <path d="M652 490v10m0 -5h96m0 -5v10" fill="none" stroke="#223640"/><text x="652" y="520">0</text><text x="748" y="520" text-anchor="end">2 m</text>
</svg>
```

### Pôdorys B1 — Variant A

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 770 436" role="img" font-family="sans-serif" font-size="14" fill="#223640">
  <title>Pôdorys B1 · Variant A</title>
  <rect width="770" height="436" fill="#fcfbf7"/>
  <text x="24" y="28" font-size="18" font-weight="700">Pôdorys B1 · Variant A</text>
  <g transform="translate(-130 564) scale(86 -86)" stroke="#223640" stroke-width=".022">
    <rect x="2.70" y="2.28" width="4.70" height="3.42" fill="#9baab0"/>
    <rect x="2.90" y="2.48" width="4.30" height="3.02" fill="#f8f4ea"/>
    <rect x="2.90" y="3.60" width="4.30" height="1.90" fill="#d1e4e0"/>
    <rect x="4.55" y="5.10" width="2.15" height=".40" fill="#bad8d1"/>
    <rect x="2.90" y="2.48" width="1.08" height=".98" fill="#e1eee7"/>
    <rect x="3.98" y="2.48" width="3.22" height=".98" fill="#dccfc7"/>
    <rect x="3.83" y="2.48" width="3.27" height=".86" fill="#e7b2a4" stroke="#a6432d" stroke-dasharray=".08 .06"/>
    <path d="M4.22 2.48v.86M3.98 2.48v.86M6.72 2.925H3.72l.14 -.10m-.14 .10l.14 .10" fill="none" stroke="#a6432d" stroke-width=".035"/>
    <rect x="2.90" y="3.46" width="4.30" height=".14" fill="#9baab0"/>
    <rect x="2.92" y="3.46" width="1.02" height=".14" fill="#f8f4ea"/>
    <path d="M2.95 3.60A.96 .96 0 0 0 3.91 4.56M3.91 3.60V4.56M2.95 3.60H3.91" fill="none" stroke="#a6432d" stroke-width=".035"/>
    <path d="M4.04 2.925H3.45V4.58" fill="none" stroke="#236c59" stroke-width=".065"/>
  </g>
  <text x="112" y="52">X 2,70 → 7,40 m</text><text x="527" y="52">↑ Y · sever</text>
  <text x="300" y="128">Sklad 4,30 × 1,90 m · 8,17 m²</text><text x="300" y="150">Svetlá výška 2,390 m</text>
  <text x="376" y="303">Priemet schodiska</text>
  <text x="122" y="395">Podesta 1,08 × 0,98 m · −2,250 m</text>
  <path d="M514 386v10m0 -5h172m0 -5v10" fill="none" stroke="#223640"/><text x="514" y="413">0</text><text x="686" y="413" text-anchor="end">2 m</text>
</svg>
```

### Rez cez schody, dosku a terén — Variant A

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 470" role="img" font-family="sans-serif" font-size="14" fill="#223640">
  <title>Rez A–A · Schody, doska a terén · Y = 2,90 m</title>
  <defs><marker id="d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#a6432d"/></marker></defs>
  <rect width="800" height="470" fill="#fcfbf7"/>
  <text x="24" y="28" font-size="18" font-weight="700">Rez A–A · Schody, doska a terén · Y = 2,90 m</text>
  <g transform="translate(83 253) scale(64 -64)" stroke-width=".022">
    <path d="M-.7 -2.45H2.7V-.055H-.7ZM7.4 -2.45H9.95V-.055H7.4Z" fill="#ded8c5"/>
    <g fill="#9baab0" stroke="#223640">
      <rect x="2.70" y="-2.45" width="4.70" height=".20"/>
      <rect x="2.70" y="-2.25" width=".20" height="2.45"/>
      <rect x="7.20" y="-2.25" width=".20" height="2.45"/>
      <rect x="0" y=".20" width="3.83" height=".25"/><rect x="7.10" y=".20" width="2.85" height=".25"/>
      <rect x="2.90" y=".14" width=".93" height=".06"/>
      <rect x="2.70" y="3.05" width="6.10" height=".20"/>
    </g>
    <rect x="2.4" y=".45" width=".3" height="2.80" fill="#e7e4dc" stroke="#223640"/>
    <path d="M2.70 .451H3.83M7.10 .451H9.95" stroke="#223640"/>
    <path d="M-.7 -.055H2.70M7.4 -.055H9.95" stroke="#236c59"/>
    <path d="M2.70 -.055H7.40" stroke="#236c59" stroke-dasharray=".07 .06"/>
    <path d="M7.10 .451V.25807h-.24V.06514h-.24V-.12779h-.24V-.32071h-.24V-.51364h-.24V-.70657h-.24V-.89950h-.24V-1.09243h-.24V-1.28536h-.24V-1.47829h-.24V-1.67121h-.24V-1.86414h-.24V-2.05707h-.24V-2.250H2.90" fill="none" stroke="#a6432d" stroke-width=".042"/>
    <path d="M4.18 -2.05707H3.70M7.08 .451V2.631" stroke="#a6432d" stroke-dasharray=".07 .04"/>
    <path d="M3.70 .14V-2.05707M.80 -.055V.20" fill="none" stroke="#a6432d" marker-start="url(#d)" marker-end="url(#d)"/>
  </g>
  <text x="280" y="61">+3,050 · spodok galérie</text><text x="612" y="203">+0,451 · hotová podlaha</text>
  <text x="606" y="237">Doska +0,200 až +0,450</text><text x="59" y="276">Terén −0,055</text><text x="64" y="227">0,255 m</text>
  <text x="219" y="325" font-weight="700">2,197 m</text><text x="251" y="250">+0,140</text>
  <text x="257" y="418">−2,250 · podlaha B1</text><text x="522" y="123">Nadpražie +2,631</text><text x="272" y="447">Západ ← X → východ</text>
  <path d="M641 420v10m0 -5h128m0 -5v10" fill="none" stroke="#223640"/><text x="641" y="447">0</text><text x="769" y="447" text-anchor="end">2 m</text>
</svg>
```

## 3. Variant B · Vstup od západného prístrešku

### Approach, descent and foundation passage

The clear space beside the stack is **0.229 m west** and **0.250 m east**. The porch is only **0.650 m wide** at `+0.450 m`. North of the stack the free bay is **2.400 × 7.350 m**, or **17.64 m²**. The direct short grade bypass crosses the orchard’s lower crown. Triangle checks cleared the south and west detour outside the orchard. The final east leg meets only the slab at the proposed notch. The terrain rays in these corridors read **−0.055 m**.

| Element | Variant B coordinates and geometry |
|---|---|
| Existing approach | From D01 `(7.875, −0.060, +0.450)`, descend the existing `+0.450`, `+0.300`, `+0.150` entry steps and follow the `+0.110` pavers south. On `V05_PATH_slab_00` go west at `Y −6.100` from `X 7.875` to its west edge `X 6.825`. The step from the paver top to grade is **0.165 m**. The existing paving joints are approximately 0.050 m along the route. |
| Grade bypass | At `Z −0.055`, follow `(6.825, −6.100) → (−5.450, −6.100) → (−5.450, 1.850) → (0.805, 1.850) → (0.805, 2.450)`. Clear grade corridor **0.900 m** outside the bay. The total horizontal route from D01 is **34.17 m**. Day-to-day exterior access can join the same route directly at the pavers or grade. |
| Top landing and threshold | Grade landing `X 0–1.500`, `Y 1.250–2.450`, `Z −0.055`, entering from `X < 0`. Threshold `Y 2.450`, `X 0.280–1.330`, `Z −0.055`. The notch begins **0.200 m** north of the rack and **1.070 m** north of the posts. The lowest sampled roof underside over this landing gives **4.385 m** clear above grade. |
| Slab cuts and retaining | West notch `X 0–1.500`, `Y 1.250–2.450`. Flight cut `X 0.180–1.500`, `Y 2.450–6.050`. Combined **6.552 m²**, **1.638 m³** nominal slab removal. Retaining bands along the flight `X 0.180–0.280` and `1.330–1.500`, with clear faces and rail profiles kept outside the stated 1.050 m. West retaining wall continues to `Y 7.070`. Guard exposed deck edges, with a top at `Z +1.500` and an open grade entry at the notch. |
| Flight | Descends north on `X 0.805` with **1.050 m** clear width. **13 risers** of `2.195/13 = 0.168846154 m` and 12 goings of **0.285 m**. `2h + g = 0.622692 m`, pitch **30.6°**, run **3.420 m**. Riser `i` is at `Y = 2.450 + (i−1) × 0.285`, with support `Z = −0.055 − i × h`. |
| Arrival and standing | Last riser `Y 5.870`, `Z −2.250`. Standing rectangle `X 0.280–2.400`, `Y 5.870–7.070`, **2.120 × 1.200 m**. Turn east along `Y 6.450`. The sheltered deck east of the cut is **0.900 m** wide to `WALL_left_closed`. |
| Underground passage and door | New wall `X 2.400–2.700`, rough cut `Y 5.940–6.980`. Threshold `Z −2.250`, lintel `Z −0.070`, clear height **2.180 m**. Vertical hinge at `(2.700, 6.940)`, leaf 0.980 m, swings **+X** into B1. Open clear `Y 5.960–6.920`, **0.960 m**. The leaf clears the full exterior standing zone. The above-grade wall starts at `Z +0.450` and has zero overlap with the passage. |
| B1 footprint and store | Gross `X 2.400–6.200`, `Y 4.700–7.350`, **10.07 m²** under the cottage, plus the exterior arrival. Store `X 2.700–6.000`, `Y 4.900–7.150`, **3.300 × 2.250 m = 7.43 m²**. Put shelves against the south wall clear of the door arc. |

At the re-entry lip `Y 6.050`, a head reaching 0.350 m ahead can first encounter the slab from support at `Y 5.700`. That is tread 12 at **−2.081154 m**, giving **2.281 m** to the `+0.200 m` underside. The **2.180 m** basement door governs the new descent and entry. The archived front steps have a separate conservative **1.939 m** head-reach result at their existing roof overhang. B’s grade approach can join below that overhang. The bay stair itself stays inside `Y 1.250–7.070`, clear of both eaves, the wood and the posts. All rooms 01–07 retain their measured footprints and doors.

### Visible plinth and envelope

B changes the geometry of **one original envelope member**, `BASE_slab`. `WALL_left_closed`, the wood-bay posts, rack, logs and glazing have **zero edits**. `PORCH_paving` has **zero edits** as well. The new guard, notch returns and retaining faces are additions outside the 289-member register.

- **West, `Záber 05`.** The opening interrupts `X 0` from `Y 1.250–2.450`. It removes **1.200 m** of the **8.400 m** edge, leaving **7.200 m**. This is **0.300 m²** of nominal projected edge band, including the bevel regions, or **0.240 m²** of the existing flat vertical face. The west retaining face is recessed **0.180 m** behind the edge. It changes the background of the **0.255 m** gap over the next **3.600 m** of bay, a **0.918 m²** orthographic projected band.
- **North, `Záber 04`.** The north edge and its **0.255 m** shadow gap remain continuous across **14.400 m**. The north end of the above-deck guard is at `Y 6.050`, **2.350 m** behind that edge. Direct rays from the fixed north camera reach the proposed guard in the open bay. The angled view can also show the western return. The diagrams measure the orthographic bands and indicate the recessed elements. Raster coverage is for the selected-variant review.

### Pôdorys prízemia a prístrešku — Variant B

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 711" role="img" font-family="sans-serif" font-size="14" fill="#223640">
  <title>Pôdorys prízemia a prístrešku · Variant B</title>
  <rect width="860" height="711" fill="#fcfbf7"/>
  <text x="24" y="28" font-size="18" font-weight="700">Pôdorys prízemia a prístrešku · Variant B</text>
  <g transform="translate(251 392) scale(39 -39)" stroke="#223640" stroke-width=".022">
    <rect width="14.40" height="8.40" fill="#e7e4dc"/>
    <rect width="2.40" height="8.40" fill="#e4d9c6"/>
    <rect x="2.40" width=".30" height="8.40" fill="#9baab0"/>
    <path d="M0 -.65H6.70V0H0ZM6.70 -1.05H9.05V0H6.70Z" fill="#e7e4dc"/>
    <g fill="#f8f4ea">
      <rect x="6.80" y=".30" width="1.85" height="2.90"/><rect x="5.30" y=".30" width="1.35" height="2.90"/><rect x="2.70" y=".30" width="2.45" height="2.90"/>
      <rect x="2.70" y="4.65" width="2.95" height="3.45"/><rect x="5.80" y="4.65" width="2.85" height="3.45"/><rect x="8.80" y=".30" width="5.30" height="7.80"/>
    </g>
    <rect x="2.70" y="3.35" width="5.95" height="1.15" fill="#d1e4e0"/>
    <path d="M7.25 -.06H8.50" stroke-width=".06"/>
    <rect x=".229476" y=".05" width="1.920524" height="1" fill="#a88461"/>
    <path d="M.03 -.02H.21V.18H.03ZM2.19 -.02H2.37V.18H2.19Z" fill="#223640"/>
    <rect x="-.55" y="-.85" width="15.50" height="10.10" fill="none" stroke="#8d999d" stroke-dasharray=".10 .09"/>
    <rect x="-4.852" y="-5.515" width="6.226" height="5.817" fill="#b1c89e44" stroke="#72845f" stroke-dasharray=".10 .08"/>
    <ellipse cx="-1.739" cy="-2.6065" rx="3.113" ry="2.9085" fill="#91a97444" stroke="none"/>
    <rect x="0" y="1.25" width="1.50" height="1.20" fill="#e7cdc4" stroke="#a6432d"/>
    <rect x=".18" y="2.45" width="1.32" height="3.60" fill="#e7b2a4" stroke="#a6432d"/>
    <rect x="6.825" y="-6.375" width="2.10" height=".55" fill="#9baab0"/>
    <path d="M6.825 -1.05V-5.825M8.925 -1.05V-5.825" stroke="#82959d" stroke-dasharray=".10 .09"/>
    <path d="M.28 2.45h1.05m-1.05 .285h1.05m-1.05 .285h1.05m-1.05 .285h1.05m-1.05 .285h1.05m-1.05 .285h1.05m-1.05 .285h1.05m-1.05 .285h1.05m-1.05 .285h1.05m-1.05 .285h1.05m-1.05 .285h1.05m-1.05 .285h1.05m-1.05 .285h1.05" stroke="#ba7665"/>
    <path d="M.805 2.72V5.69l-.12 -.19m.12 .19l.12 -.19M2.70 5.96A.98 .98 0 0 1 3.68 6.94M2.70 6.94H3.68M2.70 5.96V6.94" fill="none" stroke="#a6432d" stroke-width=".04"/>
    <path d="M7.875 -.06V-6.10H-5.45V1.85H.805V2.45" fill="none" stroke="#236c59" stroke-width=".065"/>
  </g>
  <text x="275" y="55">↑ Y · sever</text><text x="251" y="416">X 0</text><text x="813" y="416" text-anchor="end">X 14,40</text>
  <g text-anchor="middle" font-weight="700">
    <text x="552" y="325">01</text><text x="484" y="325">02</text><text x="404" y="325">03</text><text x="472" y="240">04</text>
    <text x="414" y="146">05</text><text x="533" y="146">06</text><text x="698" y="230">07</text>
  </g>
  <text x="72" y="352">0,90 m po teréne</text><text x="133" y="501">Sad</text><text x="134" y="605">Obchádzka · Y = −6,10</text>
  <text x="362" y="129" fill="#a6432d">Dvere B1 · priemet</text><text x="37" y="672">Zelená · trasa od D01. Červená · otvor a zostup od −0,055 m.</text>
  <path d="M744 659v10m0 -5h78m0 -5v10" fill="none" stroke="#223640"/><text x="744" y="687">0</text><text x="822" y="687" text-anchor="end">2 m</text>
</svg>
```

### Pôdorys B1 — Variant B

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 755 480" role="img" font-family="sans-serif" font-size="14" fill="#223640">
  <title>Pôdorys B1 · Variant B</title>
  <rect width="755" height="480" fill="#fcfbf7"/>
  <text x="24" y="28" font-size="18" font-weight="700">Pôdorys B1 · Variant B</text>
  <g transform="translate(58 659) scale(82 -82)" stroke="#223640" stroke-width=".022">
    <rect x="2.40" y="4.70" width="3.80" height="2.65" fill="#9baab0"/>
    <rect x="2.70" y="4.90" width="3.30" height="2.25" fill="#d1e4e0"/>
    <rect x="3.26" y="4.90" width="2.58" height=".40" fill="#bad8d1"/>
    <rect x=".18" y="4.30" width="1.32" height="2.77" fill="#e7b2a4" stroke="#a6432d"/>
    <rect x=".28" y="5.87" width="2.12" height="1.20" fill="#e1eee7"/>
    <rect x="2.40" y="5.94" width=".30" height="1.04" fill="#f8f4ea"/>
    <path d="M.28 4.445H1.33M.28 4.73H1.33M.28 5.015H1.33M.28 5.30H1.33M.28 5.585H1.33M.28 5.87H1.33" stroke="#ba7665"/>
    <path d="M2.70 5.96A.98 .98 0 0 1 3.68 6.94M2.70 6.94H3.68M2.70 5.96V6.94" fill="none" stroke="#a6432d" stroke-width=".035"/>
    <path d="M.805 4.35V6.45H4.18" fill="none" stroke="#236c59" stroke-width=".065"/>
  </g>
  <text x="302" y="88">↑ Y · sever</text><text x="338" y="200">Sklad 3,30 × 2,25 m · 7,43 m²</text>
  <text x="338" y="223">Svetlá výška 2,390 m</text><text x="95" y="124">Výstup −2,250</text>
  <text x="82" y="258">Posledné stupne</text><text x="218" y="349">Podzemný prah X = 2,40–2,70 m</text>
  <text x="52" y="420">Podesta 2,12 × 1,20 m · trasa sa pri päte stáča na východ.</text>
  <path d="M535 411v10m0 -5h164m0 -5v10" fill="none" stroke="#223640"/><text x="535" y="442">0</text><text x="699" y="442" text-anchor="end">2 m</text>
</svg>
```

### Rez cez schody, dosku, prístrešok a terén — Variant B

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 815 655" role="img" font-family="sans-serif" font-size="14" fill="#223640">
  <title>Rez B–B · Schody, doska, prístrešok a terén · X = 0,805 m</title>
  <defs><marker id="d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="#a6432d"/></marker></defs>
  <rect width="815" height="655" fill="#fcfbf7"/>
  <text x="24" y="28" font-size="18" font-weight="700">Rez B–B · Schody, doska, prístrešok a terén · X = 0,805 m</text>
  <g transform="translate(98 445) scale(54 -54)" stroke-width=".022">
    <path d="M-.85 2.27L4.20 7.32L9.25 2.27L9.25 2.40L4.20 7.45L-.85 2.40Z" fill="#e7e4dc" stroke="#223640"/>
    <path d="M-.9 -2.45H1.25V-.055H-.9ZM7.07 -2.45H9.57V-.055H7.07Z" fill="#ded8c5"/>
    <g fill="#9baab0" stroke="#223640">
      <rect x="1.25" y="-2.45" width="5.82" height=".20"/>
      <rect x="0" y=".20" width="1.25" height=".25"/><rect x="6.05" y=".20" width="2.35" height=".25"/>
    </g>
    <rect x=".05" y=".45" width="1" height="1.482" fill="#be9c7b" stroke="#223640"/>
    <path d="M-.9 -.055H2.45M7.07 -.055H9.57" stroke="#236c59"/>
    <path d="M2.45 -.055H7.07" stroke="#236c59" stroke-dasharray=".08 .06"/>
    <path d="M2.45 -.055V-.22385h.285V-.39269h.285V-.56154h.285V-.73038h.285V-.89923h.285V-1.06808h.285V-1.23692h.285V-1.40577h.285V-1.57462h.285V-1.74346h.285V-1.91231h.285V-2.08115h.285V-2.250H7.07" fill="none" stroke="#a6432d" stroke-width=".042"/>
    <path d="M5.70 -2.08115H6.16" stroke="#a6432d" stroke-dasharray=".07 .04"/>
    <path d="M6.07 .20V-2.08115M8.06 -.055V.20" fill="none" stroke="#a6432d" marker-start="url(#d)" marker-end="url(#d)"/>
    <path d="M6.05 .45V1.50M1.25 .45V1.50" stroke="#a6432d" stroke-width=".035"/>
  </g>
  <text x="290" y="61">+7,450 · hrebeň</text><text x="49" y="309">+2,270</text><text x="599" y="309">+2,270 · odkvap</text>
  <text x="52" y="424">Doska +0,200 až +0,450</text><text x="46" y="474">Terén −0,055</text><text x="185" y="478">Nástup −0,055</text>
  <text x="550" y="451">0,255 m</text><text x="438" y="514" font-weight="700">2,281 m</text>
  <text x="249" y="583">−2,250 · podesta B1 → dvere na východ</text><text x="93" y="620">Juh ← Y → sever</text>
  <path d="M627 601v10m0 -5h108m0 -5v10" fill="none" stroke="#223640"/><text x="627" y="628">0</text><text x="735" y="628" text-anchor="end">2 m</text>
</svg>
```

### Západný a severný pohľad — Variant B

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 770 522" role="img" font-family="sans-serif" font-size="14" fill="#223640">
  <title>Západný pohľad · Variant B</title>
  <rect width="770" height="522" fill="#fcfbf7"/>
  <text x="24" y="28" font-size="18" font-weight="700">Západný pohľad · Variant B</text>
  <g transform="translate(633 452) scale(-55 -55)" stroke="#223640" stroke-width=".022">
    <path d="M-.85 2.27L4.20 7.32L9.25 2.27L9.25 2.40L4.20 7.45L-.85 2.40Z" fill="#e7e4dc"/>
    <path d="M0 .45H8.40V3.25L4.20 7.45L0 3.25Z" fill="#f8f4ea"/>
    <rect x="0" y="-.055" width="8.40" height=".255" fill="#e5e0d4" stroke="none"/>
    <rect x="0" y=".20" width="8.40" height=".25" fill="#9baab0"/>
    <rect x="1.25" y="-.055" width="1.20" height=".505" fill="#fcfbf7" stroke="#a6432d" stroke-dasharray=".07 .05"/>
    <rect x="2.45" y="-.055" width="3.60" height=".255" fill="#e7b2a4" stroke="#a6432d"/>
    <path d="M2.45 .45V1.50H6.05V.45M1.25 .45V1.50" fill="none" stroke="#a6432d" stroke-width=".035"/>
    <rect x=".05" y=".45" width="1" height="1.482" fill="#b29172"/>
    <path d="M-.30 -.055H8.75" stroke="#236c59"/>
  </g>
  <text x="114" y="474">Sever · Y8,40</text><text x="598" y="474">Y0 · juh</text>
  <text x="378" y="366" text-anchor="middle" fill="#a6432d">3,60 m · ustúpená stena</text>
  <text x="532" y="483" text-anchor="middle" fill="#a6432d">1,20 m</text>
  <text x="48" y="505">Prerušovaná · otvor v hrane. Plná · zmena pozadia medzery a zábradlie.</text>
  <path d="M629 73v10m0 -5h110m0 -5v10" fill="none" stroke="#223640"/><text x="629" y="101">0</text><text x="739" y="101" text-anchor="end">2 m</text>
</svg>
```

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 519" role="img" font-family="sans-serif" font-size="14" fill="#223640">
  <title>Severný pohľad · Variant B</title>
  <rect width="820" height="519" fill="#fcfbf7"/>
  <text x="24" y="28" font-size="18" font-weight="700">Severný pohľad · Variant B</text>
  <g transform="translate(741 448) scale(-45 -45)" stroke="#223640" stroke-width=".022">
    <rect x="-.55" y="2.27" width="15.50" height="5.18" fill="#e7e4dc"/>
    <rect x="2.40" y=".45" width="12" height="2.80" fill="#f8f4ea"/>
    <rect x="3.45" y="1.35" width="1.40" height="1.20" fill="#c0dadd"/>
    <rect x="6.55" y="1.35" width="1.40" height="1.20" fill="#c0dadd"/>
    <rect x="0" y="-.055" width="14.40" height=".255" fill="#e5e0d4" stroke="none"/>
    <rect x="0" y=".20" width="14.40" height=".25" fill="#9baab0"/>
    <path d="M.18 .45V1.50H1.50V.45" fill="none" stroke="#a6432d" stroke-width=".035" stroke-dasharray=".09 .06"/>
    <path d="M-.45 -.055H14.85" stroke="#236c59"/>
  </g>
  <text x="80" y="472">Východ · X14,40</text><text x="733" y="472" text-anchor="end">X0 · západ</text>
  <text x="650" y="360" fill="#a6432d" text-anchor="end">Zábradlie v hĺbke zálivu</text>
  <text x="69" y="504">Severná hrana dosky a medzera 0,255 m sú spojité po celej šírke.</text>
  <path d="M691 69v10m0 -5h90m0 -5v10" fill="none" stroke="#223640"/><text x="691" y="97">0</text><text x="781" y="97" text-anchor="end">2 m</text>
</svg>
```

## 4. Selection and implementation specification

| Decision criterion | A · Interior service zone | B · West wood bay |
|---|---|---|
| Top → B1 | `+0.451 → −2.250`, **2.701 m** descent | `−0.055 → −2.250`, **2.195 m** descent |
| Stair comfort | **14 × 193 mm**, 240 mm going, **38.8°** | **13 × 169 mm**, 285 mm going, **30.6°** |
| Clear flight / tightest new doorway | **0.810 / 0.790 m** | **1.050 / 0.960 m** |
| Lowest new headroom | **2.180 m** door lintels, **2.197 m** at finished lip witness | **2.180 m** door lintel, **2.281 m** at slab lip witness. Original front approach has separate **1.939 m** overhang witness. |
| Doors and walkability | Pocket leaf stays clear of the full 04 corridor and 01 portal. 05 and 06 entrances retain their positions. Service spur reaches 03 and 02. | No basement door in 04. Lower leaf swings into B1 and leaves the exterior standing zone free. |
| Ground-floor allocation | 01 loses **0.30 m²**, 02 **1.11 m²**, 03 **4.17 m²**. 04, 05 and 06 retain their areas. | **0.00 m²** interior loss. **6.552 m²** of wood-bay deck becomes entry and stair opening. |
| Storage | **8.17 m²**, height **2.390 m** | **7.43 m²**, height **2.390 m** |
| Weather, security and thermal separation | Indoor approach. Closed top slider and B1 door give two locations for visual separation from the heated rooms. | Exposed grade walk followed by roof cover. The lockable lower door is the weather and thermal boundary in the study. |
| Shared envelope | **2.8122 m²** internal cut, **0.00 m** exposed edge removal. Fixed exterior plinth sightlines clear. | West edge opens for **1.200 m**. Guard and recessed retaining wall enter the west view and are visible in the open bay from the north. |

A satisfies the handout preference for an interior entry with a comfortable main passage and functioning service rooms. The decision assumes occasional storage access, compact fixtures and carried items that fit the **0.790 m** clear threshold.

After Michal selects A and the Orchestrator issues `01_implementation_02.md` with Native planning mode `not-used` and explicit write authority:

1. **Derive one working copy.** Recheck the pinned interior, clean project baseline and destination. Save the candidate at `work/v19/kysucka_chata_interier_pivnica_v19.blend`, derived from the `c607cb21…` interior. Use `56_BASEMENT_V19` for the study stair, rails, doors, shell, floor, ceiling, trim, service fit envelopes, lights and review cameras. Retain the V18 survey collection and embedded text as readback evidence. Keep the original frame 181 and marker camera active in the saved candidate.
2. **Build the stated openings and paths.** Use independent active derivatives of `BASE_slab`, `V10_FLOOR_oak` and the locally clipped near terrain. Retain the original data and suppress the originals where their derivatives render. Cut the slab **after** the existing edge softening and weighted normals so the outside bevel stays identical. Reuse the oak material and derive cut-edge UVs from its existing planar mapping. Record exact added, removed and retained world vertices and triangles for each derivative, with UV, normal and material comparisons outside the cut. The base slab cage is 8 vertices and 12 triangles. Its evaluated reference is 56 vertices and 108 triangles. The oak reference is 4 vertices and 2 triangles.
3. **Repartition the service strip.** Use the rectangles in §2. Limit edits to the southern corridor wall around the new spur and shaft, and to the two service demising partitions that cross it. Use the new bath and technical portals and the upper pocket’s stated closed and parked poses. Keep all original geometry and the terrain cap south of the defined air-gap intervention. Use the exact riser formula for the mesh, with `−2.250` as the final support. Reserve the specified landing and door sweep volumes when placing the shelves and fixtures.
4. **Prove the candidate.** Cold-open the saved copy. Check support at each riser and landing, the continuous body envelope down to B1, the 2.180 m lintels and the 2.197 m finished lip witness. Check the full slider travel while traversing the 01 → 04 → 07 path and the 03/05/06 branches. Prove zero intersections beyond the intended cuts. Compare all 288 other envelope rows in full and the retained `BASE_slab` source mesh and transform. Check the active slab’s outside geometry, UVs, normals and materials and repeat the bevel-aware gap test before delivery. Any contact or exterior geometry difference outside the specified edit stops the candidate at verification.
5. **Return review evidence.** Deliver updated SVG plans and section, a clearance report and two staircase renders. Use an open-door entry view from `(8.10, 3.18, 2.05)` toward `(6.65, 2.925, 0.55)` at 22 mm, and a B1 view from `(6.90, 5.00, −0.62)` toward `(3.35, 3.62, −1.12)` at 24 mm. Use matched source/candidate pairs for `Záber 07` at frame 181, `Záber 08` at frame 211, and `CAM_V10_ENTRY` and `CAM_V05_VALLEY_INSIDE` at frame 181 with explicit camera override after setting the frame. Use 1920 × 1080, Cycles CPU with four threads and 96 samples, seed 0, matched denoising and AgX/None for the review jobs. Record the settings, image differences and a same-source repeat at the same settings. Inspect any differences in the fixed reviews against the permitted service-zone visibility. Deliver the candidate, geometry diff and evidence inventory with hashes for Michal’s review.

## 5. Validation and handoff

The corrected continuity anchor matched the saved prior report. Project `main`, its local origin and AP `d7023cf037f6d17885c3ede5c04812c61640da50` passed before and after. Meta remained at `cffbe078c285f2b47a1062531fe6a2119bcb8b43` with the owner’s permitted trace files. The pinned standalone and tuned exterior `.blend` files, envelope JSON, survey JSON, two SVGs, section CSV and isolated preferences matched all eight expected SHA-256 hashes at both checks.

Blender ran with factory startup, autoexec disabled, four threads, `nice -n 10` and the isolated config. Each successful probe’s before/after RAM check exceeded 20 GiB available. The global preferences SHA-256 remained `ae7a8626c3f41081ac7dde07f2ddcf2ab7d09c807a16ae2bdd5f6d233f88a9c0`. The owner’s GUI PID 25973 retained start ticks `1606192`. The temporary directory `/tmp/opencode/v19_plan_inspect` was removed and its absence verified. The eight schematic SVG blocks were checked as standalone XML during planning. The evidence is E0 and non-independent. Rendered and cold-saved candidate verification belongs to the implementation exchange.

Changed files: none.  
Git result: no writes in either repository.  
Persistence: Orchestrator relay from this report body to `/home/agile/meta/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/01_report_01.md`.  
Smallest next step: Michal selects the layout, with A recommended. The Orchestrator records the selection in the separate implementation grant.

Orchestration critique:  
MEASURED: The initial southwest L-shaft admitted direct low-south shadow-gap sightlines. The final straight shaft and its visible sub-slab extent start at `Y 2.480`, 20.4 mm beyond the conservative bevel-aware bound. Carry that boundary into the cut and terrain checks.  
LEAD: The fixed render pairs can establish whether the service-zone changes are visible through W01 or the corridor portal. The measured shell and ray checks establish the geometric boundary.  
Resolved Execution Issues / Near-Misses: The shell rejected a recursive cleanup command before launch. The bounded cleanup used explicit file removal and directory removal. The first inspection encountered a mesh whose evaluated result consisted of instances, and Blender created nested thumbnail cache directories. The corrected probe handled empty evaluated vertex arrays, recovered the cache with directory-only removal, and completed the direct measurements. Final input and cleanup checks passed.  
Pre-Existing Failure Classification: none.  
Authority expiry: This terminal report ends the planning grant.

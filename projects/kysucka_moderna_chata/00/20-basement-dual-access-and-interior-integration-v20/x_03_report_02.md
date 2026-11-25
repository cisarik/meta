# V20 · Second access to B1 through the west shelter edge

## 1. Recommendation and measured baseline

**Recommend Hypothesis 2**, a straight eastbound descent with two flights on `Y = 5.015 m`. It reaches the accepted B1 store through its west stone wall. It saves **4.32 m of walking from D01 to the new threshold**, **1.04 m of covered passage**, and **7.81 m³ of visualization excavation** relative to Hypothesis 1. The tradeoff is a **1.420 m interruption of the west slab edge and a 1.4768 m² plan cut**. The cut leaves a **1.360 m strip of shelter deck** between the notch and the closed west wall. The firewood, rack, and front posts stay in place. The exact cuts in §2 are for approval.

Both pinned scenes opened in isolated Blender 5.3.0 processes. Both use metres at unit scale `1`.

| Pinned scene | Size and SHA-256 | Saved frame and camera |
|---|---|---|
| `work/v19/kysucka_chata_interier_pivnica_v19.blend` | 425,401,183 B · `d9021ee49f63a6dc595214932485597b3b47186b6e26487065c87964dc5dcdf8` | 181 · `Záber 07 \| Obývačka a krb` |
| `work/v18/recovery/kysucka_chata_exterier_doladeny.blend` | 435,436,722 B · `5e8ada70e99c70a3be0a7eea9b18306b422e4ef3a141a63b51b237b7957e3a24` | 1 · `Záber 01 \| Chata a údolie` |

| Shared witness | World translation | World bounds in metres, X × Y × Z |
|---|---|---|
| `BASE_slab` / active `BASE_slab_V19_STUDY` | `(7.200, 4.200, 0.325)` | `0..14.400 × 0..8.400 × 0.200..0.450` |
| `WALL_left_closed` | `(2.550, 4.200, 1.850)` | `2.400..2.700 × 0..8.400 × 0.450..3.250` |
| `D01_leaf` | `(7.875, −0.060, 1.600)` | `7.250..8.500 × −0.105..−0.015 × 0.450..2.750` |
| `WOOD_BAY_rack` | `(1.200, 0.550, 0.490)` | `0.250..2.150 × 0.050..1.050 × 0.450..0.530` |
| `GABLE_other_proposed` | `(0, 0, 0)` | `X = 2.400 × 0..8.400 × 3.250..7.450` |
| `WALL_front_0_0` | `(4.825, 0.150, 0.900)` | `2.400..7.250 × 0..0.300 × 0.450..1.350` |
| `WALL_rear_0_0` | `(8.400, 8.250, 0.900)` | `2.400..14.400 × 8.100..8.400 × 0.450..1.350` |
| `V10_FLOOR_oak` | `(0, 0, 0)` | `2.460..14.400 × 0..8.400 × Z = 0.451` |

The shared transforms have identity rotation and unit scale. The hidden interior `BASE_slab`, floor, and terrain were evaluated after a temporary unhide and view-layer update. B1 retains gross bounds `X 2.700–7.400`, `Y 2.280–5.700`, floor `−2.250`, and clear store `X 2.900–7.200`, `Y 3.600–5.500`. The built `V19_B1_West_Stone` is `X 2.700–2.900 × Y 2.480–5.700 × Z −2.250–+0.200`. The north stone occupies `Y 5.500–5.700`. The historical Variant B opening at `Y 5.940–6.980` is beyond the built wall.

`V11_TERRAIN_NEAR` has 34,263 vertices in each file and its active V19 derivative has 34,270. All three grade checks reproduced `Z = −0.055 m` at 459 vertices in `X −8..0, Y −2..9`, 84 in `X −3..0, Y 4..9`, and 100 in `X −1..1, Y 0..8.4`. Evaluated rays at intervals of at most **0.025 m** along the full polylines and **0.08 m** over the excavation footprints found near terrain at `−0.055000…−0.054999 m`. This includes the entire ground spur, both upper landings, and the ground to be cut, up to the existing V19 void.

| Other intersecting surface | Measured Z and location |
|---|---|
| `ENTRY_step_3`, `ENTRY_step_2`, `ENTRY_step_1` | `+0.450`, `+0.300`, `+0.150` on the common D01 approach |
| `PATH_slab`, `.001`, `.002`, `.003`, `.004`, `.005`, `.006`, `.007` | Tops `+0.110`. Sampled bevel minima in that order `+0.1050`, `+0.1037`, `+0.1023`, `+0.1010`, `+0.0996`, `+0.0983`, `+0.0970`, `+0.0956`. Departure is from `.007` |
| `BED_entry` | `+0.0056…+0.0350` beneath the stepped D01 approach |
| `BASE_slab` / `BASE_slab_V19_STUDY` | Above the buried traces. Sampled tops `+0.4250…+0.4500` for H1 and `+0.4459…+0.4500` for H2, including the bevel |
| `V11_TERRAIN_FAR` in V19 | `−45.02751…−45.02749` under both polylines. The V18 far mesh and both `V11_TERRAIN_EXTENSION` meshes yielded no hits on these traces |
| `V19_B1_Floor_Slab`, `V19_Stone_Grout`, `V19_Stone_Tile_0_4` | `−2.269`, `−2.252`, and `−2.250` at the receiving side of the threshold. Tile checked just inside the store at `(2.930, 4.980)` |

`V04_ORCHARD` is at `(-1.100, −2.600, −0.094966)` in both files. Its low evaluated geometry blocked the shorter approach near `(-0.78, −0.68)`. The surveyed bypass clears the apple mesh by **79.6 mm** at its tightest body sample. The closest horizontal distance from the trunk origin to either full centerline is **3.197 m**. The trunk-to-excavation distances are **7.000 m** for H1 and **6.905 m** for H2.

## 2. Routes, sections, and approval polygons

**Common approach.** From outside D01 at `(7.875, −0.105, +0.450)`, walk south on the existing steps and pavers to `(7.875, −5.500, +0.110)`. Leave `PATH_slab.007` westward onto the adjoining court at `(6.400, −5.500, −0.055)`. The horizontal distance is `6.870 m`. Both hypotheses follow the terrain through these coordinates at `Z = −0.055 m`.

| Point | X | Y |
|---|---:|---:|
| Court | 6.400 | −5.500 |
| South of apple | 0.252 | −5.916 |
| Southwest of apple | −1.751 | −5.916 |
| Southwest bend | −4.490 | −4.335 |
| West of apple | −5.274 | −2.978 |
| Branch point | −6.100 | 0.800 |

Use the existing firm grade for this bypass. Finish the approach strip at the upper landing flush to the measured grade.

| Element | H1 · Outside slab, two turns | H2 · Eastbound, partly in shelter |
|---|---|---|
| Spur after branch point, then upper landing | `(-5.720, 6.910) → (-5.200, 6.910) → (-4.000, 6.910)`, all `Z −0.055` | `(-5.080, 5.015) → (-4.560, 5.015) → (-3.360, 5.015)`, all `Z −0.055` |
| Flight 1, first and last riser axes | `(-4.000, 6.910) → (-1.760, 6.910)`, 9 risers to `−1.574615` | `(-3.360, 5.015) → (-1.680, 5.015)`, 7 risers to `−1.236923` |
| Intermediate landing | `X −1.760..−0.560`, `Y 6.370..7.450`. Turn via `(-1.160, 6.910)` to `(-1.160, 6.370)` | `X −1.680..−0.560`, `Y 4.455..5.575`. Continue east |
| Flight 2, first and last riser axes | `(-1.160, 6.370) → (-1.160, 5.530)`, 4 risers to `−2.250` | `(-0.560, 5.015) → (0.840, 5.015)`, 6 risers to `−2.250` |
| Lower landing and covered mouth | Turn east at `(-1.160, 5.015, −2.250)`. Roof starts at `X = 0`. Link faces `Y 4.550..5.540` | Landing `X 0.840..2.700`, `Y 4.455..5.575`, `Z −2.250`. Roof starts at `X = 1.040` |
| Threshold and door, both | Recessed leaf plane `X = 2.790`, clear opening `Y 4.580..5.450`, floor `−2.250`, clear head `−0.070`. Inner wall face at `X = 2.900` | Same |

Both sets use `h = 2.195 / 13 = 0.168846 m`, `g = 0.280 m`, `2h+g = 0.617692 m`, and a **31.09°** flight pitch. Riser tops in order, metres, are `−0.223846, −0.392692, −0.561538, −0.730385, −0.899231, −1.068077, −1.236923, −1.405769, −1.574615, −1.743462, −1.912308, −2.081154, −2.250000`. Set each riser by index from the first coordinate of its flight, at exactly `0.280 m` increments. H2 is **1.120 m** between faces and **1.040 m** between rails. H1 has at least **1.000 m** between flight rails and a **0.990 m** covered link.

| Comparison | H1 | H2 |
|---|---:|---:|
| Court to upper-landing approach edge / first riser | 23.404 / 24.604 m | 21.619 / 22.819 m |
| D01 to upper-landing approach edge / first riser | 30.274 / 31.474 m | 28.489 / 29.689 m |
| D01 to recessed threshold plane | 40.159 m | 35.839 m |
| Covered link to outer B1 wall, plus wall reveal separately | 2.700 + 0.200 m | 1.660 + 0.200 m |
| West slab-edge length removed / plan area | 0 / 0 | 1.420 m / 1.4768 m² |
| Excavation footprint / volume | 13.3521 m² / 22.104 m³ | 10.3092 m² / 14.299 m³ |
| Wood shelter, posts, firewood | Full deck | Local notch. Posts and firewood retained |
| Existing interior landing and door arcs | Same receiving opening and body connection as H2. Arcs clear as specified in §3 | Clear in the §3 test. Existing landing stays at `(3.450, 2.925, −2.250)` |

Distances are horizontal, including the landings. For like-for-like historical comparison, the unbuilt Variant B was **34.17 m from D01 to the stair start** with a **6.552 m²** slab cut. The excavation estimates integrate the measured grade down to the proposed stepped formation `0.180 m` below each finished tread or landing, including the wall bands. They describe visualization geometry. The separately bounded exterior B1 fragment below is common to either hypothesis and excluded from these access volumes.

**Exact H2 cut for approval**

- **Slab.** Clip the active slab to the outside of `[(0,4.305), (1.040,4.305), (1.040,5.725), (0,5.725)]` in XY through `Z +0.200…+0.450`. Preserve the source and bevel outside the polygon. At the west edge the same request is the projected fascia cut on `X = 0`, bounded by `Y 4.305…5.725` and `Z +0.200…+0.450`. The sources expose that fascia as part of `BASE_slab`.
- **B1 plinth and reveal.** Clip the local west stone through `X 2.700…2.900` to the open YZ rectangle `[(4.540,−2.250), (5.490,−2.250), (5.490,−0.035), (4.540,−0.035)]`. Keep the header above it. Use a `.040 m` jamb each side and a `.035 m` head to obtain the clear opening. The wall above the shelter remains continuous. The original south gap remains **0.255 m** from `Z −0.055` to `+0.200`. The proposed exterior excavation starts at `Y 4.305`.
- **Terrain and visible returns.** Cut `[(−4.560,4.305), (2.700,4.305), (2.700,5.725), (−4.560,5.725)]`. Close the cut with `0.150 m` stone-faced returns and light-gray concrete, including an edge return where the grade meets the slab opening. Carry slate, matte textured nosings, and continuous graphite handrails on the flights. Bound rail intrusions to `.040 m` per face. Protect both open edges and close the deck guard around the east end of the notch. Use a `1.050 m` guard above the adjacent grade or deck and a separate graspable rail `0.950 m` above the stair pitch. Continue the north rail into the lower link to `X = 2.470`.
- **Lower joint and water space.** Make a visible recessed channel `X 2.380…2.540`, spanning `Y 4.455…5.575`, with invert `−2.410` and a flush graphite grate at `−2.250`. Add a flush `12 mm` joint immediately outside the stone threshold at `X = 2.700`. The section shows the water-collection space as a visual detail.
- **Exterior-only adjoining void.** Cut `X 2.700…4.360 × Y 3.600…5.700` in the V18 near terrain to house the minimal B1 fragment. This adds about `8.35 m³` to the V18 visualization void down to `−2.450`. V19 already carries the B1 void in that area. The shared stair cut and contact geometry are identical.

H1 uses the same wall reveal and threshold with a continuous slab and a cut polygon of `[(−5.200,7.600), (−0.410,7.600), (−0.410,5.690), (2.700,5.690), (2.700,4.400), (−1.910,4.400), (−1.910,6.220), (−5.200,6.220)]`. Its channel is at the same X and Z across `Y 4.550…5.540`.

**H1 metric plan**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 744 482" role="img" font-family="sans-serif">
<title>H1 metric plan, north-west dogleg and covered B1 link</title>
<rect width="744" height="482" fill="#f8f6ef"/>
<text x="24" y="29" font-size="19" fill="#222c32">H1 · Outside slab · west descent and two turns</text>
<g transform="translate(185 280) scale(26 -26)" stroke-width=".035" stroke-linejoin="round" fill="none">
<rect x="0" y="0" width="14.4" height="8.4" fill="#eee8dc" stroke="#888278"/>
<rect x="0" y="0" width="2.4" height="8.4" fill="#dfcfb6" stroke="#888278"/>
<rect x=".25" y=".05" width="1.9" height="1" fill="#9b6748"/>
<rect x="2.7" y="2.28" width="4.7" height="3.42" stroke="#6b6460" stroke-dasharray=".12 .08"/>
<rect x="2.9" y="3.6" width="4.3" height="1.9" fill="#ebebe2" stroke="#6b6460"/>
<rect x="4.35" y="5.205" width=".34" height=".275" fill="#9b6748"/>
<polygon points="-5.2,7.6 -.41,7.6 -.41,5.69 2.7,5.69 2.7,4.4 -1.91,4.4 -1.91,6.22 -5.2,6.22" fill="#c7e0db" stroke="#387875"/>
<rect x="0" y="4.4" width="2.7" height="1.29" fill="#b8c5d3" stroke="#465b75" stroke-dasharray=".12 .08"/>
<path d="M-4 6.37v1.08m.28-1.08v1.08m.28-1.08v1.08m.28-1.08v1.08m.28-1.08v1.08m.28-1.08v1.08m.28-1.08v1.08m.28-1.08v1.08m.28-1.08v1.08 M-1.76 6.37h1.2m-1.2-.28h1.2m-1.2-.28h1.2m-1.2-.28h1.2" stroke="#387875"/>
<path d="M7.875 -.105V-5.5H6.4L.252 -5.916H-1.751L-4.49 -4.335 -5.274 -2.978 -6.1 .8 -5.72 6.91H-1.16V5.015H2.9" stroke="#126861" stroke-width=".075"/>
<path d="M2.9 4.98H3.45V2.925H3.98 M2.79 4.59A.828 .828 0 0 0 1.962 5.418 M3.879 3.622A.906 .906 0 0 1 2.973 4.528" stroke="#944c33" stroke-dasharray=".10 .06"/>
<circle cx="-1.1" cy="-2.6" r=".13" fill="#604b2c"/>
</g>
<g font-size="13" fill="#222c32">
<text x="24" y="92">Upper landing</text><text x="82" y="127">9 risers east</text>
<text x="130" y="146">4 south</text><text x="230" y="126">Covered link</text>
<text x="298" y="164">B1 store</text><text x="299" y="219">Interior landing</text>
<text x="399" y="285">D01</text><text x="362" y="415">Court</text>
<text x="162" y="350">Apple origin</text>
<text x="578" y="81">↑ North / +Y</text><text x="578" y="107">+X toward glazed gable</text>
<text x="578" y="152">Teal · excavation</text><text x="578" y="171">Blue · below slab</text>
<text x="578" y="190">Rust · doors and inner walk</text>
<path d="M580 425h52m-52-4v8m52-8v8" stroke="#222c32"/><text x="580" y="446">0</text><text x="614" y="446">2 m</text>
</g>
</svg>
```

**H1 metric section along the unfolded walking line**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 750 280" role="img" font-family="sans-serif">
<title>H1 unfolded section, with retained slab over the covered link</title>
<rect width="750" height="280" fill="#f8f6ef"/>
<text x="23" y="25" font-size="18" fill="#222c32">H1 · Unfolded section · 9 + 4 risers</text>
<g transform="translate(112 78) scale(60 -60)" stroke-linejoin="round">
<path d="M-1.55 -.055H9.45" fill="none" stroke="#8a7353" stroke-width=".028" stroke-dasharray=".10 .06"/>
<rect x="5.895" y=".20" width="3.52" height=".25" fill="#a9a39a"/>
<rect x="5.895" y=".14" width="3.52" height=".06" fill="#626f77"/>
<path d="M-1.2 -.055H0V-.223846H.28V-.392692H.56V-.561538H.84V-.730385H1.12V-.899231H1.40V-1.068077H1.68V-1.236923H1.96V-1.405769H2.24V-1.574615H3.38V-1.743462H3.66V-1.912308H3.94V-2.081154H4.22V-2.25H9.42" fill="none" stroke="#296d69" stroke-width=".049"/>
<path d="M8.595 -.070H8.795V.14H8.595Z" fill="#6c6960"/>
<rect x="8.275" y="-2.410" width=".160" height=".160" fill="#343e46"/>
<path d="M6.55 -2.25V.14M6.48 -2.25h.14m-.14 2.39h.14" fill="none" stroke="#944c33" stroke-width=".025"/>
<path d="M8.685 -2.25V-.07" fill="none" stroke="#944c33" stroke-width=".020" stroke-dasharray=".12 .07"/>
</g>
<g font-size="12" fill="#222c32">
<text x="31" y="63">Upper −0.055</text><text x="244" y="70">Original grade against side returns</text>
<text x="472" y="47">Slab +0.200 to +0.450</text><text x="524" y="94">Soffit +0.140</text>
<text x="511" y="151">2.390 m</text><text x="639" y="160">2.180 m</text>
<text x="185" y="233">Turn at −1.575</text><text x="367" y="233">Lower landing −2.250</text>
<text x="566" y="233">Water recess</text><text x="644" y="233">B1</text>
<path d="M24 254h60m-60-4v8m60-8v8" stroke="#222c32"/><text x="96" y="258">1 m · same horizontal and vertical scale</text>
</g>
</svg>
```

**H2 metric plan**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 744 482" role="img" font-family="sans-serif">
<title>H2 metric plan, eastbound descent and the proposed slab notch</title>
<rect width="744" height="482" fill="#f8f6ef"/>
<text x="24" y="29" font-size="19" fill="#222c32">H2 · Eastbound descent · proposed west edge cut</text>
<g transform="translate(185 280) scale(26 -26)" stroke-width=".035" stroke-linejoin="round" fill="none">
<rect x="0" y="0" width="14.4" height="8.4" fill="#eee8dc" stroke="#888278"/>
<rect x="0" y="0" width="2.4" height="8.4" fill="#dfcfb6" stroke="#888278"/>
<rect x=".25" y=".05" width="1.9" height="1" fill="#9b6748"/>
<rect x="2.7" y="2.28" width="4.7" height="3.42" stroke="#6b6460" stroke-dasharray=".12 .08"/>
<rect x="2.9" y="3.6" width="4.3" height="1.9" fill="#ebebe2" stroke="#6b6460"/>
<rect x="4.35" y="5.205" width=".34" height=".275" fill="#9b6748"/>
<rect x="-4.56" y="4.305" width="7.26" height="1.42" fill="#c7e0db" stroke="#387875"/>
<rect x="1.04" y="4.305" width="1.66" height="1.42" fill="#b8c5d3" stroke="#465b75" stroke-dasharray=".12 .08"/>
<rect x="0" y="4.305" width="1.04" height="1.42" fill="#ecc6a9" stroke="#944c33" stroke-width=".060"/>
<path d="M-3.36 4.455v1.12m.28-1.12v1.12m.28-1.12v1.12m.28-1.12v1.12m.28-1.12v1.12m.28-1.12v1.12m.28-1.12v1.12 M-.56 4.455v1.12m.28-1.12v1.12m.28-1.12v1.12m.28-1.12v1.12m.28-1.12v1.12m.28-1.12v1.12" stroke="#387875"/>
<path d="M7.875 -.105V-5.5H6.4L.252 -5.916H-1.751L-4.49 -4.335 -5.274 -2.978 -6.1 .8 -5.08 5.015H2.9" stroke="#126861" stroke-width=".075"/>
<path d="M2.9 4.98H3.45V2.925H3.98 M2.79 4.59A.828 .828 0 0 0 1.962 5.418 M3.879 3.622A.906 .906 0 0 1 2.973 4.528" stroke="#944c33" stroke-dasharray=".10 .06"/>
<circle cx="-1.1" cy="-2.6" r=".13" fill="#604b2c"/>
</g>
<g font-size="13" fill="#222c32">
<text x="36" y="124">Upper landing</text><text x="109" y="171">7 + 6 risers east</text>
<text x="170" y="113">Deck notch</text><text x="223" y="113">Covered link</text>
<text x="298" y="164">B1 store</text><text x="299" y="219">Interior landing</text>
<text x="399" y="285">D01</text><text x="362" y="415">Court</text>
<text x="162" y="350">Apple origin</text>
<text x="578" y="81">↑ North / +Y</text><text x="578" y="107">+X toward glazed gable</text>
<text x="578" y="152">Teal · excavation</text><text x="578" y="171">Orange · slab cut</text>
<text x="578" y="190">Blue · below slab</text><text x="578" y="209">Rust · doors and inner walk</text>
<path d="M580 425h52m-52-4v8m52-8v8" stroke="#222c32"/><text x="580" y="446">0</text><text x="614" y="446">2 m</text>
</g>
</svg>
```

**H2 metric section at `Y = 5.015 m`**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 750 331" role="img" font-family="sans-serif">
<title>H2 section through the stairs, slab notch, covered link, and B1 threshold</title>
<rect width="750" height="331" fill="#f8f6ef"/>
<text x="23" y="26" font-size="18" fill="#222c32">H2 · Section at Y 5.015 m · 7 + 6 risers</text>
<g transform="translate(116 81) scale(77 -77)" stroke-linejoin="round">
<path d="M-1.45 -.055H7.28" fill="none" stroke="#8a7353" stroke-width=".028" stroke-dasharray=".10 .06"/>
<rect x="3.36" y=".20" width="1.04" height=".25" fill="none" stroke="#944c33" stroke-width=".025" stroke-dasharray=".10 .06"/>
<rect x="4.40" y=".20" width="2.88" height=".25" fill="#a9a39a"/>
<rect x="4.40" y=".14" width="2.88" height=".06" fill="#626f77"/>
<path d="M-1.2 -.055H0V-.223846H.28V-.392692H.56V-.561538H.84V-.730385H1.12V-.899231H1.40V-1.068077H1.68V-1.236923H2.80V-1.405769H3.08V-1.574615H3.36V-1.743462H3.64V-1.912308H3.92V-2.081154H4.20V-2.25H7.28" fill="none" stroke="#296d69" stroke-width=".042"/>
<path d="M6.06 -.070H6.26V.14H6.06Z" fill="#6c6960"/>
<rect x="5.74" y="-2.410" width=".160" height=".160" fill="#343e46"/>
<path d="M4.74 -2.25V.14M4.67 -2.25h.14m-.14 2.39h.14" fill="none" stroke="#944c33" stroke-width=".021"/>
<path d="M6.15 -2.25V-.07" fill="none" stroke="#944c33" stroke-width=".019" stroke-dasharray=".12 .07"/>
</g>
<g font-size="12" fill="#222c32">
<text x="30" y="68">Upper −0.055</text><text x="253" y="65">Slab cut</text>
<text x="474" y="50">Slab +0.200 to +0.450</text>
<text x="290" y="101">Grade meets retaining returns at −0.055</text>
<text x="242" y="201">Intermediate −1.237</text>
<text x="490" y="169">2.390 m link</text><text x="599" y="168">2.180 m door</text>
<text x="382" y="275">Lower −2.250</text><text x="527" y="275">Water recess</text><text x="636" y="275">B1</text>
<path d="M26 301h77m-77-4v8m77-8v8" stroke="#222c32"/><text x="114" y="305">1 m · same horizontal and vertical scale</text>
</g>
</svg>
```

**Schematic envelope views for both hypotheses**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 790 219" role="img" font-family="sans-serif">
<title>West and north views comparing the slab edge, plinth and protected under-slab gap</title>
<rect width="790" height="219" fill="#f8f6ef"/>
<g fill="#222c32" font-size="17"><text x="26" y="26">West · looking east</text><text x="427" y="26">North · looking south</text></g>
<g transform="translate(340 145) scale(-32 -15)" stroke-width=".05">
<path d="M-.85 2.27L4.2 7.45 9.25 2.27" fill="none" stroke="#5d5650"/>
<rect x="0" y=".45" width="8.4" height="2.8" fill="#e4d5bb" stroke="#8a7353"/>
<rect x=".05" y=".45" width="1" height="1.15" fill="#9b6748"/>
<rect x="0" y=".20" width="8.4" height=".25" fill="#807970"/>
<rect x="4.305" y=".20" width="1.420" height=".25" fill="#f8f6ef" stroke="#944c33"/>
<path d="M-.35 -.055H9" stroke="#8a7353"/>
<path d="M4.4 -.12V-.58H7.6V-.12" fill="none" stroke="#387875" stroke-dasharray=".14 .08"/>
<path d="M4.305 -.055V-.92H5.725V-.055" fill="none" stroke="#944c33"/>
</g>
<g transform="translate(745 145) scale(-21 -15)" stroke-width=".055">
<rect x="2.4" y=".45" width="12" height="2.37" fill="#e4d5bb" stroke="#8a7353"/>
<path d="M-.55 2.8H14.95" stroke="#5d5650"/>
<rect x="0" y=".20" width="14.4" height=".25" fill="#807970"/>
<path d="M-.6 -.055H14.8" stroke="#8a7353"/>
<path d="M0 .32H1.04m-1.04-.45h1.04" stroke="#944c33" stroke-dasharray=".14 .07"/>
</g>
<g fill="#222c32" font-size="12">
<text x="52" y="171">H1 teal · excavation below continuous slab</text>
<text x="52" y="190">H2 rust · local slab edge and plinth opening</text>
<text x="429" y="171">H2 dashed · cut behind the intact north edge</text>
<text x="429" y="190">Slab +0.200 to +0.450 · near grade −0.055</text>
<text x="52" y="208">South undercroft gap · 0.255 m preserved</text>
</g>
</svg>
```

## 3. Passage, doors, shelf, and ceiling

**Clearance.** Along H2, the minimum centerline headroom under the link is **2.390 m**. The forward reach of the `Ø 0.700 m` body first extends under the soffit from `X = 0.690` while the feet are on tread 12 at `−2.081154`. Headroom there is **2.221 m**. The exterior door gives **2.180 m** at its lintel, leaving **80 mm** over the `2.100 m` body. Both open flight runs clear the existing shelter roof by more than these controlling dimensions.

Use body center `Y 5.015` through the stair, then shift to `Y 4.980` from `X 0.840` to `0.980` on the lower landing. Walk through the new door to `(3.450, 4.980)`, turn south through `(3.450, 3.600)` to `(3.450, 2.925)`, and continue on the V19 interior stair to the service corridor. All B1 points are at `−2.250`. Turn on the upper landing at `(-4.040, 5.015)`, the intermediate landing at `(-1.120, 5.015)`, and the lower landing at `(1.520, 4.980)`. Reserving a `0.350 m` disk at each center gives at least `170 mm` lateral reserve on the two upper landings and `90 mm` to the exterior leaf’s full swept extent at the lower waiting point.

I sampled the site bypass at no more than `0.040 m`, and the H2 descent and B1-to-corridor route in both directions at the same interval, with 419 samples per direction for the descent and connector. The geometry test combined evaluated V19 triangles with the proposed stair, wall, and door envelopes. The minimum sampled body clearance was **25.0 mm** at the existing oak rail near `(3.908, 2.925, −2.250)`. The first unmasked sample beyond the new tread transition had **26.1 mm** at `(1.216, 4.980, −2.250)`. The new open door pulls had **30.0 mm** near `(2.042, 4.980, −2.250)`, and the existing stone liner had **30.2 mm** near `(3.450, 3.362, −2.250)`. Use V19’s stair support treatment for the known tread, riser, and nosing geometry in the ankle transition only. Apply the full body to the surrounding rails, masonry, furniture, and doors.

**Door geometry and states**

- **New exterior leaf.** Put the hinge at `(2.790, 5.418)`. Swing the `0.828 m` leaf from `−Y` when shut toward `−X` when open, parking at `90°` against the north side of the link. Use a `0.040 m` leaf, `Z −2.240…−0.080`, with both pulls contained in `0.715…0.780 m` along the leaf, `±0.058 m` from its plane, and `Z −1.250…−1.070`. The closest sampled leaf-to-frame margin over `0…90°` was **9.76 mm** at the south jamb near `1.5°`.
- **Existing glazed leaf.** Place its hinge beside the west jamb at `(2.973, 3.622)`. Reuse the measured leaf parts, changing the local span from `0.960` to `0.906 m` to fit the existing opening. For a vertex from the current open pose, use local along-leaf coordinate `(Y − 3.600) × 0.906/0.960` and cross-leaf coordinate `3.910 − X`. At `0°` use axes `+X, +Y` from the new hinge, then rotate to `90°` into the store. Preserve Z and the oak, glass, and handle finishes. The closest leaf-to-jamb margin was **12.1 mm**. The handle cleared the west stone by **40.0 mm**. The leaf cleared the new south jamb by **84.9 mm** and the first shelf front post by **1.192 m**. The two entire swing envelopes separate by **61.6 mm in Y**. Arc tests used `0.25°` intervals and conservative part bounds.
- **Operating positions.** At exterior-door `0°` and `45°` use `(1.520, 4.980)` outside and `(3.450, 4.980)` inside as the waiting centers. To pull the exterior door open from outside, start at `(2.304, 4.980)` and retreat along `Y 4.980`, keeping the body center `0.428 m` west of the moving leaf or hardware’s westernmost X. This reaches `X ≈ 1.534` at `90°` and tested with **78 mm** minimum body reserve to the moving door. For the glazed door use waiting centers `(3.450, 3.200)` and `(3.450, 4.980)`. Their minimum reserves to the full swing were **55 mm** and **183 mm**. Use fully open stops for transit through both portals.
- **Upper pocket door.** Keep the V19 translation of `0`, `0.460`, and `0.920 m` for parked, mid-travel, and closed. The evaluated opening widths are `0.790`, `0.440`, and `0 m`. Test waiting on either side at `(6.660, 2.925)` and `(7.650, 2.925)` during travel, and crossing at the parked position. The measured `V19_Top_Threshold` is `X 7.100…7.143 × Y 2.520…3.330 × Z +0.444…+0.451`.

**Keep the reduced first shelf.** The five shelf boards occupy `X 4.363…4.678 × Y 5.214…5.470`, depth **0.256 m**. The uprights occupy `X 4.350…4.690 × Y 5.205…5.480 × Z −2.247…+0.055`. The proposed `0.381 m` depth would put the boards at `Y 5.089…5.470` and move the front uprights to `Y 5.080…5.105`. A direct new aisle could clear that depth. The exact V19 walking line still clipped the enlarged front upright by **44.3 mm** near `(4.144, 4.856, −2.250)`. With the reduced shelf and new hinge the original descent-to-store path passed at the planning sample spacing. The full replay of all six original routes is an implementation check.

**Fix the ceiling light plane.** I compared the 1920 × 1080 `zaber_b1_pivnica_v19.png` with `CAM_V19_B1_CELLAR`. Seventeen points on the diagonal project to within **10 mm** of the plane of `V19_Cellar_Key` at the ceiling, across several ceiling bays. The evaluated bottom faces use continuous affine UVs on both triangles and identical `(0, 0, −1)` corner normals. The 53 W tilted area rectangle spans `Z −0.056318…+0.266318` and intersects the soffit at `+0.140`. The evidence points to the light plane.

Keep the light at `(5.850, 4.290, +0.105)`, retain its 53 W, dimensions, and horizontal long-axis bearing, and level it to face `−Z`. Its whole rectangle then sits 35 mm below the ceiling. Preserve the flush wood and its mapped grain. An added 20 mm board would give `2.370 m` clearance and a 40 mm exposed beam would give `2.350 m`, with body reserves of `270` and `250 mm`. The selected light correction keeps **2.390 m** and **290 mm**. Validate the repair at the same camera with the same door state and exposure, using an A/B where the key orientation is the only difference.

## 4. Materials, lighting, and two-scene build

Use recessed stone with readable joints, light-gray concrete, matte slate, and thin graphite steel. Set starting roughness to `0.80` for stone, `0.78` for concrete, `0.85` for slate and `0.55` for graphite. Use a dark matte exterior leaf and small edge bevels to read the reveal and threshold. Keep the shaded underside of the shelter readable from the fixed west and north views.

- **Exterior fixtures.** Use a continuous **2850 K** line under the north handrail, with an `8 mm` diffuser recessed `15 mm` into an opaque graphite channel. Aim inward and down at the treads and opposite stone joints. Use linked narrow area segments on the rail path starting at `0.90 W/m`, with `55°` spread. Use one `0.65 W`, 2850 K vertical line in the south reveal at `(X 2.720, Y 4.550)`, from `Z −1.960` to `−0.310`. Hide the optic behind the recess lip and aim across the threshold and toward the grate.
- **Day and blue hour.** Use `V20_CAM_WEST`, from `(-11.650, 1.450, 2.700)` toward `(-0.750, 4.050, 1.200)`, 32 mm on a 36 mm horizontal sensor. Day uses the V18 day world and sun with the V20 exterior strips off. The blue-hour profile copies the world and sets `Lighting and reflections radiance` to `0.14` and `Camera clouds radiance` to `0.35`, with linear tint `(0.58, 0.76, 1.00)` on the two owned background branches. Set `V15_SUN_REFERENCE_KEY` energy to zero in this profile. Keep AgX / None, exposure `0`, and gamma `1` for the matched pair. Use the closed exterior door in both. The separate night detail looks along the well from `(-4.950, 5.015, 1.200)` toward `(2.650, 5.015, −1.220)`, 29 mm. The blue-hour profile is an entrance check for V20.
- **Controls.** Render from just inside the measured west fence at `(-14.800, 5.400, 1.545)` and from meadow grade `+2.892` at `(-21.300, 7.200, 4.492)`. Aim both at `(0.200, 5.015, −0.200)` at 35 mm. Compare blue-hour frames with the V20 lights on and off. Require shielded optics in both views, visible tread and threshold separation in the detail, and a grazing contribution confined to the well and immediate stone. Check those regions at full image size for clipped highlights and spill.
- **Interior arrival.** Use a shielded `0.26 × 0.08 m` area, 3.5 W at 2850 K, at `(7.540, 3.190, 2.625)` aimed at `(7.180, 2.950, 0.481)`. Compare on and off from `V20_CAM_CORRIDOR`, from `(8.280, 3.910, 2.051)` toward `(7.105, 2.940, 1.550)`, 24 mm. Rays to the pocket threshold and toward the first tread cleared the evaluated V19 scene from this eye point.

In the implementation grant, create these independently openable day candidates from the pinned V19 and V18 files respectively.

- `work/v20/kysucka_chata_interier_pivnica_v20.blend`
- `work/v20/kysucka_chata_exterier_pivnica_v20.blend`

Use one declarative world-space spec and one builder under `work/v20/`. Embed the same local `V20_B1_ENTRANCE` collection in each file at identity transform. It owns both flight runs, landings, returns, slate, joint, grate, shared door and hardware, local terrain contact pieces, and exterior lighting. Store the shared door angle as `0…90°` with saved default `0°`; use the same state in both candidates and every paired review. Store common non-rendering datums for the new threshold, the lower glazed portal, and the top interior threshold. Compare the latter two datums to the actual retained interior geometry in V19.

Build visible derivatives for the slab, near terrain, and west stone, preserving original geometry, UVs, material slots, and corner normals outside the declared cuts. Retain originals with their identity in `V20_RETAINED_ORIGINALS`. Record the V19 study slab and its already accepted interior opening as the active interior predecessor. Keep the route over existing ground and apply vegetation exclusion at the cut and landing contact. Both source files have 40 lawn origins in `V11_CORE_GRASS_V06_LAWN_-001_+000` and 142 ground-cover origins in `V17_GROUND_COVER_POINTS` inside the H2 footprint. Use evaluated plant extents to catch pieces crossing the boundary. Keep original clouds and place local masks on owned derivatives.

In the V18 candidate, populate the bounded adjoining B1 fragment with the same tile and stone appearances, floor at `−2.250`, ceiling at `+0.140`, and a closed east return at `X = 4.360` to control the open-door view and light. The V19 candidate uses its actual store, corrected glazed hinge, ceiling key, and corridor light. Save replayable day and blue-hour profiles under `work/v20/` with cameras, transforms, world values, light states, and render settings. Pack dependencies into each candidate for offline reopening. Preserve the source startup cameras and frames. Treat promotion to `blender/kysucka_chata_interier.blend` as a separate post-acceptance operation.

## 5. Implementation acceptance and delivery

1. **Geometry and passage.** Verify the actual cut, the unchanged south `0.255 m` gap, both fixed envelope viewpoints, and terrain and slab equality outside the approval polygons. Test evaluated geometry with the `Ø 0.700 × 2.100 m` body and horizontal steps at most `0.045 m` through **court → B1 → corridor** and reverse. Test turns on the three landings and the closed, mid, and open door states, including the retreat path and parked pocket condition. Use the same support rules and replay all six original V19 routes from the pinned waypoints. Record the controlling object, pose, signed clearance, and XYZ. Require zero body or hardware collisions beyond the intended support and door-stop contacts.
2. **Shared geometry and cold opening.** Compare named shared meshes, world transforms, closed-component volumes, opening and threshold coordinates, and door states at `0°`, `45°`, and `90°`. Compare the declared changes against the 289-object envelope inventory and record every visible derivative. Cold-open the two candidates separately in isolated processes. Verify packed dependencies and entrance state in each, including an open-door render check for the exterior B1 fragment.
3. **Review packet.** Deliver one dimensioned plan and one section of H2, west day and west blue-hour from the same camera, the night detail, the corridor eye-level pair, and the B1 view at `CAM_V19_B1_CELLAR`. Include fixed `Záber 05 | Západná strana` and `Záber 04 | Severná strana` before/after, the fence and meadow controls, and the four V19 regression frames `Záber 07`, `Záber 08`, `CAM_V10_ENTRY`, and `CAM_V05_VALLEY_INSIDE`. Use 960 × 540 CPU Cycles, 96 samples, seed 0, and OIDN Accurate/High for the four V19 matches. Use 1440 × 810 with the same CPU sampling for the new exterior and corridor views, and 1920 × 1080 for the matched B1 ceiling check. Record masks and reasons for every localized image difference.
4. **Report.** Include both candidate hashes, the pinned parents, and the full permitted difference register. For V18 the differences are the shared entrance, its slab and terrain derivatives, local vegetation masks, minimum B1 fragment, and owned review profiles and cameras. For V19 they are the shared entrance and derivatives, west stone opening, glazed hinge assembly, single ceiling light orientation, corridor threshold light, and owned review profiles and cameras. Report the lighting controls and any unresolved visual defects before acceptance. Restrict the work to B1, the two accesses, and their adjacent exterior context.

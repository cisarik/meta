# V18 targeted correction (01/05) — high-quality 3D spring broadleaves without billboard-card boxes, spring season palette & blossoms, and multi-layered shrub ecotone from forest to meadow

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-split-and-forest-realism-v18
Worker session ordinal: 01
Worker exchange ordinal: 05
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Bounded Correction Worker (same-session continuation of 01/01–01/04)
Phase: implementation
Task identity: SPLIT-AND-FOREST-V18-SPRING-BROADLEAVES-AND-SHRUB-ECOTONE — fix the absurd broadleaf billboard cards and lollipop trunks in viewport and Cycles, implement the spring season palette (fresh spring greens, blossoming shrubs/trees, spring meadow wildflowers), and build a genuine 1–3.5 m shrub ecotone transition from forest to meadow
Delivery route: manual Cooperator delivery
Continuity anchor: terminal BLOCKED report `01_report_03.md` (SHA-256 `c54230c7d6474928fb0f522c84a784d18b10973c11cd953d8da38b882816db00`, Worker session 01 / exchange 04) and prior implementation report `01_report_02.md` (SHA-256 `d75f710d3664868c3b0ea76520ee453bde91e22961e385543ff26417089d10a2`, Worker session 01 / exchange 03), together with Cooperator visual feedback on the live 3D viewport (`listnate chceme v exterier view vidiet kvalitne teraz su absurdne a chceme jar rocne obdobie + nejake kriky prechod z lesa na luku` with screenshot) recorded and reconciled in `00_notes.md` on 2026-11-24
Authority renewal: prior authority expired at `01_report_03.md` (which stopped BLOCKED on the prompt's continuity digest mismatch for `01_report_02.md` before any mutation); this prompt corrects the verified `01_report_02.md` SHA-256 (`d75f710d3664868c3b0ea76520ee453bde91e22961e385543ff26417089d10a2`) and `01_report_03.md` SHA-256 (`c54230c7d6474928fb0f522c84a784d18b10973c11cd953d8da38b882816db00`) and grants complete new bounded correction authority at exchange `01/05` with `Native planning mode: not-used`. Retained context is convenience, not authority. Re-gate repository, input hashes, and process state yourself; stop on any conflict between retained context and current repository evidence.
Evidence posture: non-independent
Implementation authority: explicit
Independence required: no
Reasoning recommendation: High — named risks: eliminating the `6,595.7 m²` opaque green billboard-card rectangles and black `Attribute Color` artifacts on broadleaf crowns in Solid-Texture viewport and Cycles; constructing true 3D contoured spring broadleaf crowns and `1.0–3.4 m` multi-stem spring shrubs (including white-blossoming spring blackthorn/cherry); and grading the forest-to-meadow shrub ecotone and soil boundary so no sharp dark-brown ring or wall of lollipop poles borders the meadow
Recommended context capacity: approximately 250k tokens

## Active Amended Expectation Record
Amendment record: active
Cooperator decision ownership: COOPERATOR
Cooperator decision evidence: exact COOPERATOR acceptance evidence `listnate chceme v exterier view vidiet kvalitne teraz su absurdne a chceme jar rocne obdobie + nejake kriky prechod z lesa na luku` with live 3D-viewport screenshot on 2026-11-24
Superseded expectation: un-trimmed `tevy` LOD1/LOD2 broadleaf billboard-card meshes (`6,595.7 m²` leaf-card area on `BEECH_LOD2` with 84% empty background and `alpha_mode = 'CHANNEL_PACKED'`, rendering as solid opaque green rectangular boxes in Solid-Texture viewport and black blotches via `Attribute Color` multiply in Cycles overview) on bare white/grey lollipop poles lined up along a sharp forest-to-meadow boundary with only ankle-high (`0.16–0.55 m`) herbs and a sharp dark-brown `MAT_V18_FOREST_FLOOR` edge
Amended expectation: (1) high-quality 3D broadleaf trees in both 3D viewport (`Solid Texture` and `Material Preview`) and Cycles — zero giant opaque rectangular billboard boxes, zero black `Attribute Color` multiply artifacts, zero bare white lollipop poles, using real 3D contoured/alpha-trimmed foliage clusters and organic 3D branching crowns (including 3D spring broadleaf and blossoming tree prototypes derived from `V04_ORCHARD` and alpha-trimmed/contoured `BEECH`/`BIRCH` with lower branch tiers and natural bark); (2) explicit **Spring (`jar`) season** palette — fresh vibrant spring yellow-green/lime-green deciduous foliage, white/soft-pink blossoming spring edge trees and shrubs (*Prunus spinosa* / *Prunus avium* / *Crataegus*) echoing the blossoming garden apple tree, and a fresh spring meadow with readable clusters of yellow dandelions and white spring wildflowers; and (3) a gradual, multi-layered **Shrub Ecotone transition (`prechod z lesa na lúku`)** of `0.8–3.4 m` tall 3D bushes, blossoming shrubs, and young saplings arranged in irregular bays, tongues (`výbežky`), and small meadow islands along the entire forest-to-meadow boundary, with dark brown forest soil pushed back into the closed forest interior (`forest_field > +7.5 m`) and an intermediate mossy olive-green transition under the shrub belt
Amendment boundary: V18-SPRING-BROADLEAVES-AND-SHRUB-ECOTONE
Cooperator decision authority effect: decision-only-no-worker-mutation-authority
Orchestrator superseded-expectation record: recorded by ORCHESTRATOR under V18-SPRING-BROADLEAVES-AND-SHRUB-ECOTONE
Orchestrator authority issuance: issued by ORCHESTRATOR to Worker session 01 / exchange 05 for V18-SPRING-BROADLEAVES-AND-SHRUB-ECOTONE only
Renewed task boundary: V18-SPRING-BROADLEAVES-AND-SHRUB-ECOTONE only
Worker recipient: Worker session 01 / exchange 05
Worker implementation: pending in exchange 01/05
Worker validation: pending in exchange 01/05
Role sequence: COOPERATOR-decision -> ORCHESTRATOR-record -> ORCHESTRATOR-issuance -> WORKER-implementation -> WORKER-validation
Superseded expectation reported as failure: no
Unrelated scope change: none
Rendered acceptance ownership: COOPERATOR
## End Active Amended Expectation Record

## Exact technical root causes found in `candidate.blend` and binding fix specification

The 3D basin extent (`[-320, 340] × [-220, 340] m`), north trail continuation to `[61, 340, 30.411]`, and file-size reduction (`387.16 MiB` exterior `7736c887aa45401a2bbbf2cf133542519df9ad239eb43543e7d228dcf9157a00` / `413.64 MiB` interior `d6a6edf8c29ef453354c9b067fd507406bb94af3abae9133f27514e07d3f6188`) from `01/03` succeeded and must be preserved. However, direct readback of `work/v18/stage3/candidate.blend` and Michal's live 3D-viewport screenshot identified three concrete visual defects that you must fix in `scripts/v18_split_forest.py` and re-promote to `blender/kysucka_chata_exterier.blend` (and `blender/kysucka_chata_interier.blend` for the shared broadleaf/viewport fixes):

### 1. Fix the absurd Broadleaf Trees (`V17_BROADLEAF_RENDER` and `V17_BROADLEAF_WORK`) in BOTH the 3D Viewport and Cycles

- **Why the broadleaves look absurd right now (verified by readback of `candidate.blend`):**
  1. `V17_BROADLEAF_0_BEECH_LOD2` has `3,930` leaf triangles with a total surface area of **`6,595.7 m²` (`1.68 m²` per triangle!)**, and `V17_BROADLEAF_1_BIRCH_LOD2` has `4,030` leaf triangles with **`3,178.1 m²`**. In `beech_leaves_color_512/1024` and `birch_leaves_color_512/1024`, **78–84% of each giant rectangular card is empty transparent background** (`opaque_frac = 0.158` on beech, `0.201` on birch) filled with flat green padding `rgb_transp = [0.288, 0.351, 0.116]`, AND `image.alpha_mode` is set to `'CHANNEL_PACKED'`!
  2. In Blender's **Solid Texture viewport** (`space.shading.type = 'SOLID'`, `color_type = 'TEXTURE'`), Workbench does NOT do alpha cutouts on giant billboard quads — it renders 100% of those `1.68 m²` triangles as **solid opaque green cardboard boxes/umbrellas**!
  3. In Cycles (`viewport-overview_cottage.png` and `after-forest.png`), `beech_leaves_lod1`, `birch_leaves_lod1`, `V18 beech work leaves`, and `V18 birch work leaves` wire `Attribute Color -> Mix B (MULTIPLY)` into `Base Color`. On Geometry Nodes instances without that vertex attribute (or where `Attribute` evaluates to `(0,0,0)`), or where stacked `84%`-transparent cards exceed `cycles.transparent_max_bounces` (currently default `8`!), **the broadleaf crowns render with pitch-black blotches**!
  4. On `V17_BROADLEAF_1_BIRCH_LOD2`, `retarget_pairs()` overwrote material slot 1 (`360` twig triangles, `3.14 m²`) with `V18 birch work leaves` instead of bark/twigs!
  5. Geometrically, `tevy` `BIRCH` is a 6-metre bare white pole with a tiny cone of cards on top ("lollipop"), `tevy` `BEECH` has a pale grey cylinder trunk with 45° straight rigid pipes, and `forest_for_basin()` placed them along 26% of the entire meadow edge like a fence of lollipops!

- **Mandatory technical fix for Broadleaf Trees:**
  1. **Construct true 3D non-billboard-box broadleaf crowns for `V17_BROADLEAF_RENDER` and `V17_BROADLEAF_WORK` (and `V18_TREES_RENDER` / `V18_TREES_WORK`):**
     - Load `V04_MASTER_ORCHARD` from `work/v17/complete_3d/kysucka_chata_v17_komplet_3d.blend` (or `assets/models/sketchfab_7df0631398f443379fa4541e9efc2343/master.blend` / `scene().objects['V04_ORCHARD']`). Remember: `V04_ORCHARD` (`80,000` tris) has **100% real 3D photogrammetric trunk, branch, and foliage/blossom cluster geometry with ZERO billboard quad cards** (`Apple_tree.jpg` is a solid `.jpg` with no alpha cards, so it looks completely natural in Solid Texture mode, Material Preview, AND Cycles!).
     - Replace the giant `1.68 m²` billboard-card canopies of `V17_BROADLEAF_RENDER` and `V17_BROADLEAF_WORK` with **4 distinct, organic 3D Spring Broadleaf prototypes** (each having a matched render master `~10,000–16,000` tris and working master `~5,000–7,500` tris, where **zero giant empty billboard quads exist** and maximum triangle area is `< 0.025 m²`):
       - **Prototype 0 — Spring European Beech (`Fagus sylvatica`, `V18_BROADLEAF_0_SPRING_BEECH`)**: organic branching brownish-grey trunk (`diffuse_color = (0.23, 0.20, 0.17)`) and full, multi-tiered 3D rounded/layered foliage dome (using decimated/composed 3D foliage lobes from `V04_ORCHARD` and/or tightly UV-alpha-trimmed `< 0.55` 3D leaf clusters where all transparent background triangles are physically deleted from the mesh!) reaching down to `22%` of tree height, shaded in **fresh spring yellow-green / lime-green** (`sRGB` `(0.42, 0.58, 0.18)`, `diffuse_color = (0.22, 0.36, 0.075)`).
       - **Prototype 1 — Spring Silver Birch / Mountain Maple (`Betula pendula` / `Acer pseudoplatanus`, `V18_BROADLEAF_1_SPRING_BIRCH`)**: natural slightly curved/forked trunk with dark basal bark roughing and dappled charcoal-and-cream birch bark (`diffuse_color = (0.38, 0.35, 0.31)`, never a glowing white cylinder!) with lower side branches starting at `25–30%` of height and airy 3D spring green foliage clusters (`sRGB` `(0.36, 0.55, 0.15)`, `diffuse_color = (0.19, 0.34, 0.065)`).
       - **Prototype 2 — Blossoming Spring Wild Cherry / Rowan (`Prunus avium` / `Čerešňa vtáčia`, `V18_BROADLEAF_2_SPRING_CHERRY`)**: derived from the 3D branching crown of `V04_ORCHARD` (`~12,000` tris render / `~6,000` tris work, reshaped with taller trunk/crown proportions), carrying **fresh spring green leaves and delicate white-pink spring blossom clusters** (`sRGB` `(0.92, 0.88, 0.86)` / `(0.40, 0.54, 0.18)`, `diffuse_color = (0.72, 0.76, 0.64)`).
       - **Prototype 3 — Multi-Stem Young Spring Broadleaf / Alder / Willow (`Jelša / vŕba / mladý buk`, `V18_BROADLEAF_3_SPRING_ALDER`)**: broader, low-branching multi-stem deciduous tree (`4.5–8.5 m` tall) whose foliage starts near `12–18%` of height so it merges seamlessly with the shrub belt!
     - **Hard geometry invariant on all broadleaf and shrub meshes:** No foliage polygon in `V17_BROADLEAF_RENDER`, `V17_BROADLEAF_WORK`, `V18_TREES_RENDER`, `V18_TREES_WORK`, or the shrub masters may be an un-trimmed billboard quad (`max polygon area ≤ 0.03 m²`; if any alpha-mapped leaf texture is used, physically subdivide and delete all faces with mean UV alpha `< 0.50` AND bake a solid spring-green UV texture without black/unpadded background for the Solid-Texture active image node!).
  2. **Fix all broadleaf shaders and Cycles transparency settings:**
     - Disconnect and remove the `Attribute Color` / `Attribute Alpha` multiply nodes from all broadleaf materials so no crown ever turns black!
     - Set `image.alpha_mode = 'STRAIGHT'` on every alpha-bearing image in `bpy.data.images`.
     - Set `scene().cycles.transparent_max_bounces = 32` (and `max_bounces = 12`) in `profile()` and in the saved scenes.
  3. **Natural Kysuce broadleaf grouping (no single-file row of poles around the meadow):**
     - In `forest_for_basin()`, keep Norway spruce (`Picea abies`) as the dominant forest matrix (`~82–85%`), and place the 4 spring broadleaf prototypes (`~15–18%`) in **natural clustered groves (3–8 trees per grove)** in sunlit coves, along the lower slopes, and mixed into the forest margin (with Prototype 2 blossoming wild cherry and Prototype 3 low-branching young broadleaves concentrated in clusters at the sunlit forest-to-meadow bays, and Prototypes 0 & 1 forming mixed beech-birch-spruce stands behind them).

### 2. Build a Multi-Layered 3D Shrub Ecotone Transition from Forest to Meadow (`nejake kriky prechod z lesa na luku`)

- **Why the forest-to-meadow boundary looked harsh in Michal's screenshot:**
  1. Tall trees (`10–17 m`) started abruptly along the `forest_field = 0` contour against the flat green meadow.
  2. The dark brown `MAT_V18_FOREST_FLOOR` terrain slot was assigned to every polygon with `dis <= max(3.0, r['radius']) or field > 2.0`, creating a sharp dark-brown dirt border right along the meadow edge!
  3. The `V18_ECOTONE_GROUND` cloud used tiny `0.16–0.55 m` herbs (`V04_MASTER_SHRUB_01_0` is only `0.37 m` tall at scale 1!), which are invisible at valley/overview scale and do not form real `1.0–3.5 m` bushes/shrubs (`kríky`)!

- **Mandatory technical fix for the Forest-to-Meadow Transition:**
  1. **Create a dedicated 3D Shrub & Sapling Ecotone collection and point cloud (`V18_SPRING_SHRUB_BELT`, `1,800–2,800` instances of real `0.9–3.5 m` tall 3D shrubs and saplings):**
     - Build **4 true 3D multi-stem Shrub & Sapling master prototypes** in `V18_MASTER_SHRUBS_RENDER` (`~2,500–5,500` tris each) and `V18_MASTER_SHRUBS_WORK` (`~1,200–2,800` tris each), with **100% real 3D volumetric foliage (zero flat billboard boxes!)**:
       - `00_SPRING_HAZEL_BUSH` (`Lieska / horský ker`, nominal height `2.2 m`, width `2.6 m`): multi-stem dome of fresh spring yellow-green 3D foliage clusters reaching down to `Z = 0`.
       - `01_SPRING_BLOSSOM_SHRUB` (`Kvitnúca trnka / hloh — Prunus spinosa`, nominal height `1.8 m`, width `2.2 m`): multi-stem spring bush with fresh green leaves and **creamy-white spring blossom clusters** (`sRGB` `(0.93, 0.91, 0.86)`) visible both in the 3D viewport and in Cycles!
       - `02_LOW_MEADOW_SHRUB` (`Nízky krovinný trs`, nominal height `1.1 m`, width `1.6 m`): low spreading green shrub cluster bridging grass (`0.3 m`) and taller bushes (`2.2 m`).
       - `03_JUVENILE_SPRUCE_SAPLING` (`Hustý mladý smrečok`, nominal height `2.0 m`, width `1.7 m`): full-skirted juvenile Norway spruce with lowest branches touching the ground.
     - Distribute **1,800–2,800 instances** of these 4 shrub/sapling prototypes across the forest-to-meadow transition belt (`forest_field(x, y) ∈ [-16.0 m, +9.0 m]`) modulated by a multi-frequency spatial noise field (`patch_noise`) so they form **irregular scalloped shrub thickets, tongues (`výbežky kríkov`) pushing `8–20 m` out into the meadow, and small isolated shrub/sapling islands (`ostrovčeky kríkov`) in the outer meadow**, plus dense shrub mantles around the right-valley witness (`CAM_V18_FOREST_MARGIN`), around broadleaf trunks, and along the outer edge of the trail corridor (keeping the `1.25 m` gravel trail + `1.0 m` verge and the central cottage-to-valley sightline open!).
  2. **Step tree heights smoothly across the forest edge:**
     - In `forest_for_basin()`, do NOT place `12–17 m` tall trees at `forest_field ∈ [-2, +8] m`! Instead, taper the target tree height smoothly with `forest_field`:
       - At the outer forest fringe (`forest_field ∈ [-3 m, +6 m]`): place sparser groups of **small young/edge trees (`3.8–7.5 m` tall)** emerging out of the `1.0–3.2 m` shrub thickets.
       - In the middle transition (`forest_field ∈ [+6 m, +16 m]`): **`7.5–12.5 m` trees** (including the half-height juvenile cohort clusters and spring broadleaves).
       - In the deeper forest interior (`forest_field > +16 m`): full **`12.5–18.5 m` mature stand**.
  3. **Eliminate the harsh dark-brown dirt border at the meadow edge (`forest_floor()`):**
     - Push `MAT_V18_FOREST_FLOOR` (dark brown needle soil) and `MAT_V18_BROADLEAF_LITTER` back so they are assigned **only inside the closed forest interior (`forest_field > +8.5 m` and `dis <= 2.4 m`)**!
     - Across the shrub ecotone and outer forest fringe (`forest_field ∈ [-6.0 m, +8.5 m]`), assign a new **Spring Mossy Ecotone material (`MAT_V18_SPRING_ECOTONE`, fresh mossy yellow-olive green `diffuse_color = (0.16, 0.23, 0.075)` with active 512px mossy-grass viewport texture)** that transitions smoothly into `V18 Meadow` (`diffuse_color = (0.20, 0.28, 0.088)`). That way, from any 3D orbit view, there is a natural soft green-to-moss-to-forest-floor gradient under the shrub belt instead of a dark brown ring!

### 3. Spring Season (`jar rocne obdobie`) in the Meadow, Garden, and Lighting Response

- **Meadow & Wildflowers (`jar`):**
  - Update `V18 Meadow`, `V18 Garden lawn`, and the grass materials (`V16_MASTER_MEADOW_RENDER`, `V17_GROUND_COVER_RENDER`) to a **fresh spring green palette** (shifting dry brownish-olive winter/late-summer tints toward lush spring green `(0.20, 0.28, 0.088)` in viewport and vibrant spring chlorophyll green in Cycles).
  - Expand the spring wildflower clusters (`V17_BOTANICAL_POINTS` / `V18_SPRING_FLOWERS` using the existing `tevy Wildflower Patch v1` white flower heads, `Poly Haven Dandelion 01` yellow dandelions, and `periwinkle_plant` violet-blue blossoms) so **natural drifts of yellow dandelions and white spring meadow flowers** are visible both in the foreground/trail loop of `CAM_V11_VALLEY_REVIEW` (`after-wide.png`) AND in the foreground meadow leading into the shrub ecotone in `CAM_V18_FOREST_MARGIN` (`after-forest.png`)!

## Repository gate and exact baseline

Working directory: `R = /home/agile/Projects/kysucka_moderna_chata`
Trace directory: `T = /home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18`
Exact baseline: `78534bd46020bb2bfc97eef69b05e583cba5a5e5` on `main`

Immutable input hashes (verify before and after execution):
- `work/v17/complete_3d/kysucka_chata_v17_komplet_3d.blend`: `8a733770f3f4b96922dce76d662e81b281d2047affee5adceac849fb8948113e`
- `work/v17/nature_detail_01/checkpoints/candidate_exterior_v17.blend`: `f2e0942b63c25ec813b64ad483ea535d4a44b5e0c3a9f6dcfc0eebf7cb3ec4be`
- `work/v16/meadow_trail_01/checkpoints/candidate_exterior_v16.blend`: `5d82ecf41d6555924b31fdfe5394639849f4d38db3f50cbc6619c0ff1b3225b1`
- `reference/01.png`: `7cbc989040f7b5847f63ecd0532e01ac8e8693c3cc149166f4c6e9fb58844d2d`
- `work/v12/profile_03/isolated_config/userpref.blend`: `d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561`
- `/home/agile/.config/blender/5.3/config/userpref.blend`: `8c52b5cf0d5ac23a35c9496e442a37c69399203b47b32842dd76d05653c29c02`
- `T/01_report_02.md`: `d75f710d3664868c3b0ea76520ee453bde91e22961e385543ff26417089d10a2`
- `T/01_report_03.md`: `c54230c7d6474928fb0f522c84a784d18b10973c11cd953d8da38b882816db00`

## Execution route and resource/process guards

Canonical execution route: **isolated native Blender 5.3.0 CLI route** (`/home/agile/Applications/Blender/blender --background --disable-autoexec --threads 4`), serialized one child at a time with `nice -n 10`, isolated MCP-disabled preferences (`work/v12/profile_03/isolated_config/userpref.blend`), `PYTHONPYCACHEPREFIX` in the job's runtime directory, `PYTHONDONTWRITEBYTECODE=1`, and `sys.dont_write_bytecode = True`.
- **Protect Michal's live Blender GUI (`PID 134646` or any running owner GUI process):** never signal, close, or touch the owner GUI process. Build and verify in `work/v18/stage3/` and `/tmp/opencode/v18_verify/`, then promote atomically to `blender/kysucka_chata_exterier.blend` and `blender/kysucka_chata_interier.blend`.
- Resource guards: verify available RAM ≥10 GiB before each child launch; stop your own child if own RSS >9 GiB or available RAM <4.5 GiB on two consecutive samples; 360 s watchdog for 960×540 / build jobs and 900 s for detailed jobs.

## Authority and mutation axes

Changed-path allowlist:
- `blender/kysucka_chata_exterier.blend`
- `blender/kysucka_chata_interier.blend`
- `model/shared_envelope_v18.json`
- `model/parameters.json` (only updating `forest_realism_v18`; all 21 prior top-level keys unchanged)
- `scripts/v18_split_forest.py`
- `assets/ASSET_MANIFEST.md`
- `work/v18/stage3/{before.blend,candidate.blend,interier.blend,release.json,cohort.csv,connector.csv,trail_stations.csv,resources.json,overhead.svg}`
- `work/v18/stage3/{before,after}-{wide,right,forest,root,trail,hills}.png`
- `work/v18/stage3/viewport-{overview_se,overview_nw,overview_cottage,broadleaf_closeup}.png` (including a close-up 3D viewport/working-branch witness `viewport-broadleaf_closeup.png` showing the spring broadleaf crowns and shrub ecotone transition!)
- Temporary sandbox directory `/tmp/opencode/v18_verify/**` (must be completely removed after readback before submitting the report)
- Direct-write terminal report `/home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/01_report_04.md`

Negative authority: no modification of `work/v17/**`, `work/v16/**`, `work/v10/**`, or any existing `blender/kysucka_chata_mcp_*.blend` / `kysucka_chata_seed.blend` file; no live MCP calls (`tools.blender.*` prohibited); no touching any owner GUI process or global preferences; no network calls; no Git stage, commit, or push; and never emit the project closure signal.

Repository mutation: `blender/kysucka_chata_exterier.blend`, `blender/kysucka_chata_interier.blend`, `model/shared_envelope_v18.json`, `model/parameters.json`, `scripts/v18_split_forest.py`, `assets/ASSET_MANIFEST.md`, and untracked `work/v18/stage3/**` in the Changed-path allowlist
Host/remote mutation: temporary `/tmp/opencode/v18_verify` sandbox directory for isolated headless Blender 5.3.0 `bwrap --unshare-net` verification only (must be removed before report; zero persistent host change)
Trace persistence: direct-write `/home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/01_report_04.md`

External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 18-split-and-forest-realism-v18
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 01_correction_04.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18
Report filename: 01_report_04.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

## Validation and required evidence

Evidence tier: E2
Evidence tier basis: bounded visual and geometric correction of broadleaf crown geometry/materials, spring season palette, and forest-to-meadow shrub ecotone transition with offline sandbox verification
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: `bwrap --unshare-net` masked-root offline cold-open portability, shared-envelope digest (`87288303...`), second-apply idempotence, triangle-evaluated root support, ~5% half-height juvenile cohort, and continuous north trail (`Y = 340.0 m`)
Affected tests: `after-{wide,right,forest,root,trail,hills}.png` and `viewport-{overview_se,overview_nw,overview_cottage,broadleaf_closeup}.png`
New causal regression: broadleaf & shrub foliage polygon-area and alpha-trim gate (verifying maximum foliage triangle area `≤ 0.03 m²`, zero `1.68 m²` un-trimmed billboard cards, `alpha_mode == 'STRAIGHT'` on all leaf textures, zero `Attribute Color` black-multiply links, and `cycles.transparent_max_bounces >= 32`) + shrub-ecotone census (`≥ 1,800` placed 3D shrubs/saplings of height `0.8–3.5 m` in `forest_field ∈ [-16, +9] m`)
Broad or full suite: not-used
Runtime or testbed: isolated headless Blender 5.3.0 CLI with MCP-disabled preferences and `bwrap --unshare-net`
Independent acceptance: not-required

Completion and report contract: begin `01_report_04.md` on line 1 with `### Report for ORCHESTRATOR_CHAT`; echo the coordinates (`kysucka-moderna-chata-split-and-forest-realism-v18`, `01`, `05`) once; include the compact core (`Status: PASS | PARTIAL | BLOCKED`, `Phase-qualified result: implementation-PASS | not-applicable`, `Start commit` / `End commit`, complete changed/created files and SHA-256 table including the updated `blender/kysucka_chata_exterier.blend` and `blender/kysucka_chata_interier.blend`, `scripts/v18_split_forest.py`, and all updated renders, validation summary with broadleaf triangle/area metrics, spring shrub-ecotone counts and height distribution, ~5% half-height juvenile spruce statistics, and resource metrics, Git result = no writes, deviations/risks, one smallest next step, `Report justification: new-mutation`, authority-expiry statement, `Orchestration critique` `MEASURED` / `LEAD`, `Resolved Execution Issues / Near-Misses`, and `Pre-Existing Failure Classification`). Set `Logical-whole closure: not-closed`. Write `T/01_report_04.md` directly and read it back completely before returning your short completion notice.

Authority expiry: this terminal report, cancellation, or supersession ends this grant; retained context is convenience, not continuing authority.

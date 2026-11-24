# V19 planning (corrected initial grant 01/02) — basement access and layout study in the standalone interior scene (Variant A vs Variant B)

You are the same healthy concrete Planner session that returned the `01/01` `BLOCKED` report (`01_report_00.md`, SHA-256 `73ef1865dbca0aebfefe857b191b2b9549894ab213d268f7b72b407e6b05ec25`). This is a complete corrected initial planning grant for the same logical whole **V19** (`kysucka-moderna-chata-basement-layout-study-v19`), reconciling the two environment baseline pins that blocked exchange `01/01`. Read it fully before acting.

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-basement-layout-study-v19
Worker session ordinal: 01
Worker exchange ordinal: 02
Worker session target: current-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: BASEMENT-LAYOUT-V19-PLAN — comparative layout, access, stair, headroom, door-swing, and envelope-impact study for Variant A (interior service-zone access) and Variant B (west wood-bay access) in the standalone V18 interior scene
Delivery route: manual Cooperator delivery
Continuity anchor: terminal BLOCKED report `projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/01_report_00.md` (SHA-256 `73ef1865dbca0aebfefe857b191b2b9549894ab213d268f7b72b407e6b05ec25`) from actual Worker session 01 / exchange 01
Authority renewal: prior planning authority expired at `01_report_00.md`; this prompt grants complete renewed planning-only authority in the same healthy Worker session with reconciled Meta HEAD, global `userpref.blend` hash, and owner GUI Blender process classification
Why current session: same healthy Planner session, unchanged objective and scene/survey inputs, correction of two preflight environment pins from `01_planning_00.md`, retained reading and preflight checks useful, independence not required
Retained context: convenience, not authority
Evidence posture: non-independent
Re-gate: verify current repository, reconciled environment pins, and input hashes before planning; stop on conflict between retained context and current repository evidence
Reasoning recommendation: High — named risks: 3D spatial/headroom/door-swing/corridor-passability reconciliation between ground-floor service rooms (`+0.451 m`), slab (`+0.200..+0.450 m`), perimeter terrain (`-0.055 m`), west wood bay (`X=0..2.40 m`), and basement level B1, plus shared-envelope (`289`-object) impact assessment before any geometry mutation
Recommended context capacity: approximately 250k tokens
Independence required: no

Planning cycle: initial
Prior planning report: projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/01_report_00.md
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository- and scene-grounded technical planning and comparative architectural visualization study for V19 comparing Variant A (interior basement entry from the ground-floor corridor via the service zone) and Variant B (exterior/covered basement entry from the western wood bay `X=0..2.40 m`), including schematic ground-floor plans, B1 plans, scaled cross-sections through stairs/slab/terrain, exact elevations, standing clearances, stair geometry, worst-case headroom, door-swing/corridor passability, collision checks, one recommended variant, and a decision-ready implementation specification for the selected variant
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1

This is a corrected initial planning exchange after a prompt preflight pin defect (`AP.md#consumed-coordinates`, `AP.md#planning-budget-and-expiry`, `PROMPT_CONTRACTS.md#planning-record`), not a targeted revision. Exchange `01/01` stopped `BLOCKED` at preflight before any plan existed, so the initial planning cycle remains unused (`Planning cycle: initial`, `Automatic targeted revisions used: 0`).

## Reconciled environment gates from `01_report_00.md`

1. **Meta repository (`/home/agile/meta`) gate:**
   - Current verified `HEAD` on `main` is `cffbe078c285f2b47a1062531fe6a2119bcb8b43` (Cooperator commit adding `projects/kysucka_moderna_chata/00/19-pivnica/00_handout.md` above `240b4472fca3613fac6b56b3482593c30a15a5a5`).
   - Any untracked files or subsequent Cooperator archival commits in `/home/agile/meta` (including `projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/**` and `00/19-pivnica/**`) are authorized Cooperator/Orchestrator trace activity (`unrelated-owner-work` / `accepted-continuation`) and must **never** be treated as a stop condition.
2. **Global Blender preferences (`/home/agile/.config/blender/5.3/config/userpref.blend`) and running owner GUI Blender (`PID 25973`):**
   - The current verified SHA-256 of `/home/agile/.config/blender/5.3/config/userpref.blend` on this workstation is **`ae7a8626c3f41081ac7dde07f2ddcf2ab7d09c807a16ae2bdd5f6d233f88a9c0`** (the `8c52b5cf...` value in `01_planning_00.md` was a stale hash copied from V18 notes).
   - Michal's live GUI Blender 5.3.0 process is running at **`PID 25973`** (`start_ticks 1606192`, command `/home/agile/Applications/Blender/blender`). This process (or any other owner-launched interactive GUI Blender process) is classified under RF-12 as **`unrelated-owner-work`**: preserve it untouched, do not signal or kill it, and do not connect to it via MCP.
   - Your isolated headless Blender probe uses its own `BLENDER_USER_CONFIG=/tmp/opencode/v19_plan_inspect/config` initialized from `work/v12/profile_03/isolated_config/userpref.blend` (`d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561`). Simply record the pre-probe SHA-256 of `/home/agile/.config/blender/5.3/config/userpref.blend` (`ae7a8626c3f41081ac7dde07f2ddcf2ab7d09c807a16ae2bdd5f6d233f88a9c0`) and verify after your isolated headless probe that your probe left it unchanged.

## Goal and Cooperator-framed scope

Produce one decision-complete comparative layout and access plan (no scene save in `R/` or `R/work/`, no persistent repository or Meta file write by the Worker in this planning exchange) for logical whole **V19** (`kysucka-moderna-chata-basement-layout-study-v19`).

Working hypothesis: a compact storage basement (`malá skladová pivnica`) beneath the western portion of the enclosed cottage (`X = 2.70..8.80 m`, `Y = 0.30..8.10 m`, or a justified sub-footprint thereof). Record the proposed basement footprint, clear height, floor/ceiling elevations, and storage purpose explicitly as visualization-study assumptions that Michal may adjust after reviewing the variants. No structural engineering, construction certification, waterproofing, or building-code claim is implied.

## Verified Stage 1 baseline and measured context

During Continuation Bootstrap Stage 1, the Orchestrator verified (recorded in `T/00_notes.md`):
- **Standalone interior scene:** `blender/kysucka_chata_interier.blend` (`420,066,660 B`, SHA-256 `c607cb21fbdb289b49f05596004b403e7dd5f96a64e900ce42ed8485f6a30449`, 1,288 scene objects, 262 packed images, opening at frame 181 on `Záber 07 | Obývačka a krb`).
- **Tuned daytime exterior reference scene:** `work/v18/recovery/kysucka_chata_exterier_doladeny.blend` (`435,436,722 B`, SHA-256 `5e8ada70e99c70a3be0a7eea9b18306b422e4ef3a141a63b51b237b7957e3a24`).
- **Shared building envelope:** `model/shared_envelope_v18.json` (file SHA-256 `e58959a22b2d1879828fe87cff645ec3f7ed99a28ec12ae66bfce01c4f6045b8`; 289-object aggregate SHA-256 `8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50`, directly verified on `blender/kysucka_chata_interier.blend` with 0 mismatches).
- **V18 basement survey handoff:** collection `56_BASEMENT_V18` (`{'podklad': 'V18 | Podklad pre pivnicu'}`) and embedded text block `V18 | Podklad pre pivnicu` inside `blender/kysucka_chata_interier.blend`, matching local files:
  - `work/v18/stage1/basement.json` (`4f2a87459c4ffffd8c80acdd80159f3a1b351271e6ef19a7b3f6550ec0c81a2a`)
  - `work/v18/stage1/basement_plan.svg` (`62bba44d676415cebd8e4669b58f09b0087ed37df5a411e62e8578c6f1169f93`)
  - `work/v18/stage1/cross_sections.csv` (`28940be9935bd08ad897777291c6437ba432590683cd5a59a9bcb6364f591bb4`)
  - `work/v18/stage1/cross_sections.svg` (`49b1d04d9f977148da1019302c0ca0d4b7ac4601a2a8de8d737f521ab946d4f7`)
- **Key measured datums and room/envelope bounds (metres, `+X` west-to-east, `+Y` south-to-north, `+Z` up):**
  - `BASE_slab`: `X = 0.000..14.400`, `Y = 0.000..8.400`, `Z = +0.200..+0.450` (`0.250 m` thick).
  - `V10_FLOOR_oak`: `X = 2.460..14.400`, `Y = 0.000..8.400`, `Z = +0.451`.
  - Perimeter terrain `V11_TERRAIN_NEAR` around S/N/W/E facades: `Z = -0.055` (`0.506 m` below `+0.451`), leaving an open shadow gap of `0.255 m` (`Z = -0.055..+0.200`) below `BASE_slab`.
  - `V10_GALLERY_slab`: `X = 2.700..8.800`, `Y = 0.300..8.100`, `Z = +3.050..+3.250` (clear height in ground-floor rooms/corridor `2.599 m`).
  - West wood bay (`západný prístrešok`): `X = 0.000..2.400`, `Y = 0.000..8.400`, bounded on the east by `WALL_left_closed` (`X = 2.400..2.700, Y = 0.000..8.400, Z = 0.450..3.250`) and `GABLE_other_proposed` (`X = 2.400, Z = 3.250..7.450`). Posts at south edge: `WOOD_BAY_post` (`X = 0.030..0.210, Y = -0.020..0.180`) and `WOOD_BAY_post.001` (`X = 2.190..2.370, Y = -0.020..0.180`). Firewood rack `WOOD_BAY_rack` (`X = 0.250..2.150, Y = 0.050..1.050, Z = 0.450..0.530`) and 80 logs `FIREWOOD_log..079` (`X = 0.229..2.121, Y = 0.220..0.920, Z = 0.493..1.932`). Unoccupied slab area inside the wood bay north of the firewood stack is `X = 0.000..2.400, Y = 1.050..8.400` (`2.400 × 7.350 m` at `Z = +0.450 m`). South porch paving `PORCH_paving` runs `X = 0.000..6.700, Y = -0.650..0.000, Z = 0.270..0.450` from main entry steps `ENTRY_step_1..3` (`X = 6.700..9.050, Y = -1.050..0.000`).
  - Ground-floor corridor `04 Chodba`: `X = 2.700..8.650`, `Y = 3.350..4.500` (clear width `1.150 m`, length `5.950 m`), portal to living zone `X = 8.650..8.800, Y = 3.350..4.500`.
  - South service rooms (`Y = 0.300..3.200`, depth `2.900 m`, corridor wall `Y = 3.200..3.350`):
    - `01 Zádverie`: `X = 6.800..8.650` (`1.850 × 2.900 m = 5.365 m²`), exterior entry door `D01_leaf` (`X = 7.250..8.500, Y = -0.105..-0.015`), corridor opening `X = 7.100..8.200` (`1.100 m`).
    - `02 Technická miestnosť`: `X = 5.300..6.650` (`1.350 × 2.900 m = 3.915 m²`), corridor opening `X = 5.450..6.250` (`0.800 m`), partition to `01` at `X = 6.650..6.800` (`PARTITION_proposed.001`), partition to `03` at `X = 5.150..5.300` (`PARTITION_proposed`).
    - `03 Kúpeľňa / WC`: `X = 2.700..5.150` (`2.450 × 2.900 m = 7.105 m²`), corridor opening `X = 4.100..5.000` (`0.900 m`). Note that south facade window `W01` spans `X = 4.150..6.150, Z = 1.350..2.500`.
  - North back rooms (`Y = 4.650..8.100`, depth `3.450 m`, corridor wall `Y = 4.500..4.650`):
    - `05 Izba 1`: `X = 2.700..5.650` (`2.950 × 3.450 m = 10.178 m²`), corridor opening `X = 4.400..5.300` (`0.900 m`), north window `W02` (`X = 3.450..4.850, Z = 1.350..2.550`).
    - `06 Izba 2`: `X = 5.800..8.650` (`2.850 × 3.450 m = 9.833 m²`), corridor opening `X = 6.650..7.550` (`0.900 m`), north window `W03` (`X = 6.550..7.950, Z = 1.350..2.550`).
  - Living-zone collision volumes (`X ≥ 8.800 m`): gallery stair `V10_STAIR_*` (`X = 8.800..10.785, Y = 3.350..8.100`), understair cabinet `V10_UNDERSTAIR_CABINET` (`X = 8.820..9.710, Y = 5.300..7.080, Z = 0.451..1.898`), fireplace `V10_FIREPLACE_*` (`X = 10.650..12.600, Y = 2.750..3.650, Z = 0.451..6.700`).

## Sources, identity, and repository gate

Working directory: `R = /home/agile/Projects/kysucka_moderna_chata`
Trace directory: `T = /home/agile/meta/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19`

Repository identity and baseline:
- Project checkout: standalone checkout at `R`, branch `main`, expected HEAD `f600c7a8e69a23a029559872652302ac299c2aea` (tracked working tree and index clean).
- Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `.ap` (gitlink = submodule HEAD).
- Meta repository: `/home/agile/meta`, branch `main`, HEAD `cffbe078c285f2b47a1062531fe6a2119bcb8b43` (or later Cooperator Meta archival commit on `main`; untracked trace files under `projects/kysucka_moderna_chata/00/**` are expected and permitted).

Verified immutable input hashes:
- `blender/kysucka_chata_interier.blend`: `c607cb21fbdb289b49f05596004b403e7dd5f96a64e900ce42ed8485f6a30449`
- `work/v18/recovery/kysucka_chata_exterier_doladeny.blend`: `5e8ada70e99c70a3be0a7eea9b18306b422e4ef3a141a63b51b237b7957e3a24`
- `model/shared_envelope_v18.json`: `e58959a22b2d1879828fe87cff645ec3f7ed99a28ec12ae66bfce01c4f6045b8` (289-object `aggregate_sha256`: `8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50`)
- `work/v18/stage1/basement.json`: `4f2a87459c4ffffd8c80acdd80159f3a1b351271e6ef19a7b3f6550ec0c81a2a`
- `work/v18/stage1/basement_plan.svg`: `62bba44d676415cebd8e4669b58f09b0087ed37df5a411e62e8578c6f1169f93`
- `work/v18/stage1/cross_sections.csv`: `28940be9935bd08ad897777291c6437ba432590683cd5a59a9bcb6364f591bb4`
- `work/v18/stage1/cross_sections.svg`: `49b1d04d9f977148da1019302c0ca0d4b7ac4601a2a8de8d737f521ab946d4f7`
- Isolated MCP-disabled preferences `work/v12/profile_03/isolated_config/userpref.blend`: `d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561`
- Current global `/home/agile/.config/blender/5.3/config/userpref.blend`: `ae7a8626c3f41081ac7dde07f2ddcf2ab7d09c807a16ae2bdd5f6d233f88a9c0`

Mandatory reading:
- Governing WORKER spine: `.ap/AP.md` Semantic Authority + WORKER row, RF-03/RF-06/RF-12/RF-18, §8, §18; `.ap/AP_WORKER.md` Worker Session Target and Reporting; `.ap/PROMPT_CONTRACTS.md` Worker Report Header, Planning Record, Plan-to-Execution Gate, Worker Exchange Identity, Mutation Axes Record, Cooperator Delivery and Trace Destination Record.
- Project `AGENTS.md`, `docs/OPERATIONS.md`, `model/shared_envelope_v18.json`, `work/v18/stage1/basement.json`, `work/v18/stage1/basement_plan.svg`, `work/v18/stage1/cross_sections.svg`, `/home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/01_report_00.md` (§3), `/home/agile/meta/projects/kysucka_moderna_chata/00/18-split-and-forest-realism-v18/01_report_01.md`, `T/00_handout.md`, `T/00_notes.md`, and `T/01_report_00.md`.

## Execution route for isolated read-only Blender 5.3.0 inspection

Canonical inspection route: **isolated headless Blender 5.3.0 CLI probe** (explicit bounded task route; live MCP `tools.blender.*` is prohibited):
- Leave Michal's running GUI Blender process (`PID 25973`, `start_ticks 1606192`) completely untouched (`unrelated-owner-work`).
- Verify before and after running your isolated headless probe that `/home/agile/.config/blender/5.3/config/userpref.blend` (`ae7a8626c3f41081ac7dde07f2ddcf2ab7d09c807a16ae2bdd5f6d233f88a9c0`) was not modified by your probe and available system RAM is ≥10 GiB.
- Run `/home/agile/Applications/Blender/blender --background --factory-startup --disable-autoexec --threads 4` with `nice -n 10` and isolated environment (`BLENDER_USER_CONFIG=/tmp/opencode/v19_plan_inspect/config`, `XDG_CACHE_HOME=/tmp/opencode/v19_plan_inspect/cache`, `TMPDIR=/tmp/opencode/v19_plan_inspect/tmp`, `TMP=/tmp/opencode/v19_plan_inspect/tmp`, `TEMP=/tmp/opencode/v19_plan_inspect/tmp`, `PYTHONPYCACHEPREFIX=/tmp/opencode/v19_plan_inspect/pycache`, `PYTHONDONTWRITEBYTECODE=1`) inside `/tmp/opencode/v19_plan_inspect`, initialized with a copy of `work/v12/profile_03/isolated_config/userpref.blend` (`d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561`).
- Never write into `R/` or `R/work/` or `/home/agile/meta/`; remove `/tmp/opencode/v19_plan_inspect` completely before submitting your report and verify that all eight pinned `.blend` and JSON/SVG/CSV hashes are unchanged.

## Required planning deliverables in `01_report_01.md`

1. **Direct verification of baseline datums and shared envelope on `blender/kysucka_chata_interier.blend`:**
   - Confirm file SHA-256 (`c607cb21...`), 289-object shared-envelope aggregate digest (`87288303...`), embedded `56_BASEMENT_V18` / `V18 | Podklad pre pivnicu`, elevations (`+0.451 m` floor finish, `+0.200..+0.450 m` slab, `-0.055 m` perimeter terrain, `0.255 m` under-slab shadow gap), west wood bay (`X=0..2.40 m`, firewood stack `X=0.229..2.121, Y=0.050..1.050, Z=0.450..1.932 m`, closed west wall `X=2.40..2.70 m`), corridor (`X=2.70..8.65, Y=3.35..4.50 m`, width `1.150 m`), service/back rooms (`01..06`), and collision exclusion volumes (`V10_STAIR_*`, `V10_UNDERSTAIR_CABINET`, `V10_FIREPLACE_*`).
   - State the explicit working assumptions for the basement study (`malá skladová pivnica` under the western enclosed cottage): proposed B1 finished floor elevation (e.g. `-2.150 m` to `-2.250 m`), B1 ceiling/slab underside (`+0.200 m` or stepped/insulated ceiling elevation), clear standing height in B1 (target `≥ 2.20..2.40 m`), perimeter wall thickness, and B1 storage room dimensions and net floor area (`m²`).
2. **Variant A — Interior Entry from the Service Zone (`Vstup zvnútra zo zázemia`):**
   - Design the exact stair entry from `04 Chodba` (`Y = 3.35..4.50 m`, `Z = +0.451 m`), routing the stair flight(s) inside the side space of the service zone (`02 Technická miestnosť` at `X = 5.30..6.65, Y = 0.30..3.20 m`, or a combined/adjusted service bay, evaluating whether a straight flight, L-stair with landing, or U-stair fits best within the `2.90 m` south depth or along the western service zone without touching `W01` glazing or by cleanly partitioning the stair shaft).
   - Specify exact world coordinates (`X, Y, Z`) for:
     - Top entry threshold (`nástupná kóta +0.451 m`) and top landing / door position from `04 Chodba`;
     - Door width, hinge axis, opening direction, and simultaneous passability test (`otvorenie dverí a prejdenie trasy do dennej zóny naraz`): prove with exact clearance numbers that the `1.150 m` corridor (`04 Chodba`) remains continuously passable from `01 Zádverie` (`X = 7.10..8.20 m`) to `07 Obývačka` (`X = 8.65..8.80 m`) and to `03 Kúpeľňa / WC`, `05 Izba 1`, and `06 Izba 2` even while the basement door is open (e.g. door swinging into the stair landing recess or sliding/pocket or constrained swing leaving clean passage);
     - Slab opening rectangle in `BASE_slab` / `V10_FLOOR_oak` (`otvor v doske`), stair flight width, riser count `N`, riser height `h`, tread going `g` (satisfying `2h + g ≈ 0.60..0.64 m`), any intermediate landing (`podesta`), bottom exit threshold (`výstupná kóta` in B1), and clear bottom standing zone (`čistý priestor na státie` at the foot of the stairs);
     - Worst-case vertical headroom (`svetlá výška na najhoršom mieste`) under the slab opening edge / partition lintel / ceiling along the stair pitch line;
     - Exact area accounting (`m²` before vs after): quantify to `0.01 m²` how much floor area Variant A takes from `02 Technická miestnosť` (`3.92 m²`), `03 Kúpeľňa / WC` (`7.11 m²`), or `05/06 Izba 1/2`, and verify whether the remaining service rooms retain usable function and clear passage.
     - Confirm zero impact on the exterior visible plinth (`BASE_slab` perimeter) and the 289-object exterior facade appearance in Variant A (only an internal slab cut inside the enclosed footprint, plus optional sub-grade B1 exterior volume hidden beneath terrain if needed).
3. **Variant B — Entry from the Western Wood Bay (`Vstup od západného prístrešku`):**
   - Measure the exact free space around the firewood stack (`WOOD_BAY_rack` + `FIREWOOD_log..079` at `X = 0.229..2.121, Y = 0.050..1.050 m`) and the approach route from the existing front entrance / porch paving (`PORCH_paving` at `X = 0.00..6.70, Y = -0.65..0.00, Z = +0.450 m` or perimeter terrain at `Z = -0.055 m`).
   - Model the entire descent starting from the actual level (`+0.450 m` wood-bay slab top or `-0.055 m` surrounding flat terrain) down to B1 floor level inside or alongside the wood-bay footprint (`X = 0.00..2.40 m`, `Y = 1.05..8.40 m`):
     - Specify exact world coordinates (`X, Y, Z`) for the approach, top threshold (`nástupná kóta`), stair geometry (risers, going, width, landing), slab/plinth cutout in `BASE_slab` (`zásah do dosky či viditeľného sokla`), retaining/stairwell walls, bottom door and threshold (`výstupná kóta`), and clear standing space in B1, plus the passage through the underground foundation wall at `X = 2.40..2.70 m` into the basement under the enclosed cottage.
     - Check on the cross-section whether the full stair descent and required headroom can physically fit inside the wood-bay footprint (`X = 0.00..2.40 m`, `Y = 1.05..8.40 m`) without colliding with `WOOD_BAY_post` / `FIREWOOD_log`, `WALL_left_closed` (`X = 2.40..2.70 m, Z = +0.450..+3.250 m`), or the 45° roof eave (`Z = +2.270 m` at `Y = -0.85 / 9.25 m`).
     - Quantify the exact impact on the 289-object shared envelope (`BASE_slab`, `PORCH_paving`, `WALL_left_closed`, and the `0.255 m` under-slab gap visible in `Záber 04 | Severná strana` and `Záber 05 | Západná strana`), including schematic West (`Západný pohľad`) and North (`Severný pohľad`) elevation diagrams showing how Variant B alters the visible plinth/bay.
4. **Scaled Schematic Drawings (embedded directly in `01_report_01.md` as self-contained SVG blocks + coordinate tables):**
   - For **Variant A**:
     1. Schematic Ground-Floor Plan (`Pôdorys prízemia — Variant A`) with readable metric scale, grid coordinates (`X, Y`), room boundaries (`01..07`), door swings, simultaneous corridor walk path, stair up/down arrow, and slab opening outline;
     2. Schematic Basement Plan B1 (`Pôdorys B1 — Variant A`) with metric scale, B1 perimeter walls, stair landing/arrival, door swing, clear standing zone, and net storage area;
     3. Scaled Cross-Section (`Rez cez schody, dosku a terén — Variant A`) showing `+0.451 m` finish, `BASE_slab` (`+0.200..+0.450 m`), `-0.055 m` terrain, `0.255 m` gap, stair steps, B1 floor/walls/ceiling, and the worst-case headroom dimension arrow.
   - For **Variant B**:
     1. Schematic Ground-Floor & Wood-Bay Plan (`Pôdorys prízemia a prístrešku — Variant B`) showing the approach from the existing entry, firewood clearance, stairwell cut in the wood bay, and door swing;
     2. Schematic Basement Plan B1 (`Pôdorys B1 — Variant B`) showing the exterior stairwell arrival, basement entry door at `X = 2.40..2.70 m`, clear standing zone, and B1 storage room;
     3. Scaled Cross-Section (`Rez cez schody, dosku, prístrešok a terén — Variant B`) + schematic West/North facade views (`Západný a severný pohľad pri zásahu do spoločnej obálky`) showing the slab/plinth intervention and headroom.
5. **Side-by-Side Comparison Matrix, Recommended Variant, and Post-Selection Implementation Specification:**
   - Compare Variant A and Variant B across all required criteria (entry/exit elevations, stair comfort `h × g`, clear width, worst-case headroom, door opening & simultaneous corridor walkability, ground-floor room area loss, weather protection, security/thermal boundary, and shared-envelope / exterior visual impact on `BASE_slab` and `Záber 04/05`).
   - Recommend **one variant** based on concrete measured differences (honoring the handout rule: *"Vnútorný variant má prednosť, ak ponechá pohodlný priechod a funkciu zázemia"*).
   - Specify the exact post-selection implementation plan (to be executed only after Michal selects the variant and the Orchestrator issues `01_implementation_02.md`):
     - Target working copy path (e.g. `work/v19/kysucka_chata_interier_pivnica_v19.blend` derived from verified `blender/kysucka_chata_interier.blend` `c607cb21...`, keeping `blender/kysucka_chata_interier.blend` untouched until Michal's acceptance, or labeled study copy of `BASE_slab` / `V10_FLOOR_oak` with exact vertex/triangle diff report if a slab opening is cut);
     - Collection `56_BASEMENT_V18` / new owned basement collection structure owning test stairs, B1 floor, perimeter walls, ceiling, slab opening trim, door, and basement lighting;
     - Required verification deliverables for the implementation exchange: updated plan & section SVGs, one rendered view of the stair entry (`záber nástupu`), one rendered view from inside B1 (`záber z B1`), continuous walk-envelope proof from ground floor to the last basement step, and fixed-camera regression comparison of the living room (`Záber 07 | Obývačka a krb`), gallery (`Záber 08 | Jedáleň a galéria`), and window view (`CAM_V10_ENTRY` / `CAM_V05_VALLEY_INSIDE`).

## Authority and mutation axes

Positive authority: read-only inspection of `R`, `R/work/v18/**`, and `/home/agile/meta/projects/kysucka_moderna_chata/00/**`; bounded isolated headless Blender 5.3.0 read-only inspection and geometric/SVG calculation probe strictly inside temporary `/tmp/opencode/v19_plan_inspect` (cleaned completely before report); return the complete terminal report in session output for Orchestrator persistence.

Negative authority: no writes to tracked repository files, `R/blender/**`, `R/work/**`, or `/home/agile/meta/**`; no scene save in `R/` or `R/work/**`; no live MCP calls (`tools.blender.*` prohibited); no touching or signalling Michal's GUI Blender process (`PID 25973`); no touching global Blender preferences; no package/runtime installation; no Git writes in any repository; no closure signal emission.

Repository mutation: none
Host/remote mutation: bounded temporary `/tmp/opencode/v19_plan_inspect` directory for isolated headless Blender 5.3.0 read-only inspection and geometric/SVG calculation probe only (must be removed before report; zero persistent host change; benign Python `__pycache__/*.pyc` interpreter cache permitted)
Trace persistence: none

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
Downloadable prompt filename: 01_planning_01.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/19-basement-layout-study-v19
Report filename: 01_report_01.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: ORCHESTRATOR — named exact-content relay in session output because Native Plan Mode blocks direct file writes
Git publication owner: COOPERATOR
Archival: wait-for-report

Evidence tier: E0
Evidence tier basis: read-only technical planning, geometric calculation, and isolated temporary headless Blender inspection with full cleanup
Validation ladder: not-used
Independent acceptance: not-required

Stopping conditions: failed project repository or pinned input hash gate; unexplained project-repository divergence; tampering with owner GUI Blender (`PID 25973`); temporary directory cleanup failure; instruction conflict. Stop at the terminal planning report; planning authority expires there.

Completion and report contract: begin the report on line 1 with `### Report for ORCHESTRATOR_CHAT`; echo the coordinates (`kysucka-moderna-chata-basement-layout-study-v19`, `01`, `02`) once; include the compact core (`Status: PASS | PARTIAL | BLOCKED`, `Phase-qualified result: not-applicable`, `Start commit` / `End commit`, changed files = none, validation summary including `/tmp/opencode/v19_plan_inspect` cleanup and unchanged `.blend` / JSON / SVG / CSV SHA-256 hashes, Git result = no writes, deviations/risks, one smallest next step, `Report justification: new-evidence`, authority-expiry statement, `Orchestration critique` `MEASURED` / `LEAD`, `Resolved Execution Issues / Near-Misses`, and `Pre-Existing Failure Classification`). Set `Logical-whole closure: not-closed`. Output the complete report text in the session so the Orchestrator can persist it to `T/01_report_01.md`, then stop.

Authority expiry: this terminal planning report, cancellation, or supersession ends this grant; retained context is convenience, not continuing authority.

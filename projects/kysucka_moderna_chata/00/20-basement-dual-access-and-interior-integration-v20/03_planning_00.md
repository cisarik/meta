# V20 planning — initial grant after verified Plan Mode for the second access into accepted B1

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20
Worker session ordinal: 03
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: required
Worker session profile: Planner
Phase: planning
Task identity: BASEMENT-DUAL-ACCESS-V20-PLAN — initial plan after Cooperator-confirmed Plan Mode; measure and recommend one exterior descent into the accepted V19 basement B1, with the door, ceiling, lighting, and shared-scene specification required before any scene save
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — named risks: a new stair must meet the accepted west wall of B1 without reusing the unbuilt Variant B opening, must clear both existing door arcs and the reduced first shelf, and may cut the visible west slab edge
Recommended context capacity: approximately 250k tokens
Independence required: no

Planning cycle: initial
Prior planning report: projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20/02_report_00.md
Targeted revision basis: none
Changed decision boundary: none
Preserved unaffected decisions: none
Automatic targeted revisions used: 0

Planning layer: implementation-planning
Orchestration planning owner: ORCHESTRATOR
Worker planning scope: repository- and scene-grounded technical planning for one exterior entrance into the accepted B1, including two measured hypotheses, one recommended route, plan and section drawings, door-swing and shelf clearance, the smallest B1 ceiling repair, a day and blue-hour lighting specification, and a decision-ready build specification for two separately openable scenes that share one world-space entrance
Plan disposition: approval-gated
Implementation in same Worker session: allowed
Planning stop event: terminal planning report submitted
Execution authority event: explicit ORCHESTRATOR prompt with Native planning mode: not-used
Post-plan implementation session: current-worker-session
Maximum plan-only cycles: 1

## Consumed exchanges and this grant

Exchanges `01/01` and `02/01` are consumed. Both terminal reports are `BLOCKED` because those clients were in Default mode. No scene was opened and no plan exists, so the planning cycle is still initial and this is not a targeted revision. Leave these files unchanged:

- `T/01_planning_00.md` SHA-256 `e397c38ed4c90a9e90bbcc980d2a588ad8e0c6ec0ec7a6c02e3af72a8e7f42b2` and `T/01_report_00.md` SHA-256 `40c55fdb6b27f8d9238ab81e3650044aa99802c07eece54dd68e4fdc0bce4121`
- `T/02_planning_00.md` SHA-256 `8bdc39829c5a0898709dab8058957751e54adb6b610fe8349c96ff928ec72862` and `T/02_report_00.md` SHA-256 `c7efe146ff52c926ce1345908f9cd590c4d5eb883ea98817b3b1c431bca1b15c`

This prompt is the initial Planner for a new concrete session, `03/01`. The Cooperator reported, immediately before this issuance, that the destination client is in native Plan Mode. That report is the delivery precondition. It does not replace your own observation. If this client is in Default or Agent mode, stop `BLOCKED` before creating the temporary directory and before opening either scene, and name the mode you observe. If you are in native Plan Mode, continue with the measurements. A paste of `01_planning_00.md` or `02_planning_00.md` is not authority for this exchange.

## Goal and accepted constraints

Produce one decision-complete plan. This exchange does not save a scene, does not write under `R/` or `R/work/`, and does not write the Meta report file.

Michal accepted V19 Variant A and then accepted V20: one basement with two full accesses, a separately lit exterior descent into that existing B1, a ceiling and glazed-door correction, and matching entrance parts in the interior and exterior scenes. V20 stops at the basement, its two accesses, and the adjacent piece of facade and terrain. The bathroom, bedrooms, and other room fit-outs belong to later wholes. The sunset across the valley remains `R-V18-01`. Blue hour in this whole is only a lighting check of the new entrance. No structural, drainage, waterproofing, permit, or site-calibration claim is implied. Show a visually readable water-collection space in the section; do not design the waterproofing.

Preserved product decisions:

- Accepted gross B1 remains `X 2.700–7.400 m`, `Y 2.280–5.700 m`, finished floor `−2.250 m`. Clear store remains `X 2.900–7.200 m`, `Y 3.600–5.500 m`, clear height `2.390 m` to soffit `+0.140 m`, unless the ceiling study states an explicit local change that still clears the `2.100 m` body.
- The existing interior stair from the service zone stays. The new route is additional.
- The south undercroft visibility gate remains: new geometry in the `0.255 m` gap under the south slab edge stays at `Y ≥ 2.480 m`.
- The unbuilt Variant B opening at facade `Y 5.940–6.980 m` is comparison history only. It lies outside the built north end `Y 5.700 m`. Do not place the new door there.
- Cited comparison baseline, not a built measurement: Variant B cut `6.552 m²` and a `34.17 m` walk from `D01`. Use those figures only as the comparison the handout names.
- Canonical `blender/kysucka_chata_interier.blend` stays untouched until a separate post-acceptance promotion step. Do not plan bathroom or bedroom fit-out, and do not plan the FT-V19-04 prop micro-detail.
- Original reference objects stay in the files. Visible replacements are recorded. No deletion of envelope meshes.

Working axes, already checked on both scenes: `+X` from the wood bay toward the glazed gable, `+Y` from the entrance toward the north facade, `+Z` up. Units are metres.

## Verified Stage 1 baseline

The Orchestrator recorded the revalidation in `T/00_notes.md`. Reconfirm the pinned hashes before designing. These identities were measured directly:

- Interior candidate `work/v19/kysucka_chata_interier_pivnica_v19.blend`, `425,401,183` bytes, SHA-256 `d9021ee49f63a6dc595214932485597b3b47186b6e26487065c87964dc5dcdf8`. Opens at frame `181` on `Záber 07 | Obývačka a krb`.
- Day exterior `work/v18/recovery/kysucka_chata_exterier_doladeny.blend`, `435,436,722` bytes, SHA-256 `5e8ada70e99c70a3be0a7eea9b18306b422e4ef3a141a63b51b237b7957e3a24`. Opens at frame `1` on `Záber 01 | Chata a údolie`.
- Both files are metric with unit scale `1`.
- Exterior `BASE_slab` and interior `BASE_slab_V19_STUDY`: translation `(7.200, 4.200, 0.325)`, world bounds `X 0..14.400`, `Y 0..8.400`, `Z 0.200..0.450`.
- Hidden interior `BASE_slab` stores location `(7.200, 4.200, 0.325)`. While `hide_viewport` is set, `matrix_world` can read as identity until the view layer is updated. After a temporary unhide and `view_layer.update()` in memory, its world bounds match the exterior slab. Do not save that unhide. Do not treat the stale identity matrix as a moved slab.
- Shared witnesses with matching world transforms in both files: `WALL_left_closed` `(2.55, 4.20, 1.85)` bounds `X 2.40..2.70 × Y 0..8.40 × Z 0.45..3.25`; `D01_leaf`; `WOOD_BAY_rack` bounds `X 0.25..2.15 × Y 0.05..1.05 × Z 0.45..0.53`; `GABLE_other_proposed`; `WALL_front_0_0`; `WALL_rear_0_0`; `V10_FLOOR_oak` bounds `X 2.46..14.40 × Y 0..8.40 × Z 0.451`.
- `V11_TERRAIN_NEAR` has `34,263` vertices in both files. In `X −8..0 × Y −2..9` (`459` vertices), `X −3..0 × Y 4..9` (`84`), and `X −1..1 × Y 0..8.4` (`100`), Z is exactly `−0.055`. The V19 study terrain matches those samples and has `34,270` vertices. This does not certify every other ground mesh or the orchard tree.
- Built west wall `V19_B1_West_Stone`: `X 2.70..2.90`, `Y 2.48..5.70`, `Z −2.25..0.20`. `V19_B1_North_Stone`: `Y 5.50..5.70`.
- Interior lower-landing walk points include `(3.80, 2.925, −2.25)` and `(3.45, 2.925, −2.25)`, then north toward the store door. West store jamb `V19_Store_Jamb_L`: `X 2.92..2.95`, `Y 3.46..3.60`. The open glazed leaf currently reaches about `Y 4.56` near `X 3.90`.
- `work/v19/walk_clearance_v19.json` SHA-256 `5cba280c8d164fcb7ec85eef85f4d70189364e24e07bd528505d3ba93f4a4f35` reports `PASS` for a `Ø 0.700 × 2.100 m` body, step at most `0.045 m`, and minimum side margin `0.015421 m`.
- Envelope file SHA-256 `e58959a22b2d1879828fe87cff645ec3f7ed99a28ec12ae66bfce01c4f6045b8`; 289-object aggregate `8728830343e05888183fc7072b84f0460a948e93257437de67dd6d4f996adb50`. Replacement register `work/v19/slab_envelope_diff.json` SHA-256 `aef9702d53f58638d6510732abc758598a94b6e7d006f1816e12ba955b03e837`.
- No evening reference image is attached. Use the written material and light specification below. Geometry comes from measurement, not from the ERCO page.

## Sources, identity, and repository gate

Working directory: `R = /home/agile/Projects/kysucka_moderna_chata`
Trace directory: `T = /home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20`

Repository identity:

- Project checkout at `R`, branch `main`, expected HEAD `f600c7a8e69a23a029559872652302ac299c2aea`, tracked tree and index clean, local origin at the same commit.
- Public GitHub `main` of `cisarik/kysucka_moderna_chata` was `8218cb3a27a247cc73de940462d21f3bebc27f8a` at planning issuance. It is not an ancestor of the local HEAD. Do not fetch, merge, push, or treat the public tree as the scene authority.
- Governing AP: `d7023cf037f6d17885c3ede5c04812c61640da50` at `.ap`, gitlink equal to submodule HEAD.
- Meta repository `/home/agile/meta`, branch `main`, expected HEAD `ce9d740e8cbf9be96d301a2fe8388c08881eda9c`. A later Cooperator commit, or untracked files under `/home/agile/meta`, is `unrelated-owner-work` or `accepted-continuation` when the pinned scene hashes and project HEAD still match. Do not edit those files.

Mandatory reading:

- Worker spine actually needed: `.ap/AP.md` Semantic Authority and the WORKER minimum-reading row, RF-03, RF-06, RF-12, and §18; `.ap/AP_WORKER.md` Worker Session Target and Reporting; `.ap/PROMPT_CONTRACTS.md` Worker Report Header, Planning Record, Plan-to-Execution Gate, Worker Exchange Identity, and Mutation Axes Record.
- `R/AGENTS.md`, `R/docs/OPERATIONS.md` section for `blender-local-v1`, `R/model/shared_envelope_v18.json` header and datum, `T/00_handout.md`, `T/00_notes.md`.
- V19 evidence as measurements to re-read, not as authority to mutate: `R/work/v19/walk_clearance_v19.json`, `podorys_b1_v19.svg`, `rez_aa_v19.svg`, `slab_envelope_diff.json`, and Meta `projects/kysucka_moderna_chata/00/19-basement-layout-study-v19/01_closure.md` items FT-V19-01, FT-V19-02, and FT-V19-03 only.

Pinned hashes that must be unchanged at the end:

- `blender/kysucka_chata_interier.blend` `c607cb21fbdb289b49f05596004b403e7dd5f96a64e900ce42ed8485f6a30449`
- `work/v19/kysucka_chata_interier_pivnica_v19.blend` `d9021ee49f63a6dc595214932485597b3b47186b6e26487065c87964dc5dcdf8`
- `work/v18/recovery/kysucka_chata_exterier_doladeny.blend` `5e8ada70e99c70a3be0a7eea9b18306b422e4ef3a141a63b51b237b7957e3a24`
- `model/shared_envelope_v18.json` `e58959a22b2d1879828fe87cff645ec3f7ed99a28ec12ae66bfce01c4f6045b8`
- `work/v19/walk_clearance_v19.json` `5cba280c8d164fcb7ec85eef85f4d70189364e24e07bd528505d3ba93f4a4f35`
- `work/v19/podorys_prizemia_v19.svg` `9e61f69a55a4bbf8111439c2140b1b02e2cef4b5e28c958f089f34f97ab59e61`
- `work/v19/podorys_b1_v19.svg` `fd186e9e482b9b90387af5b5498167e9627a27d1c5d59977b77eda68a862d2b5`
- `work/v19/rez_aa_v19.svg` `24b4f8ab81e8583881aee979ead25ad622afbe75c778e51dabdc03875a9871eb`
- `work/v19/slab_envelope_diff.json` `aef9702d53f58638d6510732abc758598a94b6e7d006f1816e12ba955b03e837`
- isolated preferences `work/v12/profile_03/isolated_config/userpref.blend` `d9913bc51a5a8ef87598bd0a4c782661693b9a744a65c60dfa192f0d77e2b561`

## Execution route

Read this whole grant before any repository command. Then perform read-only identity checks. `git status --short --branch`, `git rev-parse`, and SHA-256 reads are part of this grant. Git writes, fetch, checkout, reset, stash, and commit remain prohibited.

Bound route: isolated headless Blender 5.3.0 at `/home/agile/Applications/Blender/blender`. This is a read-only use of the local binary named by `blender-local-v1`. Live MCP and any `tools.blender.*` call are prohibited. Do not attach to a GUI.

Before the first Blender process, record available RAM and the SHA-256 of `/home/agile/.config/blender/5.3/config/userpref.blend`. The issuance value was `ae7a8626c3f41081ac7dde07f2ddcf2ab7d09c807a16ae2bdd5f6d233f88a9c0`. If that file already differs, or if a live `/home/agile/Applications/Blender/blender` GUI is running, stop and report the observed hash and process. Classify that GUI as `unrelated-owner-work`. Do not attach, save, or change preferences.

Run probes with `nice -n 10`, `--background --factory-startup --disable-autoexec --threads 4`, and an isolated environment: `BLENDER_USER_CONFIG`, `XDG_CACHE_HOME`, `TMPDIR`, `TMP`, `TEMP`, and `PYTHONPYCACHEPREFIX` under `/tmp/opencode/v20_plan_s03`, plus `PYTHONDONTWRITEBYTECODE=1`. Load one scene at a time. Require at least 10 GiB available RAM before a load. Temporary mesh experiments stay in that process memory or under that temporary directory. Remove `/tmp/opencode/v20_plan_s03` completely before the report. The global userpref hash after the last probe must equal the hash recorded before the first probe.

## Required planning deliverables

Put all of the following in the session report.

1. **Reconfirm the baseline.** State the two scene hashes, unit scale, the shared witness transforms, the west-stone bounds, and the near-grade samples. Name every additional ground mesh that intersects the proposed polylines, with its measured Z. Measure the orchard tree world position and its horizontal distance to each hypothesis. If a hidden object is used as a witness, update the view layer before reading `matrix_world`, and do not save.

2. **Hypothesis 1 — north of the west shelter, mostly at `X < 0`.** Place the flight mostly outside the slab, beside the northern part of the west shelter, with a short landing and a turn toward a recessed door in the west wall of the store, north of the existing interior lower landing. The door should aim at `V19_B1_West_Stone` on `Y` greater than the landing at `Y ≈ 2.925 m`, preferably into the clear store `Y 3.600–5.500 m`. Give exact world coordinates for the approach spur, upper landing, each flight, intermediate landing, lower landing, threshold, and door. The spur must start on a point that is actually reachable on the existing approach or court and stay on the measured ground surface until the upper landing. Measure terrain Z along the whole polyline, not only the flat `−0.055 m` samples.

3. **Hypothesis 2 — shifted or turned flight partly at the shelter.** Develop this hypothesis in full. Use it as the recommendation only when Hypothesis 1 needs an underground passage that conflicts with the existing B1 walk, or when its measured length, excavation, wood-bay loss, or tree clearance is clearly worse. A partial overlap with the shelter footprint `X 0..2.40 m` is allowed in this hypothesis. Keep the firewood rack and the closed west wall understandable in the west and north views.

4. **Same comparison for both hypotheses.** Report pedestrian length from `D01` and from the existing court or porch to the upper landing; length of the new underground link; west slab-edge cut length and area; visualization-only excavation volume; whether the wood shelter and firewood stay; distance to the measured apple tree; conflict with the interior lower landing and with both door arcs. Draw, for each hypothesis, one metric plan and one metric section. The section shows step elevations, the `−2.250 m` floor, the slab, the terrain contact against the new walls, headroom, and a visible water-collection zone in front of the threshold. Add a schematic west view and north view showing any change to the slab edge, plinth, and the `0.255 m` under-slab gap. Embed the drawings as self-contained SVG in the report, with coordinate tables.

5. **Recommend exactly one route.** State the measured differences that decide it. Specify the exact visualization cut in `BASE_slab`, the plinth, and the terrain as a polygon the Orchestrator can approve or reject. Do not treat that cut as already approved. Keep the south gate `Y ≥ 2.480 m` for the south undercroft. The recommended route includes terrain returns, a continuous handrail, open-edge protection, a non-slip tread surface, a lower landing, and a readable joint at the threshold.

6. **Stair and body numbers.** For the recommended route give riser count, riser, going, `2h+g`, slope, clear width, and the worst headroom on the pitch line. The later implementation test uses the V19 body `Ø 0.700 × 2.100 m` with horizontal step at most `0.045 m`, both directions of **court → B1 → corridor**, a turn on each landing, and the new door plus the existing doors in closed, open, and mid-swing positions. In this planning exchange, test the recommended door arcs and the body envelope far enough to name the tightest clearance, its value, and its location. A full replay of all six old routes is an implementation check; state that split explicitly.

7. **Glazed store door and first shelf.** Test moving the hinge to the west jamb near `X = 2.950 m`, `Y = 3.600 m`, with the leaf toward the west stone. Check the whole leaf arc and the handle against the wall, the shelf, and the new exterior threshold. V19 measured a minimum side margin of `15.42 mm` on its own test body. Remeasure the current first shelf module. The closure text proposed restoring depth `0.381 m`; that depth is a proposal, not a Stage 1 measurement. Approve restoring it only if the new test of both the interior route and the new exterior route still clears the body. Otherwise keep or locally adjust the reduced module and give the resulting bounds.

8. **B1 ceiling.** In the view corresponding to `zaber_b1_pivnica_v19.png` and `CAM_V19_B1_CELLAR`, determine whether the diagonal seam comes from fibers, UV, normals, or lighting. Choose the smallest repair. If separate boards or thin exposed beams would improve that view, compare their depth with the measured clear height `2.390 m` and with the `2.100 m` body. Do not add beams when they would consume the standing clearance without a stated remaining margin.

9. **Light and materials, day and blue hour.** Recessed stone walls, light-gray concrete, slate treads, thin graphite metal. A continuous warm line under the handrail, specified inside `2700–3000 K`, aimed at the treads and the stone joints. At the dark door, one fine vertical line in the reveal that shows the threshold. Matte surfaces and muted repeated reflections. For the later west camera, one daytime profile and one blue-hour profile from the same camera. The control views from the fence and from the meadow must not show the sources directly, blown patches, or a wide uncontrolled spill. Also specify a soft threshold light for the existing interior arrival, compared on the same eye-level corridor frame. Blue hour does not implement `R-V18-01`.

10. **Two candidates, one entrance.** Specify a later build that keeps the two source files frozen and writes new candidates under `work/v20/`, with exact proposed paths. One owned V20 collection carries the same steps, upper landing, walls, door, local terrain cut, and the lights each scene needs, in the same world coordinates. Compare volume, transforms, both thresholds, and door state between the two files. The exterior contains only the B1 fragment required to see or light through the open new door. Original objects that become hidden stay in a named registry. Day and blue-hour settings are separate reproducible scenes, view layers, or profiles. The implementation deliverable list to specify, not to render now, is: one plan, one section, a west day frame and a west blue-hour frame from the same camera, a night detail of the descent, an eye-level corridor view showing the pocket door and the descent direction, a B1 view, the fixed west and north envelope views, and the four V19 reference interior angles used in `fixed_camera_regression_v19.json` (`Záber 07`, `Záber 08`, `CAM_V10_ENTRY`, `CAM_V05_VALLEY_INSIDE`). End-state reporting must include both candidate hashes and every permitted difference from the V18 exterior and the V19 interior. Cold open of each candidate in a separate process remains an implementation check. Canonical promotion into `blender/kysucka_chata_interier.blend` stays a separate later step after Michal accepts the interior candidate.

## Authority and mutation axes

Positive authority: read `R`, `R/work/v18/**`, `R/work/v19/**`, and `/home/agile/meta/projects/kysucka_moderna_chata/00/**`; run read-only Git identity checks as specified above; run the isolated headless probe only inside `/tmp/opencode/v20_plan_s03`; return the complete English report in the session output.

Negative authority: no writes to tracked project files, `R/blender/**`, `R/work/**`, or `/home/agile/meta/**`; no scene save; no live MCP; no change to global Blender preferences; no package or runtime install; no asset download; no Git write, fetch, checkout, reset, stash, or commit; no edit to `T/01_planning_00.md`, `T/01_report_00.md`, `T/02_planning_00.md`, or `T/02_report_00.md`; no closure signal.

Repository mutation: none
Host/remote mutation: bounded temporary directory /tmp/opencode/v20_plan_s03 for isolated headless read-only Blender inspection, removed before the report
Trace persistence: none

External trace disposition: configured
Trace discovery: /home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20
Trace project key: kysucka_moderna_chata
Trace logical-whole projection identity: 20-basement-dual-access-and-interior-integration-v20
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 03_planning_00.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20
Report filename: 03_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: ORCHESTRATOR
Git publication owner: COOPERATOR
Archival: wait-for-report

Relay basis: Native Plan Mode blocks direct file writes, so the Orchestrator is the report persister named before the exchange. Return the complete report in the session. Do not write `T/03_report_00.md`, `T/02_report_00.md`, or `T/01_report_00.md` yourself.

Evidence tier: E1
Evidence tier basis: the route recommendation depends on direct measurements in the two pinned scenes; the probe is read-only and temporary
Validation ladder: not-used
Independent acceptance: not-required

Stopping conditions: project HEAD or a pinned scene hash differs; a live Blender GUI is attached or preferences change across the probe; available RAM is below 10 GiB before a load; the temporary directory remains; an instruction asks for a scene save or for the unbuilt Variant B opening. Stop at the terminal planning report. Planning authority expires there.

Completion and report contract: begin line 1 with exactly `### Report for ORCHESTRATOR_CHAT`. Echo coordinates `kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20`, `03`, `01` once. Include `Status: PASS`, `PARTIAL`, or `BLOCKED`; `Phase-qualified result: not-applicable`; start and end project commit; changed files none; validation of hashes, userpref before/after, RAM, and removal of `/tmp/opencode/v20_plan_s03`; Git result no writes; deviations and risks; one smallest next step; `Report justification: new-evidence`; `Logical-whole closure: not-closed`; authority expiry; `Orchestration critique` with `MEASURED` and `LEAD`; `Resolved Execution Issues / Near-Misses`; and `Pre-Existing Failure Classification`. The Orchestrator will save the session text to `T/03_report_00.md`.

Authority expiry: this terminal planning report, cancellation, or supersession ends this grant. Retained context is not continuing authority.

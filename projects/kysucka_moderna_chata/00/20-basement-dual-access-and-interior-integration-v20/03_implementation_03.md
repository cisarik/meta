# V20 implementation — build the approved H2 entrance into both scenes

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20
Worker session ordinal: 03
Worker exchange ordinal: 04
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker
Phase: implementation
Task identity: BASEMENT-DUAL-ACCESS-V20-IMPL — build the approved Hypothesis 2 entrance in two new work/v20 candidates
Delivery route: manual Cooperator delivery
Independence required: no

Continuity anchor: terminal PASS report T/03_report_02.md, SHA-256 a9e4e7b3381bbbf2918da8261e3bbce440b7e582772f92e49d907a658ca1c952, from Worker exchange 03
Authority renewal: prior report-rendering authority expired; this prompt grants implementation of the approved H2 entrance only
Evidence posture: non-independent

Implementation authority: explicit
Exact baseline: project HEAD f600c7a8e69a23a029559872652302ac299c2aea; frozen plan T/03_report_01.md SHA-256 9c3a1fbbed6af812f02d68b0ee7e4ab4de860c0643988bcb8812eecf15bca118; interior parent work/v19/kysucka_chata_interier_pivnica_v19.blend SHA-256 d9021ee49f63a6dc595214932485597b3b47186b6e26487065c87964dc5dcdf8; exterior parent work/v18/recovery/kysucka_chata_exterier_doladeny.blend SHA-256 5e8ada70e99c70a3be0a7eea9b18306b422e4ef3a141a63b51b237b7957e3a24
Changed-path allowlist: /home/agile/Projects/kysucka_moderna_chata/work/v20/ and /home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20/03_report_03.md
Implementation boundaries: build only the approved H2 entrance, its local slab, stone, and terrain cuts, the stated door and ceiling corrections, the owned lights and review profiles, and the minimum exterior B1 fragment; leave every parent scene byte-identical

## Approved decision

Stay in the session that wrote `T/03_report_02.md`. Plan Mode stays off. Retained context is convenience, not authority. Re-gate the hashes below before the first scene write. If a retained coordinate conflicts with the frozen plan, the frozen plan wins.

The Orchestrator accepts the frozen plan and approves Hypothesis 2 only. Do not build Hypothesis 1. The authority for every coordinate is `T/03_report_01.md` at the hash above. These approved cuts are binding:

- Slab opening, XY `[(0,4.305), (1.040,4.305), (1.040,5.725), (0,5.725)]`, through `Z +0.200…+0.450`, including the west fascia at `X = 0`, `Y 4.305…5.725`. Preserve bevel, UVs, and corner normals outside that polygon.
- West-stone reveal through `X 2.700…2.900`, open YZ rectangle `[(4.540,−2.250), (5.490,−2.250), (5.490,−0.035), (4.540,−0.035)]`, with a `0.040 m` jamb and a `0.035 m` head. Clear opening `Y 4.580…5.450`, head `Z −0.070`, leaf plane `X = 2.790`.
- Terrain cut `[(−4.560,4.305), (2.700,4.305), (2.700,5.725), (−4.560,5.725)]`, with `0.150 m` stone-faced returns. South undercroft gap stays `0.255 m` and no new south-gap geometry starts south of `Y = 2.480`.
- Water channel `X 2.380…2.540`, `Y 4.455…5.575`, invert `−2.410`, flush grate at `−2.250`, and a flush `12 mm` joint at `X = 2.700`.
- Exterior-only near-terrain void `X 2.700…4.360` by `Y 3.600…5.700`, down to `−2.450`, with the visible B1 fragment closed by an east return at `X = 4.360`.
- Stair axis `Y = 5.015`, 13 risers of `0.168846 m`, going `0.280 m`, flights of 7 and 6, clear width `1.040 m` between rails. Upper landing, intermediate landing, lower landing, and threshold are the H2 coordinates in the frozen plan.
- New exterior hinge `(2.790, 5.418)`, leaf `0.828 m`, closed toward `−Y` and open toward `−X`. Existing glazed hinge `(2.973, 3.622)`, leaf span `0.906 m`, opening into the store. Keep the first shelf at its measured reduced depth `0.256 m`.
- Level `V19_Cellar_Key` to face `−Z` at its existing position and power. Add the frozen plan’s 2850 K rail line, south reveal line, and corridor threshold light. Day and blue-hour settings remain separate profiles. Blue hour does not implement `R-V18-01`.

## Sources and outputs

Parents stay byte-identical. Write new candidates only at:

- `work/v20/kysucka_chata_interier_pivnica_v20.blend`, derived from the V19 parent
- `work/v20/kysucka_chata_exterier_pivnica_v20.blend`, derived from the V18 parent

One declarative specification and one builder under `work/v20/` own the shared entrance. Embed collection `V20_B1_ENTRANCE` in both files at identity. It owns the flights, landings, returns, slate, joint, grate, shared door and hardware, local contact pieces, and exterior lights. Door angle `0…90°` defaults to `0°` and matches in both files. Keep replaced originals in `V20_RETAINED_ORIGINALS` with their geometry unchanged. The interior candidate also records the existing V19 study slab as the predecessor of the new derivative. The exterior candidate contains only the B1 fragment needed to see and light through the open new door.

Mask the 40 lawn origins in `V11_CORE_GRASS_V06_LAWN_-001_+000` and the 142 ground-cover origins in `V17_GROUND_COVER_POINTS` that the frozen plan places inside the H2 footprint. Use evaluated extents for pieces that cross the boundary. Do not delete the source vegetation libraries.

Canonical `blender/kysucka_chata_interier.blend` stays untouched. Do not fit out the bathroom or bedrooms. Do not promote either candidate into the canonical interior.

## Execution route

Read this grant before any scene write. Bound route: isolated `/home/agile/Applications/Blender/blender` `5.3.0` with `--background --factory-startup --disable-autoexec`, `nice -n 10`, and `--threads 8`. Use `BLENDER_USER_CONFIG`, caches, and `PYTHONPYCACHEPREFIX` under `/tmp/opencode/v20_impl`. Live MCP is prohibited. Load one scene at a time and require at least 10 GiB available RAM before a load.

Owner PID `96634` was still running at issuance, started `2026-11-25 08:48:32`. A live GUI is `unrelated-owner-work`. Do not signal, attach to, or save it. Record the global userpref hash before the first Blender process and after the last one. The issuance value was `ae7a8626c3f41081ac7dde07f2ddcf2ab7d09c807a16ae2bdd5f6d233f88a9c0`. Your processes must not write that file. If it changes and the change is attributable only to the untouched GUI, do not revert it and continue only when the parent scene hashes are unchanged. If your process may have written it, stop `BLOCKED` and do not revert it.

Remove `/tmp/opencode/v20_impl` before the report. The two candidates and their builder, specification, drawings, and renders under `work/v20/` remain.

## Required result

1. Build both candidates. Re-running the builder on a fresh copy of each parent is idempotent. Compare shared entrance meshes, world transforms, thresholds, and door states at `0°`, `45°`, and `90°`.
2. Walk the `Ø 0.700 × 2.100 m` body with horizontal steps of at most `0.045 m` through court → B1 → corridor and back, including landing turns and the closed, mid, and open door states named in the frozen plan. Replay the six original V19 routes. Record the tightest clearance, object, pose, and coordinates. The south gap and the geometry outside the approved polygons stay equal to the parents.
3. Cold-open each candidate in its own isolated process. Confirm packed dependencies, startup camera and frame preserved from the parent, and no external libraries.
4. Render the frozen plan’s review packet with CPU Cycles, OIDN Accurate/High, seed 0, AgX/None, exposure 0, gamma 1. Use 960×540 and 96 samples for `Záber 07`, `Záber 08`, `CAM_V10_ENTRY`, and `CAM_V05_VALLEY_INSIDE`. Use 1440×810 for the west day and west blue-hour pair from `V20_CAM_WEST`, the night detail, the corridor pair, and the fence and meadow controls. Use 1920×1080 for the B1 ceiling check at `CAM_V19_B1_CELLAR`, with an A/B whose only change is the leveled key light. Include `Záber 05 | Západná strana` and `Záber 04 | Severná strana`. Serialize the renders. Save them under `work/v20/renders/` with a manifest of camera, samples, and file hash.
5. Write one dimensioned H2 plan and one section from the built geometry into `work/v20/`.

## Authority and mutation axes

Positive authority: read the parents, the frozen plan, and `T/03_report_02.md`; write only the allowlist above; run the isolated Blender route; save and read back `T/03_report_03.md`.

Negative authority: no writes to tracked project files, the parent blends, `blender/kysucka_chata_interier.blend`, or any trace file other than `T/03_report_03.md`; no edit to `T/03_report_01.md` or `T/x_03_report_02.md`; no Git write, fetch, commit, or push; no live MCP; no signal to the owner GUI; no asset download; no package install; no canonical promotion; no closure signal.

Repository mutation: /home/agile/Projects/kysucka_moderna_chata/work/v20/
Host/remote mutation: temporary directory /tmp/opencode/v20_impl for isolated Blender, removed before the report; no preference or GUI changes
Trace persistence: direct-write /home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20/03_report_03.md

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
Downloadable prompt filename: 03_implementation_03.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20
Report filename: 03_report_03.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Evidence tier: E2
Evidence tier basis: the new candidates must match the approved cuts, clear the body test, cold-open, and produce the named review renders
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: parent SHA-256 checks and the V19 walk record as the route baseline
Affected tests: H2 clearance, six V19 routes, shared-entrance comparison, cold open of both candidates
New causal regression: none — the parent hashes and the fixed-camera packet are the regression evidence
Broad or full suite: not-used
Runtime or testbed: isolated Blender 5.3.0 under /tmp/opencode/v20_impl
Independent acceptance: not-required

Stopping conditions: a parent hash changes; the owner GUI is attached or signaled; available RAM is below 10 GiB before a load; the temporary directory remains; the build departs from an approved polygon. Stop at the terminal report. This grant does not accept the images and does not close the whole.

Completion and report contract: begin line 1 with exactly `### Report for ORCHESTRATOR_CHAT`. Echo coordinates `kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20`, `03`, `04` once. Include `Status: PASS`, `PARTIAL`, or `BLOCKED`; `Phase-qualified result: implementation-PASS` only if both candidates, the clearance tests, the cold opens, and the review packet are complete, otherwise `not-applicable`; start and end project commit; changed files under `work/v20/` and this report; both candidate hashes and every permitted difference from the two parents; validation summary; Git result no writes; deviations and risks; one smallest next step; `Report justification: new-mutation`; `Logical-whole closure: not-closed`; authority expiry; `Orchestration critique` with `MEASURED` and `LEAD`; `Resolved Execution Issues / Near-Misses`; and `Pre-Existing Failure Classification`. Save the report, read it back, and verify its path and content before the completion notice.

Authority expiry: this terminal report, cancellation, or supersession ends this grant. Retained context is not continuing authority.

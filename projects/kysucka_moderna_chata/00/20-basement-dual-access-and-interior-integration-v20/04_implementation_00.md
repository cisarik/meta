# V20 fresh implementation — stone foundation around the whole cottage

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20
Worker session ordinal: 04
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker
Phase: implementation
Task identity: BASEMENT-DUAL-ACCESS-V20-FOUNDATION-FRESH — from the saved H2 candidates, add one shared artistic stone foundation around the whole cottage
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — the stone must close the floating gap on every visible side and still leave the approved stair, deck, firewood and entry walk clear
Recommended context capacity: approximately 250k tokens
Independence required: no

Implementation authority: explicit
Exact baseline: project HEAD f600c7a8e69a23a029559872652302ac299c2aea; exterior candidate work/v20/kysucka_chata_exterier_pivnica_v20.blend SHA-256 9d5f9399e266783688bb067219cb7e06e76163d2a554569528b5e271a71c6d6e, 446,253,211 bytes; interior candidate work/v20/kysucka_chata_interier_pivnica_v20.blend SHA-256 7114bd8e946180db565d475c88ed5ed2b48c51628c63199ecf382c3c7f7867ed, 437,407,265 bytes
Changed-path allowlist: work/v20/kysucka_chata_exterier_pivnica_v20_zaklad.blend, work/v20/kysucka_chata_interier_pivnica_v20_zaklad.blend, work/v20/foundation/ after preserving the four existing before-renders, and T/04_report_00.md
Implementation boundaries: add only the perimeter foundation and the proof renders; do not rebuild Hypothesis 2, the doors, the ceiling light, the vegetation masks, or the parents

## Why this session is fresh

You have no authority from any earlier chat. Session 03 finished the H2 build. A later current-session correction could not be continued because that agent failed. Its prepared file `T/03_implementation_04.md` is not this grant. Do not resume its process and do not overwrite its unfinished notes as if they were accepted.

If this client is in native Plan Mode, stop `BLOCKED` before opening a scene and name the mode. This grant requires Plan Mode to be off.

## What already exists

Working directory `R = /home/agile/Projects/kysucka_moderna_chata`. Trace directory `T = /home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20`.

Read these, then build. They are evidence, not a license to redesign:

- `T/03_report_03.md`, SHA-256 `6610ed4db1de002fddbb72f3069c74bda7e57e5f2030c762dfc697d0494ac9e8`. Implementation of Hypothesis 2 passed. Both candidates above are that result.
- `T/03_report_01.md`, SHA-256 `9c3a1fbbed6af812f02d68b0ee7e4ab4de860c0643988bcb8812eecf15bca118`. Frozen H2 plan. The Orchestrator approved only Hypothesis 2.
- `work/v20/spec_v20.json`. Numeric authority for the stair, slab notch, stone reveal, terrain cut and cameras.
- `work/v20/build_v20.py`. Shows how the entrance was built. Do not rerun it against the parents.

World axes, metres: `+X` from the wood bay toward the glazed gable, `+Y` from the entrance toward the north facade, `+Z` up. The slab footprint is `X 0…14.400`, `Y 0…8.400`, soffit `Z +0.200`, top `Z +0.450`. Near grade around the cottage is `Z −0.055`. The dark floating gap is that `0.255 m` of empty air.

Approved H2 opening, which stays clear:

- Slab notch `X 0…1.040`, `Y 4.305…5.725`, through `Z +0.200…+0.450`.
- West-stone reveal `X 2.700…2.900`, `Y 4.540…5.490`, `Z −2.250…−0.035`.
- Stair axis `Y = 5.015`, 13 risers, clear width `1.040 m` between rails.
- Exterior hinge `(2.790, 5.418)`. Firewood rack `X 0.250…2.150`, `Y 0.050…1.050`, on the deck top.
- South porch paving roughly `X 0…6.700`, `Y −0.650…0`. Entry steps continue east of that. Do not intersect their walking surfaces.

`work/v20/foundation/` is an unfinished attempt. It has `measurement.json`, `before_west_fixed.png`, `before_north_fixed.png`, `before_west_detail.png`, `before_south.png`, and `renders/manifest.json`. Those four PNGs were rendered from the untouched exterior candidate `9d5f9399…`. There is no `*_zaklad.blend`. Keep the four PNGs and the manifest. You may read `measurement.json`. The scripts there are not authority; replace them with your own builder if they are incomplete.

## The foundation Michal asked for

The whole cottage must visibly sit on a basement. Build an artistic fieldstone base around the entire slab, from measured grade up to the soffit. The white slab fascia `Z +0.200…+0.450` stays as the cap. A stone may overlap that fascia by at most `0.020 m` so the joint is not a black crack. This is a visualization, not a structural footing.

Use material `V20 Recessed stone` where that copy of `V10_MAT_STONE` already exists. Otherwise use `V10_MAT_STONE`. Do not download a material. Do not invent a new image texture.

Make separate stone meshes, not one extruded box. Use one deterministic seed, `13720`, and the same parameters in both candidates so every stone has the same world transform in both files. Target about one course for the `0.255 m` gap, with variation: length `0.35…1.10 m`, height `0.18…0.32 m`, face depth `0.12…0.28 m` outside the slab edge. Stagger the joints. Use larger stones at the four corners. The outer face is uneven. Bed the bottom on the measured terrain of `V11_TERRAIN_NEAR` or its V20 derivative, and bring the top to `Z +0.200`.

Before placing a stone, sample the local grade and the local slab soffit. Skip a stone where porch paving or entry steps already close the gap and would be intersected. Close any remaining visible gap beside them. On the west edge, do not put stone inside the H2 notch `X 0…1.040`, `Y 4.305…5.725`. Turn the perimeter into the existing `V20_Return_*` cheeks so the new base and the stair read as one masonry wall. Do not reduce the clear stair width. Do not cover the deck top, the firewood, or the handrails.

Own the stones in collection `V20_FOUNDATION` in both files. Leave `V20_B1_ENTRANCE` and the rest of the approved scene visible and unmoved.

## Files to write

Copy each baseline candidate and save the copies only at:

- `work/v20/kysucka_chata_exterier_pivnica_v20_zaklad.blend`
- `work/v20/kysucka_chata_interier_pivnica_v20_zaklad.blend`

The two baseline blends, `work/v19/kysucka_chata_interier_pivnica_v19.blend` (`d9021ee4…`), `work/v18/recovery/kysucka_chata_exterier_doladeny.blend` (`5e8ada70…`), and `blender/kysucka_chata_interier.blend` (`c607cb21…`) stay byte-identical.

Put the builder at `work/v20/foundation/build_foundation_v20.py`. Running it twice from the same baselines must produce the same stone transforms.

## How to run Blender

Binary: `/home/agile/Applications/Blender/blender` `5.3.0`. Flags: `--background --factory-startup --disable-autoexec --threads 8`. Prefix with `nice -n 10`. Isolate `BLENDER_USER_CONFIG`, `XDG_CACHE_HOME`, `TMPDIR` and `PYTHONPYCACHEPREFIX` under `/tmp/opencode/v20_foundation_s04`. Live MCP is prohibited. Load one scene at a time. Require at least 10 GiB available RAM before a load.

Owner PID `96634` was still running at issuance, state `SNsl`, started `2026-11-25 08:48:32`, command `/home/agile/Applications/Blender/blender`. It is `unrelated-owner-work`. Do not signal it, attach to it, or save its document. Record `/home/agile/.config/blender/5.3/config/userpref.blend` before the first Blender process and after the last. The issuance hash was `ae7a8626c3f41081ac7dde07f2ddcf2ab7d09c807a16ae2bdd5f6d233f88a9c0`. Your processes must not write that file. If it changes and only the untouched GUI could have written it, do not revert it and continue only when the two baseline hashes are unchanged. If your process may have written it, stop `BLOCKED` and do not revert it.

Remove `/tmp/opencode/v20_foundation_s04` before the report.

## Proof

1. Confirm the two baseline hashes before and after. Confirm both new files contain `V20_FOUNDATION` and the unchanged `V20_B1_ENTRANCE`.
2. Count the stones and report the minimum and maximum of their world bounds. State the tightest horizontal clearance that remains inside the H2 stair. It must stay at least `1.040 m` between rails.
3. Cold-open `kysucka_chata_exterier_pivnica_v20_zaklad.blend` in a second process. Confirm zero external libraries and that the foundation survived the reopen.
4. Reuse the four existing before PNGs only if their bytes still match `work/v20/foundation/renders/manifest.json` and that manifest’s `scene_sha256` is still `9d5f9399…`. Otherwise render them again from the untouched exterior baseline.
5. From the new exterior candidate, render the same four cameras at 1440×810, CPU Cycles, 96 samples, seed 0, OIDN Accurate/High, AgX/None, exposure 0, gamma 1: `Záber 05 | Západná strana`, `Záber 04 | Severná strana`, `V20_CAM_WEST`, and `V20_FOUNDATION_CAM_SOUTH`. The south camera position in the before manifest is `(7.400, −14.700, 3.250)`, lens 32 mm, sensor 36×24 mm, horizontal fit, clip 0.045…1000, frame 1. Match that transform. Save the after PNGs beside the before PNGs and extend the manifest with their hashes.
6. The west and north after-frames must show stone from the grass up to the slab. The stair mouth stays open. The firewood stays on the deck. The south frame must still show the entry steps and paving as a walkable surface.

## Authority and mutation axes

Positive authority: read `R/work/v18`, `R/work/v19`, `R/work/v20` and `T`; write only the allowlist; run the isolated Blender route; save and read back `T/04_report_00.md`.

Negative authority: no overwrite of the two baseline V20 candidates, the V19 or V18 parents, or `blender/kysucka_chata_interier.blend`; no edit to `T/03_report_01.md`, `T/03_report_03.md`, or `T/03_implementation_04.md`; no Git write, fetch, commit, or push; no live MCP; no signal to PID `96634`; no asset download; no package install; no canonical promotion; no closure signal.

Repository mutation: the two zaklad blends and work/v20/foundation/ only, preserving the four before PNGs and their current manifest entries
Host/remote mutation: temporary directory /tmp/opencode/v20_foundation_s04 for isolated Blender, removed before the report; no preference or GUI changes
Trace persistence: direct-write /home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20/04_report_00.md

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
Downloadable prompt filename: 04_implementation_00.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20
Report filename: 04_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Evidence tier: E2
Evidence tier basis: both new candidates must carry the same foundation, the approved stair must stay open, and the west and north frames must show stone from grade to the slab
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: the two baseline SHA-256 values and the before-render manifest
Affected tests: stone-transform comparison between the two new files, stair clearance, cold open, four after-renders
New causal regression: none — the before/after pairs are the regression evidence
Broad or full suite: not-used
Runtime or testbed: isolated Blender 5.3.0 under /tmp/opencode/v20_foundation_s04
Independent acceptance: not-required

Stopping conditions: a baseline or parent hash changes; this client is in Plan Mode; stone blocks the stair or covers the deck or the entry walk; the owner GUI is signaled; available RAM is below 10 GiB before a load; the temporary directory remains. Stop at the terminal report. Michal accepts the images later.

Completion and report contract: begin line 1 with exactly `### Report for ORCHESTRATOR_CHAT`. Echo coordinates `kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20`, `04`, `01` once. Include `Status: PASS`, `PARTIAL`, or `BLOCKED`; `Phase-qualified result: implementation-PASS` only when both zaklad files, the cold open and the four after-renders exist, otherwise `not-applicable`; start and end project commit; changed files on the allowlist; both new SHA-256 values; confirmation that both baseline hashes are unchanged; stone count and stair clearance; validation summary; Git result no writes; deviations and risks; one smallest next step; `Report justification: new-mutation`; `Logical-whole closure: not-closed`; authority expiry; `Orchestration critique` with `MEASURED` and `LEAD`; `Resolved Execution Issues / Near-Misses`; and `Pre-Existing Failure Classification`. Save `T/04_report_00.md`, read it back, and verify the path and the header before the completion notice.

Authority expiry: this terminal report, cancellation, or supersession ends this grant. Retained context is not continuing authority.

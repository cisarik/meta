# V20 fresh implementation — creative path from the entrance to the basement

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20
Worker session ordinal: 05
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker
Phase: implementation
Task identity: BASEMENT-DUAL-ACCESS-V20-PATH — add a creative exterior walk from the front entrance to the basement stair, and show it with the stone foundation
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — the path must be readable in exterior views, stay clear of the apple tree, firewood and entry steps, and meet the approved stair without narrowing it
Recommended context capacity: approximately 250k tokens
Independence required: no

Implementation authority: explicit
Exact baseline: project HEAD f600c7a8e69a23a029559872652302ac299c2aea; exterior work/v20/kysucka_chata_exterier_pivnica_v20_zaklad.blend SHA-256 394a818c86c1908c3b1cc097f0445a540efd7cea72fa491bbc4602d91a96950e, 446,304,345 bytes; interior work/v20/kysucka_chata_interier_pivnica_v20_zaklad.blend SHA-256 e9458c7ad47e235473d3799bdb1c7b1acc52b3a73baf705a770a1b37176126f5, 437,448,405 bytes
Changed-path allowlist: work/v20/kysucka_chata_exterier_pivnica_v20_chodnik.blend, work/v20/kysucka_chata_interier_pivnica_v20_chodnik.blend, work/v20/path/, and T/05_report_00.md
Implementation boundaries: add only the new walk, its edge and a few shielded lights; keep the 53 foundation stones, the H2 stair and every parent byte-identical

## What Michal wants

You are a new session. Earlier chats are not authority. If this client is in native Plan Mode, stop `BLOCKED` before opening a scene.

The stone course already exists and must remain. Michal has now said the exterior must also show a path from the main entrance to the basement entrance, and that the path should be creative. The existing south walk stops at the front door. The basement stair is on the north part of the west side and currently opens onto grass. Connect those two with a designed garden walk.

This is a visualization, not a road or drainage design.

## Scene facts

Axes, metres: `+X` from the wood bay toward the glazed gable, `+Y` from the entrance toward the north facade, `+Z` up.

- Slab `X 0…14.400`, `Y 0…8.400`, soffit `+0.200`, top `+0.450`. Grade near the house is about `−0.055`.
- Front door `D01_leaf` is on the south side, about `X 7.250…8.500`, `Y −0.105…−0.015`. A straight pale path already leads to it from the south. Keep that path.
- Porch paving is about `X 0…6.700`, `Y −0.650…0`. Entry steps are just east of the door. Do not cover their treads.
- Firewood rack `X 0.250…2.150`, `Y 0.050…1.050`, on the west deck. Leave it.
- Apple `V04_ORCHARD` is about `(−1.100, −2.600)`. A short line near `(−0.78, −0.68)` was already too close to its low branches. Keep the body `Ø 0.700 m` at least `0.90 m` clear of the trunk origin and clear of the low evaluated canopy. Measure it; do not guess.
- Basement stair, Hypothesis 2, stays: axis `Y = 5.015`, upper landing near `X −4.560…−3.360` at grade `−0.055`, then east into the notch `X 0…1.040`, `Y 4.305…5.725`. Clear width `1.040 m`. Exterior hinge `(2.790, 5.418)`. Collection `V20_B1_ENTRANCE` has 245 objects. Do not move them.
- Foundation collection `V20_FOUNDATION` has 53 meshes of `V20 Recessed stone`, seed `13720`, world bounds about `(−0.280, −0.280, −0.089)` to `(14.680, 8.680, 0.220)`. Do not delete or rescale them. The path may meet their outer face; it may not bury them.

Read `work/v20/spec_v20.json` and `T/04_report_00.md` before building. The report SHA-256 is `549f2d46cb9b66123dbd0b14647934526274f38d501302e1869142b4302ad243`.

## The walk

Own it in collection `V20_ENTRANCE_PATH` in both new files, with the same world transforms. Seed the variation with `13721`.

Start from the existing south path or the court just west of `D01`, on a point a person can already step onto. End flush with the upper landing of the basement stair, so the last flags become the threshold of the descent. Stay on measured grade. Do not climb onto the deck.

Shape: a calm designed walk from the front door to the stair, not a rectangle and not the long engineering bypass in the old plan. Use two or three gentle bends. Width varies from `1.10 m` to `1.60 m`. The surface is large pale stone flags, close in role to the existing front path and to the paved arrival Michal showed: readable as one route, with a few wider flags and a broken edge rather than a clipped corridor. Use packed `V10_MAT_STONE_SLAB` if it is in the file, otherwise a light concrete or `V20 Recessed stone` at a flat scale. Joints stay narrow, `8…20 mm`. One wider pause, about `2.0 m`, marks the turn from the south side toward the west stair. The last flags land flush with the upper stair landing and use the same surface as the first stair treads, so the descent begins from the walk.

Add three or four small shielded lights, `2700…3000 K`, aimed at the flags. No bare bright sources and no row of identical bollards. Reuse an existing warm light material or a small area light. They stay off in the daytime frames.

The `Ø 0.700 × 2.100 m` body must be able to walk the flags from the branch point to the upper landing with horizontal steps of at most `0.045 m`, without hitting the apple, the foundation, the firewood or the stair rails. Record the tightest clearance.

## Files and Blender

Copy the two zaklad candidates and save only:

- `work/v20/kysucka_chata_exterier_pivnica_v20_chodnik.blend`
- `work/v20/kysucka_chata_interier_pivnica_v20_chodnik.blend`

Write the builder at `work/v20/path/build_path_v20.py`. The zaklad files, the older V20 candidates, the V19 and V18 parents, and `blender/kysucka_chata_interier.blend` stay byte-identical.

Binary `/home/agile/Applications/Blender/blender` `5.3.0`, `--background --factory-startup --disable-autoexec --threads 8`, `nice -n 10`. Isolate config and caches under `/tmp/opencode/v20_path_s05`. Live MCP is prohibited. One scene at a time. At least 10 GiB free RAM before a load.

Owner PID `96634` may still be running. It is `unrelated-owner-work`. Do not signal it or save its file. Userpref issuance hash `ae7a8626c3f41081ac7dde07f2ddcf2ab7d09c807a16ae2bdd5f6d233f88a9c0`. Your processes must not write it. Remove `/tmp/opencode/v20_path_s05` before the report.

## Proof renders

From the new exterior file only, CPU Cycles, 96 samples, seed 0, OIDN Accurate/High, AgX/None, exposure 0, gamma 1, 1440×810, daytime, path lights off:

- `Záber 05 | Západná strana` — stone base, open stair, and the arriving walk.
- `Záber 04 | Severná strana` — the stone base still continuous; the new walk may be out of frame.
- The existing south entrance camera if one is already named for the front door; otherwise a new camera `V20_PATH_CAM_SOUTH` from about `(7.400, −14.700, 3.250)`, 32 mm, looking north, showing the old front path and the new branch.
- A new camera `V20_PATH_CAM_LINK` placed so one frame shows the front-door side and the walk continuing to the basement stair. Record its matrix.

Save them under `work/v20/path/renders/` with a hash manifest. Cold-open the exterior chodnik file in a second process and confirm `V20_FOUNDATION`, `V20_B1_ENTRANCE` and `V20_ENTRANCE_PATH` are present, with zero external libraries.

## Authority and mutation axes

Positive authority: read `work/v20`, `work/v19`, `work/v18` and `T`; write only the allowlist; run the isolated Blender route; save and read back `T/05_report_00.md`.

Negative authority: no overwrite of the zaklad blends or older candidates; no edit to prior reports; no Git write; no live MCP; no signal to PID `96634`; no asset download; no package install; no canonical promotion; no closure signal.

Repository mutation: the two chodnik blends and work/v20/path/ only
Host/remote mutation: temporary directory /tmp/opencode/v20_path_s05 for isolated Blender, removed before the report; no preference or GUI changes
Trace persistence: direct-write /home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20/05_report_00.md

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
Downloadable prompt filename: 05_implementation_00.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20
Report filename: 05_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Evidence tier: E2
Evidence tier basis: the walk must be visible from the entrance to the stair in the exterior frames, and the foundation and stair must remain
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: zaklad SHA-256 and the foundation object count
Affected tests: body clearance along the walk, cold open, four exterior frames
New causal regression: none — the new frames are the visual evidence
Broad or full suite: not-used
Runtime or testbed: isolated Blender 5.3.0 under /tmp/opencode/v20_path_s05
Independent acceptance: not-required

Stopping conditions: a zaklad or parent hash changes; the client is in Plan Mode; the walk blocks the stair, covers the deck or the front steps, or hits the apple; the owner GUI is signaled; RAM is below 10 GiB before a load. Stop at the terminal report. Michal accepts the pictures.

Completion and report contract: begin line 1 with exactly `### Report for ORCHESTRATOR_CHAT`. Echo coordinates `kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20`, `05`, `01` once. Include `Status: PASS`, `PARTIAL`, or `BLOCKED`; `Phase-qualified result: implementation-PASS` only when both chodnik files, the clearance numbers, the cold open and the renders exist, otherwise `not-applicable`; start and end commit; changed files; both new SHA-256 values; unchanged zaklad hashes; the walk polyline and the tightest clearance; Git result no writes; deviations and risks; one smallest next step; `Report justification: new-mutation`; `Logical-whole closure: not-closed`; authority expiry; `Orchestration critique` with `MEASURED` and `LEAD`; `Resolved Execution Issues / Near-Misses`; and `Pre-Existing Failure Classification`. Save the report, read it back, and check the header before the completion notice.

Authority expiry: this terminal report, cancellation, or supersession ends this grant. Retained context is not continuing authority.

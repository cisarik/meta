# V20 correction — stone foundation around the whole cottage

Persistent role identity: WORKER
Logical whole identity: kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20
Worker session ordinal: 03
Worker exchange ordinal: 05
Worker session target: current-worker-session
Native planning mode: not-used
Worker session profile: Implementation Worker
Phase: implementation
Task identity: BASEMENT-DUAL-ACCESS-V20-FOUNDATION — add an artistic stone foundation under the whole cottage so the basement reads and the slab no longer floats
Delivery route: manual Cooperator delivery
Independence required: no

Continuity anchor: terminal implementation-PASS report T/03_report_03.md, SHA-256 6610ed4db1de002fddbb72f3069c74bda7e57e5f2030c762dfc697d0494ac9e8, from Worker exchange 04
Authority renewal: prior implementation authority expired; this prompt grants only the perimeter stone foundation on new candidate copies
Evidence posture: non-independent

Implementation authority: explicit
Exact baseline: exterior candidate work/v20/kysucka_chata_exterier_pivnica_v20.blend SHA-256 9d5f9399e266783688bb067219cb7e06e76163d2a554569528b5e271a71c6d6e; interior candidate work/v20/kysucka_chata_interier_pivnica_v20.blend SHA-256 7114bd8e946180db565d475c88ed5ed2b48c51628c63199ecf382c3c7f7867ed; project HEAD f600c7a8e69a23a029559872652302ac299c2aea
Changed-path allowlist: /home/agile/Projects/kysucka_moderna_chata/work/v20/kysucka_chata_exterier_pivnica_v20_zaklad.blend, /home/agile/Projects/kysucka_moderna_chata/work/v20/kysucka_chata_interier_pivnica_v20_zaklad.blend, /home/agile/Projects/kysucka_moderna_chata/work/v20/foundation/, and /home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20/03_report_04.md
Implementation boundaries: add shared world-space foundation stones from measured grade to the slab soffit around the whole footprint, tied into the existing H2 stair returns; do not rebuild the stair, doors, lights, ceiling, or vegetation

## Cooperator decision

Michal reviewed the built exterior and rejected the floating slab. The whole cottage must visibly sit on a basement. Build an artistic stone foundation around the entire house, in effect the visible base, from the ground up to the slab. This is a visualization. It is not a structural, waterproofing, or footing design.

The empty band that reads as levitation is the retained undercroft from terrain near `Z −0.055` up to the slab soffit at `Z +0.200`. The white slab fascia from `+0.200` to `+0.450` stays as the cap. Stone closes the dark gap. A few stones may tuck at most `0.020 m` onto that fascia so the joint is not a black crack. Do not cover the deck, the firewood, the paving walk, or the stair opening.

Stay in the session that wrote `T/03_report_03.md`. Plan Mode stays off. Retained context is convenience, not authority. The two baseline candidates remain byte-identical. Write new files:

- `work/v20/kysucka_chata_exterier_pivnica_v20_zaklad.blend`
- `work/v20/kysucka_chata_interier_pivnica_v20_zaklad.blend`

## Foundation

Measure the visible gap on all four sides before placing stones. Use the existing packed stone material already used on the B1 walls. Do not download a new asset.

Place an irregular fieldstone base around the full slab footprint `X 0…14.400`, `Y 0…8.400`. Courses vary: length about `0.35…1.10 m`, height about `0.18…0.32 m`, and face depth about `0.12…0.28 m`, with staggered joints and larger quoins at the corners. The outer face is uneven, not a single extruded box. Stones bed on the measured terrain and the top course meets the soffit at `+0.200`. Where porch paving or entry steps already close the gap, stop the new stones against them without intersecting the walking surface. Where a gap remains beside those elements, close only that gap.

Keep the approved H2 opening clear: slab notch `X 0…1.040`, `Y 4.305…5.725`, and the west-stone reveal. Turn the new perimeter stones into the existing stair returns so the foundation and the stair read as one masonry base. Do not add stones inside the clear stair width.

Put the same stone meshes, at the same world transforms, in both candidates, in an owned collection `V20_FOUNDATION`. Preserve `V20_B1_ENTRANCE` and every previously approved object. Hide nothing that the H2 build left visible except where a new stone fully replaces an empty view of the gap.

## Route and proof

Use isolated `/home/agile/Applications/Blender/blender` `5.3.0`, `--background --factory-startup --disable-autoexec`, `nice -n 10`, `--threads 8`, and `BLENDER_USER_CONFIG` under `/tmp/opencode/v20_foundation`. Live MCP is prohibited. Owner PID `96634`, if still present, is `unrelated-owner-work`. Do not signal or attach to it. Record the global userpref hash before and after. The issuance value was `ae7a8626c3f41081ac7dde07f2ddcf2ab7d09c807a16ae2bdd5f6d233f88a9c0`. Your processes must not write that file. Remove `/tmp/opencode/v20_foundation` before the report.

Require at least 10 GiB available RAM before loading a scene. Load one scene at a time.

Render from the existing exterior candidate, before the change, and from the new exterior candidate: `Záber 05 | Západná strana`, `Záber 04 | Severná strana`, and `V20_CAM_WEST` daytime. Add one south view that shows the entry steps and paving. Use the same CPU Cycles settings as the H2 packet: 96 samples, OIDN Accurate/High, seed 0, AgX/None, exposure 0, gamma 1, 1440×810. Save the four pairs under `work/v20/foundation/renders/` with a hash manifest. The west and north pairs must show stone from the grass to the slab, with the stair still open and the firewood still on the deck.

Cold-open the new exterior candidate in a separate process and confirm the foundation collection, the unchanged H2 entrance, and no external libraries.

## Authority and mutation axes

Positive authority: read the two baseline candidates and the H2 plan; write only the allowlist; run the isolated Blender route; save and read back `T/03_report_04.md`.

Negative authority: no overwrite of the two baseline V20 candidates, the V19 or V18 parents, or `blender/kysucka_chata_interier.blend`; no edit to prior trace reports; no Git write; no live MCP; no signal to the owner GUI; no asset download; no package install; no canonical promotion; no closure signal.

Repository mutation: the two new zaklad blends and work/v20/foundation/ only
Host/remote mutation: temporary directory /tmp/opencode/v20_foundation for isolated Blender, removed before the report; no preference or GUI changes
Trace persistence: direct-write /home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20/03_report_04.md

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
Downloadable prompt filename: 03_implementation_04.md
Destination path: /home/agile/meta/projects/kysucka_moderna_chata/00/20-basement-dual-access-and-interior-integration-v20
Report filename: 03_report_04.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER
Git publication owner: COOPERATOR
Archival: wait-for-report

Evidence tier: E2
Evidence tier basis: the new stone must be visible from grade to the slab in the west and north views while the approved stair and parents stay intact
Validation ladder: selected
Inspection and provenance: required
Existing focused tests: baseline candidate SHA-256 checks
Affected tests: cold open of the new exterior candidate and the four before/after render pairs
New causal regression: none — the paired west and north frames are the regression evidence
Broad or full suite: not-used
Runtime or testbed: isolated Blender 5.3.0 under /tmp/opencode/v20_foundation
Independent acceptance: not-required

Stopping conditions: a baseline candidate hash changes; the stair opening is blocked; stone covers the deck or the entry walk; the owner GUI is signaled; available RAM is below 10 GiB before a load. Stop at the terminal report. Image acceptance remains with Michal.

Completion and report contract: begin line 1 with exactly `### Report for ORCHESTRATOR_CHAT`. Echo coordinates `kysucka-moderna-chata-basement-dual-access-and-interior-integration-v20`, `03`, `05` once. Include `Status: PASS`, `PARTIAL`, or `BLOCKED`; `Phase-qualified result: implementation-PASS` only when both new candidates, the cold open, and the four render pairs exist, otherwise `not-applicable`; start and end project commit; changed files on the allowlist; both new hashes; confirmation that the two baseline hashes are unchanged; validation summary; Git result no writes; deviations and risks; one smallest next step; `Report justification: new-mutation`; `Logical-whole closure: not-closed`; authority expiry; `Orchestration critique` with `MEASURED` and `LEAD`; `Resolved Execution Issues / Near-Misses`; and `Pre-Existing Failure Classification`. Save the report, read it back, and verify it before the completion notice.

Authority expiry: this terminal report, cancellation, or supersession ends this grant. Retained context is not continuing authority.

# Reference camera perspective - logical whole 02

Handout status: provisional
Author: read-only Master Chat Orchestrator
Author session scope: development-run
Development run identity: kysucka-moderna-chata-reference-visualization
Recipient access profile: Orchestrator
Recipient session scope: logical-whole
Logical whole identity: kysucka-moderna-chata-reference-camera-perspective
Destination: cisarik/meta, projects/kysucka_moderna_chata/00/02-reference-camera-perspective/00_handout.md
Prepared: 2026-11-14, Europe/Bratislava
Artifact lifecycle: operational handoff to this whole's Orchestrator; linked from the Master run map; freeze on opening and retain as historical evidence; cleanup owner COOPERATOR under an exact grant

## One outcome

Improve the cottage's **actual 3D camera perspective** against
`reference/kysucka_chata_moderna.png`, starting from the accepted v01 working
scene. Deliver a justified camera choice, a saved v02 scene and comparable
renders. Keep the building, materials, world, lights, interior and landscape
unchanged so this is a coherent camera comparison.

You and your Workers already have working Blender MCP. Use it immediately:
after brief repository reconciliation, **you inspect the active scene and
camera view yourself through MCP**, then delegate one concise native-Plan-Mode
Planner and a separately authorized implementation. At acceptance inspect
the candidate scene and actual rendered images yourself. Do not make MCP
installation, AP initialization or another environment inventory the outcome.
The Master stays read-only and prepares handouts, not your Worker grants.

Communicate with Michal in Slovak, feminine self-reference; Worker prompts and
reports are English. Preserve the selected manual delivery and model choice;
recommend Medium. Materially different routing is a Cooperator decision.

## Accepted starting boundary and evidence

Public sources independently inspected by Master on 2026-11-14:

| Source | Anchor |
|---|---|
| Project https://github.com/cisarik/kysucka_moderna_chata / main | `f0fb0ea25fcd091ff05e5e3717c433c586cac4fa` |
| Project .ap gitlink | `d7023cf037f6d17885c3ede5c04812c61640da50` |
| Meta https://github.com/cisarik/meta / main | `4db94c333340c6b77d06701d050de286c701dabc` |

The predecessor is `00/01-blender-mcp-first-reference-render/01_closure.md`,
now publicly present. Its closure and MCP receipts establish a completed
working-control/frame-shift whole. Do not repeat it or reopen initialization.
Master inspected the original reference and both supplied PNGs; their hashes
match the preceding closure. The after PNG also matches its public Git blob.

- Start scene: `blender/kysucka_chata_mcp_v01.blend`, recorded SHA-256
  `227edd9356a0e2917486351bce6e6fdbb62c58eacbfbb96101c1872d5235e4a8`.
- Reference: unchanged 1448 x 1086, SHA-256
  `05bc3e72161e5945379c86da80450ffdf82ddce6dbdd9b9e77071aa79cdecc96`.
- Predecessor after render: 640 x 480, SHA-256
  `bf5e95c925446a7c6a317e117f07ce80e4ac28ab79e379976412c8a814017801`.
- Camera: `CAM_A_REFERENCE`; location (27.5, -15.5, 1.7), target
  (7.45, 3.15, 1.7), 50 mm lens, 36 mm sensor, shift_y 0.075.
- The only previous image-affecting change was shift_y 0.17 -> 0.075:
  about 60.8 pixels upward at 640 x 480. It did not change perspective.
- Previous comparison: Cycles CPU, 32 samples, denoising off, frame 0, seed 0,
  AgX, look None, exposure 0, gamma 1. Measured renders took about 5 seconds
  on that host; this is historical measurement, not a future timing guarantee.
- The green opaque Material Preview appearance was diagnosed; actual Cycles
  glass is already transparent. Do not re-diagnose or tint-replace that glass.

Read current AGENTS.md, docs/OPERATIONS.md, the pinned role spine/contracts,
current camera JSON, predecessor closure and focused MCP receipts. The previous
MCP grant expired. Your new prompts must explicitly reactivate the existing
`blender-mcp-live-v1` route for this whole: do not treat the predecessor's
task-specific route text as continuing mutation authority. No installation or
AP update is selected. The observed add-on protocol warning did not prevent
the predecessor's operations; a warning alone is not an upgrade requirement.

At the inspected Meta commit the predecessor's before.png and
renders/render_metadata.json were absent from the public tree, although the
report says they were saved locally. The before image is available in the
Master chat with the matching recorded hash. Classify this as an archival
gap, not model corruption or a reason for another infrastructure whole.
Cooperator can archive exact missing files prospectively. Do not claim those
paths public or rewrite prior outcomes/history. Discover actual local roots
and preserve unrelated owner work; current live/dirty state is not known here.

## Visual question to answer

Master's comparison supports camera calibration before finer material work:

| Relationship | Current limitation / next control |
|---|---|
| Long roof/eave and entrance side | Relative depth and convergence differ from the reference; changing vertical shift cannot solve those relationships. |
| Entrance facade versus glazed gable | Compare their apparent widths, corner positions, door/window placement and near/far scale; avoid judging only the roof apex. |
| Interior read through glass | The fireplace can be obscured by a mullion/corner from this view. Test parallax before moving any interior object. |
| Foreground fence and house depth | Current foreshortening contributes to the miniature-like presentation; evaluate perspective, not fence remodeling. |

The predecessor suggested moving the viewpoint left and closer. Treat that as
a hypothesis, not a prescribed world-axis delta. Establish Blender/world/image
axes and test the actual projections. Position, viewing direction, focal length
and sensor shift have different effects; lens and distance can be adjusted
together to preserve house size while changing perspective.

Allowed camera variables form one coherent solve: camera location/height,
orientation or look target, lens and framing shift. Preserve an upright, plausible
architectural view and useful headroom. Shift_y 0.075 is the accepted start,
not an immutable optimum when viewpoint changes. Do not mirror, stretch or
post-warp the image or deform the building to imitate an inconsistent reference.

Use 4-6 clearly corresponding landmarks and facade/roof ratios. Normalize to
top-left image coordinates (u=x/width, v=y/height). The existing
model/reference_landmarks.json is approximate manual annotation, not a strict
ground truth. Check the correspondence in the real images before scoring it;
different eave/fascia corners must not be paired accidentally. As orientation,
the reference gable apex is near (0.8605, 0.0875), while v01 was measured near
(0.8611, 0.1249). One apex match does not establish a perspective match.

Define the few comparison controls before choosing the candidate; record
remaining mismatches. An AI-generated image may not admit an exact coherent
camera fit. Do not overfit noisy pixels, invent sub-pixel accuracy, or blame
the fixed model without a bounded camera comparison.

## Finite workflow

Open 00_notes.md with the handout-revalidation record. Actual Worker numbering
starts at 01, normal Meta mapping, no +1 exception:

- First Planner: 01/01, fresh-worker-session, Native planning mode required;
  `01_planning_00.md` and `01_report_00.md`.
- Reconcile its concise plan, then renew the healthy same Worker for
  implementation: 01/02, Native planning mode not-used;
  `01_implementation_01.md` and `01_report_01.md`.

The Planner should answer only: which perspective discrepancy to target;
which at-most-three meaningful camera candidates to compare; exact source/
scene/output scope, checkpoints, preservation and acceptance. Reuse your MCP
observations. Do not request full replacement governance text, a broad audit,
new infrastructure or another completed-scene inventory. Resolve the real
native Plan Mode report-save route before delivery: direct Worker persistence
when permitted; otherwise a named capable persister stores its complete exact
report. A finished plan needs no new planning cycle merely to save it.

Implementation uses one preserved v01 baseline, up to three purposeful camera
candidates at cheap matched preview settings, then one chosen camera's final
comparison render. A labelled candidate sheet is useful. This is an experiment
budget, not an instruction to keep producing variants until context is exhausted.
If candidates are worse, do not promote one or claim improvement: return the
measured trade-off/residual and one exact Master decision. No speculative
geometry/material repair or automatic second camera-planning cycle follows.

## Implementation boundaries and outputs

Protect any live unsaved owner state before changing camera settings. Use
unique checkpoints and v02, never overwrite v01 or the original seed. Read the
actual input path/dirty state through MCP; no forced reopen over dirty work.

Required results, placed under an exact current implementation grant:

| Location | Purpose |
|---|---|
| Project blender/kysucka_chata_mcp_v02.blend | chosen working camera scene, saved and reopenable |
| Project model/parameters.json | accepted camera values matching the saved camera and existing generator |
| This Meta whole renders/before.png and renders/after.png | fresh, matched-size 4:3 comparison with unchanged world/material/light/render profile |
| This Meta whole evidence/camera_comparison.md | baseline/candidate parameters, verified landmark/ratio comparison, actual MCP read/change/readback, choice and residuals |
| This Meta whole renders/render_metadata.json | scene/camera identity, matrices or target, optics/shift, actual render settings, device classification and artifact hashes |

Keep the existing generator as source owner: it already reads the camera
parameters. Update only camera JSON fields actually accepted and verify their
direction/projection agrees with the working .blend. Do not silently introduce
a manual camera that regeneration will lose. Preserve canonical saved output
settings separately from cheap preview settings, as the predecessor did.

Potential ancillary changes are limited to the current-working-file/camera/MCP
route portions of AGENTS.md, docs/OPERATIONS.md and README_SK.md. Fresh Planner
proposes an exact allowlist; the implementation grant authorizes it. Do not
touch the managed AP block or closure-signal stanza, and do not ask a Worker
to reproduce the literal closure signal in its plan/report.

Unchanged: seed and v01, all non-camera object geometry/transforms, materials,
glass, world, lights, vegetation, architecture, CAD/PDF, historical previews,
inventories, .ap pin and protocol. No downloads, generators, config installs,
paid services or shell-environment repairs. Project-authored Linux shell is fish.

Declare all three mutation axes coherently: exact project source/output paths;
live Blender camera/checkpoint/render effects; exact Meta report/evidence writes.
Do not demand PNGs while forbidding their writes. CLI may support Git, hashing
and a cold saved-file check; camera control and visual inspection use MCP.
One accountable Worker stream. Scope Git commit/non-force publication explicitly
in the current grant; Meta Git remains Cooperator-owned, with prompt/report
pairs first-added together after the report exists. No archival investigation
or independent-audit chain is required for this reversible camera-only slice.

## Acceptance and closeout

You inspect the saved candidate and comparison pixels yourself via MCP. Read
back the final camera independently of the write and verify v01/seed/reference
preservation and unchanged non-camera scene state. Actual rendering and the
accepted JSON camera agree; public project publication, when granted, is proved
on the exact candidate. Do not confuse a separate tool read with an independent
Worker audit, or a camera metric with Michal's subjective acceptance.

The closeout (normally 01_closure.md) returns: actual project commit and v02;
before/after/candidate images; why perspective is closer and where it still
differs; camera parameters and replay/source relationship; MCP receipts;
expired grants/no active render; and Michal's actual feedback or NOT TESTED.
Keep the frame comparison about perspective: do not attribute unchanged noise,
flat proxy planting or grey-blue sky to this camera correction.

Only the whole's Orchestrator emits the already declared closure signal after
its gates pass. Return this whole's packet to Master, who will choose the next
visual scope. Sky/daylight and material/landscape realism remain later candidates,
not work to append while this Worker still has context.

## Master run-map snapshot

The public run map inspected at 4db94c3 still had the old wrong reference name
and provisional statuses. The following exact Master-authored snapshot is for
mechanical persistence at projects/kysucka_moderna_chata/00/00_RUN_MAP.md under
an explicit positive path grant; inspect current content and preserve history.
It grants no implementation. Do not rewrite frozen predecessor notes/handouts.

```text
Run map: kysucka-moderna-chata-reference-visualization
Run objective: converge the editable Blender scene toward reference/kysucka_chata_moderna.png; architectural checking is deferred
Run map authority: discovery-only
Run entry: 00 | kysucka-moderna-chata-ap-meta-initialization | closed | depends on: none | handout: projects/kysucka_moderna_chata/00/00-init/00_handout.md | evidence: completed project foundation at b47cce6f91ae10a22fb708a8e5220ab27b471aeb
Run entry: 01 | kysucka-moderna-chata-blender-mcp-first-reference-render | closed | depends on: kysucka-moderna-chata-ap-meta-initialization | handout: projects/kysucka_moderna_chata/00/01-blender-mcp-first-reference-render/00_handout.md | evidence: public f0fb0ea25fcd091ff05e5e3717c433c586cac4fa, v01, MCP read/change/readback and supplied matching before/after renders; old archival gaps are classified separately
Run entry: 02 | kysucka-moderna-chata-reference-camera-perspective | provisional | depends on: kysucka-moderna-chata-blender-mcp-first-reference-render | handout: projects/kysucka_moderna_chata/00/02-reference-camera-perspective/00_handout.md | evidence: vertical framing is improved; Master selects a bounded actual-perspective comparison before changing materials/world
```

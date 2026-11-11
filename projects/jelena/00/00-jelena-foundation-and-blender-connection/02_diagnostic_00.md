# Fresh Evidence Probe — Cursor MCP bridge and live scene identity

Persistent role identity: WORKER
Logical whole identity: jelena-foundation-and-blender-connection
Worker session ordinal: 02
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: Fresh Evidence Probe
Phase: diagnostic
Task identity: JELENA-BRIDGE-EVIDENCE-001
Delivery route: manual Cooperator delivery
Reasoning recommendation: Medium — bounded read-only tool verification against exact expected values; no architectural ambiguity.
Recommended context capacity: approximately 250k tokens (recommendation, not observed capacity)
Requested model: Grok 4.7 High if available; otherwise the Cooperator-selected Cursor model. Report the observed model if exposed, otherwise unknown.
Independence required: no

## Probe contract

Probe hypothesis: Cursor's actual MCP client route can reach the live Blender addon through the running mcp-for-blender bridge and identify the intended live file and scene.

Exact scope: one read-only Cursor MCP tool sequence using the `blender` server's actual exposed tools — get_addon_status, then get_scene_info with settings and bounded object queries. Optionally one read-only code-execution call only if get_scene_info does not expose `bpy.data.is_dirty`. Plus read-only inspection of the local bridge process/package metadata, Cursor MCP registration, and the current Cursor MCP log.

Allowed mutation domains:
- repository mutation: none
- temporary probe-state mutation: none
- durable project-state mutation: none
- external or production mutation: none

Expected evidence: exact exposed tool names, arguments and outputs; addon/server/Blender versions; telemetry consent; optional generators; live filepath; dirty state; scene/camera identity; foundation dimensions; render settings.

Interpretation rule: PASS only if the actual Cursor MCP route returns the intended live file and scene and the observed versions match the expected values below. A running process, a listed server, a raw socket response, a Cursor metadata entry, or a log line alone is not PASS.

Cleanup paths and owner: none; no temporary artifacts are created.

Stop condition: stop when the named evidence is collected or the first causal failure is identified. No workaround attempts, installs, updates or configuration changes.

## Context

Previous planning report: `/Users/agile/meta/projects/jelena/00/00-jelena-foundation-and-blender-connection/01_report_00.md`, SHA-256 `ca08c230c26faa3c0347414de2d5f436952a0dcdac578600a709b6d57492bd1e`, status `PARTIAL`. This probe addresses its named bridge-evidence gap. It is not a new planning cycle and does not revise the plan.

Current bridge evidence, read-only Orchestrator observation on 2026-11-11:

- Global `~/.cursor/mcp.json` is 317 bytes and contains server `blender` with command `/opt/homebrew/bin/uvx`, args `--python 3.11 mcp-for-blender`, env `UV_PYTHON_PREFERENCE=only-managed`, `BLENDER_HOST=localhost`, `BLENDER_PORT=9876`.
- Cursor project metadata contains `user-blender`, named `blender`.
- Process `uv tool uvx --python 3.11 mcp-for-blender` runs as PID 23948; child `mcp-for-blender` runs as PID 23990.
- Cached package `mcp-for-blender` 2.2.7, MIT, requires Python >=3.10, entry point `blender_mcp.server:main`.
- Blender addon remains 1.8, protocol 15, socket 127.0.0.1:9876.
- Cursor log `~/Library/Application Support/Cursor/logs/20261111T111519/mcp-server-user-blender.log` records a successful stdio connection, `Connected to Blender at localhost:9876`, addon protocol 15, and Blender 5.2.3 LTS at 2026-11-11 11:15:31.
- The same log records an outbound POST to `https://yzasssndwqceclzilcdu.supabase.co/rest/v1/telemetry_events` at 11:15:31.801. This appears to be the bridge's minimal anonymous startup telemetry; it is not a Worker action. Do not intentionally trigger, suppress or change telemetry. Report the observed consent state and any startup outbound behavior.
- No actual Cursor MCP tool call has been observed yet. The connection log is strong supporting evidence, not the required proof.

Expected live scene, from prior read-only Orchestrator preflight:

```text
File: /Users/agile/Projects/jelena/Jelena/Jelena_Realistic_v001.blend
Dirty: True
Blender: 5.2.3 LTS
Addon: 1.8
Protocol: 15
Active scene: A • Chata pri lese
Other scene: B • Zariadená dispozícia
Cameras: A • Chata pri lese; B • Zariadená dispozícia; C • Interiér pri terase
Active camera: A • Chata pri lese
Objects: 767
Materials: 22
Slab_027: 8.40 x 5.80 x 0.283 m
Floor_028: 7.92 x 5.32 x 0.027 m
Engine: Cycles
Resolution: 1260 x 840, 100%
Frame: 1
Libraries: none
Images: none
Optional generators: none enabled
```

These are prior Orchestrator observations supplied as expected values, not new Worker findings. Report any material difference and stop.

## Required checks

1. Confirm the Cursor chat actually exposes the `blender` MCP server and its tools. Report the exact server name and exact tool names as exposed in this chat.
2. Call `get_addon_status` first. Record its full decision-relevant output, including Blender version, addon version, protocol version, expected protocol, up-to-date status, capabilities, libraries, generators, premium generators, telemetry consent, warning, and source. Do not change telemetry consent or enable anything.
3. Call `get_scene_info` with `fields` including `settings`, and with bounded queries for `Slab_027` and `Floor_028`. Record the exact output, including file, engine, frame range, resolution, camera, scene identity and dimensions.
4. If and only if `get_scene_info` does not expose `bpy.data.is_dirty`, make exactly one read-only code-execution call with the exact code `print("IS_DIRTY:", bpy.data.is_dirty)`. No other code. If the code tool is not safely usable, report the dirty state as `not exposed` instead.
5. Verify the addon version and protocol did not change during the probe. Verify the bridge process was already running; do not start another, do not run `uvx`, do not install or update anything.
6. Read-only inspect the cached package metadata if useful: `METADATA`, `entry_points.txt`, and the startup/addon-manager path. Confirm whether startup only detects/reports or can install/update the addon. Do not execute install commands.
7. Confirm no Blender save, close, reopen, render, scene mutation or configuration change occurred. Confirm the dirty flag is unchanged before and after. If it changed, stop and report.
8. Report exact tool-call errors and the first causal failure if the MCP route does not work. Do not fall back to a raw socket as proof of Cursor MCP access; a raw socket may be reported only as a separate diagnostic, clearly labelled.
9. Read the current Cursor MCP log read-only and report whether it shows the same connection/handshake as the supplied evidence, including any tool-call entries, errors, reconnects, or outbound telemetry. Do not clear, rotate or edit logs.

## Mandatory reading

- Governing WORKER spine: AP.md Semantic Authority; Per-Role Minimum-Reading Spine (WORKER row); RF-03, RF-06, RF-12, RF-18; §8; §18.
- AP.md Fresh Evidence Probe; §5 Task Authority; §17 Compact Communication.
- AP_WORKER.md Reporting.
- PROMPT_CONTRACTS.md Worker Report Header; Fresh Evidence Probe contract.
- The previous planning report `01_report_00.md`, especially its bridge-evidence gap and addendum.
- The cached bridge package metadata and the Cursor MCP registration metadata, read-only.
- The Blender addon source for version/protocol facts, read-only.

## Authority

Positive authority: use the Cursor `blender` MCP server's read-only tools and inspect the named local metadata and logs read-only. Allowed commands: `ps`, `lsof`, `stat`, `cat`, `sed`, `rg`, `jq`, `find`, `shasum`, and the exact MCP tool calls described above.

Negative authority: no repository, host, Blender, Cursor-configuration or Git mutation. No installs, updates, `uvx` runs, brew, package fetches, intentional network calls, credential access, secrets, subagents, parallel work, scene save/close/reopen, render, or trace write. Do not modify the addon, the global MCP config, the project, AP or Meta.

Repository mutation: none
Host/remote mutation: none
Trace persistence: none

Cooperator delivery / trace destination: configured
Downloadable prompt filename: 02_diagnostic_00.md
Destination path: /Users/agile/meta/projects/jelena/00/00-jelena-foundation-and-blender-connection
Report filename: 02_report_00.md
Prompt persistence owner: COOPERATOR
Report persistence owner: COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report

External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/jelena/00/00-jelena-foundation-and-blender-connection
Trace project key: jelena
Trace logical-whole projection identity: jelena-foundation-and-blender-connection
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: public
Trace companion outcome: report
Trace self-granted status: none

Relay basis: manual Cooperator ferry. The Cooperator persists the prompt and the report. The Worker returns the complete report in the session and does not write to Meta. No trace write is granted.

## Report contract

Begin exactly:

### Report for ORCHESTRATOR_CHAT

Echo these coordinates once: logical whole identity `jelena-foundation-and-blender-connection`; Worker session `02`; Worker exchange `01`.

Include:

- Status: PASS, PARTIAL or BLOCKED.
- Exact Cursor MCP server and tool names used, with arguments.
- Exact decision-relevant outputs from `get_addon_status` and `get_scene_info`.
- Whether the actual Cursor MCP route reached the correct live file and scene.
- Version/protocol/telemetry/generator findings.
- Dirty-state result and confirmation it did not change.
- Any difference from the expected values.
- Read-only package/startup and Cursor-log findings.
- Risks, unknowns and the smallest next step.
- Orchestration critique: MEASURED findings and LEAD possibilities; either may be none.
- Phase-qualified result: not-applicable
- Logical-whole closure: not-closed
- Report justification: new-evidence

PASS means the actual Cursor MCP route returned the intended live file and scene and the named evidence is complete. PARTIAL means some named evidence is missing. BLOCKED means the MCP route or a prerequisite failed. Do not implement, accept, publish or close.

If the MCP tools are not exposed in this chat, stop and report BLOCKED with the exact Cursor status/error. Do not try another chat, another client, raw socket substitution, installation or configuration change within this grant.

Authority expires at the terminal report, cancellation or supersession.

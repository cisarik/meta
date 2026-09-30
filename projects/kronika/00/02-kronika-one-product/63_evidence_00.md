# S9-R Model Evidence Task — Public documentation matrix (kronika-one-product, session 63)

Persistent role identity: WORKER
Logical whole identity: kronika-one-product
Worker session ordinal: 63
Worker exchange ordinal: 01
Worker session target: fresh-worker-session
Native planning mode: not-used
Worker session profile: WebSearcher
Phase: evidence
Task identity: KRONIKA-ONE-PRODUCT-S9-R-MODEL-EVIDENCE
Delivery route: manual Cooperator delivery
Reasoning recommendation: High — external documentation synthesis whose result will ground a billing-adjacent planning revision
Recommended context capacity: approximately 250k tokens
Independence required: no

## Goal (one coherent outcome)

Produce a source-backed public-documentation matrix of currently supported
OpenAI model identifiers usable by the Kronika research path, so that the
S9-R planning revision can define an administrator-selectable model allowlist
with a matching usage price schedule per model. This is external evidence only:
no account access, no provider generation, no credential, no NUC interaction.

## Why this task exists

The accepted research configuration and provider selection currently enforce
one fixed model (`gpt-5.5-2026-04-23`); the Cooperator decided on 2026-09-30
that the administrator may set the model. The S9-R initial plan correctly
stopped (`62_report_00.md`, PARTIAL /
`Escalation disposition: NEEDS_ORCHESTRATOR_DECISION`) because the permitted
read-only sources substantiate only the original model and no second model's
support or pricing. This task supplies the missing external evidence; the
single authorized targeted planning revision follows separately.

## Required matrix (per candidate model)

For `gpt-5.5-2026-04-23` and for up to three additional exact model
identifiers that plausibly serve this path, report:

1. **Exact identifier** as named in first-party documentation, plus any
   alias/snapshot notes.
2. **Availability and deprecation status** (currently available, preview,
   scheduled shutdown, deprecated) with the source; avoid models named in the
   deprecation register as shutting down (for example deep-research variants
   the accepted plan already excludes).
3. **Responses API and `web_search` support**: documented support for the
   Responses API and the hosted `web_search` tool.
4. **Compatibility with the fixed request shape** used by Kronika:
   `background=true`, `store=true`, `tool_choice=required`,
   `parallel_tool_calls=false`, reasoning effort `low`/`high`,
   `max_tool_calls` 3/20, `max_output_tokens` 4,096/32,768, no attachments.
   Flag any parameter a candidate does not support.
5. **Pricing** (first-party price documentation, retrieval date): input per
   million tokens, cached input per million, output per million, and web
   search per 1,000 calls; note tiers (for example long-context pricing),
   cache discounts and reasoning-token accounting that affect the billable
   total.
6. **Fit with the existing four-rate `UsagePriceSchedule`** (input, cached
   input, output, web search per thousand micro-USD): state whether the four
   rates suffice for the candidate or which additional dimensions would be
   required.
7. **Source URLs and retrieval date**, plus explicit uncertainty for anything
   the documentation leaves ambiguous. Account-specific access is not provable
   publicly and stays a later live-acceptance precondition.

## Candidate selection rule

Prefer models from the same provider family that the accepted architecture
uses, with documented web-search support and no scheduled shutdown; include at
least one lower-cost alternative if one is documented. Do not invent
identifiers or prices; if fewer than one additional grounded candidate exists,
report that outcome truthfully.

## Method and boundaries

- Public first-party documentation and public model/pricing/deprecation
  pages only (for example the provider's documentation and pricing pages).
  Cite exact URLs and retrieval date; separate documented facts from
  inference; keep source/event dates visible.
- No account login, no API key, no generation call, no billing action, no
  credential handling, no private data, no NUC/SSH/sudo, no repository
  mutation, no other external services beyond public documentation reads.
- If the client's web-search capability is unavailable, stop and report the
  limitation instead of answering from memory.
- The report is evidence, not authority; it grants no implementation.

## Deliverable and report contract

Deliver the matrix (a compact table plus per-model notes), a recommendation of
two to four candidates suitable for an administrator allowlist with a
one-line rationale each, the exact prices mapped to integer micro-USD, and an
explicit list of unknowns. Also state whether the existing four-rate schedule
shape is sufficient for the recommended set or what else the plan must add.

The terminal report begins exactly `### Report for ORCHESTRATOR_CHAT`, echoes
the coordinates (`kronika-one-product`, 63, 01), and carries the compact core:
status; `Phase-qualified result: not-applicable`; start and end commit
`3bf424586289b500cf45cb0d49676b50d27328fa` (unchanged); changed files (none in
the repository; the report file only); sources with URLs and dates; the matrix;
recommendation; `Report justification: new-evidence`; deviations/risks/missing
evidence; smallest next step (the targeted planning revision); critique;
`Logical-whole closure: not-closed`; authority expiry. Save the report exactly
at `63_report_00.md` if the client permits; read back the full content;
otherwise preserve it in chat and mark delivery PARTIAL.

## Delivery record

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Trace project key: kronika
Trace logical-whole projection identity: 02-kronika-one-product
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
Trace visibility: private
Trace companion outcome: report
Trace self-granted status: none
Cooperator delivery / trace destination: configured
Downloadable prompt filename: 63_evidence_00.md
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 63_report_00.md
Prompt persistence owner: ORCHESTRATOR
Report persistence owner: assigned WORKER (exact write if the client permits); otherwise COOPERATOR
Git publication owner: COOPERATOR
Archival: wait-for-report
```

## Stopping conditions

Stop (PARTIAL/BLOCKED) if the required public evidence cannot be retrieved, if
a source conflicts materially with another first-party source (report both),
or if the task would require account access or any call to the provider. Do
not expand into general model benchmarking or unrelated provider comparison.

Authority expiry: the terminal report ends this evidence exchange.

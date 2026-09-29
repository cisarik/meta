# KRONIKA-ONE-PRODUCT-NUC-RELEASE-89A4029 — executed deployment plan (autonomous mode)

## Identity and route

Persistent role identity: ORCHESTRATOR (autonomous execution under the
Cooperator's 2026-09-28 directive; no fresh Worker session was used)
Logical whole identity: kronika-one-product
Worker session ordinal: 46
Worker exchange ordinal: 01
Phase: deployment
Task identity: KRONIKA-ONE-PRODUCT-NUC-RELEASE-89A4029
Delivery route: direct Orchestrator execution (recorded plan)

## Goal

Bring the NUC to the accepted published release
`89a402981a9eac83646199c77984c3fc21c0744d` through
`deploy/ubuntu/framenest-release`, with the expected schema continuation
`0033` -> `0034`, and capture the as-left state. Capture stays parked.

## Starting state

- MacBook checkout on `feat/kronika-one-product` at `89a4029…`, clean; public
  `main` = `89a4029…`; AP pin `73e20ef…`.
- NUC: web release `40e51cb2…`, capture release `94e605c…`, database revision
  `0033`, `framenest.service` active, backup readiness ready.
- The three `FRAMENEST_NUC_SSH_*` names are exported in the execution
  environment; the Cooperator established the NUC sudo timestamp before the
  sequence and releases it afterwards; the executor never runs `sudo -v`/`-K`.

## Executed sequence

1. Gate probe, `sudo -n true`, repository gate, public readback.
2. `framenest-release status`, `check --release 89a4029…`.
3. `framenest-release deploy --release 89a4029… --yes` (stopped; see report).
4. Root-cause and continuation per the documented `migration-required` annex,
   adapted to the discovered private-catalog mode prerequisite.
5. Host unit alignment: `StateDirectoryMode=0700` (repo commit `3f5dc5c…`),
   installed and hash-verified on the NUC.
6. Migration from the target tree; cutover via
   `framenest-release rollback --release 89a4029… --yes`.
7. Final `status` and read-only as-left capture.

## Authority and containment

The Cooperator's 2026-09-28 autonomy directive; routine NUC release updates per
ADR-0075 including the documented schema-jump continuation; no database reset;
no capture action; no credential or `private/**` reading; sanitized reporting
only.

## Trace and delivery record

```text
External trace disposition: configured
Trace discovery: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Destination path: /Users/agile/meta/projects/kronika/00/02-kronika-one-product
Report filename: 46_report_00.md
Trace authority: historical-evidence-only
Trace archival owner: COOPERATOR
```

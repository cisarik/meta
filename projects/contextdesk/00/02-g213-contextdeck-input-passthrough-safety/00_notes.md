# Orchestrator notes — g213-contextdeck-input-passthrough-safety

Operational lifecycle artifact. Consumer: Orchestrator. Not task authority.

## Baseline

- Product repository `https://github.com/cisarik/contextdesk.git`, branch `main`
- Exact M2 planning baseline: `b5c4be6b179a3df6e3f3803c02d819c1a7b4fe8c`
- Prior logical whole `01-g213-contextdeck-mvp-context-lighting` is closed and accepted IRL.
- AP gitlink / `.ap` HEAD: `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`

## Strategic routing for M2

Per COOPERATOR decision, M2 begins with a mandatory Planner Worker in Native Plan Mode
(`Native planning mode: required`).

M2 focuses strictly on **input pass-through safety and zero-lockout crash recovery**:
- G1 hardware routing probe for all 20 controls
- G3 permission model for G213 event nodes without compromising system security
- G4 fail-safe broker architecture (libevdev + uinput, EVIOCGRAB, synthetic key ledger, zero remapping)
- Handout §29 crash/hang recovery invariants: SIGTERM, SIGKILL, watchdog, TTY recovery
- Bounded lease IPC with session app

Logical-whole closure: not-closed.

## Worker 14 reconciliation and Worker 15 routing — 2026-09-12

Authored by the ContextDesk ChatOrchestrator; exact persistence delegated to Worker 15.

Public META 5d4bcf9811974aa71e6d17acc3c2375a5015db40 contains the matching first-add prompt/report pair for 14/01. The issued prompt bytes match. Deployment-PASS is reconciled only for candidate cb72ae0388307b514182efc6936712e3da42cda4 installed while inactive, under AP pin 0cf2cff483a36a4cc2254aa424a7c53bd57a97e9. Owner install output corroborates installed hashes/state; further readback, 13/13 tests and backup cleanup are attributed Worker evidence. No physical G4 claim is accepted.

Manual delivery and smaller coherent tasks remain selected. Worker 14 authority expired. Worker 15 receives a fresh independent, single-invocation physical pass-through/cutoff evidence slice, not a repeat of the broad primary audit. Its outcome is not yet known in this entry. Remaining G4 claims and canonical product-state documentation reconciliation stay open. The AP-update whole is separate and grants no ContextDesk mutation.

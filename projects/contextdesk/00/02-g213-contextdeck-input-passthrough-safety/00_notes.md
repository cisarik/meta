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

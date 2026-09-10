# Orchestrator notes — g213-contextdeck-foundation-architecture

Operational lifecycle artifact. Consumer: Orchestrator. Not task authority.

## Frozen baseline (G0)

Product repository `https://github.com/cisarik/contextdesk.git` branch `main`.

- Frozen HEAD: `6b4e4b30c29b154a99a96061c1b692781f82c400`
- `origin/main` at freeze: `ca3ac07c5fecfe3c983078e343ec6b3e02c75bea` (local main two commits ahead; no push)
- AP gitlink / `.ap` HEAD: `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`

The two local commits `1d4b160` (adopt AP) and `6b4e4b3` (reconcile AGENTS managed block) are Cooperator-authored. Do not schedule AP adoption again.

## Planning exchange 01/01

- Status: `PARTIAL`
- Justification: architecture is decision-complete; G1 physical-control routing and G2 RGB behavior remain unmeasured under read-only authority
- Companion integrity: `01_report_00.md` begins `### Report for ORCHESTRATOR_CHAT` and is not a prompt duplicate
- Routing defects recorded, not used to reopen general planning:
  - Prompt required `fresh-worker-session` and `Native planning mode: required`
  - Report observed Default mode, same continuing conversation, context compaction
  - Planning does not require independence; substance is accepted as a claim package reconciled against current repository evidence
- No second automatic targeted revision. Hardware gaps are probe/acceptance gates, not a new planning cycle.

## Accepted for routing (not implementation authority)

- C++20 / Qt6 / KF6 / CMake / Kirigami session app + isolated libevdev/uinput broker + external OpenRGB SDK client
- Event-driven KWin context; measured best-effort focus safety
- Typed profile contract; inherit ≠ pass-through; no shell actions
- Five-zone RGB truth; v1 one base color
- Game Mode / Backlight not promised until G1
- Next implementation whole: `g213-contextdeck-profile-contract` (V1)
- G1 physical probe is a separate manually dispatched task and is not a prerequisite for V1

## Remaining Cooperator-owned gates (not required for V1)

G3 device authority, G6 license confirmation if dependency provenance changes, G4–G8 as later verticals.

## META hygiene

Trace project key: `contextdesk` (canonical repo name). Handout’s provisional `g213-contextdeck` is not used as the directory key.

Misplaced untracked stubs `projects/contextdesk/00/00_handout.md` and `projects/contextdesk/00/01_planning.md` were not archived and are not this whole’s storage. This directory is the archival location.

Logical-whole closure: not-closed.

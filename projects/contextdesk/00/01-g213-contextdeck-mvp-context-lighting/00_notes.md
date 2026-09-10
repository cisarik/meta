# Orchestrator notes — g213-contextdeck-mvp-context-lighting

Operational lifecycle artifact. Consumer: Orchestrator. Not task authority.

## Baseline

- Product repository `https://github.com/cisarik/contextdesk.git`, branch `main`
- Exact M1 baseline: `13231c319ad4c4b59f5860c03a1a79520d2933cc`
- Product `origin/main`: `ca3ac07c5fecfe3c983078e343ec6b3e02c75bea`. Local
  `main` is ahead by ORCHESTRATOR-owned documentation commits. Nothing pushed.
- META local checkout: `main` ahead of its `origin/main` by the archived
  foundation exchange; nothing pushed.
- AP gitlink / `.ap` HEAD: `7ef45da756ed3cc14808e89bf25d0a9f9aba5d26`

## Routing decision that created this whole

The COOPERATOR rejected the narrow `g213-contextdeck-profile-contract` slice as
too slow and re-routed to one aggressive MVP slice. M1 merges the former
V1 (profile contract), V2 (KWin context), V3 (application lighting), and the
typed power-action IDs of V7. Input interception is explicitly **out** of M1.

COOPERATOR decisions recorded for this whole:

- Aggressive MVP routing; the COOPERATOR tests IRL and reports what works.
- Division of labour: Workers write code, the COOPERATOR runs host enablement
  and hardware acceptance, the ORCHESTRATOR reads logs and routes.
- Minimal safety-only tests: exactly three CTest units.
- Evidence tier raised to E3 by consequence (D-Bus trust boundary, external
  protocol client, host power actions, package-based host enablement), using
  the E3 allowance to combine explicit stages under per-stage gates. Final
  acceptance stays with the COOPERATOR plus a later fresh independent audit.

## Granted mutation classes (named, bounded)

- Install `openrgb` from the repository including its udev rules — COOPERATOR-run
- Run the OpenRGB SDK server on loopback — COOPERATOR-run
- Install or load the KWin script (`kpackagetool6` or `org.kde.KWin /Scripting`)
  — COOPERATOR-run
- A systemd **user** unit, started manually, no autostart
- Local commits on `main` without push
- A udev rule or privileged identity for G213 **event nodes** was granted in
  principle and is **reserved for the input whole (M2)**; M1 must not use it

## Trace hygiene

- Archive `00`, whole sequence `01` for this logical whole.
- The planning prompt in whole `00` was normalized from `01_plan_00.md` to
  `01_planning_00.md`, matching the dominant META convention; the bytes are
  identical, so this is path normalization, not a rewrite.
- An empty, misplaced `02_implementation_00.md` stub in whole `00` was removed;
  the M1 prompt belongs to this whole as `01_implementation_00.md`.
- The prompt was committed before dispatch under explicit COOPERATOR authority,
  as a recorded deviation from the default prompt-plus-report single commit.

Logical-whole closure: not-closed.

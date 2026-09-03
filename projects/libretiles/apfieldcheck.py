#!/usr/bin/env python3
"""Check a Worker prompt's AP structural field values against the pinned .ap enums.

Written after Worker session 15 returned BLOCKED twice on protocol-conformance
defects: three invalid fields in exchange 01, then a FOURTH in exchange 02 that
the Orchestrator introduced while hand-fixing the first three. Reading the enum
"carefully" is not enough; the values are closed literals and must be compared
mechanically.

Usage:  python3 apfieldcheck.py <prompt.md> [--ap /path/to/.ap]

Exit 0 = no defects. Exit 1 = at least one defect. Exit 2 = could not parse spec.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

DEFAULT_AP = pathlib.Path("/home/agile/Projects/libretiles/.ap")


def fenced_block_after(text: str, anchor: str, occurrence: int = 1) -> str | None:
    """Return the first ```text fenced block that follows `anchor`."""
    idx = -1
    for _ in range(occurrence):
        idx = text.find(anchor, idx + 1)
        if idx == -1:
            return None
    start = text.find("```", idx)
    if start == -1:
        return None
    start = text.find("\n", start) + 1
    end = text.find("```", start)
    return text[start:end] if end != -1 else None


def parse_fields(block: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for raw in block.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        # Values may themselves contain a colon, so split on the FIRST one only.
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def load_spec(ap: pathlib.Path, planning_cycle: str | None) -> dict[str, str]:
    contracts = (ap / "PROMPT_CONTRACTS.md").read_text(encoding="utf-8")
    spec: dict[str, str] = {}

    block = fenced_block_after(
        contracts, "Every plan-only prompt includes exactly one value for each field"
    )
    if block:
        spec.update(parse_fields(block))

    # The two Planning Record variants are MUTUALLY EXCLUSIVE. Merging them makes
    # the checker demand targeted-revision values from an initial prompt, which is
    # a false positive the first version of this tool actually produced.
    if planning_cycle == "targeted-revision":
        anchor = "The sole authorized targeted revision uses"
    else:
        anchor = "Every initial implementation-planning prompt uses the existing fields in"
    block = fenced_block_after(contracts, anchor)
    if block:
        spec.update(parse_fields(block))

    ap_md = (ap / "AP.md").read_text(encoding="utf-8")
    # The justification enum wraps across two lines inside its fenced block, and
    # the literal "Report justification:" also occurs in prose earlier, so anchor
    # on the enum's own first value rather than on the field name.
    m = re.search(
        r"Report justification:\s*((?:[a-z-]+\s*\|\s*)+[a-z-]+)",
        ap_md.replace("\n", " "),
    )
    if m:
        spec["Report justification"] = re.sub(r"\s+", " ", m.group(1)).strip()

    block = fenced_block_after(contracts, "Phase-qualified result:")
    if block:
        for key, value in parse_fields(block).items():
            spec.setdefault(key, value)
    # Not a structural field, just prose that happens to contain a colon.
    spec.pop("concrete values for every boundary", None)
    return spec


def check(prompt_path: pathlib.Path, ap: pathlib.Path) -> int:
    prompt = prompt_path.read_text(encoding="utf-8")
    m = re.search(r"^Planning cycle:[ \t]*(.+)$", prompt, re.M)
    cycle = m.group(1).strip() if m else None
    spec = load_spec(ap, cycle)
    if not spec:
        print("could not parse any spec block from .ap", file=sys.stderr)
        return 2

    defects: list[tuple[str, str | None, str]] = []
    print(f"AP field check: {prompt_path.name}")
    print(f"spec source:    {ap}/PROMPT_CONTRACTS.md + AP.md")
    print("-" * 78)

    for key, allowed in sorted(spec.items()):
        m = re.search(rf"^{re.escape(key)}:[ \t]*(.+)$", prompt, re.M)
        mine = m.group(1).strip() if m else None
        if mine is None:
            print(f"  --   {key:40} (not present in this prompt)")
            continue
        if allowed.startswith("<"):
            verdict = "free"
        elif "|" in allowed:
            options = [o.strip() for o in allowed.split("|")]
            verdict = "OK" if mine in options else "BAD"
        else:
            verdict = "OK" if mine == allowed else "BAD"
        if verdict == "BAD":
            defects.append((key, mine, allowed))
        print(f"  {verdict:4} {key:40} = {mine[:44]}")

    print("-" * 78)
    for key, mine, allowed in defects:
        print(f"DEFECT {key}\n   mine:    {mine}\n   allowed: {allowed}")

    # Two defects this whole cannot catch by field comparison alone, both real:
    #  - exchange 01 used `planning-PASS` inside the REPORT-FORMAT prose, not as a
    #    `Phase-qualified result:` field line, so a field check misses it;
    #  - `Native planning mode: required` is only invalid against a client that
    #    lacks the mode, which is an environmental fact, not a value error.
    extra: list[str] = []
    # Ignore lines that are quoting the bad value in order to correct it: a line
    # containing "NOT the structural result enum" is documentation, not an
    # instruction. Without this the tool flags its own correction notes.
    scan = "\n".join(
        line
        for line in prompt.splitlines()
        if "NOT the structural result enum" not in line
    )
    for invented in re.findall(r"\bplanning-(?:PASS|PARTIAL|BLOCKED)\b", scan):
        extra.append(
            f"invented result value `planning-{invented.split('-')[-1]}` in prose — "
            "planning uses `not-applicable` (PROMPT_CONTRACTS.md:203)"
        )
    if re.search(r"^Native planning mode:[ \t]*required[ \t]*$", prompt, re.M):
        extra.append(
            "`Native planning mode: required` — the prompt MUST NOT be pasted unless the "
            "client has that mode enabled (PROMPT_CONTRACTS.md:695-698). Confirm with the "
            "Cooperator, or reissue as `not-used` with prompt-level planning authority."
        )
    for note in dict.fromkeys(extra):
        print(f"WARN   {note}")

    # --- coordinate consistency -------------------------------------------
    # PROMPT_CONTRACTS.md:38-41 requires the terminal report to echo the
    # authoritative prompt's coordinate values UNCHANGED. A prompt built by
    # string-patching a previous one can declare exchange N in its header while
    # its report-format section still instructs the Worker to echo N-1, because
    # the ordinal appears in two textual forms: "ordinal: NN" and "ordinal NN".
    # That is defect five of this whole and it is why this check exists.
    coord_defects: list[str] = []
    hs = re.search(r"^Worker session ordinal:[ \t]*(\d+)[ \t]*$", prompt, re.M)
    he = re.search(r"^Worker exchange ordinal:[ \t]*(\d+)[ \t]*$", prompt, re.M)
    if hs and he:
        want = (hs.group(1), he.group(1))
        echo = re.search(
            r"Worker session ordinal[: ]+(\d+),\s*Worker exchange ordinal[: ]+(\d+)",
            prompt,
        )
        if echo is None:
            coord_defects.append(
                "the report-format section never instructs the Worker to echo the "
                "coordinate fields (PROMPT_CONTRACTS.md:38-41)"
            )
        elif echo.groups() != want:
            coord_defects.append(
                "report-format section tells the Worker to echo session "
                f"{echo.group(1)} exchange {echo.group(2)}, but the header declares "
                f"session {want[0]} exchange {want[1]} — the report must echo the "
                "authoritative values UNCHANGED (PROMPT_CONTRACTS.md:38-41)"
            )
        others = sorted(
            {m for m in re.findall(r"\bexchange (\d\d)\b", prompt)} - {want[1]}
        )
        if others:
            print(
                f"  note  other exchange ordinals referenced in prose: {', '.join(others)}"
                " — confirm each is a deliberate historical reference"
            )
    else:
        coord_defects.append("header is missing a session or exchange ordinal field")

    for note in coord_defects:
        print(f"DEFECT coordinate consistency\n   {note}")

    total = len(defects) + len(coord_defects)
    print(f"\nDEFECTS: {total}   WARNINGS: {len(dict.fromkeys(extra))}")
    return 1 if total else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", type=pathlib.Path)
    parser.add_argument("--ap", type=pathlib.Path, default=DEFAULT_AP)
    args = parser.parse_args()
    return check(args.prompt, args.ap)


if __name__ == "__main__":
    raise SystemExit(main())

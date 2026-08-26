# External Research Brief — Scrabble Strategy for Small-Model Play

Project: Libre Tiles, logical whole `playable-free-rivals`
Issued by: Agent Orchestrator, 2026-08-26, at explicit Cooperator request
Classification: read-only external evidence gathering; grants NO mutation, NO task authority, is NOT an AP Worker exchange
Execution route: Cooperator runs this brief in ChatGPT (deep research / browsing enabled) and returns the full result to the Orchestrator
Integration owner: Orchestrator distills accepted findings into Slice-2 SEARCH_PROFILE texts and future prompt polish; rejected findings are dropped with reasons

---

## Role

You are two experts in one:

1. A tournament-caliber Scrabble strategist with deep knowledge of club and championship play under the Collins Scrabble Words (2019) lexicon and standard North American-style rules.
2. A research analyst writing for a software engineering team that is building an automated Scrabble opponent driven by SMALL free-tier LLMs (roughly 7B–30B parameters). The opponent proposes tile placements in strict tool-call JSON; a server-side engine validates every placement against Collins 2019. Your reader will convert your findings into SHORT system-prompt instructions of a few sentences each.

Optimize every sentence for convertibility into such instructions — not for scholarship, not for completeness.

## Mission

Produce a prioritized strategy dossier that measurably raises average per-turn score and reduces blunders for a WEAK-to-MEDIUM automated player. Rank by marginal point gain for that skill level, not by expert-level refinements.

## Scope IN

- Rack leave evaluation: which letters to keep or dump (S, blanks, J/Q/X/Z, vowel/consonant balance, duplicates); simple numeric heuristics a small model can apply.
- Hooks and affixing: front/back hooks onto existing words (-S, -ED, -ING, -ER, -Y; RE-, UN-, OUT-, IN-), including hook squares as high-value targets.
- Parallel plays: crossing words to score several small words simultaneously and refresh the rack.
- Premium squares: targeting TW/DW lanes, extending words through DWS/TWS, and DENYING premium lines to the opponent.
- Bingo principles: general stem thinking and when to hold a promising six-letter setup versus banking points.
- Endgame play: procedure when the bag is empty, counting out, unloading high-value tiles, avoiding being stuck with Q or a dead pair.
- Exchange policy: concrete thresholds (rack quality measures, bag size) for exchanging instead of playing a weak scoring move.
- Defensive shapes: closing lanes, avoiding vowel-heavy open boards, playing safely when ahead.
- Novice blunders ranked by typical cost.

## Scope OUT

Clock handling, tournament procedures, lexicon controversies, exhaustive word/stem lists beyond illustrative examples, physical game logistics, other board variants, opponent psychology.

## Grounding contract

Tag every substantive claim inline:

- [VERIFIED] — official rules text or multiple independent reputable sources agree.
- [LIKELY] — single reputable source or strong expert consensus.
- [SPECULATIVE] — plausible but weakly sourced; include only if valuable.

Name the source type inline where possible (e.g., "official rules", "coach guide", "champion interview"). Never invent dictionary words; example words must be common English or explicitly marked "illustrative". If you cannot ground something, tag it or drop it.

## Output contract (Markdown, English, 1800–3000 words total)

1. **Executive summary** (≤200 words): the five highest-leverage behaviors for a weak automated player.
2. **Ranked recommendations R01–R15**: each = one imperative decision rule (≤30 words) + mechanism (why it scores) + expected impact for novice-strength automation (high/medium/low) + grounding tag.
3. **Topic dossiers**: one short section per Scope-IN area; principles first, then concrete triggers and numeric thresholds wherever the literature offers them (e.g., "exchange when rack scores below ~X points and more than Y tiles remain in the bag"), each with at most one worked micro-example described in plain grid text.
4. **Endgame checklist**: a numbered procedure starting when the bag becomes empty.
5. **TOP-10 MICRO-RULES**: final distillation — ten imperative rules, each ≤25 words, directly embeddable into a system prompt, ordered by expected point gain per token spent.
6. **Model-failure notes** (optional, ≤300 words): credible public analyses of why LLMs play word-placement games poorly, if you find any.

## Facts you may take as given (do not spend research time on them)

Standard 15×15 board and premium layout; 7-tile racks; full rack = 50 bonus points ("bingo"); tile values; exchange legal only while ≥7 tiles remain in the bag; pass always legal; our engine validates all words server-side against Collins 2019; the model sees its own rack plus the full board but not the opponent's rack; the opponent is a human club-amateur.

## Constraints

English only. Prefer precision over volume; every sentence must earn its tokens. No paid sources required. Use your browsing/deep-research capability freely within your plan's limits.

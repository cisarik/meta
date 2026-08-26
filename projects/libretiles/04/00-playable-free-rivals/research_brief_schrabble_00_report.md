# Scrabble Strategy for Small-Model Play

## Executive summary

For a weak-to-medium automated player, the largest gains should come from **better move-class search, rack management, and avoiding catastrophic leaves**, not expert-level defensive finesse. [VERIFIED] (expert handbook; Quackle documentation) Competitive strategy treats immediate score and rack leave as the dominant midgame variables, while Quackle explicitly evaluates moves as **play score + estimated leave value**. citeturn20view0turn25view1

The five highest-leverage behaviors are: **scan hooks/parallels/premiums before ordinary words; preserve a playable leave instead of blindly maximizing score; shed Q/J and duplicates; exchange genuinely dead racks instead of limping; and switch sharply to exact sequence planning near the endgame.** [VERIFIED] (multiple expert/AI sources) citeturn20view1turn20view2turn20view3turn24search0turn22view0

[LIKELY] (expert handbook) Blanks deserve exceptional protection—roughly **20–30 points of strategic value**—and the first S roughly **8–10 points**; ordinary duplicates and badly imbalanced vowel/consonant racks should normally be repaired. citeturn20view0turn20view2

[LIKELY] (independent LLM Scrabble benchmarks) Small models particularly need explicit placement-search instructions: public experiments find that models often recognize rack words yet fail to connect them legally to the actual board. citeturn25view0turn25view2

## Ranked recommendations

1. **R01 — Before ordinary words, scan every usable hook, parallel lane, and premium-square extension.**  
   [VERIFIED] (expert handbook + expert strategy guide) Multiple-overlap plays repeatedly turn mediocre racks into 20–30-point turns, and a specialist guide considers parallels a major scoring source for developing players. **Impact: High.** citeturn23view0turn24search1

2. **R02 — Optimize immediate score plus rack leave; never choose the raw top score automatically.**  
   [VERIFIED] (expert handbook + Quackle documentation) This is the standard static-evaluation abstraction: current points plus the future value of retained tiles. **Impact: High.** citeturn20view0turn25view1

3. **R03 — Shed Q and J promptly unless a substantially better move compensates; do not wait indefinitely for a jackpot.**  
   [LIKELY] (expert handbook) Q is especially damaging; the handbook even gives positions where an 11-point Q dump beats a 25–30-point alternative that retains Q. **Impact: High.** citeturn20view1turn21view1

4. **R04 — Break non-S duplicates and extreme vowel/consonant imbalance; aim roughly toward three vowels and four consonants after replenishment.**  
   [LIKELY] (expert handbook) Duplicate removal and approximately 3V/4C balance are explicit rack-management recommendations. **Impact: High.** citeturn20view2

5. **R05 — Keep a blank unless using it gains about 20–30 extra points, makes a bingo, outs, or materially changes the game.**  
   [LIKELY] (expert handbook) The handbook assigns a rule-of-thumb intrinsic value of roughly 20–30 points to the blank. **Impact: High.** citeturn20view0

6. **R06 — Keep the first S when another move scores within about 8–10 points; treat a second S as an ordinary duplicate.**  
   [LIKELY] (expert handbook) S is unusually flexible for hooks and bingo formation, but duplicate-S protection is specifically discouraged. **Impact: Medium–High.** citeturn20view0turn20view2

7. **R07 — Strongly consider exchanging when no move reaches roughly 20 points or preserves a balanced, bingo-prone leave.**  
   [LIKELY] (expert strategy guide; consistent with handbook) This ~20-point trigger is the clearest published simple threshold found; the handbook likewise treats exchange as normal rack repair. **Impact: High.** citeturn24search0turn20view3

8. **R08 — During exchanges, keep synergistic useful letters; do not automatically exchange all seven.**  
   [LIKELY] (expert handbook) Worked examples prefer keeps such as ER or IRT and describe indiscriminate seven-tile exchanges as unnecessarily random. **Impact: Medium–High.** citeturn21view0

9. **R09 — Search existing word ends for legal S, ED, ING, ER, Y and front-prefix extensions before forming isolated rack words.**  
   [LIKELY] (expert handbook) Hooks and extensions create additional scoring geometry; listed affixes are **search patterns, not universally legal additions**, so validation remains essential. **Impact: High.** citeturn23view0turn23view1

10. **R10 — Fish one tile only from an exceptionally bingo-ready rack; otherwise take useful points while retaining a good core.**  
    [LIKELY] (expert handbook) The handbook reserves one-tile fishing for racks that nearly assure a bingo and shows that excessive score sacrifice can be inferior. **Impact: Medium.** citeturn20view2

11. **R11 — Take strong scoring premiums early; do not sacrifice substantial points merely to deny an opponent a possible TWS reply.**  
    [LIKELY] (expert handbook) Simulations and expert examples repeatedly find weaker players overestimate early premium-square exposure. **Impact: Medium–High.** citeturn23view1turn21view3

12. **R12 — When ahead late, reduce volatility by closing bingo lanes; when behind, preserve or create bingo and premium access.**  
    [LIKELY] (expert handbook) “Open behind, block ahead” is supported, but only after preserving reasonable scoring. **Impact: Medium.** citeturn21view2turn22view3

13. **R13 — Never keep U merely because Q remains unseen; surplus U is a rack liability.**  
    [LIKELY] (expert handbook) The handbook explicitly calls U the least helpful vowel and advises prompt Q disposal rather than Q/U speculation. **Impact: Medium.** citeturn20view2

14. **R14 — With about fifteen bag tiles remaining, shift from generic equity toward concrete threats, outs, dangerous unseen tiles, and lane control.**  
    [LIKELY] (expert handbook) The handbook defines roughly this region as pre-endgame and recommends thinking increasingly about what is possible rather than merely probable. **Impact: Medium.** citeturn22view3

15. **R15 — When the bag is empty, reconstruct the opponent rack and calculate complete out-in-one/out-in-two sequences against their best reply.**  
    [VERIFIED] (expert handbook; Scrabble-AI literature) Empty-bag play becomes perfect-information sequence optimization, and going out first is usually strongly advantageous. **Impact: High, but fewer turns affected.** citeturn22view0turn22view1turn24search19

## Topic dossiers

**Rack leave evaluation.**  
[VERIFIED] (expert handbook + Quackle documentation) A small model should compare candidates using the mental approximation **move score + leave quality**, because raw score alone discards substantial future equity. citeturn20view0turn25view1 [LIKELY] (expert handbook) The simplest actionable leave hierarchy is: protect blank strongly; protect the first S moderately; prefer flexible low-point letters and balanced combinations; remove ordinary duplicates; rapidly unload Q/J; treat X as middling and Z as materially easier to retain than Q/J. citeturn20view0turn20view2turn21view1

[LIKELY] (expert handbook) Numeric shortcuts suitable for a small prompt are **blank ≈ +20–30 reserve points**, **first S ≈ +8–10**, and **target approximately 3 vowels/4 consonants** on a full rack; these are heuristics, not exact equity tables. citeturn20view0turn20view2 [LIKELY] Duplicate S is explicitly less precious than the first S. citeturn20view2

**Hooks and affixing.**  
[VERIFIED] (expert handbook) Short hooks and extensions are fundamental because adding one or a few letters to an existing word can simultaneously create the anchor for a perpendicular scoring word. citeturn23view0 [LIKELY] The model should therefore inspect both ends of every promising existing word, particularly those adjacent to premium squares, for **-S, -ED, -ING, -ER, -Y** and plausible **RE-, UN-, OUT-, IN-** extensions; none should be assumed legal without engine validation. citeturn23view0turn23view1

A particularly valuable pattern is a **hook square** where one newly placed tile both modifies an existing word and participates in the new main word. [LIKELY] That geometry extracts value from a single rack tile twice and can also unlock a word premium or perpendicular lane. citeturn23view0

**Parallel plays.**  
[VERIFIED] (expert handbook + expert strategy guide) Playing beside an existing word so that several newly placed tiles form short perpendicular crosswords is one of the highest-value patterns for developing players. The handbook shows ordinary-looking racks reaching the 20s and 30s through multiple overlaps; Breaking the Game argues that parallels should supply a very large fraction of beginner/intermediate scoring. citeturn23view0turn24search1

[LIKELY] Operational search rule: whenever two rows or columns can run adjacent, test a short main word for **multiple valid 2–3-letter crosses**, especially where a newly placed high-value tile reaches DL/TL. Premiums under newly placed crossing tiles can magnify the combined score. citeturn23view0

Plain-grid micro-example, using only common words:

```text
existing:  A N
new:       T O
```

[LIKELY] Playing **TO** parallel beneath **AN** also forms perpendicular **AT** and **NO**, so the turn scores all three newly formed words rather than only TO. The example illustrates the multiple-overlap mechanism described by the handbook. citeturn23view0

**Premium squares and defensive shapes.**  
[LIKELY] (expert handbook) Early and middle game, prioritize scoring and leave before defensive board cosmetics. A weak player should not burn 10–25 immediate points merely to cover a TWS because the opponent *might* exploit it. citeturn21view2turn21view3 [LIKELY] The handbook specifically warns that isolated TWS threats are often less important than bingo lanes when defending a lead. citeturn21view3

[VERIFIED] (standard scoring source + expert handbook) Parallel/premium combinations are especially attractive because a turn scores every newly formed word, while newly covered letter/word premiums apply during that play. citeturn24search22turn23view0

[LIKELY] When ahead late, remove flexible “floaters,” bingo alleys, and premium hotspots where doing so also scores reasonably; when behind, avoid strangling the board that you need for a comeback. citeturn21view2turn22view3 [SPECULATIVE] For small-model prompt simplicity, a useful tie-breaker is: **if two late-game moves differ by ≲5 points, prefer the one that closes the opponent's strongest bingo/premium lane when ahead**. No authoritative source gives this exact five-point cutoff; it is an engineering approximation of the handbook's “small sacrifice for effective defense” principle. citeturn21view2

**Bingo principles.**  
[LIKELY] (expert handbook) Favor leaves built from mutually compatible common letters rather than “good letters plus one clunker”; mixing a promising core with Q/J/X/Z often destroys bingo potential. citeturn20view2 Think in **stems**, meaning a strong four-to-six-letter core that combines with many draws, rather than memorizing one hoped-for seven-letter word. [VERIFIED] This agrees with both expert rack-leave advice and Quackle's empirically learned preference for leaves that generate future bingos. citeturn20view2turn25view1

[LIKELY] Do not over-fish. The handbook says a one-tile fish is justified only when the retained rack is exceptionally close to a bingo; in its example, keeping ERS alone produces a bingo on roughly one-third of subsequent draws, yet a much larger immediate score may still be preferable. citeturn20view2

**Exchange policy.**  
[LIKELY] (expert strategy guide) The cleanest published weak-player trigger found is: **strongly consider exchanging if you cannot score approximately 20 points or retain a balanced, bingo-prone leave**. citeturn24search0 [LIKELY] The handbook's worked vowel-heavy and consonant-heavy racks independently supports exchanging when both immediate score and resulting leave are poor. citeturn21view0

[SPECULATIVE] A deliberately simple automation rule is: **while the bag has more than about 15 tiles, exchange when the best move is under ~20 and every resulting leave remains severely duplicated or grossly imbalanced; keep the best 2–3 synergistic tiles.** The ~20 threshold is sourced; the >15 cutoff is a conservative engineering synthesis because expert literature begins “pre-endgame” thinking around 15 tiles, where zero-point exchanges become more position-dependent. citeturn24search0turn22view3

[LIKELY] Do not exchange seven automatically. Partial exchanges retaining ER, RT, IRT or another balanced useful core can dominate complete randomization. citeturn21view0

**Endgame play.**  
[VERIFIED] (expert handbook; AI literature) Once the bag is empty in a two-player game, correct tile tracking makes the opponent's rack deducible, turning play into a finite sequence problem. citeturn22view0turn24search19 [LIKELY] The first search should be an out-in-one; otherwise construct an out-in-two with either multiple second-turn outlets or a spot the opponent cannot block. citeturn22view1

[VERIFIED] (expert handbook) Going out first normally gains not only the move's points but also the rack-penalty swing and denies the opponent further scoring, so Q and other awkward/high-value leftovers become particularly dangerous. citeturn22view0turn22view1 [LIKELY] If the opponent can be stuck with an unplayable tile, rushing out can become inferior to safely scoring additional turns without reopening that tile. citeturn22view2

**Novice blunders by expected cost.**  
[SPECULATIVE] No robust public dataset was found giving population-average point losses per novice error, so this ordering is an engineering ranking based on direct scoring opportunities, published leave values, and expert examples—not measured novice averages.

**Very high expected cost:** missing a bingo or multi-cross premium play; retaining Q/J through repeated turns; or refusing a needed exchange and carrying a dysfunctional rack. [LIKELY] These can lose tens of points immediately or suppress several subsequent turns. citeturn23view0turn20view1turn21view0

**High expected cost:** burning a blank cheaply, worth roughly 20–30 points in expert leave heuristics; maximizing raw score while retaining duplicates or severe imbalance; and failing to recognize hooks/parallels. [LIKELY] citeturn20view0turn20view2turn23view0

**Medium expected cost:** burning the first S for <8–10 extra points; fishing from a merely “nice” rather than near-bingo rack; knee-jerk blocking TWS squares; or keeping U solely for a future Q. [LIKELY] citeturn20view2turn21view3

## Endgame checklist

1. **Reconstruct the opponent rack from the complete tile pool, board, and your rack.** [VERIFIED] Empty-bag tile tracking yields perfect rack information in two-player play. citeturn22view0turn24search19

2. **Flag Q, J, X, Z, awkward duplicates, and any tile with few remaining outlets on either rack.** [LIKELY] High-value/unwieldy tiles can create decisive endgame penalties or trapping opportunities. citeturn22view2

3. **Enumerate every out-in-one before considering ordinary scoring plays.** [LIKELY] Going out first is usually strategically superior even when another non-out scores substantially more immediately. citeturn22view1

4. **If no out-in-one exists, build an out-in-two with two second-move locations or one unblockable location.** [LIKELY] This is the handbook's central two-move endgame construction. citeturn22view1

5. **For each candidate, calculate the opponent's strongest reply—not an average reply—then your continuation.** [VERIFIED] Endgame strategy is explicit move-sequence optimization from both players' perspectives. citeturn22view0

6. **Block an opponent out when its scoring-plus-rack swing changes the result, especially if it strands their expensive tile.** [LIKELY] citeturn22view1turn22view2

7. **Prefer the line maximizing final score difference or win, not merely your next-turn score.** [VERIFIED] Expert endgame analysis evaluates the complete remaining sequence. citeturn22view0

8. **If an opponent tile is provably unplayable, consider scoring slowly without creating a new outlet for it.** [LIKELY] The handbook explicitly demonstrates this trapping strategy. citeturn22view2

## TOP-10 MICRO-RULES

1. **Scan parallel overlaps, hooks, and premium extensions before ordinary words.** [VERIFIED] citeturn23view0turn24search1

2. **Maximize score plus leave; avoid duplicates and severe vowel/consonant imbalance unless the extra score clearly compensates.** [VERIFIED] citeturn20view0turn20view2turn25view1

3. **Dump Q and J promptly; never save them indefinitely for a jackpot, and never keep U merely for an unseen Q.** [LIKELY] citeturn20view1turn20view2

4. **Keep a blank unless spending it gains about 20–30 points, completes a bingo, outs, or changes the game's outcome.** [LIKELY] citeturn20view0

5. **Keep your first S when another move scores within 8–10 points; treat a second S as a normal duplicate.** [LIKELY] citeturn20view2

6. **Strongly consider exchanging when no play reaches ~20 or keeps a balanced bingo-prone rack; exchange clunk, not automatically all seven.** [LIKELY] citeturn24search0turn21view0

7. **Prefer parallel plays creating several legal short crosswords, especially when a new tile also exploits a letter or word premium.** [VERIFIED] citeturn23view0turn24search22

8. **Fish one tile only from an almost-bingo rack; otherwise score and preserve a useful core.** [LIKELY] citeturn20view2

9. **Ahead late, close bingo lanes cheaply; behind late, preserve or create bingo and premium lanes.** [LIKELY] citeturn21view2turn22view3

10. **Bag empty: infer opponent tiles, search outs, test their best response, and prioritize a guaranteed fast out over raw immediate score.** [VERIFIED] citeturn22view0turn22view1

## Model-failure notes

[LIKELY] (independent 2025 Scrabble benchmark) **Placement reasoning is a more urgent prompt target than vocabulary.** ScrabbleBench initially required models to provide coordinates but abandoned that interface because models repeatedly produced off-by-one, disconnected, or otherwise impossible placements. It also observed “rack blinders”: models found plausible words from their tiles and asserted that those words fit without accurately checking the board. citeturn25view0

[LIKELY] (independent 2026 Scrabble arena; small sample) A separate 18-game LLM experiment showed the same pattern dramatically in Gemma 3 4B: when its plays were legal, scores could be competitive, but it repeatedly exhausted retries proposing words that did not fit the board. Even stronger models generated rejected placements. The author therefore interprets much of the failure as structured-state and constraint reasoning rather than vocabulary deficiency. citeturn25view2

[LIKELY] (research preprint) GTBench independently finds broader weaknesses in LLM strategic reasoning in complex complete/deterministic games and reports that extra Chain-of-Thought or Tree-of-Thought prompting does not reliably fix them. citeturn25view3

[SPECULATIVE] **Prompt implication for Libre Tiles:** spend scarce system-prompt tokens on a fixed search order—`hooks/parallels → premiums → score+leave → exchange → defense/endgame`—and require explicit board-fit verification immediately before the JSON tool call. This targets the observed small-model failure mode more directly than adding long word or stem lists. citeturn25view0turn25view2
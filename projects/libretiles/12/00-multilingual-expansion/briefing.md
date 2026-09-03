# Libre Tiles: multilingual expansion implementation briefing

You are implementing the next stage of Libre Tiles multilingual expansion.

This is implementation guidance, not an orchestration document.

The product goal is not merely to add one more language. The goal is to make Libre Tiles capable of supporting a large set of real Scrabble-language variants while keeping both gameplay rules and UI localization correct, maintainable, testable, and data-driven.

The repository already has working English, Slovak, Czech, and Polish gameplay variants and corresponding UI locales. Atomic tile-token work has also begun and must be treated as the architectural baseline rather than bypassed.

Do not reimplement solved multilingual foundations independently for each new language.

---

# 1. First principle: there are three separate concepts

Never collapse these into one concept:

## A. UI locale

The language in which Libre Tiles itself talks to the player.

Examples:

- `en`
- `sk`
- `cs`
- `pl`
- later `hu`, `de`, `fr`, etc.

This controls:

- buttons;
- dialogs;
- settings;
- lobby;
- game status;
- errors;
- accessibility strings;
- profile;
- dates;
- pluralization;
- descriptions.

It must NOT control game legality.

A player must eventually be able to play:

- Hungarian Scrabble with an English UI;
- Polish Scrabble with a Slovak UI;
- German Scrabble with a Czech UI.

Do not bind the selected gameplay variant to the UI locale.

---

## B. Language

The linguistic identity, usually represented by a BCP-47/ISO-like language code.

Examples:

- English: `en`
- Slovak: `sk`
- Czech: `cs`
- Polish: `pl`
- Hungarian: `hu`

This is useful metadata but is still not necessarily sufficient to identify one Scrabble ruleset.

---

## C. Game variant / ruleset

This is the authoritative Scrabble configuration.

A language may eventually have more than one real Scrabble distribution or ruleset.

Therefore do not make:

`language_code`

the primary game identity.

Continue using a stable variant slug.

Conceptually:

```text
slug: spanish-international
language_code: es
variant_name: International
```

or:

```text
slug: english
language_code: en
```

when there is only one supported edition.

This separation will save a future migration when a language has multiple national or historical distributions.

---

# 2. Do not implement 20+ languages as one mega-change

This is the most important project-management recommendation.

Do NOT create one giant commit/PR/logical implementation containing:

- 20+ dictionaries;
- 20+ distributions;
- 20+ UI translations;
- 20+ flag icons;
- hundreds/thousands of translated strings;
- dozens of special linguistic rules.

The resulting failures will be impossible to localize efficiently.

Instead first finish the reusable multilingual machinery and then add languages in small waves.

A good batch is approximately:

**2–4 closely related complexity profiles per implementation wave.**

Every batch should leave `main` fully playable.

---

# 3. Define what "adding a normal language" should eventually mean

For an ordinary supported language, adding gameplay should ideally require only something close to:

```text
backend/assets/variants/<variant>.json
backend/assets/dicts/<dictionary>.txt
backend/assets/dicts/<optional-two-tile-authority>.txt
backend/assets/dicts/<license/provenance>
tests for the new variant
```

and UI localization should ideally require:

```text
messages.<locale>.ts
locale metadata / registration
translation parity tests
```

plus a language icon or other presentation metadata if the product still uses them.

If adding German or Italian still requires editing core scoring, board, move search, persistence, and serializers, stop and determine whether a generic assumption remains in the engine.

---

# 4. Preserve the atomic tile-token model

The core invariant should be:

> One physical board square contains zero or one atomic game tile.

An atomic tile is NOT synonymous with:

- one Unicode code point;
- one JavaScript character;
- one Python character;
- one grapheme;
- one alphabet letter.

Examples of valid future atomic tokens include:

```text
A
Á
SZ
GY
CH
DŽ
LL
L·L
```

Therefore never introduce new logic equivalent to:

```python
len(tile) == 1
```

or:

```typescript
tile.length === 1
```

as a game-rule invariant.

Also avoid validating game tiles globally with:

```python
str.isalpha()
```

because a legitimate future tile can contain punctuation such as `L·L`.

Atomicity must come from the variant definition, not from Unicode shape.

---

# 5. Preserve the distinction between physical token and lexical text

A physical tile and the text contributed to a dictionary word are related but conceptually different.

Today many variants can use:

```text
physical token == displayed text == lexical contribution
```

Examples:

```text
A -> A
Á -> Á
SZ -> SZ
```

Do not bake that equality so deeply into new APIs that it becomes impossible to separate later.

The engine should preserve the physical sequence of tokens for:

- rack accounting;
- board occupancy;
- tile exchange;
- bingo counting;
- scoring;
- move history;
- persistence;
- drag/drop;
- AI placements.

Dictionary lookup may use the resulting lexical spelling.

Do not reconstruct physical tiles by blindly tokenizing the completed textual dictionary word unless absolutely necessary.

The board/rack already know which physical tokens were played. Preserve that information.

---

# 6. Do not confuse alphabet order with playable tiles

This distinction already matters for Slovak and Hungarian.

A language alphabet may contain letters which do not exist as physical tiles.

Conversely, a Scrabble set may define specific physical tokens.

Keep separate concepts for:

```text
alphabet_order
tile definitions / distribution
dictionary lexical space
```

`alphabet_order` is useful for:

- deterministic tile ordering;
- starting draw;
- display;
- language-aware token ordering.

It should not necessarily be treated as a full dictionary collation algorithm.

Do not rely on Unicode code-point sorting for official alphabet order.

---

# 7. Make variant JSON the source of gameplay configuration

A mature variant should contain or resolve the following classes of information.

Exact schema may evolve, but avoid scattering these decisions through Python/TypeScript conditionals.

## Identity

```text
slug
language
language_code
variant_name if applicable
```

## Provenance

```text
source
source_url
fetched_at / version date
ruleset edition if known
```

## Dictionary

```text
dictionary_file
dictionary identity/version
license/provenance
```

## Short-word authority

Where necessary:

```text
two_tile_words_file
```

The semantic concept should be physical two-tile words, not two Unicode characters.

Do not regress this into `len(word) == 2`.

## Tiles

Each physical tile must have:

```text
token
count
points
```

even if the historical JSON field is still called `letter`.

## Alphabet ordering

```text
alphabet_order
```

## Future-compatible rules

Where evidence requires them, allow variant-level policies such as:

```text
blank_targets
normalization profile
```

Do not add speculative fields merely because they might theoretically exist.

Add them when a supported real language needs them.

---

# 8. Variant-specific normalization needs a clean boundary

Never implement a universal rule such as:

```text
strip every accent
```

or:

```text
uppercase then ASCII-fold
```

for gameplay.

Different Scrabble languages interpret orthography differently.

Examples of the class of problem:

```text
Slovak: Á and A are distinct
French: many printed accents do not require distinct physical tiles
German: Ä/Ö/Ü matter differently from ß
Turkish: I and İ are distinct
```

Therefore gameplay normalization should belong to the variant/rules layer.

UI search folding is a separate problem.

The current UI already contains a search fold used to make language/variant pickers forgiving. That kind of folding must NEVER become dictionary legality logic.

---

# 9. Blank semantics should eventually be variant-driven

Avoid hardcoding:

```text
blank may represent every item in alphabet_order
```

or:

```text
blank may represent every physical tile
```

These sets may differ.

Model the concept cleanly enough that a variant can eventually expose:

```text
blank_targets
```

If all currently supported variants can derive this safely from playable tiles, derivation is fine.

But do not design APIs that make a later explicit target list impossible.

Tests should distinguish:

- physical blank token `?`;
- assigned value `blank_as`;
- rendered lexical value;
- zero scoring value.

---

# 10. Bag size and number of blanks must always be data-derived

Never assume:

```text
100 tiles
2 blanks
```

A language variant defines its own distribution.

The authoritative bag size is:

```text
sum(tile.count)
```

Similarly blank count comes from the variant distribution.

Starting draw, game-state reporting, endgame accounting, diagnostics and tests must work with arbitrary distribution sizes.

---

# 11. Gameplay language implementation checklist

Every new game variant must be verified through the same pipeline.

Do not merely prove that the JSON loads.

For each new variant verify:

## Variant load

- identity;
- language code;
- distribution;
- tile points;
- total tile count;
- alphabet order;
- dictionary file;
- optional two-tile authority.

## Bag

- exact physical token counts;
- exact total;
- correct blank count;
- no silent token loss.

## Starting draw

- correct alphabet ordering;
- blanks handled according to current game rules;
- multi-character tokens treated atomically.

## Rack

- exactly one rack slot per physical tile;
- exchange round trip;
- blanks;
- serialization.

## Placement

- server validates against the active variant;
- unknown token rejected;
- valid Unicode/multi-character token accepted.

## Board

- one token occupies exactly one coordinate;
- board does not shift because token text has multiple characters.

## Word formation

- lexical spelling constructed correctly;
- physical token sequence retained.

## Dictionary

- correct dictionary selected;
- no cross-language contamination;
- normalization correct.

## Two-tile authority

- correct physical-tile semantics;
- not based on Unicode string length.

## Scoring

- token points once;
- letter multiplier once per square;
- word multiplier once per premium square;
- blank remains zero;
- bingo counts physical tiles, not text length.

## AI

- correct language appears in AI context;
- rack tokens remain atomic;
- alphabet/tile values supplied correctly;
- backend candidates remain authoritative;
- model cannot invent illegal letters and bypass backend validation.

## Endgame

- leftover rack points;
- bag empty behavior;
- exchange limits;
- game-end scoring.

---

# 12. UI localization must remain independent and typed

Current UI localization is moving in the right direction.

Preserve one canonical message-key shape.

A new locale should fail tests/build if it is missing keys.

Do not allow:

```text
English has 540 messages
German has 491
```

with silent fallback hiding missing translation work unless fallback is an explicit temporary development mechanism.

Production-ready locale means message parity.

---

# 13. Do not translate code identifiers or protocol values

Translate user-facing text.

Do not translate:

```text
API field names
status enum values
error codes
game_mode values
variant slugs
JSON keys
websocket event names
provider identifiers
```

Correct pattern:

```text
backend:
code = "exchange_required"

UI:
t("game.errors.exchangeRequired")
```

Incorrect:

```text
backend returns "Výmena je potrebná"
frontend parses that sentence
```

The recent repository work already fixed one version of this class of defect around localized 429 prose.

Do not reintroduce it.

---

# 14. Server authority and UI locale

The recent i18n work intentionally made the server-resolved locale authoritative for rendered HTML.

Preserve that architecture.

A UI locale change needs to consistently update:

- locale cookie;
- `<html lang>`;
- server-rendered metadata/title;
- client LocaleProvider;
- subsequent backend request locale where applicable.

Do not create a second competing locale state machine.

Persisted Zustand state may assist UX, but should not become an independent language authority that disagrees with the server render.

---

# 15. Backend localization must use stable semantic codes

Where backend events need localized presentation, prefer structured semantics.

Examples:

```text
game end reason code
authentication error code
validation code
throttle metadata
```

Translate at the appropriate presentation boundary.

Do not make frontend behavior depend on detecting translated text.

For every future locale test security-sensitive messages as well, particularly:

- login failure enumeration resistance;
- authorization failures;
- rate limiting;
- validation.

Translations must not accidentally reveal information that English correctly hides.

---

# 16. Plurals must be language-aware

Do not assume English singular/plural logic.

English:

```text
1 tile
2 tiles
```

is not sufficient architecture for Slavic languages.

Polish already proves this.

Future locales may have more plural categories.

Continue using a locale-aware plural abstraction and test representative values such as:

```text
0
1
2
3
4
5
11
12
14
21
22
25
101
```

as appropriate for the locale.

Do not encode plural grammar inside components.

---

# 17. Dates/numbers must use locale-aware formatting

Never manually translate month names or build dates with string concatenation.

Use locale-aware platform APIs such as `Intl`.

Verify:

- game history dates;
- profile join date;
- timestamps;
- numeric formatting if exposed.

UI locale controls formatting.

Game language does not.

---

# 18. Accessibility is part of localization

Recent commits added substantial accessibility work.

Every new locale must include correct translations for:

- tile accessible names;
- rack positions;
- blank picker;
- buttons;
- dialogs;
- status/announcer text;
- search controls;
- game results.

Do not localize only visible strings.

Screen-reader output must be translated too.

For a multi-character tile, accessibility should describe one physical tile.

For example, Hungarian `SZ` is one tile, not two draggable letters.

---

# 19. Searchable locale/variant pickers

Current searchable premium pickers are a good foundation.

Keep game-variant discovery backend-driven.

Avoid rebuilding a giant hardcoded union such as:

```typescript
type Variant =
  | "english"
  | "slovak"
  | "czech"
  | "polish"
  | "hungarian"
  | ...
```

for every future variant.

Variant slugs are data.

Static frontend metadata may still exist for polished presentation, but unknown valid server variants must degrade gracefully rather than crash.

Likewise locale search should be accent-tolerant for UI discovery only.

---

# 20. Language names and flags need care

A language and a country are not identical.

Examples:

- English is not uniquely the UK or US.
- Spanish spans many countries.
- Portuguese spans Portugal/Brazil and others.

Do not make a country flag part of gameplay identity.

Flags can remain a presentation convenience if that is the chosen product UX, but architecture should use stable language/variant codes.

A missing flag should never make a valid game variant unplayable.

Eventually consider language-native labels such as:

```text
Deutsch
Français
Español
Magyar
```

alongside localized UI labels if useful.

---

# 21. Dictionary integration is the highest linguistic-risk area

Do not trust a word list merely because:

- it exists on GitHub;
- it is large;
- it calls itself a dictionary;
- Hunspell accepts it.

For each gameplay language document:

```text
source
version/date/commit
license
redistribution permission
normalization performed
number of entries
encoding
```

The Worker implementing a language must distinguish:

1. language dictionary;
2. official Scrabble word authority;
3. technically useful open-source lexicon.

These are not automatically the same.

Do not silently synthesize a game dictionary from general dictionaries if product intent requires official Scrabble validity.

If only a non-official open dictionary is available, encode/document that truth rather than presenting it as an official Scrabble lexicon.

---

# 22. Validate dictionary assets before activating the variant

Before a variant gets readiness=`playable`, mechanically verify its dictionary.

Suggested checks:

- UTF-8 strict decoding;
- NFC normalization;
- no BOM unless intentionally handled;
- no empty records;
- no accidental whitespace;
- no obvious headers in word data;
- deterministic duplicate removal policy;
- expected casing;
- stable sorted form if the engine benefits;
- no impossible symbols for the variant lexical rules;
- minimum/expected word count sanity;
- license/provenance file present.

Do not activate a language in Settings if the dictionary is missing or invalid.

Fail closed.

---

# 23. Add asset metadata validation

With many languages, hand-edited JSON will eventually contain errors.

Build tests which mechanically verify every installed variant.

For each JSON:

```text
unique physical tokens
counts > 0
points >= 0
exactly intended blank records
total_tiles matches derived total
all playable tokens normalized NFC
alphabet_order entries unique
required physical tokens present in alphabet ordering where applicable
dictionary exists
optional two-tile file exists
language_code shape valid
slug valid
source metadata present
```

Where an authoritative distribution gives a known tile count, assert it in the variant-specific test.

The generic loader should not necessarily hardcode these language-specific totals.

---

# 24. Never copy game rules from another language because it "looks similar"

Czech and Slovak are close linguistically.

That does NOT mean:

```text
same tile distribution
same short words
same blank targets
same dictionary rules
same alphabet ordering
```

Likewise:

```text
Danish != Norwegian != Swedish
Croatian != Slovenian
Spanish != Portuguese
Russian != Ukrainian
```

Reuse architecture, not linguistic facts.

Every variant needs its own sourced evidence.

---

# 25. Recommended expansion waves

Do not treat the exact number "28" as an architectural constant.

The product should support a catalog of approved variants.

The following waves are a complexity strategy, not a claim that each language belongs to a particular current Mattel catalog.

## Wave 0: finish the foundation

Before rapidly adding languages, ensure:

- atomic physical tokens work end-to-end;
- variant discovery is data-driven;
- alphabet order is explicit;
- short-word authority uses tile semantics;
- UI locale and game variant are separate;
- generic variant validation exists;
- locale message parity exists.

Hungarian is the best production stress test for this wave.

---

## Wave 1: ordinary Latin LTR languages

Good candidates include languages such as:

```text
German
French
Italian
Dutch
Danish
Swedish
Norwegian
Finnish
Icelandic
Romanian
Portuguese
```

They exercise:

- new distributions;
- diacritics;
- normalization differences;
- plural/date localization;
- dictionaries;

without demanding a fundamentally different board direction.

Implement these in small batches.

---

## Wave 2: languages with stronger token/rule quirks

Examples:

```text
Hungarian
Croatian
Welsh
Catalan
Spanish edition(s)
Turkish
```

These are useful for proving:

- multigraph atomic tiles;
- unusual token spelling;
- physical sequence restrictions;
- blank rules;
- special normalization.

Do not special-case them by language slug if a generic variant rule can express the behavior cleanly.

---

## Wave 3: non-Latin LTR scripts

Examples:

```text
Greek
Russian
Bulgarian
Ukrainian
```

By this point they should mostly prove that Libre Tiles is actually Unicode/script agnostic.

If adding Greek requires a core board redesign, something is still wrong in the foundation.

Likely work should concentrate around:

- assets;
- dictionaries;
- font coverage;
- AI prompting;
- locale translations;
- search/filtering.

---

## Wave 4: RTL

Treat this as a separate deliberate foundation.

Examples:

```text
Hebrew
Arabic
```

Do NOT sneak RTL into a random language batch.

It affects:

- layout direction;
- board/read direction decisions;
- bidirectional text;
- move notation;
- AI context;
- drag/drop expectations;
- punctuation;
- accessibility.

Make RTL its own bounded implementation.

---

## Explicit non-goal for the current expansion

Do not design now for Thai-style exotic multi-realization mechanics unless the product explicitly decides to support them.

Avoid making today's architecture worse in pursuit of hypothetical universal language coverage.

---

# 26. Font coverage is going to become a real problem

Latin EN/SK/CS/PL can hide font problems.

Greek, Cyrillic, Vietnamese-style diacritics and eventually Hebrew/Arabic can expose them.

Before enabling a locale/variant:

- inspect the actual production fonts;
- verify every tile glyph;
- verify UI strings;
- verify bold/black headings;
- verify numerals;
- verify fallback behavior.

Never bundle random replacement fonts without licensing review.

Avoid using tofu-box glyphs as a production fallback.

---

# 27. Multi-character tile visual design

Do not shrink every tile globally because Hungarian has `SZ`.

Tile component should adapt only when necessary.

Preserve:

- physical tile size;
- point placement;
- drag target;
- rack spacing.

Adjust face typography for longer tokens.

Test at least:

```text
A
Á
SZ
DŽ
L·L
```

as synthetic/render cases.

A multi-character token still occupies one tile.

---

# 28. AI opponents require explicit language awareness

This is especially important because Libre Tiles uses smaller/free models.

Do not assume an LLM infers gameplay language solely from rack letters.

AI context should state clearly:

```text
game variant
language
rack as atomic tokens
board as coordinates/cells
tile values
blank rules where relevant
dictionary validation remains server authoritative
```

For Hungarian:

```text
["A", "SZ", "GY", "?", ...]
```

not a concatenated string.

The prompt should explicitly explain that `SZ` and `GY` are one physical tile when applicable.

Do not trust the AI to know official Scrabble distributions.

The backend provides truth.

---

# 29. Never make LLM correctness part of game legality

The LLM proposes.

The engine decides.

For every language:

```text
LLM move
→ structural validation
→ rack ownership
→ variant-token validation
→ physical legality
→ dictionary authority
→ scoring
→ apply
```

No locale-specific prompt should bypass backend validation.

This is especially important once dictionaries become less familiar to the model.

---

# 30. Do not explode prompts with full dictionaries

A full word list does not belong in the LLM prompt.

Continue using backend:

- membership checking;
- prefix search;
- ranked candidates;
- move validation.

Prompt only the compact information needed for move choice.

This is critical when supporting many languages and free-tier models.

---

# 31. Test the model-independent engine first

For every variant, tests should succeed without any live LLM provider.

A language is not "supported" because one AI happened to make a valid move once.

Core acceptance:

```text
pure engine
backend services
REST
persistence
frontend state/rendering
```

Then separately exercise AI integration.

---

# 32. Add one universal multilingual variant test harness

Instead of creating 20 nearly identical test files, create parameterized generic tests where appropriate.

Conceptually:

```text
for each playable variant:
    loads
    has dictionary
    distribution totals correctly
    playable token set non-empty
    blank exists if expected
    tile points complete
    alphabet metadata valid
    can create game
    starting draw works
    rack contains variant tokens
```

Then retain dedicated tests for genuinely language-specific rules.

Use:

```text
generic invariant tests
+
language-specific fixture tests
```

not:

```text
copy test_slovak.py twenty times
```

---

# 33. Add translation parity tests across every locale

The English message catalog should effectively define the key contract.

For every locale ensure:

```text
keys(locale) == keys(en)
```

unless an intentional mechanism says otherwise.

Also detect:

- accidentally empty string;
- untranslated English placeholder where prohibited;
- interpolation variable mismatch.

Example bug to catch:

```text
EN: "Player {name} won"
PL: "Gracz {username} wygrał"
```

If runtime expects `{name}`, the translation is broken.

Validate placeholder sets.

---

# 34. Test translated strings for layout expansion

German and several other languages can be substantially longer than English.

Czech/Polish already give a taste of this.

Manually or visually test:

- action buttons;
- game controls;
- settings cards;
- modals;
- mobile widths;
- overlay pills;
- game-over dialog;
- error banners.

Avoid fixed widths based on English text.

Text should wrap or containers should grow gracefully.

---

# 35. Do not localize proper technical/game identities accidentally

Decide deliberately which terms are translated.

Examples requiring product decision:

```text
Libre Tiles
Scrabble terminology
Double Letter
Triple Word
Bingo
AI
model names
provider names
```

Use the i18n glossary as terminology authority.

Once a term is chosen for a locale, keep it consistent.

Do not let different Workers translate the same concept differently in different files.

---

# 36. Build a durable localization glossary

Current `GLOSSARY.md` is the right direction.

Expand it as languages grow.

For each locale or shared concept record preferred translations for recurring game terms:

```text
tile
rack
bag
board
move
exchange
pass
blank
score
word
dictionary/lexicon
opponent
game
variant
interface language
game language
double-letter
triple-letter
double-word
triple-word
```

The glossary prevents LLM-generated translation drift.

A strong LLM should read this before generating a new locale.

---

# 37. Native-speaker quality gate where possible

LLMs are useful for first-pass translation, but UI text should ideally receive at least one quality check from:

- a native speaker;
- a highly reliable authoritative translation source;
- another strong independent language model used as critic.

Particularly review:

- concise buttons;
- game terminology;
- plural forms;
- authentication/security messages;
- error text;
- accessibility text.

Literal translations often sound robotic.

---

# 38. Source gameplay facts separately from UI translation

Do not let an LLM "remember" a tile distribution.

For every language, research gameplay facts independently.

Require evidence for:

```text
tile token
count
points
blank count
alphabet/order
special multigraph rules
blank restrictions
official/accepted dictionary
short-word authority if required
```

Record the sources in variant metadata/docs/tests where appropriate.

UI translation is subjective linguistic work.

Tile distribution is factual game data.

Treat them differently.

---

# 39. Suggested definition of "playable language complete"

A gameplay language is complete only when:

1. authoritative/reasonable distribution is present;
2. dictionary is present;
3. dictionary redistribution is legally acceptable;
4. variant loads;
5. alphabet/token model is correct;
6. blank behavior is correct;
7. bag/rack counts are correct;
8. human move works;
9. exchange/pass work;
10. scoring works;
11. move search works;
12. AI candidate pipeline works;
13. persistence works;
14. history/reload works;
15. frontend renders every physical tile;
16. tests pass.

A JSON file alone is not a completed language.

---

# 40. Suggested definition of "UI locale complete"

A UI locale is complete only when:

1. locale registered;
2. full key parity;
3. glossary reviewed;
4. placeholders match;
5. plurals tested;
6. date formatting tested;
7. settings language picker works;
8. metadata/title localized;
9. auth localized;
10. lobby localized;
11. game board/actions localized;
12. AI overlay localized;
13. dialogs localized;
14. profile localized;
15. history localized;
16. accessibility localized;
17. backend-presented end reasons/errors behave correctly;
18. responsive layout reviewed.

Do not call a locale complete merely because Settings and Game screen are translated.

---

# 41. Avoid coupling release readiness of gameplay and UI unnecessarily

A useful product decision is whether:

```text
German gameplay
```

must wait for:

```text
German UI
```

Technically they should remain independent.

For example, Libre Tiles could safely support German gameplay while its UI remains English.

However, if product policy requires every gameplay language to ship with a matching UI locale, enforce that at catalog/readiness level.

Do not enforce it through architecture.

---

# 42. Readiness should be explicit

With many languages, you will eventually have assets in progress.

Useful conceptual states:

```text
unavailable
incomplete
playable
```

Potentially UI locale availability has its own status.

Do not expose half-installed variants as playable just because their JSON file exists.

The backend variant catalog should remain authoritative.

---

# 43. Prefer catalog-driven frontend presentation

The backend already exposes meaningful variant metadata.

Continue moving toward:

```text
backend owns available gameplay variants
frontend renders catalog
```

rather than duplicating all game variants in TypeScript.

Static frontend enhancements such as a flag/icon can be optional metadata/fallback.

Eventually consider exposing enough catalog metadata that adding a normal new gameplay variant requires minimal or zero frontend code.

Possible safe catalog metadata:

```text
slug
language_code
display_name
variant_name
readiness
```

Potential presentation metadata should be evaluated separately.

---

# 44. Locale registry can remain explicit

Unlike game variants, UI locales contain compiled TypeScript message files.

It is reasonable for supported UI locales to be explicitly registered in:

```text
LOCALES
```

because adding a locale requires shipped application code.

Do not force UI locale discovery into the same dynamic mechanism as gameplay variants.

They have different deployment semantics.

---

# 45. Think in capability profiles, not language names

When deciding whether a language requires engine work, classify it by features:

```text
latin / greek / cyrillic / rtl
single-token labels
multi-codepoint tokens
special lexical realization
variant-specific normalization
blank restrictions
special alphabet order
plural complexity
```

Then ask:

> Does the engine already support this capability?

If yes, the new language should mostly be data.

If no, implement the generic capability first and use the language as its acceptance fixture.

Never add:

```python
if variant.slug == "hungarian":
```

unless the rule is truly exclusive and cannot be represented generically.

---

# 46. Maintain a language capability matrix

Create or maintain a small developer-facing matrix, not necessarily user-facing.

Conceptually:

| Variant | Script | Atomic multigraph | Special normalize | Special blank | RTL | UI locale |
|---|---|---:|---:|---:|---:|---:|
| English | Latin | no | no | no | no | yes |
| Slovak | Latin | no physical multigraph | yes/basic | inspect | no | yes |
| Czech | Latin | no | inspect | inspect | no | yes |
| Polish | Latin | no | inspect | inspect | no | yes |
| Hungarian | Latin | yes | inspect | inspect | no | planned |

As variants grow this makes the remaining architectural gaps obvious.

Do not make the matrix itself runtime authority.

Runtime truth remains the variant configuration/code.

---

# 47. Recommended concrete implementation sequence from the current repository state

## Step 1

Reverify current `main` and audit the atomic-token implementation end-to-end.

Do not assume previous commits completed every frontend/API edge merely because pure `gamecore` is atomic.

Specifically search again for:

```text
length === 1
.length(1)
max_length=1
len(...) == 1
row[col] on serialized text
join(tile...)
split characters
isalpha()
[A-Z]
```

Classify findings.

Fix only actual surviving gameplay assumptions.

---

## Step 2

Finish Hungarian as the production atomic-token acceptance language.

Hungarian should prove:

```text
SZ
GY
CS
NY
LY
TY
ZS
```

as atomic physical tiles wherever applicable to the selected official distribution.

Test at least two independently, not only `SZ`.

Do not consider Hungarian complete until a real game survives:

```text
draw
rack
placement
score
persist
reload
AI candidate
render
exchange
```

with a multigraph tile.

---

## Step 3

Complete generic variant metadata validation.

Before adding many JSONs, make malformed language assets fail loudly.

This prevents copying subtle mistakes twenty times.

---

## Step 4

Complete the generic locale quality harness.

Before adding many `messages.xx.ts` files, ensure:

```text
key parity
placeholder parity
plural tests
locale registration tests
```

are automatic.

---

## Step 5

Add 2–4 ordinary LTR Latin languages.

Choose languages with reliable redistributable dictionaries.

Use this batch primarily to prove that the process is now repetitive data work.

If each language requires bespoke engine patches, stop expanding and fix the abstraction.

---

## Step 6

Add the next complexity-profile batch.

Use a language only when it adds useful real-world coverage or tests a capability that matters.

Do not chase exotic mechanics solely for architecture purity.

---

## Step 7

Add Greek/Cyrillic.

Use this as the Unicode/font/script-agnostic acceptance gate.

---

## Step 8

Only after the mainstream LTR catalog is healthy, decide whether RTL deserves its own foundation.

Do not mix it into ordinary localization work.

---

# 48. Definition of architectural success

The multilingual foundation has succeeded when adding a normal language looks boring.

A strong Worker should eventually be able to say:

```text
Added variant JSON.
Added licensed dictionary.
Added source metadata.
Added locale messages.
Added tests.
No core engine changes required.
```

That is the target.

The most dangerous outcome is twenty language slugs accompanied by twenty tiny exceptions distributed across:

```text
board.py
services.py
move_search.py
route.ts
Tile.tsx
settings/page.tsx
```

That becomes a localization jungle.

Keep the jungle in the dictionaries. Keep the engine boring.

---

# 49. Things to actively resist during implementation

Do not:

- implement all remaining languages in one branch;
- use Wikipedia memory as the only distribution authority;
- guess dictionary licenses;
- conflate UI locale with game language;
- assume every language has one Scrabble edition;
- hardcode a frontend union for every game variant;
- use Unicode length as tile count;
- use textual word length as bingo count;
- globally strip accents;
- use UI search folding for dictionary legality;
- assume 100 tiles;
- assume two blanks;
- assume Latin;
- assume LTR forever;
- implement RTL prematurely;
- implement Thai mechanics prematurely;
- add per-language engine `if` branches where variant metadata can express the rule;
- let AI decide legality;
- trust a language because one sample move worked;
- expose incomplete variants;
- silently fall back to another dictionary;
- parse behavior from localized error prose;
- forget accessibility translations;
- forget mobile layout expansion;
- forget font glyph coverage.

---

# 50. What to optimize for

Optimize for this workflow:

```text
Research authoritative rules
        ↓
Acquire legally usable dictionary
        ↓
Create variant data
        ↓
Run generic variant validators
        ↓
Run language-specific rule tests
        ↓
Create UI locale
        ↓
Run translation contract tests
        ↓
Run full backend/frontend regression
        ↓
Manual language UX/gameplay acceptance
        ↓
Mark playable
```

Every new language should travel the same road.

Do not optimize for the raw number of languages committed.

Optimize for the number of languages that are actually trustworthy and playable.
Artifact class: **Orchestrator-authored decision and evidence record**, not a Worker exchange and not
authority. Logical whole `ui-internationalization` (Meta 10/00). Filename deviation per
`90_orchestrator-restoration.md`.

Produced after Cooperator decision **8 = option B** (`en + sk + cs + pl` interface locales), given
2026-09-02. This file carries the terminology the Cooperator delegated to the Orchestrator and the
primary-source evidence behind every entry. Its durable home for the shipped product is
`frontend/src/lib/i18n/GLOSSARY.md`; this is the design record.

---

# 1. Cooperator decision 8, recorded

```text
Question put to him ONCE, with three options and a recommendation:
  which locales does the INTERFACE ship in?
  A  en + sk                B  en + sk + cs + pl  (recommended)   C  all five including hu
His answer, verbatim: `1. B`
```

So the `Locale` union grows from `["en","sk"]` to `["en","sk","cs","pl"]`. Interface locale and game
variant remain **two independent axes**; B makes them coincide in extent, not in meaning. Hungarian
interface is **not** shipped, which is consistent with Hungarian gameplay being blocked on a real
inflection lexicon (`11/02`). `frontend/public/hu.png` is committed and currently **unreferenced** —
that is deliberate, not a defect: it is ready for `11/02` and costs 242 B.

---

# 2. Method

The Cooperator's instruction was explicit: he decided `písmeno` / `zásobník` / `žolík` for Slovak
personally, said Czech was "obviously the same", said he does not know Polish or Hungarian, and told the
Orchestrator to **solve it itself** and he would report bugs on the fly. The handout's recorded method
is: research actual Scrabble usage in that language, present a short evidenced recommendation, and let
him overrule.

Sources are **primary and national**, not dictionaries and not machine translation. Every one was
retrieved and parsed directly on **2026-09-02**:

```text
pl   Polska Federacja Scrabble — official rules + tournament regulations
     https://pfs.org.pl/regulaminy.php            retrieved 2026-09-02, 82 188 B, parsed to text
     status: current national federation regulations
cs   Česká asociace Scrabble — "Pravidla hry scrabble"
     https://scrabble.hrejsi.cz/pravidla          retrieved 2026-09-02
     status: current national association rules. NOTE: the sub-pages are Turbo-rendered and return
     HTTP 404 to a plain HTTP client; the page had to be read through a real browser engine. Recorded
     because the next person will hit the same 404 and must not conclude the page is gone.
cs   Wikipedie, "Scrabble" (cs)                    retrieved 2026-09-02, corroborating only
sk   Wikipédia, "Scrabble" (sk), via the MediaWiki extracts API
     retrieved 2026-09-02, used to TEST the Cooperator's own Slovak decision rather than assume it
```

Locked fork 7 (Browser MCP forbidden as a diagnostic driver) was respected in substance: CLI routes were
tried first and exhausted — `curl` returned HTTP 404 on every `/pravidla*` sub-path, DuckDuckGo served a
bot challenge, and the MediaWiki API returned nothing for the Czech terms. The browser was used for
**one** page of external public research, not to diagnose the product. The lock's stated reason is that
browser-driven *diagnosis* was too slow; that reason does not apply here.

---

# 3. The result — and the Cooperator's Czech assumption is WRONG

```text
              tile          letter     rack        blank                    bag        board
en            tile          letter     rack        blank                    bag        board
sk  DECIDED   písmeno       písmeno    zásobník    žolík                    vrecko     hracia plocha
cs  EVIDENCED kámen         písmeno    zásobník    žolík                    sáček      hrací deska
pl  EVIDENCED płytka        litera     stojak      blank                    woreczek   plansza
```

## 3.1 Czech: the tile is `kámen`, and `písmeno` means the LETTER

⛔ **This contradicts what the Cooperator stated.** He said that for Czech `písmeno` is clearly right
just as in Slovak. The Czech Scrabble Association's own rules use `kámen` for the physical tile
throughout and reserve `písmeno` for the letter printed on it. Verbatim, from
`https://scrabble.hrejsi.cz/pravidla`:

```text
"Každý hráč si vytáhne ze sáčku jeden KÁMEN. Hráč s PÍSMENEM nejblíže k začátku abecedy začíná."
"Poté si každý hráč vylosuje sedm KAMENŮ a uloží do svého ZÁSOBNÍKU tak, aby je ostatní neviděli."
"Hráč, který je na řadě, vybere ze svého ZÁSOBNÍKU jeden nebo více KAMENŮ a položí je na hrací desku."
"PRÁZDNÝ KÁMEN (ŽOLÍK) lze použít místo kteréhokoli PÍSMENE ... Hráč však musí oznámit, místo kterého
 PÍSMENE ŽOLÍK použil."
"Za každé PÍSMENO všech nově vytvořených nebo obměněných slov obdrží hráč počet bodů, který je na něm
 uveden."
"Hráč, který v jednom tahu umístí všech sedm KAMENŮ ze svého ZÁSOBNÍKU, získá zvláštní prémii 50 bodů."
```

The two words do different jobs in one sentence — `kámen` is the object you pick up, `písmeno` is what
is printed on it and what scores points. Using `písmeno` for the tile in Czech would collide with the
word the rules use for the letter, in exactly the place where the distinction matters (the blank
picker and the score explanation).

**Decision: Czech ships `kámen`.** Not asked as a question, per his standing instruction to be asked
less: the evidence is stated and one word from him overrides it.

## 3.2 Slovak: he was right, and here is the proof he was right

The Orchestrator offered `kameň` and `dlaždica`; he rejected both and chose `písmeno`. Tested against
Slovak Scrabble usage rather than assumed:

```text
sk.wikipedia "Scrabble", full text:   písmen* 29 occurrences   kameň/kamen 0 occurrences
"Na začiatku hry hráči vytiahnu po jednom PÍSMENE. Hráč s PÍSMENOM najbližšie k začiatku abecedy ..."
"Všetci hráči si vytiahnu po sedem PÍSMEN a uložia ich do svojho ZÁSOBNÍKA ..."
"... po položení PÍSMENIEK na hrací plán ..."
"Hráči si spočítajú hodnotu PÍSMEN vo svojom ZÁSOBNÍKU"
zásobník 9 occurrences        žolík 2 occurrences        vrecko present
```

`kameň` appears **zero** times in Slovak Scrabble usage. His override was not personal taste — it was
the actual national convention, and the Orchestrator's two suggestions were both outside it. **This is
the fourth time his answer beat the Orchestrator's recommendation, and the first time the Orchestrator
has been able to prove why with a primary source.**

Consequence worth stating: Slovak and Czech genuinely diverge here despite being close languages, and
"it is obviously the same in Czech" was the reasonable-sounding inference that turned out false. That is
the same failure shape as a negative grep.

## 3.3 Polish: all three unverified candidates were correct

The handout labelled `płytka?` `stojak?` `blank?` as unverified candidates. All three are confirmed by
the Polska Federacja Scrabble regulations, with frequencies over the whole document:

```text
płytka   62      stojak   28      blank   24      woreczek 26  (worek 1)     plansza 49
"Gracze mają do dyspozycji 98 PŁYTEK z literami alfabetu oraz dwie PŁYTKI PUSTE, które będziemy
 nazywać BLANKAMI."                       <- the rules NAME the blank explicitly
"Przed rozpoczęciem gry każdy jej uczestnik bierze STOJAK, na którym będzie układał swoje PŁYTKI."
"Na koniec każdego ruchu gracz dobiera z WORECZKA tyle płytek, ile wyłożył, dzięki czemu zawsze ma na
 STOJAKU siedem płytek."
```

`blank` is a normal Polish masculine noun and **declines**: `blank`, `blanka`, `blankiem`, `blanki`,
`blanków`, `blankami`. Any parameterized string touching it must decline it correctly rather than
concatenating a fixed form.

---

# 4. Actions, and one that would have shipped a wrong word

```text
en    tile          letter    rack        blank      bag        board          word    point   move
sk    písmeno       písmeno   zásobník    žolík      vrecko     hracia plocha  slovo   bod     ťah
cs    kámen         písmeno   zásobník    žolík      sáček      hrací deska    slovo   bod     tah
pl    płytka        litera    stojak      blank      woreczek   plansza        słowo   punkt   ruch

              premium square      exchange    pass                 50-pt bonus
sk            prémiové pole       Vymeniť     Vynechať             prémia 50 bodov
cs            prémiové pole       Vyměnit     Vzdát tah            prémie 50 bodů
pl            pole premiowe       Wymiana     Pauza                premia 50 punktów
```

⚠ **`pass` in Polish is `Pauza`, and `Pas` would have been wrong.** The Orchestrator's instinct was
`Pas`, by analogy with the Slovak reasoning where `pas` was rejected as a card-game term. Measured
against the PFS regulations: **`pas` appears ZERO times**, while `pauza` / `pauz*` appears 24 times and
has its own numbered section:

```text
3.4.    Pauza
3.4.2.  "Zawodnik zgłaszający pauzę mówi „PAUZA", wyłącza zegar ..."
3.4.3.  "Cztery kolejne PAUZY oznaczają zakończenie partii. Wymiana ani strata kolejki nie jest pauzą."
5.1.4.  "Jeżeli partia kończy się czterema PAUZAMI z rzędu ..."
```

A Polish player literally says "pauza" to pass. Checking cost one grep and prevented shipping the wrong
verb on a primary game button.

Czech is the mirror image and is worth recording as a curiosity that must **not** be copied into the UI:
the Czech rules say the player announces a pass with the **English** word — *"Ostatním to oznámí tím, že
řekne pass."* A spoken table call is not a button label; the Czech button says `Vzdát tah`.

---

# 5. The mechanical trap decision B introduces: Polish needs a THIRD plural function

`pluralSk(n, one, few, many)` implements `1 / 2..4 / otherwise`. That is correct for Slovak **and for
Czech** — both take the genitive plural from 5 upward and for 21, 22, 101, so `22 minút` and `22 minut`
are right. It is **wrong for Polish**, which keys on the last digit with a 12–14 exception:

```text
n            sk           cs           pl
1            minútu       minutu       minutę
2, 3, 4      minúty       minuty       minuty
5 .. 21      minút        minut        minut
22, 23, 24   minút        minut        MINUTY      <- pluralSk would produce "minut" here
25 .. 31     minút        minut        minut
112 .. 114   minút        minut        minut
122 .. 124   minút        minut        MINUTY
```

Required shape, and it must be a separate function rather than a parameter on the existing one:

```ts
export function pluralPl(n: number, one: string, few: string, many: string): string {
  const abs = Math.abs(Math.trunc(n));
  if (abs === 1) return one;
  const mod10 = abs % 10;
  const mod100 = abs % 100;
  if (mod10 >= 2 && mod10 <= 4 && !(mod100 >= 12 && mod100 <= 14)) return few;
  return many;
}
```

`pluralSk` is reused verbatim for Czech. Naming it `pluralSk` while calling it from `messages.cs.ts`
would be confusing, so it gets an exported alias `pluralCs = pluralSk` with a comment recording that
Slovak and Czech share the integer rule and that the shared name is deliberate, not an accident. The
existing `uii-01-N02` residual (the third argument is CLDR `other`, not CLDR `many`) is unchanged and
still correct for integer counts, which is every count in this product.

**Points abbreviate differently too**, and the score panel is the tightest container in the product:

```text
en  pts        sk  b.        cs  b.        pl  pkt
```

`pkt` is the PFS regulations' own abbreviation — their score tables are headed `Płytki / Pkt.` — so
Polish is one character wider than Slovak and Czech in the worst container. That is a layout item for
the R1/R3 acceptance batch, not a translation question.

---

# 6. Consequences for keys that already exist

The 57 existing keys are not neutral about terminology. Four of them change meaning per locale:

```text
draw.subtitle       en "Whoever draws the tile closer to A starts. A blank always wins."
                    sk "Začína ten, kto vytiahne písmeno bližšie k A. Žolík vyhráva vždy."   (shipped)
                    cs must say KÁMEN, not písmeno:  "Začíná ten, kdo vytáhne kámen blíž k A ..."
                    pl must say PŁYTKA:              "Zaczyna ten, kto wyciągnie płytkę bliżej A ..."
draw.pending        sk "Ťahám písmená z vrecka..."  cs "sáčku"  pl "woreczka"
draw.blankCaption   sk "žolík"   cs "žolík"   pl "blank"
draw.reason.*       three strings, all naming the blank
settings.gameVariant.description
                    sk "Písmená, vrecko a lexikón."  cs "Kameny, sáček a lexikon."
                    pl "Płytki, woreczek i leksykon."
```

**The `BlankPicker` heading works in all four locales, for two different reasons.** In Slovak
"Vyber písmeno pre žolíka" reads correctly *precisely because* `písmeno` (tile) and `žolík` are distinct
words. In Czech "Vyber písmeno pro žolíka" reads correctly for the *opposite* reason — `písmeno` means
the letter there, which is literally what is being chosen. Polish is unambiguous: "Wybierz literę dla
blanka". Same sentence shape, three different grammatical justifications, and none of them accidental.

## 6.1 One Orchestrator-owned wording change, disclosed rather than slipped in

`settings.uiLanguage.en` currently renders as `Angličtina` in Slovak — an exonym translated into the
active locale. With four locales that becomes a 4x4 matrix of sixteen translated language names, and it
has a real usability defect: a user who has accidentally set an interface language they cannot read
cannot find their own language in the list.

**Decision: the interface-language list uses endonyms** — each language named in itself, identical in all
four catalogs:

```text
English      Slovenčina      Čeština      Polski
```

That is standard practice for a language switcher, it collapses sixteen strings to four constants, and
it makes the R1 dropdown's diacritic-insensitive autocomplete meaningful ("cestina" matching "Čeština"
is exactly the example the Cooperator gave). The **game-variant** list is a different control and keeps
translated exonyms via `settings.gameVariant.*`, because a Slovak player choosing a *lexicon* is reading
Slovak prose; that panel already works this way through `VARIANT_NAME_KEYS` in
`GameLanguagePanel.tsx:13-18` with a `display_name` fallback, and it is not changed.

---

# 7. What is NOT decided here

```text
Hungarian terminology   NOT researched and NOT needed. Decision B excludes the hu interface. The
                        handout's candidates (betű? tartó? joker?) remain UNVERIFIED and must not be
                        used. hu.png stays committed and unreferenced until 11/02.
Register in cs and pl   Slovak is tykanie by Cooperator decision 3. Czech and Polish inherit the
                        informal register by consistency: Czech ty-forms, Polish 2nd person singular
                        ("Zaczynasz ty", not "Pan zaczyna"). Orchestrator decision, stated so it can be
                        overruled; Polish formal address would be a materially different product voice.
Board (cs)              the Czech rules use hrací deska and hrací plán interchangeably; hrací deska is
                        chosen because it is the one used in the placement clauses.
Word (pl)               PFS uses wyraz in numbered clauses (53) and słowo in prose (58). UI copy uses
                        słowo, which is the everyday word.
```

---

# 8. Where this goes

`frontend/src/lib/i18n/GLOSSARY.md` must grow a per-locale table with these entries and the plural
contract before the first cs/pl translation batch enters the tree. That file is inside the next Worker
slice's allowlist. Every subagent that produces a candidate translation batch receives this table and
the register rule verbatim, so batches cannot drift apart.

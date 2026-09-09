### Report for ORCHESTRATOR_CHAT

```text
Logical whole identity: admin-frontend-console
Worker session ordinal: 09, Worker exchange ordinal: 01

Status: PASS
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: not-applicable
Logical-whole closure: not-closed
Start commit: f040a644f9f233234ba94ec6f2a620eebc933c39
End commit: f040a644f9f233234ba94ec6f2a620eebc933c39
Changed files and purpose: none — this exchange mutates nothing
Commit/push result: not-applicable
Resolved Execution Issues / Near-Misses: pôvodný baseline/mode gate vyriešený explicitným obnovením autority Cooperatorom
Pre-Existing Failure Classification: none
```

**PASS sa vzťahuje na pripravenosť technického plánu.** Implementácia, výkon endpointu a browserová akceptácia ešte neprebehli. Aktuálne používateľské povolenie nahradilo pôvodný blokujúci baseline a požiadavku natívneho režimu; analýza prebehla bez zmien repozitára.

```text
Planning cycle: targeted-revision
Prior planning report: predchádzajúci BLOCKED report v tomto chate
Targeted revision basis: explicitné povolenie Cooperatora pokračovať a dopracovať plán
Changed decision boundary: prijatý skutočný HEAD; plánovanie v dostupnom režime klienta
Preserved unaffected decisions: advisory, read-only, no network, no secrets, no implementation
Automatic targeted revisions used: 0
```

### D1 — Analytics Data Model & Aggregation Queries

**Odporúčaný návrh je čítacia analytická vrstva nad existujúcimi tabuľkami, bez novej perzistencie, migrácie alebo zásahu do vykonávania hry.** Najdôležitejšie je správne pripisovanie výsledkov a meraní.

Repozitár potvrdzuje tieto východiská:

| Zistenie | Dôsledok pre návrh |
|---|---|
| Skóre patrí `PlayerSlot`; víťaz je `GameSession.winner_slot`. | Výsledky počítať zo sedadiel, nie z `GameSession.ai_model` samotného. |
| Playground uchováva snapshot oboch konfigurácií. | CPU identitu a konfiguráciu simulácie čítať zo snapshotu. |
| Model aj prompt bežnej hry sa môžu zmeniť. | Posledné nastavenie nemožno vydávať za konfiguráciu celého zápasu. |
| Ťah obsahuje požadovaný aj vykonávajúci model. | Víťazstvo konfigurácie a autorstvo vykonávajúceho modelu majú odlišné menovatele. |
| Diagnostika môže odkazovať na už existujúci `Move`. | Diagnostický záznam sa nesmie započítať ako ďalší herný ťah. |
| Aktuálny diagnostický runner zapisuje režim `fake` a niektoré metriky ako `None`. | Simulované merania nepatria do produkčného odporúčania; chýbajúce hodnoty zostávajú neznáme. |

Opora: [dátové modely](/home/agile/Projects/libretiles/backend/game/models.py:17), [snapshot simulácie](/home/agile/Projects/libretiles/backend/game/simulations.py:35), [zmeny modelu a promptu](/home/agile/Projects/libretiles/backend/game/services.py:1870), [diagnostický záznam](/home/agile/Projects/libretiles/backend/game/management/commands/run_diagnostic_match.py:445).

**Rozsah dát a filtre**

Endpoint:

```text
GET /api/admin/analytics/
    ?days=30
    &source=all
    &variant_slug=all
```

- `days`: celé číslo 1–365, predvolene 30.
- `source`: `all | gameplay | playground | diagnostic`.
- `variant_slug`: `all` alebo nainštalovaný variant.
- Neplatné, opakované alebo neznáme parametre: HTTP 400.
- Kohorta zahŕňa hry vytvorené v intervale `[as_of − days, as_of)`. UI výslovne uvedie „Games started in this period“.
- Rozdelenie zdroja: playground podľa existencie `PlaygroundSimulation`; diagnostika podľa diagnostického príznaku/väzby; zvyšok gameplay. Konfliktné záznamy vykázať ako nejednoznačné a nepoužiť na odporúčanie.
- Zmiešané varianty alebo zdroje možno zobraziť ako opisný prehľad. Odporúčanie výkonnosti vyžaduje porovnateľnú kohortu.

**Presné definície výsledkov**

| Metrika | Definícia |
|---|---|
| `games_played` | Počet rôznych hier s účasťou danej konfigurácie. |
| `seat_appearances` | Počet jej sedadiel; pri CPU proti CPU sú dve účasti v jednej hre. |
| `completed_seats` | Účasti v hre so `status="finished"` a `game_over=True`. |
| `wins` | Dokončené účasti, kde `game.winner_slot == slot`. |
| `draws` | Dokončené účasti s `winner_slot=None`. |
| `losses` | Dokončené účasti s platným víťazným sedadlom odlišným od vlastného. |
| `win_rate_pct` | `100 × wins / completed_seats`; pri nulovom menovateli `null`. |
| `avg_score` | Priemer konečného `PlayerSlot.score` dokončených účastí. |
| `avg_spread` | Priemer `vlastné konečné skóre − súperovo konečné skóre`. |
| `avg_terminal_pass_streak` | Priemer uloženého `PlayerSlot.pass_streak` pri dokončení. |

`give_up` sa v aktuálnom kóde ukladá ako `abandoned`, hoci má víťaza. Preto ho viesť v osobitnom počte vzdaných hier; nezmiešať ho s prirodzene dokončenými zápasmi. Rovnako oddeliť stopnuté simulácie a limit 300 ťahov.

`pass_streak` je **koncová séria**, nie historicky najdlhšia séria. Historické maximum tento slice nebude predstierať.

**Identita modelu a stratégie**

Výsledková identita konfigurácie:

1. Playground: snapshot `config_json.slots[slot]`, vrátane `engine/cpu`.
2. Diagnostika: identita konkrétneho sedadla a diagnostického cieľa; nikdy cieľ automaticky nepovažovať za katalógového poskytovateľa.
3. Gameplay: požadovaná identita zachytená v metadátach AI ťahov, pokiaľ je úplná a jednotná.
4. Viac identít: kategória `mixed`.
5. Chýbajúca história: kategória `unknown`; aktuálne nastavenie možno uviesť ako pomocný popis, nie ako dokázané historické autorstvo.

Pri gameplay musí jednotnosť kontrolovať **požadovaný model**, nie runtime model: fallback nemení pôvodnú konfiguráciu.

Prompt sa posudzuje samostatne. Jednotný model s viacerými promptmi môže mať výsledok modelovej konfigurácie, ale nepatrí do výsledku jedného presetu.

Snapshot playgroundu uchováva názov a ID presetu, **neuchováva jeho text ani digest**. `prompt_version` z move route označuje verziu spoločného promptového mechanizmu, nie nemennosť textu databázového presetu. Porovnanie preto označiť ako výsledky identity presetu s neoverenou historickou verziou obsahu.

**Metriky ťahov**

- `total_moves`: počet kanonických `Move` pripísaných vykonávajúcemu modelu.
- `provider_candidate_pct`: počet presne `provider_candidate` delený počtom ťahov so známym platným `completion_source`.
- Osobitné počty všetkých šiestich completion sources.
- `unknown_completion_source_moves` a pokrytie merania.
- `repair_candidate` nezapočítavať do striktnej kategórie `provider_candidate`.
- CPU zobrazí autorstvo poskytovateľa ako „N/A“; jeho engine ťahy zostanú vo vlastných počtoch.
- Runtime identitu brať z `runtime_provider` a `runtime_model_id`; historické záznamy bez nej nepresúvať automaticky na posledný model hry.

**Latencie a požiadavky**

Existujúci [inspection trace](/home/agile/Projects/libretiles/frontend/src/lib/ai-inspection-trace.ts:171) obsahuje najviac tri pokusy, ich identity, latencie a počty požiadaviek.

Počítať tri rozdielne metriky:

1. `avg_attempt_latency_ms`: priemer zaznamenaných pokusov daného runtime modelu.
2. `avg_recorded_turn_latency_ms`: súčet latencií úplnej série pokusov pri dokončenom ťahu; nejde o presnú latenciu celej používateľskej interakcie.
3. `avg_provider_requests_per_turn`: súčet počtov požiadaviek úplnej série pokusov, spriemerovaný cez takéto ťahy.

Úplná séria vyžaduje verziu 1, jedinečné súvislé indexy od nuly, potrebné číselné hodnoty a koncový pokus zhodný s runtime identitou ťahu. Neúplné série prispievajú do známych pokusových metrík, nie do úplných súčtov.

Samotné `provider_requests_used` či `turn_provider_requests` v aktuálnej move route obsahuje počet daného pokusu. Nesmie sa bez overenia interpretovať ako celý fallbackový turn. [Zápis metadát](/home/agile/Projects/libretiles/frontend/src/app/api/ai/move/route.ts:924).

Diagnostické `wall_clock_ms` je samostatné meranie s inou hranicou časovania. Zobrazovať oddelene od latencie runtime pokusov. CPU playground dnes priamo nezapisuje latenciu; výsledkom je `null`, nie nula.

**SQL/ORM stratégia**

Použiť samostatné agregácie, aby joiny nenásobili riadky:

- `GameSession`: summary a varianty.
- `PlayerSlot`: výsledky a presety.
- `Move`: dokončené ťahy a ich zdroje.
- Tri pevné projekcie trace položiek `[0]`, `[1]`, `[2]`: pokusové metriky.
- `DiagnosticRun` a `DiagnosticPly`: diagnostika podľa `instrument`, `assist_mode` a runtime režimu.
- Malé katalógové dotazy: aktuálne selektovateľné modely, presety a uložené capability observations.

Výsledková agregácia použije napríklad:

```python
Count("game_id", distinct=True)
Count("pk", filter=finished & Q(game__winner_slot=F("slot")))
Avg("score", filter=finished)
Avg(F("score") - F("opponent_score"), filter=finished)
```

`opponent_score` získať cez `Subquery` nad druhým sedadlom toho istého zápasu. Historickú jednotnosť identít zisťovať agregovanými poddotazmi nad ťahmi. Chýbajúce alebo neplatné sedadlá nepretvárať na nulové skóre.

Vyhodnocovať `.values(...).annotate(...)` na úrovni výsledných skupín. V Pythone spájať iba agregované počty, súčty a menovatele; nikdy nepočítať priemer z priemerov bez váženia. Nenačítavať boardy, racky, replay snapshoty ani jednotlivé ply objekty.

Pre JSON čísla pridať malé testované ORM výrazy pre SQLite a PostgreSQL: overiť JSON typ pred konverziou; odmietnuť bool, textové čísla, záporné a neplatné hodnoty. Nekontrolovaný `Cast` historického JSON nesmie zložiť celý endpoint.

**Výkonnostná akceptácia**

Cieľ `<50 ms` nemožno garantovať len výberom ORM funkcií. Navrhujem:

- Najviac 20 analytických SQL dotazov vrátane katalógového obohatenia, nezávisle od počtu modelov.
- Žiadne N+1 ani hydratácia individuálnych ťahov.
- Benchmark na izolovanom PostgreSQL: 1 000 hier, 30 000 ťahov, reprezentatívne fallback traces.
- Po zahriatí 100 meraní; cieľ p95 **celého analytického výpočtu pod 50 ms**, bez HTTP a autentifikácie.
- Osobitne zmerať väčší dataset a zaznamenať `EXPLAIN ANALYZE`.

Bez dosiahnutého benchmarku nemožno deklarovať splnenie výkonovej požiadavky. Indexy či predpočítané tabuľky by vyžadovali následné odôvodnené rozšírenie plánu; tento E2 slice ich nezavádza preventívne.

### D2 — Analytics API Contract & Serializer

Pridať verziovaný kontrakt s explicitnými menovateľmi:

```ts
type AnalyticsResponse = {
  analytics_schema_version: 1;
  as_of: string;
  filters: {
    days: number;
    source: "all" | "gameplay" | "playground" | "diagnostic";
    variant_slug: string;
  };

  summary: {
    total_games: number;
    finished_games: number;
    total_plies: number; // iba kanonické Move
    variants_played: number;
    variants: Array<{
      variant_slug: string;
      total_games: number;
      finished_games: number;
      total_plies: number;
    }>;
    abandoned_games: number;
    diagnostic_runs: number;
    diagnostic_observations: number;
    unlinked_diagnostic_observations: number;
  };

  models: ModelMetrics[];
  presets: PresetMetrics[];
  diagnostics: DiagnosticMetrics[];
  recommendations: DeploymentRecommendations;

  coverage: {
    unknown_model_seats: number;
    mixed_model_seats: number;
    unknown_preset_seats: number;
    mixed_preset_seats: number;
    unknown_runtime_moves: number;
    unknown_completion_source_moves: number;
    ambiguous_games: number;
    limitations: string[]; // uzavreté reason codes
  };
};
```

`ModelMetrics`:

| Skupina | Polia |
|---|---|
| Identita | `key`, `provider`, `model_id`, `display_name`, `source`, `runtime_mode`, `is_selectable`, `is_current_flagship` |
| Výsledky | `games_played`, `seat_appearances`, `completed_seats`, `wins`, `losses`, `draws`, `win_rate_pct`, `avg_score`, `avg_spread`, `avg_terminal_pass_streak` |
| Ťahy | `total_moves`, `completion_source_counts`, `known_completion_source_moves`, `provider_candidate_pct` |
| Časovanie | `avg_attempt_latency_ms`, `measured_attempts`, `avg_recorded_turn_latency_ms`, `measured_turns` |
| Požiadavky | `avg_provider_requests_per_turn`, `request_measured_turns` |
| Limity | `identity_basis`, `limitations` |

Výsledky konfigurácie a merania runtime budú vnorené do samostatných objektov `outcomes` a `turns`; tabuľka ich môže zobraziť vedľa seba, ale nesmie zamlčať rozdielnu atribúciu.

`PresetMetrics` obsahuje ID/názov, zdroj atribúcie, počet hier a účastí, výhry/remízy/prehry, percento výhier, priemer skóre a `content_version_verified: false` tam, kde chýba dôkaz textovej verzie. CPU má `prompt_id=null` a do rebríčka promptov nevstupuje.

`DiagnosticMetrics` obsahuje kohortu `(instrument, assist_mode, executed_runtime_mode)`, počty behov a pozorovaní, pokrytie nullable polí a samostatné priemery. `position-set` nikdy nevytvára víťazstvá celých zápasov.

Serializer:

- Explicitné DRF serializery; žiadne všeobecné serializovanie modelov.
- Počty sú nezáporné integer hodnoty.
- Percentá 0–100; neznáme priemery a percentá sú `null`.
- Skóre a spread môžu byť záporné.
- Zaokrúhlenie až pri serializácii, na dve desatinné miesta.
- Stabilné triedenie podľa katalógového poradia, potom identity.
- Nevracať raw JSON, prompt texty, traces, používateľov, cesty reportov, diagnostické URL ani credential metadata.

Frontend pridá runtime validáciu cez už dostupný Zod. Chybný kontrakt zobrazí stav chyby s Retry, nie zavádzajúce nuly.

### D3 — Comparison Matrix Table UI

Stránka zostane v existujúcom zlatom/tmavom štýle a bude pozostávať z:

1. Nadpisu „Model Analytics“, obdobia, zdroja, variantu a tlačidla Refresh.
2. Summary kariet.
3. Modelovej matice.
4. Porovnania stratégií.
5. Odporúčania nasadenia.
6. Rozbaliteľných informácií o pokrytí dát a diagnostike.

Matica:

```text
Model | Provider | Games / Seats | Win Rate | Avg Score | Spread
      | Provider Authorship | Attempt Latency | Requests / Turn
```

- Numerické triedenie podľa výhier, skóre, autorstva, spreadu a latencie.
- Predvolené poradie podľa katalógu; triedenie analytiky neovplyvní odporúčaný model aplikácie.
- Stabilný tie-break podľa identity; `null` zostane posledný v oboch smeroch.
- Hlavička používa tlačidlo a `aria-sort`.
- Percento má číslo aj statický progress bar; význam nie je založený iba na farbe.
- Pri percentách zobraziť vzorku, napríklad „8 / 12 wins“.
- „— Not measured“ pre chýbajúce meranie; „N/A“ pre neaplikovateľnú metriku.
- Historické neaktívne modely zostanú viditeľné s označením „Not currently selectable“.

Pri mobilnom rozmere zachovať sémantickú tabuľku v pomenovanom horizontálnom scroll kontajneri. Širšie údaje možno rozbaliť v detaile riadka. Samotná stránka nesmie horizontálne pretekať.

Štyri seed presety sa zobrazia aj bez meraní, ak existujú v katalógu. Ďalšie vlastné presety sa nestratia. Žiadne hardcoded databázové ID a žiadne stotožnenie `AIPrompt.fitness` s analyticky zistenou výkonnosťou.

### D4 — VPS Deployment Recommendation Card

**Karta musí oddeliť aktuálny prevádzkový default od najlepšieho pozorovaného výsledku.**

Aktuálny kód už radí aktívnych priamych poskytovateľov pred kompatibilné OpenRouter/NIM riadky. Gemma teda nie je univerzálne platný flagship. Zdrojom zostane [get_selectable_models()](/home/agile/Projects/libretiles/backend/catalog/selection.py:131) a existujúce [flagship označovanie](/home/agile/Projects/libretiles/backend/catalog/serializers.py:26).

Kontrakt odporúčania:

```ts
type Recommendation = {
  status: "catalog_default" | "observed_leader"
        | "available" | "insufficient_evidence";
  provider: string | null;
  model_id: string | null;
  prompt_id: number | null;
  reason_codes: string[];
  evidence: {
    completed_seats: number;
    measured_attempts: number;
    variant_slug: string | null;
  };
};

type DeploymentRecommendations = {
  current_flagship: Recommendation;
  primary_flagship: Recommendation;
  high_throughput_rival: Recommendation;
  offline_cpu: Recommendation;
  strategic_preset: Recommendation;
  reliability_notes: string[];
  changes_catalog: false;
};
```

**Deterministické rozhodovanie**

- `current_flagship`: aktuálny prvý selektovateľný katalógový riadok.
- Bez dostatočných meraní `primary_flagship` prevezme tento riadok so stavom `catalog_default`; jasne uvedie, že ide o konfiguráciu katalógu.
- `high_throughput_rival` zostane bez modelu, pokiaľ chýbajú porovnateľné merania. NIM sa nedosadí iba na základe mena.
- `offline_cpu`: `engine/cpu`, označenie „CPU Master — no external provider requests“. Dostupnosť CPU neznamená novú automatickú fallback politiku ani sľub určitej kapacity VPS.

Pre označenie `observed_leader` navrhujem tieto konzervatívne technické podmienky:

- Model je aktuálne selektovateľný.
- Jedna varianta, playground zápasy proti CPU Master, rovnaké nastavenie časového a krokového rozpočtu.
- Minimálne 20 dokončených účastí, 10 rôznych seedov a aspoň päť účastí na každom sedadle.
- Úplná identita konfigurácie a runtime; zmiešané modely, diagnostické fake dáta a fallback na iný model sa do tohto porovnania nezahrnú.
- Posledný uložený capability probe pre presnú dvojicu je `live/pass`, nie starší než 30 dní. GET žiadny probe nespúšťa.
- Všetky počty vylúčení sú viditeľné v dôvodoch/pokrytí.

Poradie primárneho kandidáta:

1. Dolná 95 % Wilsonova hranica podielu výhier.
2. Priemerný spread.
3. Podiel `provider_candidate`.
4. Nižšia nameraná latencia.
5. Aktuálne katalógové poradie.

Wilsonova hranica tu slúži ako opatrný triediaci ukazovateľ pri malých vzorkách, nie ako dôkaz nezávislého experimentu.

Rýchly rival sa vyberie z tej istej oprávnenej kohorty podľa najnižšej priemernej latencie, s rovnakými explicitnými menovateľmi. Preset sa porovnáva v rámci jedného modelu a rovnakej kohorty; kartu nemožno zostaviť spojením najlepšieho modelu z jednej skupiny a presetu z nesúvisiacej skupiny.

**Hranica tvrdení o spoľahlivosti**

Traces pripojené k uloženým ťahom nedokazujú všetky úplne zlyhané turny. Preto:

- Nepublikovať „production success rate“ z počtu úspešne uložených ťahov.
- Uložený capability probe je bodové pozorovanie, nie záruka dostupnosti.
- `first_validate_valid` a `malformed_or_non_tool` zostávajú neznáme, ak ich diagnostika nemerala.
- Označenie víťazného presetu hovorí o historickej identite presetu; jeho textovú nemennosť netvrdí.

Výsledkom je užitočné poradné odporúčanie s oporou v dátach, bez vymysleného „optimálneho modelu“. Veľkosť VPS, paralelizmus a produkčné nasadenie zostávajú mimo tohto slice.

### D5 — Navigation & UI Polish

Pridať spoločný klientsky `AdminNavigation`, použitý v existujúcom serverovom layoute.

| Kontext | Správanie |
|---|---|
| `/admin` | Aktívny Games List. |
| `/admin/playground` | Aktívny Simulation Playground. |
| `/admin/analytics` | Aktívny Model Analytics; odstránené „Preview“. |
| `/admin/replay/[id]` | Aktívny Replay Studio a skrátené ID hry. |
| Ostatné admin stránky | Replay Studio je vysvetľujúci indikátor „Open a game to replay“, nie nefunkčný odkaz. |
| `/admin/login` | Bez prevádzkovej navigácie konzoly. |

- Aktívny odkaz má `aria-current="page"`.
- Jednotný breadcrumb pod navigáciou; replay má odkaz späť na Games List.
- Existujúce odkazy zo zoznamu a simulácie otvárajú konkrétny replay.
- Zachovať „Back to Game“ na `/play`.
- Navigácia sa zalamuje, má viditeľný keyboard focus a primerané dotykové ciele.
- Použiť `usePathname`; analytics filtre cez `useSearchParams` pod `Suspense`, v súlade s lokálnou dokumentáciou Next 16.
- Zachovať existujúci `AdminAccessGate`; navigačná úprava nemení autentifikáciu.

Overiť aj dlhé modelové názvy a UUID v replay hlavičke. Prípadná úprava zalamovania patrí do presne povoleného `ReplayStudio.tsx`.

### D6 — Security & Cache Controls

Nový `AdminAnalyticsView` zdedí existujúci [_AdminAPIView](/home/agile/Projects/libretiles/backend/game/admin_views.py:24):

```text
authentication:
  PasswordAwareJWTAuthentication
  SessionAuthentication

permissions:
  IsAuthenticated
  IsAdminUser

response:
  Cache-Control: private, no-store
  Vary: Authorization, Cookie
```

- Anonymný alebo neplatný JWT: 401.
- Prihlásený používateľ bez staff oprávnenia: 403.
- Staff: 200.
- Nepovolená metóda: 405.
- Hlavičky overiť aj pri 400/401/403/405, nielen pri úspechu.
- Frontend použije existujúci `api` transport s bearer tokenom a `cache: "no-store"`.
- Žiadna nová Next proxy route, serverová cache ani perzistencia analytických dát v Zustand/localStorage.
- Pri zmene tokenu alebo filtrov zahodiť starú odpoveď; po odhlásení nesmie oneskorený request znovu zobraziť údaje.
- Backend GET nesmie volať providerov, DNS, diagnostické reportové súbory ani katalógový sync.

Hranica zmeny je čítanie agregovaných staff dát cez existujúce oprávnenie. Nový bezpečnostný model ani ďalšia rola nevznikajú.

### D7 — Component Testing & Playwright Verification Plan

**Backend regresné testy**

Povinné prípady:

- 401/403/200 a cache hlavičky vrátane chýb.
- Prázdna databáza: nulové počty, `null` merania, žiadny vymyslený líder.
- Výhra, prehra, remíza, záporné konečné skóre a správny spread.
- CPU proti CPU: jedna hra, dve účasti; žiadne zdvojené summary.
- `give_up`, simulation stop a ply limit mimo prirodzených výsledkov.
- Dva modely, rovnaký model na oboch sedadlách, fallback A → B.
- Zmena modelu/promptu počas hry a neúplná staršia história.
- Zachovaná identita snapshotu po odstránení katalógovej referencie.
- Linked `DiagnosticPly` nezvyšuje počet kanonických ťahov.
- `fake`, neznámy režim a `position-set` neovplyvňujú produkčné odporúčanie.
- Všetkých šesť completion sources, vrátane odlíšenia repair od provider autorstva.
- Úplné, neúplné, duplicitné a nesúvislé trace indexy.
- Nulové CPU požiadavky verzus chýbajúca CPU latencia.
- Chybné JSON typy bez pádu na SQLite aj PostgreSQL.
- Vzorky a váženie priemerov; stabilné poradie odporúčaní.
- Aktuálny flagship rešpektuje selekciu a deaktivácie.
- Počet SQL dotazov nerastie s počtom modelov.
- Endpoint nemá žiadnu write alebo provider side effect.

**Vitest**

Repozitár používa Node test environment a serverové renderovanie komponentov, nie Testing Library. Rozšíriť existujúci prístup bez závislostí:

- Zod parsing validného/neplatného payloadu.
- Čistá triediaca funkcia: čísla, záporné skóre, remízy, `null`, stabilita.
- `renderToStaticMarkup`: hlavičky, `aria-sort`, menovatele, N/A a neznáme merania.
- Recommendation card: default, observed leader, insufficient evidence, CPU.
- API test: query encoding, bearer auth, `no-store`.
- Navigácia: presné aktívne cesty a replay indikátor.

Skutočné kliknutia a efekty overí browser; statický render sa nebude vydávať za interakčný test.

**Playwright akceptácia**

V oddelenom lokálnom testovacom prostredí so syntetickými účtami a dátami:

1. Priamy vstup na analytics bez prihlásenia a návrat po staff login.
2. Non-staff odmietnutie v UI aj API.
3. Zobrazenie fixture dát s vopred spočítanými očakávaniami.
4. Triedenie vzostupne/zostupne a kontrola `aria-sort`.
5. Zmena filtrov, browser Back/Forward a Refresh.
6. Prázdny výsledok, API chyba, Retry a oneskorená odpoveď starého filtra.
7. Všetky stavy odporúčania vrátane neexistujúceho meraného lídra.
8. Games List → Replay → Playground → Analytics a breadcrumbs.
9. Viewporty 390, 768 a 1440 px; keyboard navigation a reduced motion.
10. Overenie, že nevznikli provider požiadavky ani automatická simulácia.

Playwright nie je deklarovaný v `frontend/package.json` a repozitár nemá vlastný e2e harness. Použiť dostupný externý browser runner v akceptačnom prostredí; neinštalovať balík cez implicitné `npx`. Ak runner nie je dostupný, browserová akceptácia ostane výslovne nesplnená.

**Validačné príkazy budúcej implementácie**

Backend: projektové Ruff, mypy, pytest a focused analytics testy; performance test osobitne na PostgreSQL. Frontend: typecheck, lint, Vitest a build. Build je súčasťou budúcej implementačnej autority, v tomto plánovaní sa nespustil.

### D8 — Slice 5 Implementation Plan & Path Allowlist

**Poradie implementácie**

1. Zafixovať schému odpovede, definície metrík a fixtures s vypočítanými očakávaniami.
2. Implementovať bezpečné JSON projekcie a samostatné ORM agregácie.
3. Pridať serializer, staff GET endpoint a backend regresné testy.
4. Implementovať čisto poradný algoritmus odporúčania.
5. Overiť query budget a PostgreSQL benchmark pred dokončením prezentácie.
6. Pridať frontend parsing, API metódu, tabuľku a preset/recommendation karty.
7. Dokončiť navigáciu a responzívne úpravy.
8. Spustiť projektové kontroly, browserovú akceptáciu a uzatvárací audit.

**Presný navrhovaný allowlist**

Backend:

```text
backend/game/analytics.py                         NEW
backend/game/analytics_expressions.py             NEW
backend/game/analytics_serializers.py             NEW
backend/game/analytics_views.py                   NEW
backend/game/admin_urls.py                        EDIT

backend/tests/test_admin_analytics_api.py         NEW
backend/tests/test_admin_analytics_aggregation.py  NEW
backend/tests/test_admin_analytics_performance.py  NEW
```

Frontend:

```text
frontend/src/app/admin/analytics/page.tsx                      EDIT
frontend/src/app/admin/layout.tsx                              EDIT
frontend/src/lib/api.ts                                        EDIT
frontend/src/lib/admin-api.test.ts                             EDIT
frontend/src/lib/admin-analytics.ts                            NEW
frontend/src/lib/admin-analytics.test.ts                       NEW

frontend/src/components/admin/AdminAnalyticsDashboard.tsx     NEW
frontend/src/components/admin/ModelAnalyticsTable.tsx          NEW
frontend/src/components/admin/PresetAnalyticsCards.tsx         NEW
frontend/src/components/admin/DeploymentRecommendationCard.tsx NEW
frontend/src/components/admin/AdminNavigation.tsx              NEW
frontend/src/components/admin/AdminAnalytics.test.ts           NEW
frontend/src/components/admin/AdminNavigation.test.ts          NEW
frontend/src/components/admin/admin.module.css                 EDIT
frontend/src/components/admin/ReplayStudio.tsx                 EDIT
```

Dokumentácia:

```text
docs/admin-analytics.md                                        NEW
```

Dokument obsahuje definície menovateľov, limity histórie, benchmark a presný browserový scenár.

Mimo implementačného allowlistu zostávajú `.ap/`, environment súbory, databázové modely a migrácie, katalógová selekcia, autentifikácia, provider runtimes, gameplay route, runner, prompty, lockfiles a deployment konfigurácia.

**Evidence tier**

- Toto plánovanie: **E0**, neindependentné statické dôkazy.
- Implementácia: **E2**, pretože mení backend aj frontend, používa existujúcu staff hranicu a je reverzibilná bez dátovej migrácie.
- Migrácia, zmena oprávnení, dopĺňanie perzistentnej telemetrie alebo produkčné nasadenie by vyžadovali nové posúdenie rozsahu a tieru.
- Čerstvá cielená akceptácia sa odporúča najmä pre atribúciu fallbackov, SQL agregácie a odporúčania.

**Rollback**

Revert implementačného commitu odstráni endpoint a obnoví preview stránku/navigáciu. Nie je potrebný dátový rollback ani zásah do katalógu. Počas prípadného nesúladu frontend/backend analytics zobrazí štandardnú chybu načítania.

**Uzatvárací audit**

Slice môže dostať implementačné PASS až keď:

- API, filtre, menovatele a UI zodpovedajú kontraktu.
- Fake diagnostika a neúplné merania nevytvárajú produkčné tvrdenia.
- Fallback nemá chybnú atribúciu ani stratené známe požiadavky.
- Staff/cache negatívne testy prešli.
- Benchmark má skutočne nameraný výsledok.
- Browserové scenáre a mobilné rozmery prešli.
- Zmizlo označenie analytics preview a všetky admin prechody fungujú.
- Diff rešpektuje allowlist a nemení katalóg, prompty ani vykonávanie hry.

To uzatvára Slice 5; uzavretie celého `admin-frontend-console` zostáva rozhodnutím ORCHESTRATORA.

```text
Orchestration critique:
MEASURED — Zadaný príklad flagship modelu neodráža celú aktuálnu selekciu;
           aktívni priami poskytovatelia predchádzajú compatibility riadkom.
MEASURED — Gameplay model/prompt sú meniteľné; posledná FK nie je spoľahlivá história.
MEASURED — Diagnostický runner zapisuje fake režim a nemerané compliance polia.
MEASURED — Metadata turn_provider_requests v move route zachytávajú daný pokus;
           úplný súčet treba overiť cez trace.
MEASURED — Playground snapshot neobsahuje textový digest presetu.
LEAD — Globálna dostupnosť providerov, kapacita VPS a limit 50 ms
       vyžadujú samostatné vykonané meranie; z tohto čítania ich nemožno odvodiť.

Enumeration widened:
Doplnené súvisiace konzumenty: metadata sanitizer, inspection trace collector,
capability probes, model/prompt update services a aktuálna katalógová selekcia.
Živá databáza, produkčný host a externí poskytovatelia neboli skúmaní.

Context pressure: stredný; rozhodujúce zistenia a hranice zostávajú konzistentné.
```

**Report justification: new-evidence**

**Authority expiry:** Odovzdaním tohto reportu sa obnovená plánovacia autorita končí. Nebola vykonaná implementácia, mutácia, publikovanie ani nasadenie.

**Smallest next step:** ORCHESTRATOR vydá čerstvej implementačnej session ohraničený E2 prompt pre tento plán na baseline `f040a644f9f233234ba94ec6f2a620eebc933c39`, s uvedeným allowlistom a samostatne určeným testovacím/browserovým prostredím.
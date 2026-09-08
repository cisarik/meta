# AFC-SLICE-1-PLAN — Admin Replay API a záznam budúcich hier

```text
Logical whole identity: admin-frontend-console
Worker session ordinal: 01
Worker exchange ordinal: 01
Status: PASS
Phase-qualified result: not-applicable
Result artifact or commit: not-applicable
Result evidence: not-applicable
Logical-whole closure: not-closed
Start commit: 531a80963115fa7a3ab42f86710f1a2f360df90d
End commit: 531a80963115fa7a3ab42f86710f1a2f360df90d
Changed files and purpose: none — this exchange mutates nothing
Commit/push result: not-applicable
Resolved Execution Issues / Near-Misses: evidence-tier blocker resolved by explicit Cooperator instruction; implementation tier E3
Pre-Existing Failure Classification: none
Evidence posture: non-independent
```

**PASS označuje dokončený technický plán, nie hotovú implementáciu.** Tento report nahrádza predchádzajúci BLOCKED report. Cooperator výslovne obnovil plánovanie a vybral rozšírenie o záznam budúcich hier.

```text
Planning cycle: initial
Prior planning report: preceding BLOCKED report; no completed plan
Targeted revision basis: explicit Cooperator continuation and selection of future-game recording
Changed decision boundary: E3 implementation; capture and migration added to API scope
Preserved unaffected decisions: staff-only endpoints, existing gameplay authority, free-only product
Automatic targeted revisions used: 0
```

Základným rozhodnutím je **ukladať skutočné stavy nových hier**. Rekonštrukcia zo seedu bude záložná cesta pre staršie záznamy, s kontrolou výsledku a výslovným označením chýbajúcich údajov.

Priame čítanie kódu a lokálna syntetická skúška potvrdili:

- `TileBag` je v `backend/gamecore/tiles.py`; požadovaný `tile_bag.py` neexistuje.
- Rozdaniu rackov predchádza vytiahnutie dvoch kameňov, ich vrátenie a ďalšie zamiešanie. Vynechanie tohto kroku zmenilo výsledok vo všetkých 12 testovaných variantoch.
- Výmena ukladá iba `tiles_exchanged`, nie identitu kameňov. Rovnaký počet výmen môže viesť k rôznym rackom a obsahu vrecka.
- `Move.ai_metadata` neuchováva surové tool calls ani zoznam odmietnutých kandidátov.
- Diagnostický pokus môže vytvoriť `DiagnosticPly` bez `Move`. Indexy nemožno bezpečne spájať jednoduchým odčítaním jednotky.
- Diagnostické sady pozícií nahrádzajú stav hry medzi pokusmi; nejde o jednu súvislú partiu.
- Koncové úpravy skóre sa vykonávajú po vytvorení `Move` a nie sú súčasťou `Move.points`.

## D1 — Routing, permissions a identita používateľa

Pridať `backend/game/admin_urls.py` a namontovať ho v `config/urls.py` pod `api/admin/`.

| Metóda | Cesta | View |
|---|---|---|
| GET | `/api/admin/games/` | `AdminGameListView` |
| GET | `/api/admin/games/<game_id>/replay/` | `AdminGameReplayView` |

Použiť namespace `game_admin`, názvy `games` a `game-replay`. Existujúci Django Admin na `/admin/` zostáva samostatný.

Obe views budú mať:

```python
authentication_classes = [
    PasswordAwareJWTAuthentication,
    SessionAuthentication,
]
permission_classes = [
    permissions.IsAuthenticated,
    permissions.IsAdminUser,
]
http_method_names = ["get", "head", "options"]
```

Poradie autentifikátorov je zámerné: existujúca JWT implementácia poskytuje `WWW-Authenticate: Bearer ...`, takže anonymné požiadavky dostanú 401. Autentifikovaný používateľ bez `is_staff` dostane 403.

Použiť `<str:game_id>` a UUID spracovať až po permission checks. Neplatné alebo neexistujúce ID vracia staff používateľovi 404; nepovolenej osobe sa existencia hry neodhaľuje.

Do `UserSerializer.fields` a `read_only_fields` pridať `is_staff`. `GET /api/auth/me/` ho vracia ako boolean. Pokus o zmenu cez PATCH ani registráciu nesmie zmeniť oprávnenia.

Admin views používajú vlastné explicitné projekcie dát. Nebudú rozširovať `_build_state()` o rack súpera ani obchádzať členské kontroly existujúcich hráčskych endpointov.

## D2 — Kontrakt zoznamu hier

### Parametre

| Parameter | Predvolené nastavenie | Správanie |
|---|---|---|
| `page` | `1` | Celé číslo ≥ 1. |
| `page_size` | `20` | Celé číslo 1–100; mimo rozsahu 400. |
| `game_mode` | `all` | `all`, `vs_ai`, `vs_human`. |
| `variant_slug` | bez filtra | Presný slug, najviac 50 znakov; nesmie závisieť od aktuálne nainštalovaných variantov. |
| `status` | `all` | `all`, `waiting`, `active`, `finished`, `abandoned`. |
| `is_diagnostic` | `all` | `all`, `true`, `false`. |
| `search` | prázdny | Orezaný text, najviac 150 znakov. |

`waiting` je existujúci stav modelu a bude podporovaný aj vo filtri. Neznáme hodnoty enumov a neplatné čísla vracajú 400.

Vyhľadávanie je OR medzi:

- prefixom verejného UUID, bez ohľadu na veľkosť písmen a pomlčky;
- `username__icontains` ktoréhokoľvek hráča.

UUID vetvu aplikovať iba na neprázdny hexadecimálny prefix po odstránení pomlčiek. Na jednotné správanie SQLite/PostgreSQL použiť textovú projekciu UUID cez `Cast` a `Replace`. Hráčsku vetvu realizovať pomocou `Exists`, aby viac zhôd nerozmnožilo výsledky.

Zoradenie: `-created_at`, potom `-pk`. Použiť existujúcu konvenciu `Paginator.get_page()`: príliš vysoká platná strana sa upraví na poslednú; prázdny zoznam má `page=1`, `total_pages=1`.

### Odpoveď

```text
{
  count,
  page,
  total_pages,
  page_size,
  results: [{
    game_id,
    game_mode,
    variant_slug,
    status,
    is_diagnostic,
    created_at,
    finished_at,
    move_count,
    winner_slot,
    game_end_reason,
    slots: [{
      slot,
      username,
      score,
      is_ai,
      model_id,
      model_display_name
    }],
    diagnostic: {
      run_id,
      status,
      assist_mode,
      instrument,
      model_ids: [seat0_model_id, seat1_model_id]
    } | null,
    diagnostic_run_count
  }]
}
```

`game_id` je verejné UUID, nie interné PK. Časy sú ISO 8601; chýbajúce hodnoty sú `null`.

Sloty sú zoradené podľa `slot`. Model sa určí v poradí:

1. diagnostický target daného slotu;
2. model daného slotu;
3. model session pre bežný AI slot.

Ľudský slot nededí model session. Pri targete sa projektuje iba model ID; ako zobrazovací názov možno použiť toto ID. URL, credential konfigurácia a allowed host sa neserializujú.

`diagnostic` je najnovší run podľa `created_at`, `id`; `diagnostic_run_count` zabráni predstieraniu vzťahu jedna k jednej. Replay detail obsahuje všetky runy.

## D3 — Replay payload a nové uložené údaje

### Verejný kontrakt

Replay má vlastné `replay_schema_version: 1`; nezamieňať ho s existujúcou verziou game-state wire formátu.

```text
{
  replay_schema_version: 1,
  game_id, variant_slug, game_mode, status,
  created_at, finished_at, winner_slot, game_end_reason,
  tile_points, alphabet, variant_rules,
  rules_source,
  players,
  initial_board,
  initial_racks,
  initial_scores,
  initial_premium_used,
  starting_turn_slot,
  bag_seed,
  initial_state_source,
  timeline_mode: "continuous" | "positions" | "unknown",
  replay_status: "complete" | "partial" | "not_started",
  issues: [{code, seq: integer | null}],
  plies: [...],
  diagnostic_runs: [...],
  final_state
}
```

`complete` znamená úplnú hernú časovú os. Dostupnosť AI udalostí sa hodnotí samostatne; orezaná telemetria nemení úplnosť zaznamenanej dosky a rackov.

Každý ply obsahuje:

```text
{
  ply_index,
  seq,
  player_slot,
  kind,
  created_at,
  placements: [{row, col, letter, blank_as}],
  words_formed: [{word, score, multiplier, coords}],
  tiles_exchanged,
  exchanged_tiles: string[] | null,
  points,
  cumulative_scores: [integer | null, integer | null],
  score_adjustments: [integer | null, integer | null],
  racks: [string[] | null, string[] | null],
  bag_remaining: integer | null,
  current_turn_slot: 0 | 1 | null,
  board_delta: [{row, col, token, blank_as}] | null,
  continuity: "continuous" | "reset" | "unknown",
  state_before: object | null,
  state_source,
  racks_source,
  ai_metadata: object | null,
  diagnostic_ply: object | null,
  diagnostic_plies: [...]
}
```

- `seq` aj `ply_index` zachovávajú uložené 1-based `Move.seq`. Medzery sa neopravujú prečíslovaním.
- `[]` znamená známy prázdny rack; `null` znamená neznámy rack.
- `words_formed` a `points` pochádzajú z uloženého ťahu. Replay znova nerozhoduje o platnosti slov.
- `score_adjustments` je rozdiel medzi skóre po ťahu a skóre pred ťahom po odpočítaní `points` aktéra. Zachytí koncové odpočty aj bonusy.
- `state_before` sa posiela pri prvom dostupnom zázname po medzere alebo pri nahradení pozície. Umožní pokračovať v prehrávaní bez predstierania súvislej dosky.
- `final_state` je samostatná projekcia aktuálne uloženého stavu session. Zahŕňa aj administratívne ukončenie diagnostiky, ktoré nevytvorilo ďalší ťah.

### Databázové rozšírenie

Pridať jednu aditívnu migráciu `0013_admin_replay_capture.py`:

| Model | Nové pole | Definícia |
|---|---|---|
| `GameSession` | `replay_initial_state` | Nullable JSON, default `None`, `editable=False`. |
| `Move` | `replay_before` | Nullable JSON, default `None`, `editable=False`. |
| `Move` | `replay_after` | Nullable JSON, default `None`, `editable=False`. |
| `Move` | `exchanged_tiles` | Nullable JSON, default `None`, `editable=False`. |
| `DiagnosticPly` | `move` | Nullable FK na `Move`, `SET_NULL`, `related_name="diagnostic_plies"`, `editable=False`. |
| `DiagnosticPly` | `replay_before`, `replay_after` | Nullable JSON, default `None`, `editable=False`. |
| `DiagnosticPly` | `ai_trace` | Nullable JSON, default `None`, `editable=False`. |

Pridať podmienenú unikátnosť `(run, move)` pre nenulové `move`. Pri zápise aj čítaní skontrolovať zhodu session a slotu; FK samotný tieto vzťahy negarantuje.

**Bez spätnej dátovej migrácie.** Staré neznáme údaje zostanú `NULL`.

Interný snapshot verzie 1 obsahuje dosku, použité prémiá, oba racky a skóre, poradie vrecka, turn slot, scoreless counter, stav ukončenia a pravidlá účinné pri zachytení. Pravidlá obsahujú iba herné údaje: tile points, distribúciu, abecedu, poradie abecedy, prémiovú mriežku, veľkosť dosky/racku a existujúce bodovacie konštanty.

Snapshot pravidiel zachytiť aj pred každým novým ťahom; pri jeho zmene verejný replay vloží nový `state_before` s príslušnými pravidlami. Neukladať cesty k súborom ani celé slovníky.

Poradie zostávajúcich kameňov je interné. Verejná projekcia poskytuje `bag_remaining` a požadovaný `bag_seed`.

## D4 — Záznam stavov a historická rekonštrukcia

### Nové hry a ťahy

Implementovať samostatné capture/projection funkcie v `game/replay.py`.

1. `_initialize_session()` uloží `replay_initial_state` po úvodnom losovaní a rozdaní oboch rackov.
2. `create_game()` obaliť transakciou, aby vytvorenie session, slotov a počiatočného snapshotu bolo atómové. Matchmaking a diagnostické vytvorenie už transakcie používajú.
3. V `_submit_move_locked`, `_submit_exchange_locked`, `_submit_pass_locked` a `submit_give_up_for_user` zachytiť stav pred zmenou.
4. Existujúcu hernú operáciu vykonať bez zmeny jej pravidiel, poradia draw/exchange alebo RNG.
5. Zachytiť stav po `_check_endgame()` a konečnom uložení session. Aktualizovať novovytvorený `Move` v tej istej transakcii.
6. Pri výmene uložiť presný normalizovaný zoznam v pôvodnom poradí vrátane opakovaných kameňov. Pri ostatných nových ťahoch uložiť `[]`.

Neúspešný alebo odmietnutý ťah nevytvorí záznam. Chyba databázového uloženia snapshotu rollbackne celú transakciu; úspešný ťah nesmie potichu stratiť svoju replay históriu.

Aktívna stará hra začne zaznamenávať `replay_before/replay_after` od prvého nového ťahu. Tento stav sa nesmie vydávať za pôvodný Ply 0.

Snapshoty sa nebudú ukladať do `ai_metadata`, klientského Zustand store ani websocket payloadov. Nové polia sú neprístupné na zápis cez klientské serializery.

### Staršie záznamy

Poradie dôvery:

1. platný uložený snapshot;
2. deterministická rekonštrukcia potvrdená uloženým kontrolným stavom;
3. nedostupný údaj.

Algoritmus pre bežnú inicializovanú hru:

1. Vytvoriť `TileBag(seed=session.bag_seed, variant=...)`.
2. Vytiahnuť kameň pre slot 0 a slot 1.
3. Vrátiť oba cez `put_back()` v rovnakom poradí.
4. Určiť začínajúci slot cez `variant.slot0_wins_starting_draw()`.
5. Rozdať najprv sedem kameňov slotu 0 a potom sedem slotu 1.
6. Spracovať uložené ťahy v poradí `seq`.

Pri `place` odoberať fyzické tokeny, nie znaky slova. Blank spotrebuje `"?"`. Pred použitím `consume_rack()` skontrolovať dostupnosť všetkých kameňov, pretože súčasná helper funkcia chýbajúci kameň potichu preskočí. Doplnenie racku kopíruje existujúcu implementáciu.

Pri rekonštrukcii výmeny s uloženou identitou znovu vytvoriť vrecko z jeho aktuálneho poradia a pôvodného seedu, tak ako `_bag_from_session()`. Súčasná service cesta obnovuje RNG zo seedu pre každú operáciu; dlhodobo držaný `TileBag` by výmeny nereprodukoval správne. `exchange()` najprv kamene vráti a zamieša, až potom vyťahuje náhrady.

Pri výmene bez `exchanged_tiles` sa rekonštrukcia rackov a poradia vrecka preruší. Žiadne hádanie kombinácií ani spätné skladanie neznámych draw udalostí.

Rekonštruované racky a vrecko porovnať **vrátane poradia** s finálnym alebo zaznamenaným kontrolným stavom. Dosku a skóre kontrolovať samostatne. Nesúlad znamená `partial`, nie HTTP 500 ani prepísanie DB.

Ďalšie pravidlá:

- Seed `0` je platná hodnota; neznamená automaticky chýbajúci seed.
- Neinicializovaná waiting hra má `not_started`, prázdne racky a žiadny odvodený začínajúci slot.
- Bez dôveryhodného checkpointu sa kandidátna seed rekonštrukcia rackov nevydáva za overenú históriu.
- Staré výmeny nemusia znemožniť prehrávanie dosky a uložených bodov.
- Koncové skóre sa rekonštruuje cez existujúce finálne bodovanie iba v overiteľnom prípade; aktuálne finálne skóre je vždy dostupné osobitne.
- `give_up` sa nesmie odmietnuť pri replay len preto, že aktér nebol na ťahu; súčasná service cesta takú podmienku nemá.
- Poškodená obsadená bunka sa nesmie premeniť na prázdnu.
- Pri historickej diagnostickej sade pozícií sa nepoužije prázdna doska ani seed ako domnelý začiatok každej pozície.

## D5 — Diagnostika a AI telemetria

### Priame priradenie diagnostiky

Runner už pred pokusom zisťuje počet ťahov a po pokuse hľadá nový `Move`. Túto informáciu uložiť do nového `DiagnosticPly.move`.

- Presne jeden nový ťah s očakávanou session a aktérom: uložiť FK.
- Žiadny nový ťah: `move=null`.
- Viac než jeden alebo nesúlad aktéra/session: nepriradiť domnelý ťah; zaznamenať uzavretý diagnostický dôvod nejednoznačnosti.

`ply_index` zostáva 0-based poradím **pokusov**. Nenahrádza `Move.seq`.

Runner uloží `replay_before/replay_after` každého pokusu, aj keď nevznikol ťah. Pri position-set sa stav pred pokusom zachytí až po `apply_position_snapshot()`.

Replay načíta všetky runy. Každý obsahuje ich zoradené diagnostické plies vrátane `move_seq:null`, `position_index`, príslušných snapshotov a metrík.

Na `Move` sa pripoja iba overené priame väzby:

- `diagnostic_plies` obsahuje všetky;
- `diagnostic_ply` obsahuje jediný záznam, ak existuje presne jeden, inak `null`.

Staré neprepojené diagnostické riadky zostanú dostupné v rune s označením `link_status="unrecorded"`. Nepoužije sa heuristika `move.seq - 1`, `.first()` ani párovanie časovou blízkosťou.

### Ohraničený záznam AI udalostí

Pridať samostatné TypeScript a Python validátory replay telemetrie. Existujúcu všeobecnú ochranu proti raw output a tool arguments neuvoľniť. Nový údaj v `Move.ai_metadata` bude `replay_trace`, s vlastným uzavretým kontraktom.

Jednotlivý attempt zaznamená:

- index, provider/model identitu a výsledkový kód;
- počet provider requests, dokončených krokov a časovanie;
- `completion_source`, `terminal_cause`, `repair_attempted`;
- prvý výsledok `validateMove`, počty validných/odmietnutých kandidátov;
- najvyššie namerané skóre modelového kandidáta;
- najvyššie skóre z už vykonaného backend ranked search a jeho `search.complete`;
- usporiadané udalosti `validateMove` a `finishMove`.

Udalosť `validateMove` obsahuje iba explicitne projektované placements, vrátené slová/skóre/validitu, fázu `search|repair` a trvanie. Zaznamenáva sa aj odmietnutý kandidát; súčasné pole `candidates` obsahuje iba validné výsledky a nesmie byť jediným zdrojom histórie.

Obmedzenia:

- najviac 3 attempts;
- najviac 64 udalostí a 64 KiB serializovaných detailov na attempt;
- najviac 256 KiB celého `replay_trace`;
- najviac 7 placements a 8 formed words na validáciu;
- súhrnné počítadlá sa aktualizujú aj po naplnení limitu;
- pri prekročení limitu sa zahadzujú ďalšie detaily, zachová sa poradie začiatku a nastaví sa `truncated=true`.

Neukladať generovaný voľný text, prompty, HTTP hlavičky, surové chybové správy, URL, credentials ani ľubovoľné objekty SDK. Metadáta nikdy nerozhodujú o umiestnení, skóre alebo oprávnení.

### Fallback a odolnosť proti strate SSE

Rozšíriť existujúci `orchestrateFallbackTurn` o prenos už ukončených ohraničených attempts:

1. Route priloží sanitizovaný záznam aktuálneho attemptu k terminálnemu SSE eventu.
2. `consumeAIStream()` ho zachová v terminálnom výsledku.
3. Orchestrátor drží záznamy iba v pamäti a pri ďalšom attempt-e ich odovzdá cez voliteľný `replay_context`.
4. Úspešná route uloží predchádzajúce attempts spolu s aktuálnym do už existujúceho terminálneho backend POST.
5. Diagnostický driver prenesie dokončený trace do `TerminalObservation`; runner ho môže uložiť aj pri pokuse bez ťahu.

Do AI contextu pridať `replay_anchor={game_id, move_count, ai_slot}`. Prenesený kontext sa na Django strane pri uložení porovná s aktuálnou session v transakcii. Pri nesúlade sa zahodí cudzia telemetria; nesmie ovplyvniť validáciu samotného ťahu.

Záznam úspešného ťahu sa uloží pred odoslaním `done`, takže stratené SSE neodstráni jeho trace. Pri ukončení procesu pred doručením neúspešného attemptu zostanú chýbajúce údaje označené ako nezachytené. Bežný neúspešný pokus bez vykonaného ťahu nevytvára falošný `Move`.

Prenesené AI udalosti majú pôvod `reported`; autoritatívnymi údajmi zostávajú Django snapshoty a uložený výsledok ťahu. Počítadlá telemetrie sa nepoužijú na nové rozhodovanie o rozpočte, retry alebo výbere modelu.

Latenciu pomenovať presne: čas route do odoslania commit požiadavky nie je celý wall-clock čas ťahu. Diagnostické `wall_clock_ms` zostáva samostatným meraním runnera.

Chýbajúce historické `first_validate_valid`, ranked score alebo tool calls sú `null`, nikdy vymyslené `false`, nula či prázdny meraný zoznam.

## D6 — Bezpečnosť, izolácia a výkon

### Bezpečnostná hranica

Aktívny staff používateľ smie čítať replay akejkoľvek hry bez členstva v nej. Bežný účastník hry nemá túto výnimku.

Verejné projekcie používajú výhradne explicitný zoznam polí. Nepoužívať `model_to_dict`, `fields="__all__"` ani priame vrátenie JSONField.

Vynechať najmä:

- `credential_env_name`, target URL a allowed-host konfiguráciu;
- `parameters_json`, `report_path`, `log_path`, PID a interné cesty;
- JWT, heslá, e-mailové adresy, cookies a autentifikačné údaje;
- raw provider output a voľné chybové správy.

Aj staré `ai_metadata` sa znovu sanitizujú pri čítaní. Replay neotvára reporty, logy ani súbory pomenované databázovým obsahom.

Pridať `Cache-Control: private, no-store` aj na chybové odpovede admin views a `Vary: Authorization, Cookie`.

Nové snapshoty sa nesmú dostať do hráčskeho game-state API, AI contextu, websocketov ani histórie bežného používateľa. Overiť to regresnými testami.

### Query plán

**Zoznam:**

- `select_related("ai_model")`;
- `Count("moves", distinct=True)`;
- stránkovaný `Prefetch` slotov s `user`, `ai_model` a minimálnymi modelovými poľami targetu;
- zoradený `Prefetch` diagnostických runov, bez ich JSON parametrov a plies;
- veľké replay polia session odložiť pomocou `defer`.

**Replay:**

- session s potrebným modelovým vzťahom;
- sloty cez jeden `Prefetch`;
- moves podľa `seq`, `pk`, s `select_related("player_slot")`;
- runy a ich plies cez dva ďalšie dotazy;
- priradenie diagnostiky vykonať nad načítanými kolekciami, bez dotazov v cykle.

V hráčskej service load ceste odložiť nové snapshoty a nepotrebnú veľkú AI telemetriu v move prefetchi. Samotný pohľad na aktuálnu hru nesmie načítavať celú novú replay históriu.

Replay čítanie nebude zamykať hru počas serializácie. Po načítaní overí, že session `updated_at` a posledné `seq` stále zodpovedajú načítanému stavu. Pri zmene zopakuje načítanie raz; ďalšia zmena vráti 409 `replay_changed`. Diagnostické metriky môžu pribudnúť po commite ťahu, preto ich dočasná absencia nie je poškodenie hry.

Počet dotazov musí zostať konštantný vzhľadom na počet ťahov. Testovací rozpočet pri stabilnom čítaní a `force_authenticate`: najviac 5 pre zoznam a 8 pre replay. Samostatné reálne JWT testy zohľadnia autentifikačný DB dotaz.

## D7 — Testovací a akceptačný plán

Požadované základné testy budú v `backend/tests/test_admin_replay_api.py`:

| Test | Kritérium |
|---|---|
| `test_admin_games_list_requires_staff` | Anonymous 401; regular user 403; staff 200. |
| `test_admin_games_list_filtering` | Všetky filtre, ich kombinácie, username/UUID search, stabilné poradie, pagination, bez duplicitných hier. |
| `test_admin_game_replay_requires_staff` | Rovnaká matica, aj pre cudziu hru a diagnostickú session. |
| `test_admin_game_replay_structure` | Ply 0, všetky ťahy, oba racky, skóre, blanks, board deltas a finálny stav. |
| `test_admin_game_replay_diagnostic_integration` | Priame FK, neúspešný pokus bez Move, viac runov, legacy neprepojené riadky. |
| `test_user_serializer_exposes_is_staff` | Boolean v `/me/`; PATCH ani registrácia nezvýšia oprávnenia. |

Ďalšie povinné scenáre:

- Reálne JWT aj session authentication; neplatný, expirovaný a po zmene hesla zneplatnený JWT; neaktívny alebo degradovaný staff účet.
- Neexistujúce a neplatné ID; nepovolené HTTP metódy; hlavičky cache.
- Presné poradie rackov pri inicializácii, opakovaných výmenách a dočerpaní vrecka.
- Blank s nulovým skóre, opakované kamene, Unicode a multigraph tokeny.
- Koniec po šiestich scoreless ťahoch, vyprázdnení racku, bingo a vzdanie mimo vlastného ťahu.
- Transakčný rollback a žiadny snapshot po odmietnutom ťahu.
- Staré záznamy bez snapshotov, seed 0, neznáma výmena, nezhoda checkpointu, medzera v `seq`, poškodená bunka a chýbajúci variant.
- Staršia rozbehnutá hra, ktorá začne mať presné snapshoty uprostred partie.
- Position-set s resetom dosky/skóre, počiatočnými obsadenými bunkami a pokusmi bez ťahu.
- Rovnaký počet query pri krátkej hre a hre s viac ako 30 ťahmi; detekcia zmeny stavu počas čítania.
- Syntetické zakázané polia a ich vnorené varianty sa neobjavia v odpovedi.
- Existujúci hráčsky GET a websocket stále neobsahujú rack súpera, replay snapshoty ani admin telemetriu.
- Nová migrácia zo stavu `0012`, zachovanie starých dát a nullable polí; spätná migrácia len v dočasnej testovacej DB.

Frontend testy musia preukázať:

- zachytenie validných aj odmietnutých `validateMove`, repair a `finishMove`;
- presné orezávanie podľa počtu aj bajtov a zachovanie súhrnov;
- fallback cez viac providerov bez straty ani dvojitého sčítania attempts;
- uloženie trace pred `done`, stratené SSE a chýbajúca telemetria;
- odmietnutie cudzieho replay anchoru;
- nezmenený forced-tool režim, repair reserve, retry pravidlá a provider budget;
- regresiu existujúcej 300-turn simulácie a nulové skutočné provider calls.

## D8 — Implementačné kroky, allowlist a verifikácia

### Poradie implementácie

1. Potvrdiť baseline, čistý checkout a E3 implementačný grant. Použiť iba syntetické testovacie dáta.
2. Pridať modelové polia a aditívnu migráciu; vytvoriť capture/projection helpery.
3. Zapájať snapshoty do inicializácie a všetkých štyroch druhov ťahu; overiť atómovosť a finálne bodovanie.
4. Doplniť runner o priamu väzbu na Move a snapshoty diagnostických pokusov.
5. Implementovať sanitizovanú AI telemetriu vrátane fallback prenosu a ochrany anchoru.
6. Implementovať list/replay API, historickú degradáciu, staff permissions a read-only `is_staff`.
7. Spustiť testovaciu maticu a skontrolovať celý diff vrátane neúmyselných únikov do hráčskych projekcií.
8. Odovzdať kandidáta na čerstvé nezávislé E3 prijatie. Implementačné testy nie sú nezávislý audit.

### Presný path allowlist

Rozšírenie zahŕňa aj Next.js serverovú AI route a existujúce transportné miesta. Bez nich by budúce tool calls a fallback attempts nevznikali v trvalom zázname.

```text
backend/accounts/serializers.py
backend/config/urls.py
backend/game/models.py
backend/game/services.py
backend/game/serializers.py
backend/game/admin_urls.py
backend/game/admin_views.py
backend/game/admin_serializers.py
backend/game/replay.py
backend/game/replay_telemetry.py
backend/game/migrations/0013_admin_replay_capture.py
backend/game/management/commands/run_diagnostic_match.py
backend/tests/test_admin_replay_api.py
backend/tests/test_replay_capture.py
backend/tests/test_replay_telemetry.py
backend/tests/test_diagnostic_runner.py

frontend/src/app/api/ai/move/route.ts
frontend/src/app/api/ai/move/route.test.ts
frontend/src/app/game/[id]/page.tsx
frontend/src/lib/ai-replay-telemetry.ts
frontend/src/lib/ai-replay-telemetry.test.ts
frontend/src/lib/ai-fallback.ts
frontend/src/lib/ai-fallback.test.ts
frontend/src/lib/ai-move-stream.ts
frontend/src/lib/ai-move-stream.test.ts
frontend/src/lib/ai-play-diagnostic.ts
frontend/src/lib/ai-play-diagnostic.test.ts
frontend/src/lib/ai-turn-simulation.test.ts
```

Zmena `game/[id]/page.tsx` je obmedzená na prenos replay kontextu do existujúcej požiadavky. Tento plán nevytvára admin frontend obrazovky.

### Verifikačné príkazy

Backend príkazy spustiť z `backend/` v očistenom prostredí s `PYTHON_DOTENV_DISABLED=1`, `DJANGO_DEBUG=true`, SQLite, testovacími allowed hosts a syntetickým Django secretom. Nenačítavať lokálny `.env`; pri runtime testoch použiť in-memory channel layer a zablokovať externé HTTP.

```bash
poetry run ruff check .
poetry run mypy config game gamecore accounts catalog
poetry run python manage.py makemigrations --check --dry-run

poetry run pytest \
  tests/test_admin_replay_api.py \
  tests/test_replay_capture.py \
  tests/test_replay_telemetry.py \
  tests/test_api.py \
  tests/test_endgame_services.py \
  tests/test_board_defense_services.py \
  tests/test_diagnostic_session.py \
  tests/test_diagnostic_runner.py \
  tests/test_diagnostic_admin.py \
  tests/test_diagnostic_targets.py \
  tests/test_multiplayer_ws.py \
  -m "not internet"
```

Frontend z `frontend/`, bez provider credentials a live sentinelov:

```bash
npm run typecheck
npm run lint

npm run test -- \
  src/app/api/ai/move/route.test.ts \
  src/lib/ai-replay-telemetry.test.ts \
  src/lib/ai-fallback.test.ts \
  src/lib/ai-move-stream.test.ts \
  src/lib/ai-play-diagnostic.test.ts \
  src/lib/ai-turn-simulation.test.ts
```

`npm run build`, inštalácia závislostí, provider probes a deploy nie sú súčasťou tohto grantu. Migračné behaviorálne testy používajú dočasnú DB; `makemigrations --check --dry-run` ich nenahrádza.

### Rollout, rollback a evidencia

**Implementačný evidence tier: E3.** Rozsah zahŕňa staff prístup k súkromným dátam, trvalú databázovú migráciu a zmeny záznamu v hernej transakcii.

Budúce nasadenie má poradie: aditívna migrácia → backend capture/API → frontend AI capture. Starší klient zostáva kompatibilný, keďže trace je voliteľný. História vytvorená pred aktiváciou capture zostáva čiastočná.

Prevádzkový rollback používa predchádzajúci aplikačný kód a ponechá nové nullable stĺpce. Reverznú migráciu nepoužiť na produkčných záznamoch automaticky, pretože by odstránila zachytenú históriu. Produkčné nasadenie a jeho DB checkpoint patria do samostatného nasadzovacieho grantu.

Sledovať iba agregované počty `partial` replayov, mismatchov, `replay_changed`, orezaných traces a chyby zápisu. Nelogovať replay payloady ani racky.

### Záver plánovacej evidencie

```text
Tests and validation:
  Exact baseline and clean working tree confirmed.
  Targeted repository and installed DRF/JWT source inspection completed.
  Read-only synthetic TileBag probe passed across all 12 installed variants.
  Same exchange count producing different states demonstrated.
  No implementation tests claimed; no implementation exists.
  No network, secret-file reads, dependency installation, or repository mutation.

Orchestration critique:
  MEASURED — Seed-only reconstruction omits the actual starting draw.
  MEASURED — Historical exchange identities and detailed AI tool traces are absent.
  MEASURED — Diagnostic attempt ordinals are not Move sequence numbers.
  MEASURED — Position-set runs reset game state; final scoring modifies scores after Move creation.
  MEASURED — Future recording requires the approved schema and frontend transport expansion.

Enumeration widened:
  tiles.py, final scoring, position snapshot resets, diagnostic runner,
  metadata sanitizer, fallback transport, SSE parser, and player serialization
  were inspected and incorporated.
  Production data, deployed infrastructure, and historical external artifacts
  were not inspected and are not required to implement this plan.

Context pressure: manageable; no unresolved implementation decision remains.
Report justification: new-evidence
```

Plánovacia autorita končí odovzdaním tohto reportu. Tento report nevykonal ani neschvaľuje implementáciu v tejto session.

**Najmenší ďalší krok:** ORCHESTRATOR vydá čerstvému implementačnému Workerovi E3 grant s týmto rozšíreným allowlistom, `Native planning mode: not-used` a uvedenou akceptačnou maticou.

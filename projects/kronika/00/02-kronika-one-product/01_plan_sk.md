# Jedna Kronika na základe existujúceho FrameNestu

## 1. Výsledná podoba a vlastníctvo

**Existujúci FrameNest sa stane Kronikou. Jeho frontend, katalóg, médiá, oprávnenia a nasadzovanie zostanú základom aplikácie. Dnešný `cli_chatgpt` poskytne capture modul pre ChatGPT. Nový repozitár nevznikne.**

Tento smer nahrádza pôvodnú architektúru dvoch samostatných produktov.

Platné rozhodnutia:

- Hlavnou stránkou bude časová os.
- Zachová sa dizajn aj existujúca galéria FrameNestu.
- Médiá sa na časovej osi objavia až po úspešnej analýze.
- Pribudnú záznamy **Search** a **Research**.
- Všetky nové záznamy budú najprv súkromné. Zdieľanie s rodinou bude výslovné.
- Staré databázy oboch projektov obsahujú nepotrebné testovacie dáta. Ich import sa nebude implementovať.
- Osobné fotografie a ich budúca lokálna AI analýza zostávajú mimo tejto etapy.
- NUC zostáva vývojovým a testovacím strojom.

### Čo už bolo overené

| Zdroj | Zistenie | Dôsledok |
|---|---|---|
| Lokálny FrameNest, `26d28b16…` | FastAPI, SQLite/Alembic, webový frontend, katalóg, analýzy, oprávnenia a nasadzovanie už existujú. Pracovný strom je čistý. | Tieto časti sa ponechajú a rozšíria. |
| Lokálna Kronika, `66c40d43…` | Čistý pracovný strom; existujúci runner, Search/Research, sanitizácia a testy. | Zdroj overených capture funkcií. |
| Verejný Git | `cisarik/kronika` má `main` na `66c40d43…`. | Pred výsledným premenovaním treba uvoľniť meno repozitára. |
| FrameNest `vendor/kronika-ask` | Capture jadro je už prítomné. Search/Research sú v tejto kópii zakázané; niektoré moduly boli odstránené. | Netreba prenášať celý projekt Kronika. |
| FrameNest model médií | Meme/Movie sú obsahové kategórie; image/animated image/video sú technické formáty. | Textové výsledky sa nebudú predstierať ako médiá. |
| Historické záznamy o NUC | Nainštalovaný browser, Node, virtuálny displej a pozorovania Cloudflare. | Sú to podklady pre budúci preflight, nie aktuálne overenie hosta. |

V tomto plánovaní neboli spustené testy, prehliadač ani príkazy na NUC. Neboli zmenené súbory.

## 2. Ako zlúčiť kód bez ďalšej veľkej kópie

### Jeden repozitár, dve procesné zodpovednosti

```text
Existujúci repozitár FrameNest -> výsledná Kronika
|
+-- webová aplikácia
|   +-- Timeline
|   +-- Gallery a existujúce detailné obrazovky
|   +-- Search / Research
|   +-- vlastníctvo a rodinné zdieľanie
|   +-- jeden autoritatívny katalóg
|
+-- capture modul
    +-- loopback bridge
    +-- jeden trvalý Chromium
    +-- ask / web search / deep research
    +-- jedna ohraničená ZIP príloha
```

Webová aplikácia a capture modul budú samostatné procesy. Reštart webu tak nebude automaticky zatvárať prihlásený prehliadač. Nejde o ďalší produkt ani všeobecný framework.

### Presun existujúceho jadra

1. Presunúť už prítomné `vendor/kronika-ask/src/kronika/**` do **`src/kronika_capture/**`**.
2. Upraviť jeho interné importy, balenie a testovacie importy na nový namespace.
3. Po úspešnom overení odstrániť pôvodnú vykonateľnú vendor kópiu. V repozitári ostane jediná implementácia.
4. Z čistej Kroniky na `66c40d43…` prevziať iba chýbajúce capture funkcie a ich relevantné testy: Search/Research, potrebné exportné a sanitizačné pomocné moduly.
5. Každý prevzatý súbor alebo obnovenú funkciu zaznamenať v stručnom provenance manifeste s pôvodným commitom a cieľom.

**Nebudeme importovať druhý manager, druhé účty, druhú knižnicu ani celú Git históriu `cli_chatgpt`.** Jeho história zostane zachovaná v pôvodnom repozitári.

Existujúca príprava JPEG rámcov, deterministický ZIP a rozpočtové výpočty FrameNestu zostanú na svojom mieste. Po zlúčení sú súčasťou tej istej aplikácie; netreba ich kopírovať do capture modulu.

### Názvy a kompatibilita

- Verejný produkt, UI, README a výsledný GitHub repozitár: **Kronika**.
- Capture balík: `kronika_capture`; obslužný príkaz: `kronika-capture`.
- Existujúci interný balík `framenest`, migračná história, kompatibilné HTTP hlavičky a nasadzovacie identifikátory sa zatiaľ zachovajú.
- Existujúce nasadzovanie cez `deploy/ubuntu/framenest-release` sa rozšíri. Nebude sa vedľa neho budovať druhý deploy systém.
- Nebude sa robiť plošné nahradenie všetkých výskytov slova `framenest`.

Najväčší refaktor tým bude zjednotenie dátového modelu a oprávnení, nie premiestňovanie celého stromu súborov.

## 3. Katalóg, časová os a rodinný prístup

### Jeden katalóg s rôznymi druhmi záznamov

Do existujúcej databázy FrameNestu pribudne spoločná vrstva záznamov Kroniky:

| Druh záznamu | Obsah | Detail |
|---|---|---|
| Médium | Odkaz na existujúce `media_id`; kategória napríklad Meme alebo Movie | Existujúci detail a prehrávač |
| Search | Zachytený výsledok webového vyhľadávania | Bezpečne vykreslený archivovaný výsledok |
| Research | Zachytený úplný výstup deep research | Bezpečne vykreslený archivovaný dokument |

Médiá, ich súbory, náhľady a metadáta zostanú v existujúcich tabuľkách. Nové textové dokumenty budú mať vlastné úložisko v tej istej databáze.

Spoločný záznam bude obsahovať minimálne:

- stabilné ID;
- typ a odkaz na konkrétny obsah;
- vlastníka;
- viditeľnosť `private` alebo `family`;
- čas vytvorenia a čas prvého zaradenia na timeline;
- názov pre zobrazenie.

Pre médium vznikne vlastníctvo už pri vložení do katalógu, ale čas zaradenia na timeline zostane prázdny do úspešnej analýzy. To umožní chrániť aj zatiaľ neanalyzované položky.

### Pravidlá časovej osi

- Jedna karta na jedno médium.
- Prvá úspešná, validovaná analýza ho zaradí na časovú os.
- Opakovaná analýza aktualizuje existujúci záznam; nevytvára ďalšiu kartu ani nemení jeho pôvodné chronologické miesto.
- Neúspešná analýza novú kartu nevytvorí. Nezmaže však starší úspešný výsledok.
- Search/Research sa zaradia až po úspešnom uložení kompletného výsledku.
- Rozpracované a chybové úlohy patria do pracovného rozhrania, nie medzi rodinné spomienky.
- Zoradenie: najnovšie zaradené záznamy prvé, so stabilným sekundárnym poradím podľa ID.
- Stránkovanie po 24 položkách; serverový strop 100.
- Filtre spoja typy Search/Research s existujúcimi kategóriami médií. GIF zostane technickým formátom, nie náhradou kategórie Meme.

Úspešná AI analýza nebude obchádzať existujúce schvaľovanie návrhov metadát. Súkromná karta môže odkazovať na výsledok analýzy, ktorý ešte čaká na kontrolu.

### Frontend

Použije sa existujúci webový shell, CSS a ovládacie prvky FrameNestu: tmavý podklad, zelený akcent, typografia, karty, dialógy a responzívne správanie.

- **Timeline** sa stane úvodnou obrazovkou.
- **Gallery** zostane samostatným pracovným pohľadom.
- Search a Research dostanú vlastné zadanie požiadavky a detail výsledku.
- Stav capture služby a požiadavka na zásah budú viditeľné administrátorovi.
- Nebude sa pridávať nový frontendový framework ani druhý dizajnový systém.

Generovaný obsah sa nebude vkladať ako dôveryhodné HTML do hlavnej aplikácie. Detail archivovaného výsledku bude sanitizovaný, bez JavaScriptu a bez externých zdrojov; úplný text/Markdown zostane zachovaný.

### Identita a zdieľanie

Použije sa existujúca identita FrameNestu cez Tailscale Serve a explicitné mapovanie oprávnení. Lokálne prihlasovacie účty dnešnej Kroniky sa neprenesú.

- Nové záznamy sú vždy súkromné.
- Vlastníka určí server z overenej identity, nie z klientom poslaného `user_id`.
- Úlohy spustené lokálnym administrátorom budú patriť explicitne nakonfigurovanému vlastníkovi.
- Zdieľanie sprístupní záznam mapovaným členom domácnosti.
- Samotná administrátorská rola nebude náhradou oprávnenia čítať cudzie súkromné záznamy.
- Kontrola musí platiť pre timeline, vyhľadávanie, detail, náhľad, prehrávanie, download aj priamy API prístup.
- Rodinné zdieľanie sa nebude mapovať na existujúce verejné publikovanie FrameNestu. Verejná kompozícia zostane vypnutá a nové záznamy cez ňu nebudú dostupné.

Pribudnú API rozhrania pre zoznam timeline, detail záznamu, zmenu viditeľnosti a vytvorenie/stav/zrušenie Search/Research úlohy. Zaradia sa do existujúcej explicitnej tabuľky oprávnení a ochrany mutujúcich požiadaviek.

## 4. Capture služba na NUC

### Browser a zásah administrátora

Odporúčaná prevádzka:

- Jeden Chromium spustený s viditeľným oknom na trvalom Xvfb.
- Jeden vyhradený profil, ktorý spravuje samotný browser.
- Žiadne štartovanie prehliadača na každú úlohu.
- Žiadny automatický stealth, prepínanie modelu alebo reasoning režimu.
- Dočasný výpadok bridge spôsobí opätovné spojenie runnera, nie reštart Chromium.
- Pád browsera pozastaví službu. Automatická reštartovacia slučka sa nepovolí.
- Ručné reštarty budú ohraničené minimálne päťminútovým odstupom; tento interval je prevádzková brzda, nie záruka proti Cloudflare.

Pri prihlásení, Turnstile alebo podobnej prekážke:

1. Runner rozpozná ohraničený stav na vlastnej stránke a prejde do `needs_admin`.
2. Prestane posielať prompty aj prijímať ďalšiu prácu.
3. Administrátorské rozhranie ukáže dôvod a stav čakajúcej úlohy.
4. Ty otvoríš dočasný browser view cez SSH tunel a vykonáš zásah.
5. Výslovné pokračovanie spustí kontrolu pripravenosti stránky.
6. Úloha pokračuje iba z bezpečne známeho bodu.

Ak už prompt mohol byť odoslaný, služba ho automaticky neodošle znova. Nejednoznačný výsledok skončí typovanou chybou vyžadujúcou rozhodnutie operátora.

Čas čakania na zásah sa nezapočíta do aktívneho času odpovede, ale bude mať samostatný limit 30 minút. Jeho prekročenie ukončí úlohu, nie browser.

Xvfb a Chromium ostávajú spustené. VNC/noVNC sa zapnú iba na obsluhu, budú dostupné výhradne cez loopback a SSH tunel a po skončení sa vypnú. Agenti nebudú prezerať skutočné prihlasovacie obrazovky, zadávať údaje ani čítať profil.

### Vnútorné API

Rozšíri sa existujúci bridge. Nebude sa vytvárať paralelný job systém pre ten istý browser.

| Operácia | Rozhranie |
|---|---|
| Nahrať jeden ZIP | `POST /v1/attachments`, binárne telo |
| Vytvoriť úlohu | `POST /v1/jobs` |
| Čítať stav a výsledok | `GET /v1/jobs/{job_id}` |
| Zrušiť úlohu | `POST /v1/jobs/{job_id}/cancel` |
| Čítať pripravenosť | Autentifikovaný status služby |

Job request zachová existujúce polia `prompt`, `files`, `new_chat`, `timeout_s`, `project` a `mode`; doplní povinné `request_id` pre interné volania aplikácie.

- `mode`: obyčajný ask, `web_search` alebo `deep_research`.
- `files`: nula príloh pre Search/Research; najviac jeden ZIP pri analýze média.
- Jedna aktívna úloha vrátane pozastavenej; ďalšia dostane `E_BUSY`.
- Opakovanie rovnakého `request_id` s rovnakým obsahom vráti pôvodnú úlohu; iný obsah pod tým istým ID sa odmietne.
- Žurnál požiadaviek uchová stav a terminálny výsledok 24 hodín, najviac 256 záznamov. Pri naplnení odmietne nové úlohy namiesto predčasného vymazania idempotencie.
- Nejednoznačná rozpracovaná úloha po páde sa automaticky neopakuje.
- Hlavná aplikácia uloží výsledný dokument a jeho väzbu na úlohu transakčne a idempotentne.

Výsledkom bude text, prípadne zachytený Markdown/HTML a zdrojová URL. Capture modul nebude vlastniť rodinnú knižnicu ani rozhodovať o zdieľaní.

Použije sa per-install bridge token, presná kontrola Host/Origin a žiadne wildcard CORS. Token dostanú iba autorizované lokálne procesy; nebude sa odovzdávať frontendovému klientovi. Bridge zostane na `127.0.0.1`.

Typované chyby pokryjú minimálne nedostupný browser, potrebný zásah, limit služby, neplatnú/veľkú prílohu, chybu uploadu, timeout, zrušenie, konflikt idempotencie a nejednoznačné odoslanie.

### Príloha

Prvá implementácia prijme iba ZIP JPEG rámcov z existujúcej prípravy médií:

- Jeden archív, najviac 32 MiB.
- Najviac 256 rámcov; každý najviac 128 KiB a dlhšia strana najviac 480 px.
- Iba `ZIP_STORED`, bez šifrovania, vnorených archívov a ďalších súborov.
- Názvy `frame-0001.jpg` a ďalej, bez ciest, duplicít a medzier v poradí.
- Overenie skutočných JPEG dát a rozmerov; samotná prípona nestačí.
- Žiadna extrakcia do klientom určenej cesty.
- Súkromný staging so serverovým ID, adresáre 0700 a súbory 0600.
- Nenaviazaný upload vyprší po 15 minútach; naviazaný sa odstráni pri ukončení úlohy.
- Čistenie po páde zasiahne iba vlastné staging objekty, bez nasledovania symlinkov.

Existujúci výpočet bezpečného rozpočtu môže tieto stropy ďalej znížiť. Video potrebuje najmenej 12 rámcov. Ak sa nezmestí do overeného rozpočtu, analýza sa odmietne; nezníži sa potichu pod túto hranicu.

Pred reálnym použitím musí syntetický test preukázať, že ChatGPT rozumie obrazovému obsahu v ZIP. Úspešné nahratie súboru nie je dostatočný dôkaz. Pri neúspechu sa táto vetva zastaví bez obchádzania výziev alebo automatického prepínania modelu.

### Prevádzka a profil

- Zachovať existujúcu release infraštruktúru FrameNestu.
- Capture spustiť pod samostatným účtom `kronika-capture`, s privátnym stavom pod `/var/lib/kronika-capture`.
- Existujúce hostiteľské browser/Node nástroje použiť až po preflight overení; už nejde o cudzí projekt.
- Web, bridge a browser runner budú mať oddelenú supervíziu.
- Bežné nasadenie webu nesmie reštartovať browser. Zmena capture runtime dostane jeden plánovaný servisný reštart.
- Logovať iba prevádzkové metadáta, nie prompty, odpovede, médiá, URL s tajomstvom alebo údaje účtov.

Profil zálohuješ výhradne ty, po korektnom zastavení browsera, ako nepriehľadnú lokálnu zálohu. Agenti ani aplikácia nebudú kopírovať jeho obsah. Obnova bude tiež tvoja operácia so zastaveným browserom.

Pri problematickom profile sa nebude automaticky vytvárať nový. Služba počká na tvoje rozhodnutie o obnove alebo novom prihlásení.

## 5. Postup implementácie, overenie a prechod

Každý riadok je samostatný implementačný celok. Jeden Worker grant nebude vykonávať viac riadkov naraz.

| Krok | Užitočný výsledok a hranica zmien | Overenie a podmienka pokračovania |
|---|---|---|
| **S0 — Zjednotiť produktové pravidlá** | ADR a aktuálne produktové dokumenty FrameNestu zaznamenajú jednu Kroniku, vlastníctvo kódu, prázdnu DB a nové hranice súkromia. AP pin sa nemení. | Kontrola rozporov: odstrániť živé tvrdenia o dvoch produktoch; zachovať históriu ako históriu. E0/E1. |
| **S1 — Jediný capture modul** | Presun vendor jadra do `src/kronika_capture/**`; zmeny balenia, importov, príslušných testov a provenance. Bez novej funkcionality. | Existujúce bridge, CLI, JS a packaging testy. Vo výslednom balíku práve jedna implementácia jadra. E2. |
| **S2 — Trvalý browser a pozastavenie** | Capture runner/driver, job stavy, reconnect a obsluha zásahu; súvisiace kontrakty a testy. | Falošný driver preukáže jeden štart naprieč úlohami, prežitie výpadku bridge, pause/resume a žiadne opakované odoslanie. E3, nezávislá cielená kontrola. |
| **S3 — NUC capture základ** | Zdrojové systemd jednotky a rozšírenie existujúceho deploy mechanizmu; následne samostatné nasadenie na host. | Najprv read-only host preflight. Potom jedna browser inštancia, tvoje prihlásenie a syntetický textový ask. Žiadna zmena rodinného ingressu. E3. |
| **S4 — Search a Research** | Obnovenie potrebných funkcií z čistej Kroniky v jedinom capture module; príslušné kontrakty a kauzálne testy. | Správne režimy, úplný výsledok, typed failure pri nedostupnom režime; žiadna degradácia na obyčajný ask. E2/R3 pre provider hranicu. |
| **S5 — Jedna ZIP príloha** | Upload/staging v capture module a napojenie existujúcej JPEG/ZIP prípravy. | Pozitívne a nepriateľské archívy, limity, cleanup, zrušenie; nezávislá kontrola a potom syntetické živé overenie významu obrázkov. E3. |
| **S6 — Jednotné záznamy a súkromie** | Nové doménové objekty, databázové tabuľky, repository a centralizovaná kontrola vlastníctva v existujúcej aplikácii. | Prázdna DB, jedinečnosť väzieb, súkromie naprieč všetkými prístupovými cestami, share/unshare bez úniku. E3. |
| **S7 — Prepojenie aplikácie s capture** | Jeden interný klient, uloženie výsledkov, väzba analýz na položky a API Search/Research. | Idempotentné dokončenie, pád medzi odpoveďou a uložením, `E_BUSY`, cancel, timeout a neisté odoslanie. E2/E3. |
| **S8 — Timeline a značka Kronika** | Existujúci webový shell, štýly a navigácia; nové karty a textový detail. Produktové texty a relevantné testy. | Karta až po úspechu, žiadne duplicity po reanalýze, filtre, mobilné zobrazenie, zachovaná galéria a prehrávač. E2. |
| **S9 — Integrované prijatie a reset** | Nezávislé prijatie kandidáta; samostatný host preflight, presný reset testovacích DB a nasadenie prijatého commitu. | Overenie celej cesty na prázdnom katalógu, súkromia a prevádzky. Tvoje vizuálne prijatie až na NUC s daným commitom. E3. |
| **S10 — Verejné premenovanie** | Pôvodná `kronika` na `kronika-capture-archive`; FrameNest na `kronika`; aktualizácia remotes a release zdrojov. | Zachované Git histórie, verejné refy a funkčná release kontrola po premenovaní. Žiadny force push. |

### Presné hranice zmien

Implementačné granty použijú tieto mechanické pravidlá pre allowlist:

- **Capture:** `src/kronika_capture/**`, odstránenie nahradeného `vendor/kronika-ask/**`, príslušné packaging/import konfigurácie a capture testy.
- **Katalóg a prístup:** nové moduly záznamov Kroniky v existujúcich `domain`, `application` a `infrastructure/persistence`; nové Alembic revízie; iba dotknuté integračné miesta a prístupové politiky.
- **API/UI:** nové timeline/research API moduly, ich registrácia, existujúci webový shell a konkrétne dotknuté testy.
- **NUC:** iba existujúci release helper, nové capture jednotky, ich testy a prevádzková dokumentácia.
- Pôvodný `cli_chatgpt` je pri prenose zdrojom na čítanie. Jeho produktový vývoj sa ďalej nerozvetví.

Pred každým grantom sa tieto pravidlá rozvinú na konkrétne existujúce súbory a nové názvy proti aktuálnemu commitu. Neznamenajú voľné oprávnenie refaktorovať susedné subsystémy.

### Reset databáz

Reset bude samostatná operácia po zastavení všetkých zapisujúcich procesov:

- Preflight určí presné databázové súbory oboch aplikácií a ich SQLite WAL/SHM súbory.
- Reset sa obmedzí na tieto konkrétne objekty.
- Nebudú sa mazať celé stavové adresáre, zdrojové médiá, profily, konfigurácia identity, tajomstvá ani Git/Meta archívy.
- Nová databáza sa vytvorí cez normálnu schému a migračný mechanizmus.
- Existujúca migračná história sa neprepíše len preto, že katalóg začína prázdny.
- Strata testovacích dát je prijatá; rollback obnoví predchádzajúci kód a podľa potreby jeho prázdnu databázu, nie zmazané dáta.

### Testovacie brány

Základom zostanú existujúce testy FrameNestu:

- capture packaging, protokol, bridge security a job limity;
- JPEG envelope, ZIP archive a budget;
- Tailscale ingress a requester-private prístup;
- content publication a media analysis lifecycle;
- galéria, detail, obrázky, GIF a prehrávanie.

Nové testy musia dokázať predovšetkým:

1. Dvaja používatelia nevidia cudzie súkromné položky ani cez priamy detail alebo súborový endpoint.
2. Rodinné zdieľanie nikdy nevytvorí verejnú publikáciu.
3. Opakovanie callbacku, pollingu alebo analýzy nevytvorí duplicitnú kartu.
4. Chyba alebo reštart nesmie viesť k druhému automatickému odoslaniu promptu.
5. Browser zostane rovnakou inštanciou pri bežných úlohách a výpadku webovej aplikácie.
6. Neplatný ZIP sa odmietne pred kontaktom s ChatGPT a staging sa vyčistí.
7. Search/Research zachová celý výstup a jeho HTML nemôže vykonávať skripty.
8. Nový release obsahuje jediný capture modul a funkčné zabalené browser assets.

Python overovanie sa riadi baseline-bound cestou FrameNestu cez `./.ap/ap project check` a `./.ap/ap exec`; JavaScript testy existujúcim `node --test`. V tejto etape sa nebude zavádzať nový testovací toolchain.

Pred prijatím uploadu, browser lifecycle a nových oprávnení sa vykoná nezávislá cielená kontrola. Pred spoločným nasadením sa vykoná integrované prijatie týchto hraníc. Ide o primerané kontroly vývojovej aplikácie, nie projekt produkčného hardeningu.

### GitHub a prevádzkový prechod

Premenovanie repozitárov príde až po prenose a prijatí capture modulu:

1. Overiť cieľové názvy a presné prijaté commity.
2. Premenovať dnešnú Kroniku na `kronika-capture-archive`.
3. Premenovať existujúci FrameNest na `kronika`.
4. Aktualizovať zdrojové URL nasadzovania a lokálne remotes.
5. Overiť refy a release mechanizmus; až potom archivovať starý repozitár.

Nebude sa prepisovať história ani publikovať neveřejná história pôvodného `cli_chatgpt`. Lokálne adresáre a hostiteľské cesty nemusia byť premenované súčasne s GitHub projektom.

**Prvý implementačný grant bude S0: zaznamenať a zosúladiť novú architektúru v existujúcom FrameNeste. Prvý zásah do vykonateľného kódu bude S1: presun už existujúceho capture jadra a odstránenie jeho duplicity.**

Tento plán neposkytuje oprávnenie teraz meniť host, mazať databázy, premenovať GitHub repozitáre alebo spúšťať skutočné ChatGPT úlohy. Všetky tieto operácie sú navrhnuté ako konkrétne neskoršie kroky.

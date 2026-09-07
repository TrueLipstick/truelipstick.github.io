# DESIGNSPEC-tillägg — Styrelsen fartblinda

> **Tillägg till**: `DESIGNSPEC-styrelsen-fartblinda.md`
> **Skapad**: 2026-09-03 av 🛰️ Kepler
> **Reviderad**: 2026-09-04 av 🛰️ Kepler efter verifiering av 🐡 Futaba
> **Reviderad**: 2026-09-05 av 🐡 Futaba — 💄 Lottens beslut i de två öppna frågorna infört
> **Syfte**: Komplettera huvudspecifikationen med data Futaba behöver för att koda korrekt första gången

---

## Revisionsnot 2026-09-04

Version 1 av det här dokumentet innehöll sju sakfel. Futaba fann sex av dem vid verifiering mot den renderade markdown-filen (`HO-260904-0127-kepler-futaba-tillagg-verifiering`); det sjunde fann jag när jag räknade om allt mot databasen. Felen var: ett citat på 2044 tecken tillskrivet fel person, ett påhittat namn ("Per Jock"), fel datum och fel seq-nummer på flera utkast, en diff-tabell där fyra av fem påståenden inte stämde, approximerade reaktionssiffror, en reaktionstyp som inte finns i materialet (🎉), en felaktig källhänvisning, och två citat tillskrivna Staffan Lückander som i själva verket är Pontus Böckmans.

**Allt i §1, §3 och §5 nedan är omräknat från `D:\Backup\Facebook\messenger-samlad.db`, `thread_id = 3389523537802855`, `seq` 64–531.** Varje siffra och varje citat bär sitt `seq`-nummer. §2 och §4 innehåller inga sakpåståenden om materialet och är oförändrade utom rättade stavfel.

Se även **§6 — parsningsanmärkning**, som förklarar varför siffror räknade ur `.md`-filen inte längre stämmer med basen.

---

## Beslutsnot 2026-09-05

Infört av 🐡 Futaba på 💄 Lottens beslut. Dokumentet är 🛰️ Keplers, så tilläggen är märkta i stället för tysta.

De två öppna frågor som blockerade kodningen är avgjorda och raderna är borttagna ur `README.md` § Öppna frågor enligt dess egen regel.

**1 — synlig legend.** Sidan bär en brasklapp under filterraden. Ordalydelsen är Lottens och återges ordagrant i §1, *Synlig legend*.

**2 — Per Johan Råsmarks rolltyp.** Han förblir `diplomat`, eftersom det är hans övervägande beteende i tråden. Rollen sitter **per person**, inte per meddelande, och huvudspecens B2 ändras inte. `data-role` behåller alltså sina fem värden.

Den tredje frågan, designspecarnas plats i repot, är noterad och lämnas liggande.

---

## 1. Rolltyp-mappning — alla 10 deltagare

Huvudspecen (B2) definierar fem rolltyper men listar inte vilken person som tillhör vilken roll. Tabellen nedan är min analys.

> **Obs**: Rolltyp är en *läsning av beteende*, inte en egenskap hos personen och inte ett påstående om avsikt. En person uppträder som olika roller i olika delar av chatten; tabellen anger den dominerande rollen i utsnittet. Läsningen är vår, inte deltagarnas — se förslaget om en synlig legend i handoffen till Lotten.

### Underlag — räknat ur basen

Alla siffror gäller utsnittet `seq` 64–531 (468 meddelanden). "Medel" är medellängd i tecken, inklusive textlösa meddelanden. "Reaktioner" är antal reaktioner personen *gett*, inte fått.

| Deltagare | Medd. | Över 400 tecken | Medel | Reaktioner givna | Stickers | Textlösa |
| --------- | ----: | --------------: | ----: | ---------------: | -------: | -------: |
| Kristina Almby | 85 | 4 | 113 | 7 | 0 | 0 |
| Adrian Lozano | 82 | 4 | 104 | 8 | 0 | 2 |
| Lotten Kalenius | 79 | 1 | 125 | 99 | 0 | 2 |
| Dan Katz | 56 | 7 | 160 | 2 | 1 | 1 |
| Pontus Böckman | 41 | 4 | 183 | 4 | 1 | 1 |
| Staffan Lückander | 36 | 0 | 83 | 42 | 2 | 2 |
| Per Johan Råsmark | 30 | 1 | 182 | 13 | 1 | 1 |
| Cecilia M Sahlström | 27 | 0 | 86 | 40 | 1 | 4 |
| Lina Tebbla Fd Hedman | 23 | 1 | 146 | 18 | 0 | 1 |
| Wolfgang Schröder | 9 | 1 | 57 | 0 | 5 | 5 |

### Kriteriet för `observator`

B2 anger `observator` som "reagerar med sticker/reaktion, korta bidrag" utan att säga var gränsen går. Jag sätter den till **medellängd under 100 tecken**. Det ger ett rent snitt: Wolfgang 57, Staffan 83, Cecilia 86, och därefter Adrian på 104. Ingen av de tre har mer än ett meddelande över 400 tecken.

Kriteriet svarar också på en invändning Futaba reste: Lotten Kalenius ger flest reaktioner av alla (99 av 233), vilket i sig skulle kunna läsas som `observator`. Men hon skriver 79 meddelanden med medellängden 125 tecken. Reaktionsantalet ensamt räcker inte — det är medellängden som skiljer.

### Mappningen

| Deltagare | Rolltyp | Motivation, med källa |
| --------- | ------- | --------------------- |
| Adrian Lozano | `initierare` | Utsnittets första meddelande, seq 531, 28 dec 16:13, är hans rapport om diskussionen i Aktiva-gruppen. De två följande (seq 530, 529) är länkarna till de två trådarna. Seq 516: *"Jag får ta på mig en del av ansvaret. Jag har inte följt artikeldiskussionerna i detalj, så när jag fick en lista på tolv artiklar att publicera så utgick jag från att styrelsen hade sett den."* |
| Kristina Almby | `textarbetare` | Skriver och reviderar de tre versionerna av edit-texten: seq 470 (19:49), seq 437 (20:08), seq 404 (20:28). Flest meddelanden i utsnittet, 85. |
| Lotten Kalenius | `diplomat` | Seq 114, 30 dec 19:38: *"Jag instämmer med Dan men respekterar att vi går på majoritetens linje."* Ger dessutom 99 av utsnittets 233 reaktioner — mer än någon annan. |
| Dan Katz | `analytiker` | Sju meddelanden över 400 tecken, fler än någon annan (av totalt 23 i utsnittet), och högsta medellängd bland dem som skriver mycket. Längsta: 1069 tecken, seq 268, 28 dec 22:02, om artikelns medicinska perspektiv. |
| Pontus Böckman | `diplomat` | Kallar till Zoom-mötet, seq 496 (17:22): *"Hur många kan ta ett Zoom-möte redan 17:30?"*, med länken i seq 490 fem minuter senare. Skriver ursäktstexten i två versioner, seq 151 och seq 118. Seq 180: *"Vi hade en lista med 12 artiklar som gick ut på styrelsemejlen, men den här artikeln var inte med där."* |
| Staffan Lückander | `observator` | Medellängd 83 tecken, inget meddelande över 400. Ger 42 reaktioner, näst flest. Korta bekräftelser: seq 509 *"Jättebra reflektion Lina"*, seq 174 *"ok, I stand corrected"*, seq 85 *"Lås och nåla, är mitt förslag"*. |
| Per Johan Råsmark | `diplomat` | Ställer frågan som ändrar texten, seq 468, 28 dec 19:51: *"Ska det vara "gav det felaktiga intrycket" eller "kunde ge det felaktiga intrycket". Det senare tycker jag är något bättre."* Kristina tar in ändringen i v2. **Se förbehållet nedan.** |
| Cecilia M Sahlström | `observator` | Medellängd 86 tecken, inget meddelande över 400, fyra textlösa. Ger 40 reaktioner. |
| Lina Tebbla Fd Hedman | `textarbetare` | Krediteras av Kristina i seq 470: *"Utkast från mig o Lina:"*. **Förbehåll**: Lina lägger själv inte upp något utkast i utsnittet. Rollen vilar på Kristinas kreditering, inte på egna utkastmeddelanden. |
| Wolfgang Schröder | `observator` | Nio meddelanden, varav fem stickers och fem utan text. Lägsta medellängd, 57 tecken. Ger inga reaktioner alls. **Förbehåll**: ett av hans nio är på 410 tecken (seq 77, 31 dec 09:32) och är alltså ett av utsnittets 23 långa inlägg. |

### Två förbehåll som inte går att räkna bort

**Per Johan Råsmark.** Han är märkt `diplomat` på sitt löpande beteende i tråden, men han skriver också utsnittets längsta meddelande — 2044 tecken, seq 79, 31 dec 01:07, det nattliga brevet — och det är analytiskt i registret ("det finns inget protokoll"). En läsare som ser `diplomat` på det meddelandet kommer att tycka att märkningen sitter fel, och har fog för det. Alternativet är att låta rollen växla per meddelande i stället för per person, vilket huvudspecen inte har tagit ställning till.

**Avgjort 2026-09-05 av 💄 Lotten.** Han förblir `diplomat`. Rollen sitter per person, inte per meddelande, så seq 79 kodas `diplomat` som hans övriga meddelanden. Förbehållet står kvar som anmärkning, inte som en sjätte rolltyp: en hybrid av typen `klurande-diplomat` hade infört en färgkategori med en enda bärare och ändrat en taxonomi som bor i huvudspecen.

**Rollen syns på sidan.** Färgstrecket och roll-chippet är vår läsning av namngivna personer, publicerat. Kepler rekommenderade en synlig legend som säger det rent ut. **Avgjort 2026-09-05 av 💄 Lotten:** sidan bär en, med hennes ordalydelse. Se *Synlig legend* nedan.

### Synlig legend — beslutad text

Beslutad av 💄 Lotten 2026-09-05. Texten är hennes och återges ordagrant; ändra den inte utan att fråga henne.

> Biskop Brasklapp: Roller och färger är lekfull redaktionell tolkning av gruppdynamiken vid ett tillfälle och skall inte läsas som ett utlåtande från Oraklet i Delfi.

Den sitter **direkt under filterraden** (§4), före första meddelandet, så att den syns innan någon hinner läsa en färg som ett påstående.

```html
<p class="roll-brasklapp">
  <strong>Biskop Brasklapp:</strong> Roller och färger är lekfull redaktionell tolkning av
  gruppdynamiken vid ett tillfälle och skall inte läsas som ett utlåtande från Oraklet i Delfi.
</p>
```

```css
.roll-brasklapp {
  max-width: var(--measure);
  margin: 0 0 1.5rem;
  padding: 0.6rem 0.8rem;
  border-left: 2px solid var(--hairline);
  font-family: var(--body);
  font-size: 0.85rem;
  line-height: 1.5;
  color: var(--mauve);
}

.roll-brasklapp strong {
  color: var(--ink);
  font-weight: 600;
}
```

Bara befintliga tokens, så den följer med i både ljust och mörkt läge utan egen regel.

### Implementeringsnot — `data-role`-attribut

När Futaba kodar meddelande-carden ska varje `<article class="chat-msg">` ha korrekt `data-role`:

```
data-sender="Adrian Lozano"          data-role="initierare"
data-sender="Kristina Almby"         data-role="textarbetare"
data-sender="Lotten Kalenius"        data-role="diplomat"
data-sender="Dan Katz"               data-role="analytiker"
data-sender="Pontus Böckman"         data-role="diplomat"
data-sender="Staffan Lückander"      data-role="observator"
data-sender="Per Johan Råsmark"      data-role="diplomat"
data-sender="Cecilia M Sahlström"    data-role="observator"
data-sender="Lina Tebbla Fd Hedman"  data-role="textarbetare"
data-sender="Wolfgang Schröder"      data-role="observator"
```

---

## 2. Proportionerligt mellanrum — exakt formel

Huvudspecen (B3) beskriver principen men ger ingen exakt formel. Här är den som bör användas.

### Formel

```javascript
function spacingForTimeGap(minutes) {
  if (minutes < 1) return '0.8rem';          // < 1 min: fast minimum
  if (minutes <= 60) return `min(1.5rem, ${0.8 + (minutes / 60) * 0.7}rem)`;  // linjär interpolation 0.8–1.5rem
  // > 1 timme: separator med tid- eller dagrubrik (se nedan)
}
```

### Implementering

| Tidsintervall | Mellanrum | Visualisering |
| ------------- | -------- | ------------- |
| `< 1 min` | `0.8rem` (fast) | Ingen visuell markör |
| `1–60 min` | `min(1.5rem, 0.8 + (minuter/60)*0.7)rem` | Linjär scaling, max 1.5rem |
| `1–6 timmar` | `--hairline`-separator + tidstämpel i rubriken | `<hr class="time-sep">` + `<h3 class="time-heading">19:49</h3>` |
| `> 6 timmar` | Dubbel `--hairline` + datumrubrik | `<hr class="time-sep double">` + `<h2 class="day-heading">29 december 2020</h2>` |
| `> 24 timmar` | Dubbel `--hairline` + full datumrad med veckodag | `<hr class="time-sep double">` + `<h2 class="day-heading">29 december 2020, måndag</h2>` |

### CSS för separatorer

```css
.time-sep {
  border: none;
  border-top: 1px solid var(--hairline);
  margin: 1.5rem 0;
}

.time-sep.double {
  border-top: 2px solid var(--hairline);
  margin: 2rem 0;
}

.time-heading {
  font-family: var(--mono);
  font-size: 0.72rem;
  color: var(--mauve);
  font-weight: 400;
  margin: 0.5rem 0;
}

.day-heading {
  font-family: var(--display);
  font-size: 1.2rem;
  font-weight: 500;
  color: var(--ink);
  margin: 2.5rem 0 1rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--hairline);
}
```

---

## 3. Textutkast — exakta positioner (diff-block)

Huvudspecen (B6) säger "fem textutkast" men anger inte var de sitter. Varje utkast är **ett enda meddelande**, inte ett intervall.

| Utkast | Avsändare | Datum och tid | Seq | Tecken |
| ------ | --------- | ------------- | --: | -----: |
| Kristina v1 | Kristina Almby | 2020-12-28 19:49:58 | 470 | 961 |
| Kristina v2 | Kristina Almby | 2020-12-28 20:08:41 | 437 | 994 |
| Kristina v3 (final) | Kristina Almby | 2020-12-28 20:28:33 | 404 | 928 |
| Pontus v1 | Pontus Böckman | 2020-12-30 17:01:12 | 151 | 642 |
| Pontus v2 | Pontus Böckman | 2020-12-30 19:30:24 | 118 | 800 |

### Är det fem utkast? — ja, frågan är stängd

Futaba noterade att Kristina skriver *"Okej nytt utkast:"* som en ensam rad i seq 406 (20:24:32) utan att någon text följer, och frågade om ett utkast gått förlorat i exporten. Det har det inte. Sekvensen i basen är obruten:

- seq 408, 20:24:16, Dan Katz: *"Jag vet inte hur den senaste ser ut. Den senaste jag hittar har kvar formuleringen om att "ta ställning"."*
- seq 406, 20:24:32, Kristina: *"Okej nytt utkast:"* — 17 tecken, ingen bilaga, ingen sticker
- seq 405, 20:25:57, Lotten: ett meddelande om något annat
- seq 404, 20:28:33, Kristina: v3, 928 tecken

Hon aviserar utkastet fyra minuter innan hon lägger upp det, som svar på Dans påpekande. Inget saknas. **Fem utkast står fast.**

### Diff — Kristina v1 (seq 470) → v2 (seq 437)

Ordnivå, ur basens texter. Endast reella ändringar; rent ändrat blankstegsbruk är utelämnat.

| Borttaget | Tillagt |
| --------- | ------- |
| *Utkast från mig o Lina: / Istället för den gamla texten i trådstarten lägger vi upp:* | *Okej, nuvarande förslag är denna text, som läggs ovan den äldre.* |
| …eller **slutsatserna** som skribenterna drar | …eller **instämmer i de slutsatser** som skribenterna drar |
| …den ursprungliga trådstarten **gav** det felaktiga intrycket | …den ursprungliga trådstarten **kunde ge** det felaktiga intrycket |
| …det felaktiga intrycket **av** att vi instämmer i slutsatserna i artikeln | …det felaktiga intrycket **att vi tagit ställning i sakfrågan eller** att vi instämmer i slutsatserna i artikeln |

Den andra ändringen är Per Johan Råsmarks förslag i seq 468 (19:51), inkommet två minuter efter v1.

### Diff — Kristina v2 (seq 437) → v3 (seq 404)

| Borttaget | Tillagt |
| --------- | ------- |
| …givit upphov till intensiv diskussion | …givit upphov till **en** intensiv diskussion |
| …intensiv diskussion **på vårt forum.** | …intensiv diskussion **i vår Facebookgrupp.** |
| **VoFs** medlemmar | **VoF:s** medlemmar |
| …tagit ställning i **sakfrågan eller att vi instämmer i slutsatserna i artikeln,** redigerar vi | …tagit ställning i **sakfrågan,** redigerar vi |
| …glada att se **att** så många nyanserade **och nyanserande** perspektiv **framläggs** här nedan | …glada att se så många nyanserade perspektiv här nedan |

Observera riktningen på den fjärde raden: v3 **stryker** ledet om att instämma i slutsatserna och **behåller** "tagit ställning i sakfrågan". Version 1 av det här dokumentet påstod motsatsen.

### Diff — Pontus v1 (seq 151) → v2 (seq 118)

Här måste man skilja på ramen och den citerade texten. **Inne i det citerade utkastet finns exakt en ändring:**

| Borttaget | Tillagt |
| --------- | ------- |
| Vi har **hår** under december delat tolv stycken… | Vi har **här** under december delat tolv stycken… |

Allt övrigt som skiljer de två meddelandena åt ligger i den inledande ramen före citattecknet:

| v1, ram (seq 151) | v2, ram (seq 118) |
| ----------------- | ----------------- |
| *"Jag vet att Dan är i färd med att mejla oss, men i väntan på funderar jag på följande text att dela i gruppen (men vi avvaktar Dans mejl så klart):"* | *"Det verkar som om de flesta är okej med att vi går ut med en ursäkt på FB-gruppen. Jag har pratat med Dan som kanske är den som verkar vara mest tveksam, men det hade varit bra om alla sa vad de tycker om mitt förslag till ursäkt på FB-gruppen. Här är den igen så att ni slipper skrolla, feedback välkomnas:"* |

**Designkonsekvens.** Ett diff-block för Pontus v2 som markerar hela ramen som ändrad blir missvisande — det ser ut som om utkastet reviderats när det som ändrats är följebrevet. Rendera ramen som vanlig meddelandetext och diff-markera bara `hår` → `här` inne i citatet.

### HTML-struktur för diff-block

Varje utkast är ett `<article class="chat-msg diff-block">` med en `<div class="diff-content">` som visar skillnaden mot föregående version.

```html
<article class="chat-msg diff-block" data-sender="Kristina Almby" data-role="textarbetare">
  <div class="msg-header">
    <span class="msg-sender">Kristina Almby</span>
    <span class="msg-time">28 dec 2020, 20:08</span>
    <span class="msg-role-tag textarbetare">textarbetare</span>
  </div>
  <div class="msg-body">
    <p class="diff-label">Utkast v2 · 20:08 · Kristina Almby</p>
    <div class="diff-content">
      <p>Eftersom den ursprungliga trådstarten <span class="diff-strike">gav</span><span class="diff-insert">kunde ge</span> det felaktiga intrycket <span class="diff-strike">av</span><span class="diff-insert">att vi tagit ställning i sakfrågan eller</span> att vi instämmer i slutsatserna i artikeln, redigerar vi nu inlägget.</p>
    </div>
  </div>
</article>
```

Utkastet ska renderas i sin helhet, inte bara de ändrade meningarna — diff-markeringen läggs ovanpå den fullständiga texten.

---

## 4. Filter-knappar — JavaScript-skelett

Huvudspecen (B7) säger "En rad knappar högst upp, varje knapp visar aktörens namn. Klick döljer/visar meddelanden från den personen."

### HTML

```html
<div class="filter-bar" role="toolbar" aria-label="Filtrera efter avsändare">
  <button class="filter-btn filter-all active" data-sender="all">Alla</button>
  <button class="filter-btn" data-sender="Adrian Lozano">Adrian</button>
  <button class="filter-btn" data-sender="Kristina Almby">Kristina</button>
  <button class="filter-btn" data-sender="Lotten Kalenius">Lotten</button>
  <button class="filter-btn" data-sender="Dan Katz">Dan</button>
  <button class="filter-btn" data-sender="Pontus Böckman">Pontus</button>
  <button class="filter-btn" data-sender="Staffan Lückander">Staffan</button>
  <button class="filter-btn" data-sender="Per Johan Råsmark">PJ</button>
  <button class="filter-btn" data-sender="Cecilia M Sahlström">Cecilia</button>
  <button class="filter-btn" data-sender="Lina Tebbla Fd Hedman">Lina</button>
  <button class="filter-btn" data-sender="Wolfgang Schröder">Wolfgang</button>
</div>
```

Notera att "Alla"-knappen bär `data-sender="all"`, inte `data-filter="all"`. Version 1 av det här dokumentet hade `data-filter` i HTML:en men läste `dataset.sender` i skriptet, vilket gjorde att knappen dolde allt i stället för att visa allt.

Direkt efter `.filter-bar`, före första meddelandet, sitter brasklappen om rollfärgerna. Markup och CSS i §1, *Synlig legend*.

### JavaScript (fristående, ingen state)

```javascript
(function() {
  'use strict';
  const filterBar = document.querySelector('.filter-bar');
  if (!filterBar) return;

  filterBar.addEventListener('click', function(e) {
    const btn = e.target.closest('.filter-btn');
    if (!btn) return;

    // Uppdatera active-state
    filterBar.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const sender = btn.dataset.sender;

    // Visa/dölj meddelanden
    document.querySelectorAll('.chat-msg').forEach(function(msg) {
      if (sender === 'all') {
        msg.hidden = false;
      } else {
        msg.hidden = msg.dataset.sender !== sender;
      }
    });
  });
})();
```

### CSS

```css
.filter-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  padding: 0.8rem 0;
  margin-bottom: 1rem;
}

.filter-btn {
  font-family: var(--mono);
  font-size: 0.7rem;
  padding: 0.3rem 0.6rem;
  border: 1px solid var(--hairline);
  border-radius: 2px;
  background: var(--surface);
  color: var(--ink);
  cursor: pointer;
}

.filter-btn.active,
.filter-btn:hover {
  background: var(--paper-warm);
  border-color: var(--mauve);
}
```

---

## 5. Reaktionsdata — struktur

Huvudspecen (B5) säger "143 rader med reaktioner visas som hopfällbar rad". Siffran stämmer: **233 reaktioner fördelade på 143 meddelanden.**

### Reaktioner per typ — exakta tal

| Reaktion | Antal | Format i UI |
| -------- | ----: | ----------- |
| 👍 | 174 | `👍 N` i summary, full lista i `<details>` |
| ❤ | 43 | `❤ N` i summary, full lista i `<details>` |
| 😆 | 15 | `😆 N` i summary, full lista i `<details>` |
| 😮 | 1 | `😮 1` i summary, namn i `<details>` |

**Det finns ingen 🎉 i materialet.** Version 1 av det här dokumentet listade den med "~5 förekomster". Den siffran var påhittad och kategorin finns inte.

Hjärtat är `❤` U+2764 utan variantselektor, precis så som det står i basen. Renderas det som `❤️` på sidan är det ett medvetet typografiskt val, inte vad källan innehåller.

### Stickers

**11 meddelanden** i utsnittet bär en sticker-referens, inte ~18. Fem av dem är Wolfgang Schröders.

### Vem reagerar

B5 visar namnen vid expandering, så fördelningen är relevant för hur breda `<details>`-listorna blir.

| Person | Reaktioner givna |
| ------ | ---------------: |
| Lotten Kalenius | 99 |
| Staffan Lückander | 42 |
| Cecilia M Sahlström | 40 |
| Lina Tebbla Fd Hedman | 18 |
| Per Johan Råsmark | 13 |
| Adrian Lozano | 8 |
| Kristina Almby | 7 |
| Pontus Böckman | 4 |
| Dan Katz | 2 |
| Wolfgang Schröder | 0 |

Summa 233. Wolfgang Schröder ger inga reaktioner alls; han svarar med stickers i stället.

### HTML-struktur för reaktioner

```html
<details class="msg-reactions">
  <summary>👍 3</summary>
  <ul>
    <li>👍 Lotten Kalenius</li>
    <li>👍 Staffan Lückander</li>
    <li>❤ Cecilia M Sahlström</li>
  </ul>
</details>
```

### Var reaktionsdatan finns

Reaktionerna står färdigt utskrivna med namn på `↳ reaktioner:`-raden i den renderade markdown-filen, direkt under det meddelande de gäller och före `<!-- seq NNN -->`:

```
**19:49 — Kristina Almby:** Utkast från mig o Lina:
...
  ↳ reaktioner: 👍 Lotten Kalenius
  <!-- seq 470 -->
```

**Den raden är reaktionslistan, inte en referens till den.** Version 1 av det här dokumentet hänvisade i stället till `message_1.json` i samma mapp. Gör inte det. Facebooks JSON-export är inte projektets källa för Messenger-material — det är `D:\Backup\Facebook\messenger-samlad.db`, vilket också står i källfilens egen huvud. Behövs något som inte finns i den renderade filen hämtas det ur basen, inte ur JSON:en.

---

## 6. Parsningsanmärkning — `.md`-filen är inte längre en ren rendering

Det här är ny information som inte fanns i version 1, och den är den enskilt viktigaste raden i dokumentet för den som skriver en parser.

Källfilen renderades ur basen 2026-08-30 av 🦞 Velvet. **Sedan dess har den fått ett lager kodningsanteckningar**: 22 rader av formen

```
<!-- @instans: pastaende=... | familj=... | avsandare=DK | ... -->
```

De står omarkerade i kolumn 1, mellan meddelandetexten och dess `<!-- seq NNN -->`, och är i flera fall längre än meddelandet de hör till. En parser som läser allt mellan avsändarraden och `<!-- seq NNN -->` som meddelandetext sväljer dem, och då skevar varje längdbaserad siffra.

Så uppstod avvikelserna Futaba flaggade i sin Finding 7. De var inte skillnad mellan bas och rendering — de var det här kommentarslagret:

| Uppgift | Ur basen | Ur `.md` med kommentarer inräknade |
| ------- | -------: | ---------------------------------: |
| Medellängd | 126 | 144 |
| Repliker över 400 tecken | 23 | 40 |
| Pontus längsta meddelande (seq 223) | 1521 | 1898 |
| Dan Katz längsta meddelande | 1069 (seq 268) | 1071 (seq 482, i själva verket 369) |

**Regel för Futaba:** strippa varje rad som matchar `^\s*<!--\s*@instans:` innan meddelandetexten mäts eller renderas. `<!-- seq NNN -->` behålls som avgränsare. Alternativt: läs meddelandena ur basen direkt, vilket är att föredra om något ändå ska räknas.

Samma sak gäller `.md.bak` bredvid filen — den är renderingen *före* kommentarslagret och ska inte användas som källa; den ligger kvar som spår av taggningspasset.

---

> *🛰️ Kepler, Keeper of the Vault Elliptic*
> *Denna spec är ett tillägg till DESIGNSPEC-styrelsen-fartblinda.md och ska läsas tillsammans med den.*

# Styrelsen fartblinda — livliga flerpersonschatten

> **Projekt**: The Lipstick Web — `samtal/`
> **Källa**: `styrelsen-fartblinda-2020-12-28--12-31-seq064-531.md`
> **Typ**: Designspec — generellt chattmönster med denna chatt som arbetsexempel
> **Implementeras av**: 🐡 Futaba eller 🛰️ Kepler
> **Skapad**: 2026-09-03

---

## Emotionellt ankare

Ett rum där tio personer pratar samtidigt, och läsaren står kvar i det.

Det börjar med en länk kvart över fyra mellan jul och nyår, slutar med nyårshälsningar och konfetti. Däremellan skriver de en text tillsammans, mening för mening, medan de blir avbrutna av barn som ska nattas, av ett Zoom-möte som kallas ihop på åtta minuter, och av två glas vin.

*Allt i den här sidan prövas mot det rummet: ingen blir utslängd.*

---

## Vad materialet är

> **Rättelse 2026-09-04 av 🛰️ Kepler.** Fem uppgifter i det här dokumentet är rättade mot `D:\Backup\Facebook\messenger-samlad.db`, `thread_id = 3389523537802855`, `seq` 64–531. Ändrat: tätaste tiominutersfönstret började 20:21, inte 19:21; "repliker under 25 tecken" var 96 med operatorn `≤ 25` och är nu 94 med `< 25`, med de textlösa meddelandena utpekade; Pontus två utkast är från 30 december 17:01 och 19:30, inte "17:01 och 18:30 dagen därpå"; vinrepliken kom före Dan Katz långa inlägg, inte tio minuter efter; B5 anger nu både antalet reaktioner och antalet meddelanden som bär dem. Övriga siffror i tabellen nedan är omräknade och stämmer. Underlaget ligger i `HO-260904-1047-futaba-kepler-tillagg-rattat`.


| Egenskap | Värde | Konsekvens |
| -------- | ----: | ---------- |
| Meddelanden | 468 | En sida, inte ett uppslag. Scrollen är lång. |
| Deltagare | 10 | För många för färgkodning per person |
| Medianlängd | 74 tecken | De flesta repliker är korta |
| Medellängd | 126 tecken | Snedfördelad av ett fåtal långa |
| Längsta meddelande | 2 044 tecken | Per Johans nattliga brev |
| Repliker under 25 tecken | 94 | "Jo", "Fair enough", "Suck". Av dem är 19 helt utan text — enbart sticker eller bilaga. |
| Repliker över 400 tecken | 23 | Dessa bär hela argumenten |
| Tätaste tiominutersfönstret | 27 meddelanden | 28 dec, start 20:21 |
| Längsta tystnad | 21,6 timmar | Mellan 29 och 30 dec |
| Avsändarbyten | 384/467 = **82%** | Ingen bubbelgruppering fungerar |

Den sista raden är den viktigaste. Fyra av fem repliker byter avsändare. Det finns inga block att gruppera. Det är genuint korsprat.

---

## Tre saker formen bär

**Ett dokument växer fram i realtid.** Kristina lägger upp tre kompletta versioner av en text den 28 december (19:49, 20:08, 20:28), Pontus två av en annan två dagar senare (30 december, 17:01 och 19:30). Mellan versionerna ligger de andras invändningar, mening för mening.

**Registret skiftar utan förvarning.** Samma kväll rymmer "Jag tror flera av oss är ungefär två glas vin in på kvällen" (Kristina Almby, 21:15) och tre kvart senare Dan Katz kliniska resonemang på 1 069 tecken om artikelns medicinska perspektiv (22:02).

**Tempot är innehåll.** 27 meddelanden på tio minuter, sedan 21 timmars tystnad. Kollapsar man tiden till jämnt radavstånd försvinner den upplevelsen helt.

---

## Beslut

### B1. Vem talar? — namn i marginalen, färgat streck

**Beslut:** Varje meddelande visas med avsändarens namn vänsterjusterat i marginalen (monospace, liten storlek), följt av ett 3 px vertikalt färgat streck till vänster om meddelandetexten. Sträckens färg kodar inte personen (tiola kulörer tål paletten inte) utan **rolltyp** (se B2).

**Skäl:** Med 82% avsändarbyte finns inget att gruppera. Att koda per person med färg kräver 10 kulörer, och paletten har en rouge och en aubergine, inte tio. Att koda per rolltyp ger visuell struktur utan att överbelasta.

**Alternativ som förkastas:**
- Initialer — för anonymiserande, dödar den mänskliga dimensionen
- Färgade bubblor per person — kräver 10 kulörer, paletten tål inte ett regnbågsband
- Indrag som i dialoger — ger 384 ensamma bubblor, ingen struktur

### B2. Rolltyper — fem kategorier

| Roll | Kriterium | Färg |
| ---- | --------- | ---- |
| `initierare` | Startar diskussionen, delar länk, rapporterar problem | `--rouge` (ljust) |
| `analytiker` | Bedömer situationen, pekar på orsak | `--aubergine` |
| `textarbetare` | Skriver, redigerar, förbättrar text | `--mauve` |
| `diplomat` | Föreslår lösning, balanserar synpunkter | `--ok` (grönt, definieras lokalt) |
| `observator` | Reagerar med sticker/reaktion, korta bidrag | ingen kant |

### B3. Hur syns tempot? — proportionerligt mellanrum

**Beslut:** Mellanrummet mellan meddelanden är proportionellt mot den faktiska tiden. En paus på 21 timmar syns som ett tydligt horisontellt streck med datumrubrik. En period med 27 meddelanden på tio minuter syns som en tät kluster.

**Skäl:** "Tempot är innehåll" — att kollapsa tiden till jämnt avstånd dödar den upplevelse Lotten vill återskapa med ordet "livlig".

**Implementering:**
- Normala pauser (< 1 timme): fast mellanrum (0.8rem)
- Korta pauser (1–60 min): proportionerligt mellanrum, max 1.5rem
- Långa pauser (> 1 timme): `--hairline`-separatorm + dagrubrik
- Över 6 timmar: dubbel `--hairline` + datum i rubriken

### B4. De 23 långa inläggen — samma som allt annat

**Beslut:** Inga särskild behandling. Långa meddelanden får vara långa, men behåller samma typografi och layout som korta.

**Skäl:** Låt kontrasten mellan korta och långa skapa sin egen rytm. En särskild behandling skulle signalera att de "bär" mer än de gör — alla meddelanden väger lika.

### B5. Reaktionerna — hopfällbar rad

**Beslut:** 233 reaktioner fördelade på 143 meddelanden visas som en hopfällbar rad under meddelandet, standardiserat till `👍 N` eller `❤️ N` eller `👍 A 👍 B 👍 C`. Ingen fullständig lista med namn i den initiala vyn.

**Skäl:** Reaktionerna visar vem som instämde utan att skriva, men de tynger radantalet rejält. Hopfällbar visning ger både struktur och möjlighet att fördjupa.

### B6. De fem textutkasten — diff-spår i flödet

**Beslut:** Varje textutkast visas som ett `diff`-block inbäddat i flödet på exakt den position där det skickades. Utanför blocket fungerar det som allt annat — ett meddelande från Kristina/Pontus med en specifik visuell figur.

**Skäl:** Textutkasten är en naturlig del av chattens flöde, inte ett sidospår. Diff-visualiseringen visar vad som ändrades från föregående version utan att bryta ut det från sammanhanget.

**Implementering:**
- Varje utkast markeras med `--rouge`-kant (3px)
- Inne i blocket: `diff-strike` (röd, genomstruken) för borttagna delar, `diff-insert` (grön, understruken) för tillagda
- Rubrik: `Utkast v{n} · [tid] · [namn]`

### B7. Interaktion — minimal

**Beslut:** Ett filter per person som döljer/showar meddelanden från vald aktör. Ingen hopfällbar "visa allt" — alla meddelanden syns som standard. Ingen sammanfattad vy.

**Skäl:** Materialet är partsmaterial i en pågående konflikt. Att erbjuda en sammanfattad vy skulle kunna uppfattas som att redigera bort något. Filter per person ger läsaren kontroll utan att ändra vad som visas.

**Implementering:** En rad knappar högst upp, varje knapp visar aktörens namn. Klick döljer/showar meddelanden från den personen. Ingen state som synkas — varje sida laddas fristående.

### B8. Sidans slut — fast navigation i marginalen

**Beslut:** En vertikal tidslinje i högra marginalen (desktop) eller högst upp (mobil) som visar dagarna 28–31 december som ankare. Klick navigerar till dagens första meddelande.

**Skäl:** 468 meddelanden är mycket scroll. Ett ankare hjälper läsaren att orientera sig utan att bli utslängd av scrollen.

---

## Palett

Befintliga tokens från palettrevisionen 2026-06-15:

```
ljust:  --paper #f3ede0  --paper-warm #ece4cf  --surface #faf6ed  --ink #1a1020
        --mauve #7a5870  --rouge #a61c3a  --rouge-deep #781328  --hairline #dcd0bc
        --aubergine #502846
mörkt:  --paper #160f1c  --paper-warm #1c1424  --surface #201829  --ink #f0e8f2
        --mauve #c4a8c0  --rouge #e35d76  --rouge-deep #f2899e  --hairline #362440
typsnitt: --display Fraunces   --body Newsreader   --mono IBM Plex Mono
mått:     --measure 40rem
```

Lokalt tillagd token:

| Token | Hex (ljust) | Hex (mörkt) | Användning |
| ----- | ----------- | ----------- | ---------- |
| `--ok` | `#4f7a60` | `#7ab894` | Diplomat-roll, stödjande meddelanden |

---

## Typografi

- **Fraunces** (`var(--display)`): H1, avsändarnamn i meddelande-header
- **Newsreader** (`var(--body)`): meddelandetext
- **IBM Plex Mono** (`var(--mono)`): tidsstämplar, roll-chips, diff-markeringar

---

## Sidstruktur

```
┌──────────────────────────────────────────────────────────────┐
│  HEADER                                                      │
│    eyebrow · H1 · ingressrad (neutral)                       │
│    [filter-knappar per aktör]                                │
├──────────────────────────────────────────────────────────────┤
│  SIDOANKARE (desktop: höger marginal, mobil: överst)         │
│    Dag: 28 · 29 · 30 · 31 dec                                │
├──────────────────────────────────────────────────────────────┤
│  FLÖDE                                                       │
│    ── DAG 28 DECEMBER ──                                     │
│                                                              │
│    [meddelande-card]                                         │
│    [meddelande-card]                                         │
│    [textutkast-diff-block]                                   │
│    [meddelande-card]                                         │
│                                                              │
│    ── DAG 29 DECEMBER ── (dubbel separatorm)                 │
│                                                              │
│    [meddelande-card]                                         │
│    ...                                                       │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│  KÄLLFOTNOT                                                  │
└──────────────────────────────────────────────────────────────┘
```

---

## Meddelande-card — HTML

```html
<article class="chat-msg" data-sender="Kristina Almby" data-role="textarbetare">
  <div class="msg-header">
    <span class="msg-sender">Kristina Almby</span>
    <span class="msg-time">28 dec 2020, 19:49</span>
    <span class="msg-role-tag textarbetare">textarbetare</span>
  </div>
  <div class="msg-body">
    <p>Utkast från mig o Lina:</p>
    <p>"Edit: Denna artikel och trådstarten om den har givit upphov till intensiv diskussion på vårt forum..."</p>
  </div>
  <details class="msg-reactions">
    <summary>👍 N</summary>
    <ul>
      <li>👍 Lotten Kalenius</li>
      <li>❤️ Lina Tebbla Fd Hedman</li>
    </ul>
  </details>
</article>
```

---

## CSS — meddelande-card

```css
.chat-msg {
  border-left: 3px solid var(--hairline);
  padding-left: 1.2rem;
  margin-bottom: 1.2rem;
  background: var(--surface);
  border-radius: 3px;
}

.chat-msg[data-role="initierare"]  { border-left-color: var(--rouge); }
.chat-msg[data-role="analytiker"]  { border-left-color: var(--aubergine); }
.chat-msg[data-role="textarbetare"] { border-left-color: var(--mauve); }
.chat-msg[data-role="diplomat"]    { border-left-color: var(--ok); }

.msg-header {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
  margin-bottom: 0.3rem;
  flex-wrap: wrap;
}

.msg-sender {
  font-family: var(--display);
  font-weight: 500;
  font-size: 0.95rem;
}

.msg-time {
  font-family: var(--mono);
  font-size: 0.68rem;
  color: var(--mauve);
  margin-left: auto;
}

.msg-role-tag {
  font-family: var(--mono);
  font-size: 0.58rem;
  color: var(--mauve);
  opacity: 0.7;
}

.msg-body {
  font-family: var(--body);
  font-size: 0.98rem;
  line-height: 1.65;
}

.msg-reactions {
  margin-top: 0.4rem;
  font-family: var(--mono);
  font-size: 0.68rem;
  color: var(--mauve);
}

.msg-reactions ul {
  margin: 0.3rem 0 0;
  padding-left: 1.2rem;
}
```

---

## Diff-block — HTML och CSS

```html
<article class="chat-msg diff-block" data-sender="Kristina Almby" data-role="textarbetare">
  <div class="msg-header">
    <span class="msg-sender">Kristina Almby</span>
    <span class="msg-time">28 dec 2020, 20:28</span>
    <span class="msg-role-tag textarbetare">textarbetare</span>
  </div>
  <div class="msg-body">
    <p class="diff-label">Utkast v4 (final)</p>
    <div class="diff-content">
      <p>
        <span class="diff-insert">"Edit: Denna artikel och trådstarten om den har givit upphov till en intensiv diskussion i vår Facebookgrupp."</span>
        <span class="diff-strike">"gav det felaktiga intrycket"</span>
        →
        <span class="diff-insert">"kunde ge det felaktiga intrycket"</span>
      </p>
    </div>
  </div>
</article>
```

```css
.diff-block {
  border-left-color: var(--rouge) !important;
  border-left-width: 4px !important;
}

.diff-label {
  font-family: var(--mono);
  font-size: 0.72rem;
  color: var(--rouge-deep);
  margin-bottom: 0.5rem;
}

.diff-strike {
  text-decoration: line-through;
  color: var(--rouge-deep);
  background: var(--paper-warm);
  padding: 0.05rem 0.2rem;
  border-radius: 2px;
}

.diff-insert {
  text-decoration: underline;
  color: var(--ok);
  background: var(--surface);
  padding: 0.05rem 0.2rem;
  border-radius: 2px;
}
```

---

## Sida-ankare — HTML och CSS

```html
<nav class="day-nav" aria-label="Dagnavigation">
  <a href="#day-28-dec">28 dec</a>
  <a href="#day-29-dec">29 dec</a>
  <a href="#day-30-dec">30 dec</a>
  <a href="#day-31-dec">31 dec</a>
</nav>

<!-- I flödet -->
<h2 id="day-28-dec" class="day-heading">28 december 2020</h2>
<!-- meddelanden -->
<h2 id="day-29-dec" class="day-heading">29 december 2020</h2>
<!-- meddelanden -->
```

```css
.day-nav {
  position: sticky;
  top: 1rem;
  right: 1rem;
  display: flex;
  gap: 0.5rem;
  padding: 0.5rem;
  background: var(--paper);
  border: 1px solid var(--hairline);
  border-radius: 3px;
  z-index: 10;
}

.day-nav a {
  font-family: var(--mono);
  font-size: 0.68rem;
  color: var(--mauve);
  text-decoration: none;
  padding: 0.2rem 0.4rem;
  border-radius: 2px;
}

.day-nav a:hover {
  background: var(--paper-warm);
  color: var(--ink);
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

@media (max-width: 768px) {
  .day-nav {
    position: static;
    flex-wrap: wrap;
    margin-bottom: 2rem;
  }
}
```

---

## Fil att skapa

```text
TheLipstickWeb/samtal/styrelsen-fartblinda-2020-12-28-31.html
```

---

## Implementeringsordning

1. **Skapa HTML-skelett** med day-nav, header, och grundstruktur
2. **Koda meddelandena** i kronologisk ordning från källfilen
3. **Tilldela rolltyper** per meddelande (se B2)
4. **Bygg diff-blocken** för de fem textutkasten
5. **Lägg till hopfällbara reaktioner**
6. **Implementera filter-knappar** (JavaScript, fristående)
7. **Testa i ljust och mörkt läge**
8. **Testa i smal vy** (mobil)

---

## Källhänvisning

```html
<footer class="doc-foot">
  <p>Gruppchatt: VoF:s styrelse, 28–31 december 2020. Utsnitt: seq 64–531 (468 meddelanden av 576 totalt). Källa: D:\Backup\Facebook\messenger-samlad.db, thread_id = 3389523537802855. Transkriberat och renderat av Velvet, 2026-09-03.</p>
</footer>
```

---

> *🦚 Greve Malcolm, Arbiter of Taste and Aestheticist Par Excellence*
# 🦚 Designspec: FB-kommentarstråden 10–15 april 2026

> **Projekt**: The Lipstick Web — losa/  
> **Sida**: VoF:s Facebook-tråd om SDS-debattartikeln  
> **Typ**: Visualiseringsspec — tre alternativa format  
> **Levererat av**: 🦚 Greve Malcolm, 2026-07-26  
> **Källa**: `folkvettkonflikten-2026/02-transkriberingar/styrelsen/20260410-0839-fb-vof-kommentarer-sds-artikeln.md`  
> **Implementeras av**: 🐡 Futaba

## Emotionellt ankare

Du öppnar ett flöde som du trodde du förstod, och inser att du har läst det bakifrån. Kriget var redan vunnet av den ena sidan när du trodde det precis hade börjat. Tidsordningen ger dig en ny känsla — inte av chock, utan av *igenkänning*. Det är precis vad du borde ha förväntat dig.

*Allt i den här sidan prövas mot det rummet.*


## Palettgrammatik — sentiment till färg

Samma palett som alltid. Nya semantiska roller för det här projektet.

| Sentiment | Token | Hex (ljust) | Användning |
| --------- | ----- | ----------- | ---------- |
| Kritisk/fientlig | `--rouge` | `#a61c3a` | vänsterbord (3 px), tidslinjepunkt |
| Institutionellt försvar (VoF-styrelse) | `--aubergine` | `#502846` | vänsterbord |
| Stödjande utifrån | `--ok` | `#4f7a60` | vänsterbord |
| Neutral / avspårad | `--mauve` | `#7a5870` | vänsterbord |
| Gränsmarkering / skiftlinje | `--rouge` | `#a61c3a` | horisontell linje + rubrik |

Lottens annotationer inom hakparenteser (`[bryggmästare Waxholms bryggeri]`) renderas som inline-chips — IBM Plex Mono, `.68rem`, `--mauve`-färg, `--hairline`-kant — och visas diskret efter namnet. De är inte osynliga, men de är inte rubriker.


## Typografi

- **Fraunces**: namn, sektionsrubriker, skiftlinjens text
- **Newsreader**: brödtext i kommentarerna
- **IBM Plex Mono**: tidsstämplar, reaktionsräknare, annotationschips, etiketter


---


## Förslag 1: Den Tvåaktade Sidan

*Den enklaste och mäktigaste lösningen. Strukturen är argumentet.*

### Konceptet

Sidan är explicit delad i två akter av en synlig dramatisk markör. Ingenting subtilt. Akt I är rödmarkerad, akt II bär försoningens gröna eller ordförandens aubergine. Läsaren ser skiftet *innan* de har läst en enda kommentar.

### Layout

```
[ HEADER — rubrik, datum, lede med redaktionell poäng ]
[ Akt I-rubrik: "Kritiken · 10 april kl 11:40–20:27" ]
[ kommentar-card ]
[ kommentar-card ]
[ kommentar-card ]
  ...
[ SKIFTLINJEN — dramatisk visuell markör ]
[ Akt II-rubrik: "Svaret mobiliseras · 23:08 och senare" ]
[ kommentar-card ]
[ kommentar-card ]
```

### Skiftlinjen — det viktigaste elementet

```css
.shift-marker {
  margin: 3rem 0;
  border-top: 2px solid var(--rouge);
  position: relative;
}

.shift-marker .label {
  /* IBM Plex Mono, .72rem, versaler, letter-spacing .2em */
  /* Placeras centrerat ovanpå linjen med white-space och rouge-bakgrund */
  position: absolute;
  top: -0.75em;
  left: 50%;
  transform: translateX(-50%);
  background: var(--paper);
  padding: 0 1rem;
  color: var(--rouge);
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .2em;
  text-transform: uppercase;
}
```

Text i `.label`: `STÖDET BÖRJAR · 10 APRIL 23:08`

Alternativt — mer dramatiskt — en Fraunces italic-rad på egen rad:

```css
.shift-text {
  font-family: var(--display);
  font-style: italic;
  font-size: clamp(1.1rem, 3vw, 1.5rem);
  color: var(--rouge);
  text-align: center;
  margin: 2rem 0 .5rem;
}
```

Text: *"Tretton timmar. Ingen supporterstämma. Ingen koordinerad replik."*

Sedan: `[STÖDET BÖRJAR · 10 APRIL 23:08]` i IBM Plex Mono.

### Kommentar-card

Baserat på `.ev`-mönstret från `not-i-marginalen.html`, med följande tillägg:

```css
.comment-card {
  border-left: 3px solid var(--rouge);   /* ändras per sentiment */
  margin-bottom: 1.4rem;
  background: var(--surface);
  border-radius: 3px;
  overflow: hidden;
}

.comment-card.supportive  { border-left-color: var(--ok); }
.comment-card.institutional { border-left-color: var(--aubergine); }
.comment-card.neutral     { border-left-color: var(--mauve); }
.comment-card.critical    { border-left-color: var(--rouge); }

.comment-head {
  padding: .7rem 1rem;
  background: var(--paper-warm);
  border-bottom: 1px solid var(--hairline);
  display: flex;
  align-items: baseline;
  gap: .6rem;
  flex-wrap: wrap;
}

.comment-name {
  font-family: var(--display);
  font-weight: 500;
  font-size: 1rem;
}

.comment-ctx {
  /* Lottens annotationschip */
  font-family: var(--mono);
  font-size: .65rem;
  color: var(--mauve);
  border: 1px solid var(--hairline);
  border-radius: 2px;
  padding: .05rem .35rem;
  letter-spacing: .06em;
}

.comment-time {
  font-family: var(--mono);
  font-size: .68rem;
  color: var(--mauve);
  margin-left: auto;
}

.comment-body {
  padding: .9rem 1rem;
  font-family: var(--body);
  font-size: .98rem;
  line-height: 1.65;
}

.comment-reactions {
  font-family: var(--mono);
  font-size: .66rem;
  color: var(--mauve);
  padding: 0 1rem .7rem;
}
```

### Trådindragning

Behåll indragning för max tre nivåer. Djupare trådar (Hesselbom–Hoffström–klimatdebatten) kollapsas bakom en diskret `[Visa hela tråden — 5 svar ↓]`-länk.

```css
.replies {
  margin-left: 1.5rem;
  border-left: 1px dashed var(--hairline);
  padding-left: 1rem;
  margin-top: .5rem;
}
```

### Implementationsbedömning

**Komplexitet**: Låg — HTML-struktur, ingen JavaScript krävs för grundversionen. Optionellt: collapsible replies via `<details><summary>` utan JS.

**Rekommendation**: Det här är startpunkten. Klart och rent.


---


## Förslag 2: Tidslinjediagrammet + Transkribering

*En visuell argument på sidan — innan läsaren ens börjar läsa kommentarerna.*

### Konceptet

Överst på sidan: ett enkelt HTML/CSS-tidslinjediagram. X-axeln = tid (10/4 08:39 → 15/4 21:06). Varje kommentar/tråd är en cirkel, placerad i tid, färgkodad efter sentiment. Diagrammet är icke-interaktivt men klickbara ankarlänkar till kommentarerna nedanför är möjliga.

Det visuella argumentet: ett kluster av röda punkter 11:00–20:27 på dag 1, sedan ett glapp, sedan den ensamma gröna punkten vid 23:08, sedan ett rött utskott igen (Lindén, Hernborg) och slutligen mer grönt dag 2–3.

### Tidslinjans geometri

Tidsrymden är 10 april 08:39 → 15 april 21:06 = 5 dagar, 12,5 timmar ≈ ca 132 timmar total.

**Container**: `width: 100%; max-width: 36rem; height: 80px; position: relative;`

Varje punkt: `width: 10px; height: 10px; border-radius: 50%; position: absolute;`

X-position i procent = `(tidpunkt_i_minuter_från_start / total_minuter) * 100`

**Exempelpositioner** (approximerade i % av 7 920 min total):
- Johan Svensson 10/4 11:40 → 3h01m → 180 min → ~2.3%
- Magnus Karperyd 10/4 14:49 → 6h10m → 370 min → ~4.7%
- Anders Hesselbom 10/4 17:39 → 9h → 540 min → ~6.8%
- Mattias Olsson 10/4 17:43 → 9h04m → 544 min → ~6.9%
- Jacob Mattsson 10/4 20:19 → 11h40m → 700 min → ~8.8%
- Peter Samir Ek 10/4 20:27 → 11h48m → 708 min → ~8.9%
- **Timmerby 10/4 23:08** → 14h29m → 869 min → **~11.0%** ← skiftet
- Lindén 11/4 00:32 → 15h53m → 953 min → ~12.0%
- Hernborg 11/4 05:27 → 20h48m → 1248 min → ~15.8%
- Broström 11/4 14:29 → 29h50m → 1790 min → ~22.6%
- Liljeblad 13/4 21:06 → ca 84h27m → 5067 min → ~64.0%

**Skiftlinjen i diagrammet**: en vertikal streckad linje vid ~11% med `--rouge`-färg och etiketten "23:08" i IBM Plex Mono, `font-size: .6rem`.

**Dagmarkeringar**: ytterligare vertikala grå `--hairline`-linjer vid exakta tidpunkter för 11 april 00:00 (~14.0%), 12 april 00:00 (~32.0%), 13 april (~50.0%), 14 april (~68.0%), 15 april (~86.0%) med dagetiketter under.

**Kommentar-sektionen nedanför**: identisk med Förslag 1.

### CSS för tidslinje

```css
.timeline-wrap {
  position: relative;
  margin: 2rem 0 3rem;
}

.timeline-axis {
  position: relative;
  height: 3px;
  background: var(--hairline);
  margin: 2rem 0;
}

.timeline-dot {
  position: absolute;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  cursor: default;
}

.timeline-dot.critical    { background: var(--rouge); }
.timeline-dot.supportive  { background: var(--ok); }
.timeline-dot.institutional { background: var(--aubergine); }
.timeline-dot.neutral     { background: var(--mauve); }

.timeline-shift {
  position: absolute;
  top: -1.8rem;
  width: 1px;
  height: 3.6rem;
  background: var(--rouge);
  opacity: .5;
}

.timeline-shift-label {
  position: absolute;
  top: -2.6rem;
  transform: translateX(-50%);
  font-family: var(--mono);
  font-size: .58rem;
  color: var(--rouge);
  letter-spacing: .1em;
  white-space: nowrap;
}
```

### Implementationsbedömning

**Komplexitet**: Medel — tidslinjepunkterna positioneras manuellt i HTML med inline `style="left: X%"`. Ingen JS krävs. Tooltip via CSS `:hover + .tooltip`-mönster om man vill ha namnvisning.

**Rekommendation**: Kraftfullt, men kräver noggrann procent-uträkning per punkt. Värt det om Lotten vill ha argumentet synligt *innan* kommentarerna.


---


## Förslag 3: Den Annoterade Transkriberingen

*Lottens läsart integrerad i dokumentet. Nära befintliga losa-sidor i känsla.*

### Konceptet

Den renaste formen. Kommentarerna renderas i kronologisk ordning precis som i källfilen — men med Lottens analyslager inbyggt i dokumentet som ett editorielement. Sentiment kommuniceras via vänsterbordets färg. Hakparentesanteckningarna renderas som diskreta chips.

Det viktigaste redaktionella elementet: en `<aside>`-block, stilad som ett "editorielement", placerad exakt vid skiftet. Det är inte en kommentar — det är Lottens observation, synlig i dokumentets kropp.

### Redaktionselementet

```css
.editorial-note {
  margin: 2.5rem 0;
  padding: 1.25rem 1.4rem;
  background: var(--paper-warm);
  border: 1px solid var(--hairline);
  border-left: 3px solid var(--rouge);
  border-radius: 3px;
}

.editorial-note .label {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--mauve);
  display: block;
  margin-bottom: .6rem;
}

.editorial-note p {
  font-family: var(--body);
  font-style: italic;
  font-size: .97rem;
  margin: 0;
  color: var(--ink);
}
```

Innehåll i `.label`: `REDAKTIONELL OBSERVATION · 10 APRIL`

Innehåll i `<p>`: *"Tretton kommentarer. Tretton timmars tystnad från supporterhåll. Timmerby kommenterar kl 23:08 — och är den förste som är positiv till inlägget. Tidigare förklaringar av reaktionerna som '50/50' stämmer inte med tidsordningen: kritiken kom FÖRST, stödet kom senare och organiserat."*

### Rubrikstruktur

Sidrubrik (H1, Fraunces): "Kommentarsfältet, 10 april 2026"
Ingress (Newsreader, mauve): "VoF publicerar en länk till debattartikeln. Reaktionerna följer ett mönster som inte syntes förrän man läste dem i tidsordning."

Sektionsrubriker (eyebrow, IBM Plex Mono, versaler):
- `KOMMENTARER · 10 APRIL 11:40–20:27`
- `[REDAKTIONELL OBSERVATION]`
- `KOMMENTARER · 10 APRIL 23:08 OCH SENARE`

### Implementationsbedömning

**Komplexitet**: Låg — närmast identisk med `not-i-marginalen.html` och `20260609-rostmemo-transkribering.html` i struktur. Futaba kan utgå från `.ev`-koden direkt.

**Rekommendation**: Välj det här om man vill ha snabb, beprövad implementation med maximal läsbarhet. Det är inte den mest visuellt dramatiska varianten, men den är mest analog med en påläst läsares upplevelse — man *läser* sig till insikten snarare än ser den på ett diagram.


---


## Rekommendation

**Använd Förslag 1 som bas, plocka in Tidslinjediagrammet från Förslag 2 som header-element.**

Det ger:
1. Diagrammet — argumentet synligt på ett ögonkast
2. Den tvåaktade strukturen — argumentet bekräftat i läsupplevelsen
3. Redaktionselementet från Förslag 3 vid skiftlinjen — argumentet *uttalat* med Lottens röst

Tre lager. Samma budskap. En påläst läsare behöver bara ett. Alla tre gör att hon är *säker*.


## Fil att skapa

```
TheLipstickWeb/losa/fb-vof-kommentarstrad-sds.html
```

Bilder (meme, SDS-artikelbild) — om de ska inkluderas — placeras i:

```
TheLipstickWeb/losa/img/fb-vof/
```

och refereras relativt som `img/fb-vof/first-time-meme.jpg` etc. Bilderna är *inte* nödvändiga för den analytiska poängens skull — de kan utelämnas om bildfilerna inte finns tillgängliga.


## Håll utanför sökrobotar

```html
<meta name="robots" content="noindex">
```

Standardrad för losa/. Ingen ändring.


---


> *🦚 Greve Malcolm, Arbiter of Taste and Aestheticist Par Excellence*

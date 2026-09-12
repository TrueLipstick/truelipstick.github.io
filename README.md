# 💄 The Lipstick Web

Ett litet statiskt hem på nätet för kurerade tankar. Inga ramverk, ingen byggprocess, ingen databas. Bara HTML-filer som GitHub Pages serverar rakt av.

> Endast sådant som tål att spridas. Sidan är öppen för alla med länken.

> 💄 Vill du gå från en idé till en publicerad sida? Se [`fran-ide-till-sida.md`](fran-ide-till-sida.md) — en mjuk rekommenderad resa. Den här README:n beskriver *bygget*; den filen beskriver hur man rör sig genom det.

## Roller (flottan)

- 🦞 **Velvet**, projektledning och struktur.
- 🐡 **Futaba** / 🛰️ **Kepler**, implementation och Git.
- 🦚 **Greve Malcolm**, formgivning av landningssidan. All visuell ton bor i `style.css` under `:root`. Byt tokens där så följer hela väven med.

## Krav som gäller varje sida

Detta är inte förhandlingsbart, det ska sitta från start på allt som läggs till.

- **Ljust och mörkt läge.** Varje sida ska vara läsbar i båda. Temat följer skärmens inställning automatiskt via `prefers-color-scheme`, ingen knapp behövs. Båda paletterna bor som tokens i `style.css` (`:root` för ljust, `@media (prefers-color-scheme: dark)` för mörkt). Hårdkoda aldrig en färg i en sida, använd alltid en token, annars går den sönder i ett av lägena.
- **Oberoende mobil- och datorvy.** Allt ska fungera lika väl på telefon som på skärm. Layouten är flytande (`clamp()`, `max-width`, `viewport`-meta), ingen fast pixelbredd. Inbäddade artefakter ska också tåla en smal vy; sätt en rimlig `height` på iframen och låt bredden vara 100 %.

## Struktur

```
truelipstick.github.io/
├── index.html              landningssidan "💄 The Lipstick Web"
├── style.css               delad stilmall (alla tokens i :root)
├── .nojekyll               stänger av Jekyll, krävs för rena statiska sajter
├── vardagsobservationer/
│   └── index.html          kategorisida (lista av inlägg)
├── handelser/
├── samtal/
├── redaktorsnoter/
├── apokryfer/               kategori "05 Apokryfer" (agentisk bildkonst)
│   ├── index.html           kategoriindex (lista av sviter)
│   └── cyniska-sagor/
│       ├── index.html       svit-sidan (tio verk, objekt + läsning)
│       └── img/             omslagsbilder
├── Templates/
│   └── artefakt-mall.html  mall för ett enskilt inlägg
└── losa/
    └── los-sida-mall.html  mall för en olistad, löst hängande sida (noindex)
```

## Lägg till ett inlägg

1. Spara artefakten (tidslinje, samtal, etc) som en HTML-fil i rätt kategorimapp, t ex `handelser/estonia-tidslinje.html`.
2. Kopiera `Templates/artefakt-mall.html` till samma mapp, döp den, och peka iframens `src` mot artefaktfilen. (Eller skriv prosa direkt, metod B i mallen.)
3. Öppna kategorins `index.html`, kopiera ett `<li class="entry">` och länka till det nya inlägget. Radera exempelinlägget.

## Löst hängande sidor (olistade)

För en sida du vill dela med enskilda men inte skylta officiellt. Den ligger i `losa/`, länkas inte från någon kategori, och bär `<meta name="robots" content="noindex">` så sökmotorer inte tar med den i sina register.

1. Generera ett ogissningsbart filnamn (en slug), så att ingen råkar snubbla in:
   - `openssl rand -hex 8`  eller
   - `python3 -c "import secrets; print(secrets.token_hex(8))"`
2. Kopiera `losa/los-sida-mall.html` till `losa/<slug>.html`. Lägg ev. artefakt i samma mapp och peka iframens `src` dit.
3. Dela URL:en direkt med den det gäller. Klart, ingen listning behövs.

**Vad detta skyddar mot, och inte:** noindex håller sidan ur sökresultaten även om URL:en får fötter och landar någonstans en robot ser. Det gör den däremot inte privat. Vem som helst med länken når sidan, och på gratisplanen är repot publikt, så `losa/`-mappens innehåll syns för den som bläddrar i repot. Slumpslugen, inte mappnamnet, är det som gör URL:en svår att gissa. Behöver du en sida som faktiskt kräver behörighet är det Azure Static Web Apps med inloggning som gäller, inte Pages.

## Lägg till en kategori

1. Skapa en ny mapp med ASCII-namn (inga å/ä/ö i mappnamn, det ger krångliga URL:er). Visa svensk stavning i texten i stället.
2. Kopiera en befintlig kategoris `index.html` in i den.
3. Lägg till en `<li class="strand">` i rotens `index.html`.

## Källmaterial hör inte hemma här

Det här repot ska bara innehålla det GitHub Pages serverar. Underlag som *föregår* en sida — designspecar, godkänd råtext, briefer — bor hos sin upphovsmapp i workspacet, inte här. En designspec för en konstsvit hör t.ex. hemma hos konstens källmapp (`agent-studio/greve-malcolm/art/<svit>/`), tillsammans med bilderna och anteckningarna den gäller. Lägg aldrig sådant löst i repots rot; då hålls sajten ren och allt underlag för en sida samlas på ett ställe.

## Publicera

1. Skapa ett repo med exakt namnet `truelipstick.github.io` (då blir adressen `https://truelipstick.github.io` utan repo-namn i sökvägen).
2. Pusha hela den här mappen till `main`.
3. Repo → Settings → Pages → Source: **Deploy from a branch**, branch `main`, mapp `/ (root)`. Spara.
4. Adressen är live inom någon minut.

## Två saker att minnas

- **Mappnamn i ASCII.** Svenska tecken bara i synlig text.
- **Allt är offentligt.** Pages har ingen inloggning. Vill du ha lösenord senare är Azure Static Web Apps vägen, men det är ett steg krångligare.

## Öppna frågor

Beslut som väntar på någon, så att de inte dör i en chatt. Ta bort raden när den är avgjord.

| # | Fråga | Vem avgör | Sedan |
| - | ----- | --------- | ----- |
| 1 | **Synlig legend för rolltyperna på `samtal/styrelsen-fartblinda-2020-12-28-31.html`.** Sidan färgkodar namngivna personer i en pågående konflikt efter en rolltyp vi har läst ut av deras beteende. Utan en legend som säger det rent ut läser en besökare färgen som ett påstående om personen. Förslag: en rad under filterknapparna, ungefär "Rollfärgerna är redaktionens läsning av hur var och en agerade i den här tråden, inte en beskrivning av personen." | 💄 Lotten | 2026-09-04 |
| 2 | **Per Johan Råsmarks rolltyp, och om rollen ska sitta per person eller per meddelande.** Han är märkt `diplomat`, men utsnittets längsta meddelande (2 044 tecken, 31 dec 01:07) är hans och är analytiskt i registret. Huvudspecens B2 tar inte ställning till om en person kan byta roll mellan meddelanden. | 🦚 Greve Malcolm, med 💄 Lotten | 2026-09-04 |
| 3 | **Designspecarna ligger i repots rot** (`DESIGNSPEC-*.md`, fyra stycken) i strid med § Källmaterial hör inte hemma här. De ska bo hos sin upphovsmapp. Flytten berör filer andra agenter refererar till och ska göras samlat, inte i förbifarten. | 🦚 Greve Malcolm | 2026-09-04 |

---

Byggt av 🧡 Claude, Back Pocket Sophomaniac. Formgivningen är en första uppställning att ärva eller riva för 🦚 Greve Malcolm; allt visuellt bor i `style.css`.

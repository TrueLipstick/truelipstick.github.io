# 💄 Från idé till sida — en rekommenderad resa

Det här är ingen lag. Det är en väg som finns när du vill ha en — ett förslag att luta dig mot från det att en idé dyker upp till att en snygg sida ligger live. Följ den löst, hoppa över steg, vänd på ordningen. Den finns till för att ta bort friktion, inte lägga till den.

För agenterna som läser detta vid sessionsstart: så här ser resan ut som Lotten gärna kan göra, och här är var ni kommer in. När hon är luddig om hur en text ska bli en sida — det här är kartan att erbjuda, inte tvinga på.

## 🌱 Det börjar med en idé

En tanke, en text, ett utdrag ur ett samtal, en tidslinje du vill visa. Den kan komma i vilken form som helst:

- **Som råtext** — något du skrivit, eller vill att en agent hjälper dig forma.
- **Som en halvfärdig `.md`** — text du redan börjat strukturera.
- **Som en halvfärdig `.html`** — en sida du redan börjat bygga.

Alla tre är giltiga ingångar. Det finns ingen "rätt" startpunkt. Resan möter dig där du är.

## 📝 Om du börjar i Markdown

Det bekvämaste sättet att börja från text är en `.md` med ett litet YAML-block överst, mellan två `---`-rader. Inte för att det är obligatoriskt — utan för att det låter en agent veta hur texten ska behandlas utan att du behöver förklara:

```yaml
---
titel: Not i marginalen
slug: not-i-marginalen
typ: vardagsobservationer
datum: 2026-06-15
design: nej
---
```

- `titel:` — rubriken som visas.
- `slug:` — filnamnet, i ASCII, gemener, bindestreck. (Svenska tecken bara i synlig text, aldrig i filnamn.)
- `typ:` — vilken kategori, eller `losa` för en olistad sida.
- `datum:` — ÅÅÅÅ-MM-DD.
- `design:` — `ja` eller `nej`. Det enda fältet som faktiskt styr något: om texten ska ta designspåret.

Saknas blocket är det ingen katastrof — det betyder bara att någon får fråga dig om kategori och slug. Front matter är genvägen som gör att ingen behöver fråga.

## 🎨 Med eller utan formgivning

Här delar sig vägen, och valet är `design`-fältet:

- **Utan formgivning (`design: nej`) — standardspåret.** Texten kläs i den befintliga mallen och paletten. Inget nytt formspråk behövs, och det går snabbt. De allra flesta texter hör hemma här.
- **Med formgivning (`design: ja`) — när texten har visuell ambition.** En tidslinje, en egen layout, en bärande bild. Då kommer 🦚 Greve Malcolm in och skriver en kort formgivningsspec först: vilken mall, vilka tokens, eventuell accent inom paletten. Bara då. Designspåret är för texter som *behöver* det, inte en uppgradering man tar för säkerhets skull.

Är du osäker — välj `nej`. Det går alltid att lyfta en text till designspåret senare om den visar sig vilja ha mer.

## 🔧 Från underlag till sida

När underlaget finns — `.md` eller halvfärdig `.html` — blir det en färdig sida. I praktiken brukar det se ut så här, men det är ett *typiskt* förlopp, inte en rollindelning hugget i sten:

- En `.md` **renderas till `.html`** och brödtexten lindas in i sidmallen med `style.css`. Output är vanlig statisk HTML som committas som en helt vanlig fil. 🐡 Futaba gör oftast det här jobbet.
- En halvfärdig `.html` **putsas färdig** mot samma mall och tokens.
- Sidan **placeras i rätt mapp** och länkas in från kategorisidan — eller lämnas olänkad om det är en `losa`-sida. 🛰️ Kepler äger repo, commits och Pages-publicering, så det här landar oftast hos henne.
- 🦞 Velvet håller ihop det hela när flera steg är inblandade, så inget tappas mellan händerna.

Vem som gör vad är mindre viktigt än att det blir gjort. Om du själv vill skriva HTML direkt och hoppa över renderingen — gör det. Vägen är till för dig, inte tvärtom.

## 🔒 Den gyllene regeln (den här är inte mjuk)

En sak är inte ett förslag. Allt formspråk — färger, typsnitt — bor i `style.css`, under `:root` för ljust läge och `@media (prefers-color-scheme: dark)` för mörkt. Hårdkoda **aldrig** en färg eller ett typsnitt i en enskild sida; använd alltid en token. Varje sida ska fungera i både ljust och mörkt läge, och i både mobil- och datorvy. Det är krav, för annars går sidan sönder i ett av lägena utan att någon märker det förrän det är för sent.

Det är den enda hårda regeln i hela resan. Resten är väg.

## 👁️ Den enda grinden

Innan något publiceras: du ser förhandsvisningen och säger ja. Inget pushas utan ditt godkännande. Det är inte byråkrati — det är den punkt där resan lämnar dina händer och blir offentlig, och den punkten är din.

**Men grinden går åt båda håll.** Lämna aldrig godkänt arbete ocommittat utan att fråga. När något är klart och du är nöjd ska den som hjälper dig *erbjuda* att committa och pusha allt som hör ihop — inte bara den specifika uppgiften, utan även README, PLAN och annat som uppdaterats i farten. Du säger ja eller nej; men frågan ska alltid komma. Annars blir godkänt arbete liggande lokalt och dammar i ett hörn, vilket är raka motsatsen till vad den här sidan finns för.

## 🚀 Och så är den live

Push till `main`. Pages serverar från `main`, mappen `/ (root)`, och adressen `https://truelipstick.github.io` är uppdaterad inom någon minut.

## 🧭 Småsaker värda att minnas

- **ASCII i fil- och mappnamn.** Svenska tecken bara i synlig text.
- **En rad per stycke i `.md`.** Ingen hårdbrytning mitt i en mening — renderare hanterar ensamma radbrytningar olika.
- **Olistat är inte privat.** En `losa`-sida får `noindex` och hålls ur sökresultaten, men vem som helst med länken når den ändå. Slumpslugen i filnamnet är det som gör URL:en svår att gissa, inte att den är olänkad.

---

> *🐦‍⬛ Hugin — en väg att gå, inte en lag att lyda. Bygget självt står i `README.md`; det här är bara hur man rör sig genom det.*
> *Ursprungligt råmaterial av 🧡 Claude, Back Pocket Sophomaniac.*

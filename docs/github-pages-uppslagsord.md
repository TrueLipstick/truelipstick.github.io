# GitHub Pages, uppslagsord

Poster för Tech Thesaurus for Humanists. Termerna länkar till varandra: läs den du behöver och följ trådarna. Korslänkarna är gjorda för hur GitHub renderar markdown.

---

### Branch

**Kort:** en parallell version av filerna i ett [repo](#repo); `main` är huvudspåret.

En gren låter dig arbeta på ändringar vid sidan av utan att röra det som är publicerat. För en liten sida räcker det gott att hålla sig till `main`, den gren [GitHub Pages](#github-pages) publicerar från som standard. Grenar blir intressanta först när flera arbetar samtidigt, eller när du vill prova något utan risk.

*Se även:* [Commit](#commit), [Push](#push), [GitHub Pages](#github-pages).

### Commit

**Kort:** en sparad, daterad version av en ändring.

När du ändrar en fil och gör en commit fryser du ned ett ögonblick i historiken, med tidpunkt och en kort beskrivning. Du kan alltid gå tillbaka till en tidigare commit, så ingenting försvinner av misstag. Tänk på det som textkritiska varianter av en handskrift: varje version finns kvar och går att jämföra. En commit syns på sajten först när du [pushar](#push) den.

*Se även:* [Push](#push), [Branch](#branch), [Repo](#repo).

### GitHub Pages

**Kort:** en gratis funktion som publicerar filerna i ett [repo](#repo) som en webbsida på en riktig adress.

Pages tar dina färdiga filer och serverar dem som en [statisk sida](#statisk-sida). Döper du repot till `dittanvändarnamn.github.io` hamnar sidan på just den adressen. Det är ett av de enklaste sätten att få en egen plats på nätet utan webbyrå eller månadshyra. En sak att veta från start: på ett gratiskonto är sidan alltid [offentlig](#offentlig-olistad-privat).

*Se även:* [Statisk sida](#statisk-sida), [Repo](#repo), [index.html](#indexhtml), [Jekyll](#jekyll), [Offentlig, olistad, privat](#offentlig-olistad-privat).

### index.html

**Kort:** standardnamnet på en mapps förstasida.

I varje mapp är det filen `index.html` som webbläsaren visar om besökaren inte pekar ut någon annan fil. Det är en gammal konvention som hela webben vilar på, och som [GitHub Pages](#github-pages) följer. Lägg din förstasida där, så fungerar adressen utan att du behöver skriva ut filnamnet.

*Se även:* [GitHub Pages](#github-pages), [Statisk sida](#statisk-sida).

### Jekyll

**Kort:** en statisk webbplatsgenerator som [GitHub Pages](#github-pages) kör automatiskt.

En generator bygger en färdig sajt åt dig: du skriver innehåll i Markdown plus en mall för utseendet, och Jekyll sätter ihop alltihop till statiska HTML-sidor. Praktiskt när många sidor ska dela samma form, som en blogg eller dokumentation. Den skrevs i programspråket Ruby av en av GitHubs grundare runt 2008, och namnet anspelar på Stevensons *Dr Jekyll och Mr Hyde*, passande för något vars hela uppgift är att förvandla råtext till färdig sajt. Haken: GitHub Pages skickar dina filer genom Jekyll vare sig du bett om det eller inte, och generatorn har vanor som kan överraska, till exempel att den hoppar över filer och mappar vars namn börjar med understreck. Behöver du ingen generator, se [.nojekyll](#nojekyll).

*Se även:* [.nojekyll](#nojekyll), [GitHub Pages](#github-pages), [Statisk sida](#statisk-sida).

### noindex

**Kort:** en instruktion som ber sökmotorer låta bli att lista en sida.

Raden `<meta name="robots" content="noindex">` i sidans `<head>` säger till sökmotorernas robotar att inte ta med sidan i sina register. Hyfsade robotar lyder, en illvillig skrapare struntar i den. Den gör alltså sidan svårare att hitta via Google, inte omöjlig att nå för den som redan har adressen.

*Se även:* [Offentlig, olistad, privat](#offentlig-olistad-privat).

### .nojekyll

**Kort:** en tom fil som säger åt [GitHub Pages](#github-pages) att hoppa över [Jekyll](#jekyll)-steget.

Lägger du en fil som heter `.nojekyll` i repots rot serveras dina filer exakt som de ligger, utan att gå genom generatorn. Det är vad du vill när sidan är handskriven ren HTML: ingenting görs om eller trollas bort bakom ryggen på dig, och en mapp vars namn börjar med understreck publiceras som vanligt. Filen behöver inget innehåll, det räcker att den finns.

*Se även:* [Jekyll](#jekyll), [GitHub Pages](#github-pages).

### Offentlig, olistad, privat

**Kort:** tre saker som lätt blandas ihop, fast de inte är samma.

*Offentlig* är vad en [GitHub Pages](#github-pages)-sida alltid är på ett gratiskonto: vem som helst med adressen kommer in, och det finns ingen lösenordsspärr. *Olistad* betyder att du inte länkar till sidan och ger den ett svårgissat filnamn, så ingen råkar snubbla in, men den är fortfarande nåbar för den som har länken. *Privat*, i meningen att besökaren måste bevisa vem hon är, klarar inte Pages; det kräver en tjänst med inloggning. Sammanfattat: olistat är inte privat.

*Se även:* [noindex](#noindex), [GitHub Pages](#github-pages).

### Push

**Kort:** att skicka upp dina sparade [commits](#commit) till GitHub.

En commit sparas först i ditt eget arbete; pushen är när den når GitHub och, för en Pages-sida, byggs om och blir synlig på nätet. Innan du pushar har omvärlden inte sett ändringen.

*Se även:* [Commit](#commit), [GitHub Pages](#github-pages).

### Repo

**Kort:** ett förvar (repository), en samling filer som hör ihop, med historik.

Repot är grundenheten på GitHub: en mapp med allt som hör till ett projekt, plus hela historiken av [commits](#commit). En [GitHub Pages](#github-pages)-sida bor i ett repo, och varje fil du lägger där kan bli en del av sajten.

*Se även:* [GitHub Pages](#github-pages), [Commit](#commit), [Branch](#branch).

### Statisk sida

**Kort:** färdiga filer som skickas ut som de är, utan en server som räknar i stunden.

Tänk på skillnaden mellan en tryckt affisch och ett samtal: affischen är densamma för alla, samtalet svarar olika beroende på vem som frågar. En statisk sida är affischen. Du kan visa text, bilder och länkar, men inte ta emot inloggningar eller spara inskickade uppgifter. För en humanist är enkelheten ofta en fördel: sidan är billig, hållbar och läsbar långt in i framtiden.

*Se även:* [GitHub Pages](#github-pages), [index.html](#indexhtml).

---

## Kortaste vägen till en sida

1. Skaffa ett konto på github.com.
2. Skapa ett [repo](#repo), gärna döpt till `dittanvändarnamn.github.io`.
3. Lägg en [`index.html`](#indexhtml) i det.
4. Settings → Pages → publicera från `main` och mappen `/ (root)`.
5. Vänta en minut. Adressen är live.

---

*Del av Tech Thesaurus for Humanists.*

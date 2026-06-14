# GitHub Pages för humanister

### En sida på nätet, utan webbyrå och utan månadshyra

Du vill ha en liten plats på nätet: någonstans att lägga upp en text, en tidslinje, en bild, och en adress att dela med några utvalda. Du vill inte anlita en webbyrå, inte betala månadshyra till en plattform, och helst inte lära dig ett helt yrke först. GitHub Pages är ett av de enklaste sätten att få just det. Den här texten förklarar inte bara hur, utan varför det fungerar som det gör, för det är förståelsen som gör att du vågar och vet vad du ger dig in i.

## Vad det faktiskt är

GitHub är i grunden ett arkiv för filer. En samling filer som hör ihop kallas ett *repo* (kortform för repository, alltså ett förvar). GitHub Pages är en gratis funktion som tar filerna i ett sådant förvar och publicerar dem som en webbsida på en riktig adress.

Sidan är *statisk*. Det betyder att den består av färdiga filer som skickas ut precis som de ligger, utan någon dator som räknar ut något i stunden. Tänk på skillnaden mellan en tryckt affisch och ett samtal: affischen är densamma för alla som läser den, samtalet svarar olika beroende på vem som frågar. En statisk sida är affischen. Det låter som en begränsning, och ibland är det det (du kan inte ha inloggning eller en databas som minns besökare), men för en humanist är det ofta en gåva. Sidan blir enkel, billig, hållbar och fullständigt din. Filerna går att läsa, spara och begripa om tjugo år, till skillnad från innehåll inlåst i ett plattformssystem som kan ändras eller läggas ner under dina fötter.

## Kortaste vägen till en sida

1. Skaffa ett konto på github.com om du inte redan har ett.
2. Skapa ett nytt repo. Vill du ha den renaste adressen, döp det till `dittanvändarnamn.github.io`. Då blir sidan `https://dittanvändarnamn.github.io`.
3. Lägg en fil som heter `index.html` i repot. Det är förstasidan. Den kan innehålla vad som helst, även en färdig HTML-sida du fått skapad åt dig.
4. Gå till repots **Settings**, därefter **Pages**, och välj att publicera från din huvudgren (`main`) och mappen `/ (root)`.
5. Vänta en minut. Adressen är live.

Det är hela grundreceptet. Allt därutöver, fler sidor, formgivning, mappar, är bara fler filer i samma förvar.

## Vad du behöver tänka på, och varför

**Allt är offentligt.** På ett gratiskonto måste repot vara publikt, och den publicerade sidan är alltid öppen för vem som helst med adressen. Det finns ingen lösenordsspärr. Varför: gratisnivån är tänkt för öppet material. Vill du dela något halvprivat kan du låta bli att länka till sidan och ge den ett svårgissat filnamn, men *olistat är inte samma sak som privat*. Behöver du en riktig spärr får du leta efter en tjänst med inloggning.

**Statiskt, alltså inga formulär eller databaser.** Du kan visa text, bilder, länkar och sådant som körs i läsarens egen webbläsare. Du kan inte ta emot inloggningar eller spara inskickade uppgifter. Varför: det finns ingen server som tänker åt dig, bara filer som skickas ut som de är.

**Filnamn på enkel engelska.** Undvik å, ä, ö och mellanslag i fil- och mappnamn. Skriv `redaktorsnoter`, inte `redaktörsnoter`. Varför: webbadresser kodar om specialtecken till oläsligt klotter (`%C3%B6` och liknande). Den svenska stavningen hör hemma i den synliga texten, inte i adressen.

**`index.html` är alltid förstasidan.** I varje mapp är det den filen webbläsaren visar om man inte pekar ut någon annan. Varför: det är en gammal konvention som hela webben vilar på, och GitHub Pages följer den.

**Varje sparad ändring är en version.** När du sparar en ändring (på GitHubs språk en *commit*) och skickar upp den byggs sidan om. Du kan alltid gå tillbaka till en tidigare version. Varför: GitHub är byggt för att spåra ändringar över tid, ungefär som textkritiska varianter av en handskrift. Ingenting försvinner av misstag.

**Vill du hålla sidan utanför Google?** Lägg raden `<meta name="robots" content="noindex">` i sidans `<head>`. Varför: det är en artig instruktion till sökmotorernas robotar att inte ta med sidan i sökresultaten. Hyfsade robotar lyder, en illvillig skrapare struntar i den. Det gör sidan svårare att hitta, inte omöjlig att nå.

## Varför det här passar en humanist

Det fina är att begreppen inte är så främmande som de låter. Ett förvar är en samling. En commit är en daterad version. En publicering är skillnaden mellan handskriften i lådan och den tryckta upplagan. Du lär dig egentligen inte att programmera, du lär dig att ge ut, och du behåller nyckeln själv.

## Liten ordlista

- **Repo** (repository, förvar): en samling filer som hör ihop, med historik.
- **Commit:** en sparad, daterad version av en ändring.
- **Push:** att skicka upp dina sparade ändringar till GitHub.
- **Branch** (gren): en parallell version av filerna; `main` är huvudspåret.
- **Statisk sida:** färdiga filer som skickas ut som de är, utan server som räknar i stunden.
- **GitHub Pages:** funktionen som publicerar ett repos filer som en webbsida.
- **`index.html`:** standardnamnet på en mapps förstasida.
- **noindex:** en instruktion som ber sökmotorer låta bli att lista sidan.

---

*Del av Tech Thesaurus for Humanists.*

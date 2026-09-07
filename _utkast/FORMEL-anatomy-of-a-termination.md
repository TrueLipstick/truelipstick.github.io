```yaml
---
title: "FORMEL: Anatomy of a Termination"
created: 2026-09-04
modified: 2026-09-07T21:21:16+02:00
replaces: `_utkast/anatomy-termination-v4.py` och `_utkast/anatomy-termination-v3.svg` som kanonisk textkälla
author:
 - "🦞 Velvet"
model:
 - claude-opus-5 1m
editors:
 - "💄 Lipstick"
state: underlag för DESIGNSPEC `🦚 Greve Malcolm` och implementation `🐡 Futaba` / `🛰️ Kepler`
source: 
tags:
  - formel
    
actors:
 - "🦞 Velvet"
 - "🦚 Greve Malcolm"
 - "🐡 Futaba"
 - "🛰️ Kepler"
 - "💄 Lipstick"
notes: Den här filen ligger i `_utkast/`, som är gitignorerad och aldrig pushas. Fullständiga namn och privata fall får stå här. Vad som går ut i `handelser/` avgörs separat, se § Publiceringsomfattning.
---
```

# FORMEL: Anatomy of a Termination

---

## 🔬 Vad hypotesprövningen gav

Formeln testades mot ett fall 💄 Lotten inte är part i: Johan Grant och Externatet vid Lunds universitet, 2019 till 2020. Resultatet är **inte** en ren träff, och det är den viktigaste upptäckten i hela arbetet.

**Formeln föll isär i två delar, varav bara den ena generaliserar.**

| Del | Innehåll | Håller? |
| --- | -------- | ------- |
| **A. Ingången** | Vem som invände, och mot vad | ❌ Varierar. Ibland är target den som drar i nödbromsen (💄🍆, ⚜️🐿️, T), ibland den som någon annan invänder mot (Grant) |
| **B. Verkställandet** | Hur avlägsnandet genomförs | ✅ Identiskt i samtliga fyra fall |

Det betyder att sidans påstående ska handla om **B**, proceduren, inte om **A**, sakfrågan. Tre konsekvenser, alla till det bättre:

1. **Den blir svårare att avfärda.** En läsare som tycker att Grant borde ha lämnat kursen, eller att studenterna hade rätt i sak, kan ändå se att B såg likadant ut. Formeln uttalar sig inte om vem som hade rätt.
2. **Den skyddar dig.** Sidan hävdar inte att du och Grant är i samma situation moraliskt. Den hävdar att organisationerna gjorde samma sak procedurmässigt, vilket är ett kontrollerbart påstående.
3. **Den blir sann.** En formel som passade alla fyra fallen helt hade varit misstänkt. Att den sprack på precis den punkt där fallen faktiskt skiljer sig är vad som gör resten trovärdig.

### Falsifieringskriterium, satt i efterhand men uttalat

Jag noterar ärligt att jag satte kriteriet efter att ha läst fallet, inte före. Det är en svaghet. För framtida fall gäller därför detta, uttalat i förväg:

Ett fall **motsäger** formeln om det uppvisar minst tre av: target hördes innan beslutet fattades; den angivna orsaken var specifik och kontrollerbar; samma orsak framfördes i skrift och muntligt; en efterhandsprövning omfattade beslutet självt; det påstådda visade sig ha ett faktiskt värde större än noll vid kontroll.

Ett fall som uppvisar noll eller ett av dessa **stödjer** formeln. Två är obestämt.

---

## 🧬 Formeln, reviderad

### Del A — Ingången (varierar, ska redovisas som variabel)

**A1. Utgångsläget.** Inom `[organisation]` bedrivs verksamhet eller praxis som någon har invändningar mot.

**A2. Invändningen.** Någon påtalar något. Här går fallen isär, och det är hela poängen:

| Fall | Vem invände | Mot vad | Target är |
| ---- | ----------- | ------- | --------- |
| 💄🍆 Folkvett | 💄 LK och 🍆 DK | Att fyra styrelseledamöter, inklusive ordföranden, tagit partipolitisk ställning i Sydsvenskan i strid med stadgarnas § 1 om partipolitisk obundenhet | den som invände |
| ⚜️🐿️ Konsultuppdraget | 🐿️ Puff | Ny konsult ville frångå den av ledningen beslutade arbetsgången | den som invände |
| T Hellstadius | T | Avvikande siffror i redovisningen, korrekt rapporterade | den som invände |
| Johan Grant | Studenter | Kursmomentets innehåll och metod | **den som invändes mot** |

Formeln säger ingenting om vem som hade rätt i A2. Den börjar gälla vid B1.

### Del B — Verkställandet (invariant i samtliga fyra fall)

**B1. Prestigeläget.** Sakfrågan blir en personfråga. Vad invändningen gällde nämns allt mer sällan.

🎯 **Bäst belagda steget i hela formeln, och det är aktörens egna ord.** SOH uppmanade LK och DK två gånger i skrift att gå till styrelsen med kritiken (K10). De gjorde det (K11). Sju dagar senare beskriver han samma handling som något annat (K17, SMS 28 april 09:37):

> "rekommenderade jag er att kontakta styrelsen för en diskussion … Tyvärr valde ni i stället att söka konfrontation genom att meddela er avsikt att publicera en mot styrelsen starkt kritisk text."

Övergången från sakfråga till personfråga ligger i en enda mening, skriven av den som gjorde den. Ingen tolkning behövs.

**B2. Ensidig beredning.** `[beslutsfattare]` hör den ena parten. Den andra anropas aldrig.

**B3. Kapplöpningen.** *Ny, på 💄 Lottens förslag.* Beslutet fattas innan target hunnit svara på anklagelsen. Det är inte slarv, det är ordningsföljden: ett informerat beslut hade varit ett annat beslut.

- ⚜️🐿️: beskedet kom **15 minuter** efter det hetlevrade utbytet.
- Grant: begärde upprepade gånger konkreta förklaringar och fick inga. Vid samtalet 10 december 2019 antog studierektorn att diskriminering förekommit, utan att precisera.
- 💄🍆: beslutet 3 maj fattades utan att LK och DK rådfrågats, dokumenterat av DK samma kväll: *"Om detta verkligen är hela styrelsens beslut måste vi få veta konkret vad som ligger bakom det. Och likaså varför vi inte rådfrågats."* (K3)

**B4. Beslutet.** Uppdraget avslutas. Ingen sakligt formulerad grund anges vid tillfället.

**B5. Den skriftliga orsaken.** Vag, förvaltningsmässig, formulerad så att den inte går att bemöta. Den överlever granskning genom att inte påstå något kontrollerbart.

**B6. Den viskade orsaken.** *Ny.* Parallellt löper en andra kanal: specifik, grov, muntlig, aldrig nedskriven och aldrig framförd till target. Den skriftliga orsaken är oemotsäglig därför att den är tom. Den viskade är oemotsäglig därför att den aldrig sägs högt inför den som anklagas.

**B7. Efterhandsprövningen.** *Ny, upptäckt i Grant-fallet, verifierad mot primärkällan.* En formell prövning genomförs i efterhand. Dess avgränsning utesluter beslutet självt. Utfallet åberopas sedan som friande.

⚠️ **Formuleras försiktigt.** Den svaga versionen av påståendet är att avgränsningen riggades. Den håller inte, och behövs inte. Den starka versionen är att **varje enskild avgränsning är rimlig och den sammanlagda effekten är att ingen instans prövar huvudsaken.**

I Grant-fallet är det dokumenterat i tre led (P 2020/1239, s. 3). Utredaren avgränsar bort klagomålet om utebliven förlängning, eftersom det inte faller inom kriterierna för kränkande särbehandling enligt AFS 2015:4. Avgränsar bort studenternas klagomål, eftersom studenter har rätt att klaga. Avgränsar bort studierektorns beslut, eftersom besluten ligger inom hens mandat. Var och en av de tre är juridiskt-tekniskt försvarbar. Kvar att utreda blir punkt 3 och 4 av Grants fyra, alltså skvallret och medierapporteringen, medan punkt 1 och 2, avsättningen och omöjligheten att försvara sig, aldrig prövas av någon.

Samma mekanism i ditt fall, med annan apparat: "arbetsmiljö" åberopas i en organisation som inte lyder under arbetsmiljölagstiftningen. Kategorin är vald, avsiktligt eller inte, så att det inte finns något forum med jurisdiktion.

Det är den formulering som överlever en motpart som läser för att hitta felet.

**B8. Kontrollvärdet.** När det påstådda faktiskt mäts blir det noll.

---

## 📊 Materialet, per fall

### 💄🍆 Folkvettredaktionen, VoF, 2026

**Källnycklar, kontrollerade 2026-09-04.** Samtliga citat nedan är avskrivna ur transkriberingarna, med message_id där sådant är återfört.

| Nyckel | Fil (`folkvettkonflikten-2026/02-transkriberingar/styrelsen/`) | message_id |
| ------ | ---- | ---------- |
| **K1** | `20260503-1828-mail-LT-LK-Information-fran-styrelsen.md` | `<CAOXY4pSSYjC9-Crs7wfASzXJxkoGh7S6U_d7a5F_9+zgQ0tmCA@mail.gmail.com>` |
| **K2** | `20260503-1830-mail-LT-DK-Information-fran-styrelsen.md`, Mail 2 | *ej nycklad, saknar motsvarighet i indexerad .eml* |
| **K3** | `20260503-1830-mail-LT-DK-Information-fran-styrelsen.md`, Mail 3 (DK:s svar 20:40) | `<967B04C3-6B0B-415B-A642-2FE32BA4F3FE@katzkbt.se>` |
| **K4** | `20260606-1702-mail-LT-DK-angaende-brev-till-styrelsen.md` | `<CEE09622-ABD8-430D-B214-49F11C324005@vof.se>` |

#### ⚠️ RÄTTELSE 2026-09-05: vad invändningen faktiskt gällde

Tidigare versioner av det här dokumentet angav underbemanning som utlösande faktor. **Det är fel.** Rättat efter `LipstickObsidianVaults/Folkvettkonflikten/Folkvettkonflikten/Tidslinjer/faktablad-kort-skaggen-UTKAST.md`.

**A1 Utgångsläget.** 10 april 2026 publicerar fyra styrelseledamöter en debattartikel i Sydsvenskan. Ansvarig utgivare SOH skickar den till redaktionen som "notisunderlag".

**A2 Invändningen.** LK och DK skriver en kritisk artikel för Folkvett. Kritiken gäller **inte** sakfrågan (straffreformutredningen) utan principen:

> "att en partipolitiskt obunden förening som Vetenskap och Folkbildning inte bör ta ställning i frågor som ytterst avgörs av politiska värderingar snarare än av vetenskaplig kunskap"

Det åberopade stadgerummet är **§ 1**, sista raden:

> "Föreningen är religiöst och partipolitiskt obunden."

**Och de följer ordningen hela vägen.** 17 april skickas artikeln till ansvarig utgivare för läsning. 21 april svarar han, **håller med om att VoF måste vara politiskt obundet**, och ger konkreta råd om utformningen. 24 april skickar de en justerad version till redaktionen, och SOH kompletterar med villkor för publicering: ordning, placering, nummerplan. 26 april tar han tillbaka alltihop i ett kort mejl.

**Detta förändrar formelns Del A för det här fallet, och stärker Del B.** Target är den som invände, precis som hos ⚜️🐿️ och T, men här är invändningen dessutom **en åberopad regel i föreningens egen grundparagraf**, framförd i föreskriven ordning, med den ansvarige utgivarens skriftliga medhåll i sakfrågan.

#### ✅ SOH:s roll, avgjord mot primärkälla 2026-09-05

**K8.** `dan-larhammar/20260606-1426-mail-DK-DL-LK-brev-till-styrelsen.md`, sex meddelanden, samtliga nycklade. Dan Larhammars förtydligande, 6 juni 2026 11:09 (`<b28050ab4b329a41085e01b99148c953@vof.se>`) och 12:32 (`<5445787f919a098091113b0f703cac18@vof.se>`).

**Vad som är avfärdat.** DL, rakt av, två gånger:

> "Inte inblandad i debattartikeln i Sydsvenskan."

Och: SOH "Ville inte vara med och skriva en generell artikel för Folkvett om vetenskapsbaserat beslutsfattande."

**Vad som faktiskt hände**, enligt DL:s egen redogörelse:

| Datum | Vad | Vem till vem |
| ----- | --- | ------------ |
| 12 apr | DL mejlar styrelsen, SOH och Albin om att ministrar och politiker på båda sidor avfärdar vetenskapsbaserad sakkunskap | DL → styrelsen m.fl. |
| 13 apr | SOH svarar DL: *"Kan detta bli en artikel i Folkvett?"* | **SOH → DL** |
| 13 apr | DL svarar att det kan bli en analyserande text, och att *"En sådan artikel ska väl helst skrivas av dem som skrev VoF:s text för Sydsvenskan."* | DL → SOH |
| — | SOH svarar *"Bra idé"* och att han **själv inte är lämpad som undertecknare eftersom han varit politiskt aktiv**, och att en sådan artikel bör skrivas av *"personer vars utsager inte kan avfärdas som politiska partisinlägg"* | SOH → DL |

DL:s sammanfattning: *"Sven Oves kommentar gällde alltså fortsättning i Folkvett på ämnet vetenskapsbaserat beslutsfattande och hade inte direkt med debattartikeln Sydsvenskan att göra."*

🔴 **Tre påståenden ska bort ur underlaget, inte bara ur sidan.**

1. **"SOH var inblandad i Sydsvenskan-artikeln."** Motbevisat av DL, två gånger.
2. ~~**"SOH skrev 13 april till ordförande LT och föreslog en version av artikeln till Folkvett."**~~ 🔴 **RÄTTAD IGEN 2026-09-05. Punkt 1b var i allt väsentligt korrekt och min invändning mot den var fel.**

   K24, DL:s återgivning av den interna e-postväxlingen (`dan-larhammar/20260504-2027-mail-DK-DL-sydsvenskan.md`, DL till DK 1 maj 17:27), citerar SOH till DL den 13 april:

   > "Bra idé. **Jag har just skrivit till Lina om ditt förslag.** Själv är jag ingen lämpad undertecknare eftersom jag är politiskt väldefinierad (medlem i s). Bättre att detta görs av personer vars utsagor inte kan avfärdas som politiska partsinlägg."

   SOH skrev alltså till ordföranden samma dag om förslaget. Kvarstående precisering: förslaget gällde vid det laget **DL:s idé om en ny analyserande text** om vetenskapsbaserat beslutsfattande, inte en återpublicering av Sydsvenskan-artikeln. Återpubliceringen dyker upp först i publiceringsplanen 24 april (K22).
3. **"Han bestämde sig för att återpublicera den."** LK till JL samma dag (K8, msg 6). Det är LK:s karakteristik och den motsägs av DL:s redogörelse. Får inte stå på sidan.

✅ **Det som står kvar är starkare än det som föll.** SOH avböjde att underteckna en Folkvett-artikel på ämnet med motiveringen att han varit politiskt aktiv, och att sådana texter bör skrivas av personer vars utsagor inte kan avfärdas som partiinlägg. **Det är exakt den princip LK och DK åberopade i sin artikel**, uttalad av ansvarig utgivare själv, tretton dagar innan han drog tillbaka publiceringen av deras text.

Den juxtapositionen är faktisk, kontrollerbar och kräver inget påstående om avsikt. Den är sidans bästa material om SOH, och den blev tillgänglig först när det överdrivna påståendet togs bort.

⚠️ **Härkomst.** SOH:s ord är återgivna av DL i mejl till DK och LK. Kedjan är SOH → DL → K8. Skriv "enligt Dan Larhammar", aldrig som direktcitat av SOH.

#### 📇 April-förloppet, läst och nycklat 2026-09-05

**K9. 10 april 09:07.** SOH → LK och `redfive@vof.se`. `arkiv/20260410-0907-mail-SOH-LK-notisunderlag.md`, `<E4555333-AB5D-46A9-8B78-5595932EEAF6@kth.se>`.

Ämnesrad: **"Notisunderlag"**. Bilaga: Sydsvenskan-artikeln som PDF. **Brödtexten är tom.** Ingen kommentar, ingen kontext, inget förslag.

#### 🔴 Kronologin 10 till 13 april, rättad. K24.

`dan-larhammar/20260504-2027-mail-DK-DL-sydsvenskan.md`, DL till DK 1 maj 17:27, som återger styrelsens interna e-postväxling. Tre lager, ytterst DK till LK 4 maj 20:27, `<751C0C01-3364-4374-B7D1-C8693CB10041@katzkbt.se>`.

⚠️ **💄 Lottens ordningsföljd är omvänd och måste rättas innan den används.** Hon uppger att SOH bröt ut en tråd med DL och *därefter* skickade artikeln till redaktionen som notisunderlag. Materialet visar motsatsen.

| Tid | Vad | Vem |
| --- | --- | --- |
| 10 apr 08:17 | Albin meddelar **styrelsen och Sven Ove** att artikeln publicerats | Albin → styrelsen + SOH |
| **10 apr 09:07** | **"Notisunderlag" till redaktionen. Tom brödtext.** 50 minuter senare | SOH → LK + redfive |
| 12 apr | DL svarar alla med sitt tema om ministrar som avfärdar sakkunskap | DL → alla |
| 13 apr | *"Bra! Kan detta bli en artikel i Folkvett?"* | **SOH → DL** |
| 13 apr | DL: ja, och *"En sådan artikel ska väl helst skrivas av dem som skrev VoF:s text för Sydsvenskan."* | DL → SOH |
| 13 apr | *"Bra idé. Jag har just skrivit till Lina om ditt förslag."* | SOH → DL, och SOH → LT |
| **24 apr** | **Första gången redaktionen får veta att Sydsvenskan-artikeln kan ha en plats i Folkvett** | SOH → redfive (K22) |

✅ **Den substantiella poängen står kvar, och blir exaktare än i Lottens version.** SOH är inte styrelseledamot men sitter i styrelsens e-postloop. Han skickar artikeln till redaktionen utan ett ord. Tre dagar senare resonerar han med en **styrelseledamot, inte en redaktör**, om huruvida ämnet kan bli en Folkvett-artikel, och skriver till ordföranden om det. Redaktionen får veta ingenting om detta. **Elva dagar senare** kommer publiceringsplanen, och först då hör redaktionen talas om saken.

Skriv alltså inte "innan han skickade notisunderlaget". Skriv: notisunderlaget kom först, tomt, och det som sedan diskuterades om Folkvetts innehåll gick mellan ansvarig utgivare, en styrelseledamot och ordföranden i elva dagar utan att redaktionen informerades.

⚠️ **Evidensnivå.** Citaten av SOH och DL är DL:s återgivning av sin egen e-postväxling, vidarebefordrad av DK. DL citerar sig själv och SOH ur mejl han själv hade. Starkare än hörsägen, svagare än originalmejlen. **Originalen bör begäras eller sökas** om detta ska bära vikt på sidan.

⚠️ Notera också DK:s egen justering 4 maj: *"Jag misstog mig lite. S O tycks bara i efterhand varit involverad, men han är medlem i S."* Han rättade sig själv redan då.

**K13. Sydsvenskan-artikelns undertecknare**, ur `redaktionen/20260424-0756-mail-LK-R-debattartikeln-i-sydsvenskan.md`, `<893F9F34-458B-B846-A553-A7FD61A0DF61@hxcore.ol>`:

> Lina Tebbla, ordförande · Amalia Juneström, sekreterare · Albin Larsson, styrelseledamot · Mikael Andersson, styrelseledamot

**Ordföranden är en av de fyra.** Dokumenterat, i artikelns egen byline. SOH är inte bland dem, konsekvent med K8.

**K10. 21 april 23:03.** SOH → DK och LK. `_inkommande/_bred-sok-DK-Kvartal-20260814/20260421-2303-mail-SOH-DK-debattartikeln.md`. **Detta är sidans viktigaste enskilda dokument efter beskedet självt.**

SOH ger dem rätt i principen:

> "Jag håller livligt med om att VoF är och måste vara en 'religiöst och politiskt obunden' organisation."

Och han uppmanar dem, **två gånger i samma mejl**, att gå till styrelsen med kritiken:

> "Detta behöver diskuteras i styrelsen, och jag tycker därför att det vore bra om ni framför er kritik till styrelsen."

> "Vilket är ett gott skäl till att ni hör av er till styrelsen."

**De gjorde exakt det de blev tillsagda att göra, av ansvarig utgivare, i skrift.** Tolv dagar senare var de ute. Det behöver ingen tolkning och inget påstående om avsikt.

**K11. 23 april 12:04.** DK → SOH, kopia LK. Samma tråd som K10. DK redovisar att de tagit bort källhänvisningsargumentet efter SOH:s råd, och skriver:

> "Vår tanke är att nu skicka vår artikel till styrelsen och erbjuda dem att replikera. Vi måste kunna ha en öppen debatt om föreningen. Vi kommer också att be de andra redaktionsmedlemmarna att titta på artikeln. Och du som ansvarig utgivare måste naturligtvis titta igenom artikeln."

Belägg för att ordningen följdes och att SOH:s roll som ansvarig utgivare erkändes uttryckligen.

**K12. 26 april 21:10.** SOH → DK, kopia `redfive@vof.se`. `soh/20260426-2110-mail-SOH-DK-redfive-slutreplik.md`. Hela meddelandet:

> "Folkvett är organ för föreningen Vetenskap och Folkbildning. Detta innebär att om Folkvett publicerar kritik mot föreningen så publiceras i samma nummer ett svar från styrelsen, som därmed får sista ordet. / Sven Ove"

DK svarar 22:36: *"Jaha?"* Och 22:44 med den sakliga invändningen: *"Enligt publicistisk sed har de som initierat debatten sista ordet. Att Folkvett är ett organ för föreningen, som också har en styrelse, förändrar väl inte detta?"*

⚠️ **26 april gällde bara slutrepliken.** Uttaget av själva artikeln kommer dagen efter, se K14. De två stegen ska hållas isär, eftersom mellanrummet mellan dem är en del av mönstret.

**K14. 27 april 12:40.** SOH → DK. `<ED74053E-9E8F-4A24-A5EA-C445976FF82C@kth.se>`. Samma fil, rad 215 och framåt.

> "Förklaring om 'sista ordet': SDS-artikeln var en del av styrelsearbetet och uttrycker föreningens ståndpunkt. Föreningen har sista ordet i en debatt i Folkvett, som är organ för föreningen.
> Styrelsen har just fått Dans och Lottens text. Styrelsen bör få god tid på sig att svara.
> **Som ansvarig utgivare har jag beslutat att vi nu går vidare med det kraftigt försenade nummer 1, och att Dans och Lottens text inte ska ingå i det numret.**"

**K15. 27 april 19:59.** DK → `redfive@vof.se`. `<FFCAD787-F980-4CD6-BCB2-12607621F4DD@katzkbt.se>`.

> "Varför skall artikeln plötsligt inte ingå i kommande Folkvett? **Jag, och jag tror att även Lotten, var beredda att böja oss för ansvarig utgivares önskan att inte tillåta oss ett repliksvar.** Men att artikeln nu lyfts ut förstår jag inte."

Och den principiella invändningen, som är värd att citera i sig:

> "Jag vill också påpeka att styrelsen inte är föreningen. Styrelsen utses av föreningens medlemmar. Medlemmarna är föreningen. Folkvett är vår medlemstidning, inte styrelsens organ."

**K16. 28 april 08:18.** SOH → DK. Hela meddelandet:

> "Som jag redan har sagt: Nu måste vi fokusera på vårt uppdrag. Det handlar nu om att få färdigt det kraftigt försenade nummer 1. Hanteringen av er text får anstå. / Sven Ove"

**K17. SMS 28 april 09:37.** SOH → DK. `soh/20260428-0824-sms-DK-SOH.md`, transkriberad ur skärmdumpar från DK:s telefon. **Detta är SOH:s eget angivna skäl, i skrift, förstahands:**

> "När du och Lotten visade mig er text rekommenderade jag er att kontakta styrelsen för en diskussion. Jag hade förhoppningen att en sådan diskussion skulle vara till ömsesidig nytta. **Tyvärr valde ni i stället att söka konfrontation genom att meddela er avsikt att publicera en mot styrelsen starkt kritisk text.** Denna konfrontatoriska situation är inget som kan lösas mellan dig och mig."

🎯 **Detta är B1, prestigeläget, uttalat av aktören själv.** Han rekommenderade dem att kontakta styrelsen (K10, två gånger). De kontaktade styrelsen och erbjöd replik (K11). Han beskriver samma handling som att "söka konfrontation". Sakfrågan blir en personfråga, och övergången är dokumenterad i en enda mening från den som gjorde den.

**K18. Samma SMS-tråd, DK:s obesvarade svar.** DK anger att de tidigare fått klartecken:

> "Vi hade också tidigare fått klartecken av dig att publicera texten med ett svar från styrelsen. Diskussionen som uppstod sedan mellan dig och oss var om vi skulle ha replikrätt på deras svar. Vi var beredda att acceptera att släppa den replikrätten som vi ansåg oss ha rätt till. Sedan får vi ett besked från dig att vår artikel i stället lyfts ur från nr 1."

> "att vägra prata med mig när jag vill lösa situationen är inte ett särskilt framkomligt spår"

Transkriberingen noterar: **SOH svarade inte.** Och samma dag 14:03 mejlar han LK: *"Hej! Hur är läget med nummer 1?"* (K19, `soh/20260428-1403-mail-SOH-LK-Folkvett.md`).

#### 🔄 Rättad sekvens 21 till 28 april

| Datum | Vad | Nyckel |
| ----- | --- | ------ |
| 21 apr 23:03 | SOH håller med i principen, uppmanar **två gånger** att gå till styrelsen | K10 |
| 24 apr | Artikeln skickas till styrelsen med erbjudande om replik | K11 |
| 26 apr 21:10 | SOH: styrelsen får sista ordet. **Slutrepliken**, inte artikeln | K12 |
| 26 apr kväll | DK skickar flera mejl som han dagen efter ber om ursäkt för som "dumma och ogenomtänkta" | K17-tråden |
| 27 apr 12:40 | SOH: **artikeln ska inte ingå i nummer 1** | K14 |
| 27 apr 17:22 | DK ber om ursäkt per SMS, erbjuder samtal | K17-tråden |
| 27 apr 19:59 | DK: vi hade accepterat att mista slutrepliken, men uttaget förstår vi inte | K15 |
| 28 apr 08:18 | SOH: "Hanteringen av er text får anstå" | K16 |
| 28 apr 09:37 | SOH: ni "valde att söka konfrontation" | K17 |
| 28 apr | DK:s svar förblir obesvarat | K18 |
| 28 apr 14:03 | SOH till LK: "Hur är läget med nummer 1?" | K19 |
| 3 maj | Beslutet | K1, K2 |

⚠️ **Redovisa DK:s ursäkt, och redovisa den rätt.** Han bad 27 april 17:22 om ursäkt för sina mejl kvällen innan: *"Vill be om ursäkt för dumma och ogenomtänkta mail igår. Förstår att det är en knepig situation. Om du vill kan vi pratas vid i morgon."*

**DK hade då inte läst mejlet om att artikeln lyfts ut.** Belagt i samma SMS-tråd, hans nästa meddelande 19:58: *"Ser nu ditt mail från 12.40 idag. Nu behöver vi verkligen talas vid."*

Ordningen är alltså: uttaget 12:40 → ursäkten 17:22, skriven i okunskap om uttaget → upptäckten 19:58. Två slutsatser, båda till sidans fördel:

1. **Ursäkten kan inte ha orsakat uttaget.** Den kom fem timmar efter.
2. **Ursäkten var inte heller ett försök att blidka någon efter ett besked.** DK visste inte om beskedet. Han bad om ursäkt på eget initiativ för sin egen ton och erbjöd samtal.

Att utelämna ursäkten vore selektivt, och en motpart med tråden pekar på det. Att redovisa den med sin kronologi är starkare än att inte nämna den.

#### K20. Telefonsamtalet 28 april, och varför det ska användas försiktigt

`haendelseberattelser/20260509-note-LK-SOH-tel-28-april.md`. Samtal 16:55 till 17:18, 23 minuter. Nedtecknat av LK **elva dagar senare**, 9 maj.

🔴 **Citaten ur samtalet får inte publiceras.** Dokumentet säger det själv: *"Citat är ungefärliga, inte ordagranna."* Att återge en upprörd namngiven persons ord som citat, rekonstruerade elva dagar efteråt av motparten i samtalet, är den enskilt mest angripbara sak sidan skulle kunna göra. Det gäller särskilt **"De är överallt!"**, **"ÖVERALLT!"** och **"skit!"**. De stannar i arkivet.

✅ **Det som håller är strukturen och det samtida.**

**Samtida, skriftligt, samma kväll** (SMS till DK, återgivet i noten):

> "Samtalet gick helt åt helvete för övrigt"
> "Vet inte om prata är ordet så mycket som att försöka parera attacker"

**Belagt av motparten själv:** SOH:s mejl till redaktionen samma kväll 22:04, *"Efter ett samtal med Lotten idag övertar jag nummeransvaret"* (`soh/20260428-2204-mail-SOH-redfive-Nummeransvar-nr-1.md`). Det belägger att samtalet ägde rum och vad som följde av det.

🎯 **Och här är det verkligt värdefulla: uteblivet konkret skäl är nu belagt i tre oberoende led.**

| Vem | Hur | Utfall |
| --- | --- | ------ |
| DK | Skriftligt, mejl och SMS | Obesvarat [K16, K18] |
| LK | Telefon, 23 minuter, 28 april | Inget exempel [K20] |
| **DL, styrelseledamot, utomstående** | SOH tog upp saken med honom ca 22 maj | SOH **specificerade inte självmant**. DL frågade inte. [K21] |

#### 🔴 RÄTTELSE 2026-09-05: DL frågade aldrig

**K21.** `dan-larhammar/20260524-1103-tel-DK-DL.md`. Telefonsamtal DK och DL, 24 maj 11:03. **Inspelat av DK, transkriberat med Whisper large-v3 och korrekturläst mot ljudet av 💄 Lotten.** DL:s egna ord är alltså **förstahandsdokumenterade**, inte återgivna. Filens eget huvud graderar detta korrekt och skiljer ut vad DL i sin tur återger om SOH som ett förmedlat led.

Vad transkriptionen faktiskt säger, rad 91 till 106:

> **DL:** "så sa han att han tyckte att ni hade anklagat skribenterna för saker de inte skrivit. **Han gick inte in på vad det var.** Men att ni hade väl övertolkat det de skrev tyckte han."
>
> **DK:** "Ja, men han gav inga konkreta exempel?"
>
> **DL:** "**Nej, jag frågade inte om det** eftersom han var utomlands och så. Han var på konferens. Det var ganska sent på kvällen också."

**Två fel rättas här, ett mitt och ett i arkivet.**

Mitt: jag skrev att DL frågade oberoende och fick samma icke-svar. **DL frågade aldrig.**

Arkivets: `haendelseberattelser/20260509-note-LK-SOH-tel-28-april.md` innehåller meningen *"När DL frågade SOH vad han menade att DK/LK hade övertolkat, gav SOH inget konkret exempel"*. Det stämmer inte mot inspelningen. **Noten bör rättas**, eftersom en inspelad och korrekturläst transkription slår en minnesbaserad sammanfattning. 💄 Lotten avgör, men lämnas det som det är ligger en motsägelse kvar i arkivet där en motpart kan hitta den.

✅ **Vad som ändå står kvar, och det är inte lite.** Anklagelsen framfördes **ospecificerad också när den inte var riktad till de anklagade**. SOH tog upp saken med en styrelseledamot och gick inte in på vad den bestod i. Påståendet är alltså ospecificerat både när man frågar (DK, LK) och när det framförs oombett till tredje part (DL).

Det är svagare än "tre personer frågade och fick inget", men det är sant, och det är fortfarande samma steg som i Grant-fallet, där han "begärde upprepade gånger konkreta förklaringar och fick inga".

⚠️ DL:s förklaring till varför han inte frågade, att SOH var utomlands på konferens och att det var sent på kvällen, ska redovisas om DL-ledet används. Att utelämna den vore att låta ett uteblivet svar se ut som ett vägrat svar.

#### 💡 Tillägg till formeln: åskådarna kommer i tre lägen

💄 Lotten läser kombinationen av ett starkt men ospecificerat påstående och en tunn förklaring till varför följdfrågan uteblev som att **ingen ville** gå närmare in på saken. Läsningen är rimlig. Den är också ett påstående om vad två personer ville, och den kan inte beläggas.

**Men den pekar på något som går att säga, och som gör formeln bättre.** Proceduren behöver ingen som vill något. Den behöver bara att den uppenbara följdfrågan är socialt dyr att ställa. Det räcker.

Materialet ger tre distinkta åskådarlägen, och alla tre är belagda:

| Läge | Vad som händer | Belägg |
| ---- | -------------- | ------ |
| **Invänder, ignoreras** | PJ och SL frågar på mötet, får inga klara besked, reserverar sig. Beslutet går igenom ändå | K5, K7 |
| **Frågar inte** | DL får ett starkt påstående, ställer inte följdfrågan, anger tid och plats som skäl | K21 |
| **Prövar, men i fel forum** | Grants utredning prövar det som ligger utanför beslutet | P 2020/1239 |

Det första är den populerade variabeln som aldrig läses. Det andra är den som aldrig sätts. Det tredje är den som läses av fel funktion.

**Kodkonsekvens:** `Bystander`-listan ska ha tre poster, inte två. Två med `reservation` satt och aldrig läst, en med `reservation=None` och en kommentar om att frågan aldrig ställdes. Det är exaktare och roligare än två.

⚠️ **Rättviseanmärkning som ska väga in innan DL beskrivs.** DL är inte en åskådare som höll tyst. Han **berättade** för DK vad SOH sagt, vilket är hela anledningen till att uppgiften finns. Och 6 juni rättade han självmant DK och LK på en punkt som gick **emot** deras version, nämligen att SOH inte varit inblandad i Sydsvenskan-artikeln [K8]. Den som skyddar en vän gör inte något av det.

Sidan ska därför inte antyda att han höll någon om ryggen. Den ska säga vad som hände: han fick ett ospecificerat påstående, ställde inte följdfrågan, och angav varför. Läsaren drar sin egen slutsats, precis som sidan låter läsaren göra överallt annars.

#### 📅 Belagt: DL hade arbetat på det samtalet i tre veckor

💄 Lottens invändning att DL "var inställd på att ställa frågor" är **inte** en tolkning. Den är dokumenterad, och den ändrar hur mycket hans förklaring väger.

| Datum | Vad | Källa |
| ----- | --- | ----- |
| 1 maj | DL till DK: *"Har du försökt nå Linda för att höra om hon har bra kontakt med Sven Ove?"* | `dan-larhammar/20260501-1010-sms-DK-DL.md` |
| 4 maj | DK: *"Det slår mig att, om man verkligen vill ta reda på vad som hänt, borde man få till ett samtal med Sven Ove."* DL: *"Jag uppmanade Lina att verkligen försöka få till ett sådant mellan Sven Ove och dig."* | `20260504-2302-mail-DK-DL-samtal-med-lina.md` |
| 11 maj | DL: *"Säg till om du vill att jag ska kontakta någon av Lina eller Sven Ove för att vädja om samtal och i så fall vilken."* Svar: *"Jag tror att det är bäst att börja med Sven Ove."* | `20260511-1700-sms-DK-DL.md` |
| ca 22 maj | Samtalet med SOH äger rum. Den centrala frågan ställs inte | K21 |

**Juxtapositionen är faktisk:** i tre veckor arbetade DL på att få till kontakt med SOH, och den 11 maj enades man om att börja just med honom. När kontakten sedan kom, ställdes inte frågan om vad anklagelsen bestod i, med hänvisning till att det var sent och att SOH var utomlands.

Sidan ska ställa de två uppgifterna intill varandra och inte skriva ut slutsatsen. Läsaren räknar själv.

⚠️ **Nyansering som ska med, annars är juxtapositionen orättvis.** DL:s uppdrag som han själv formulerade det 11 maj var att **vädja om ett samtal mellan SOH och DK**, alltså att medla, inte att själv förhöra SOH. Att han inte krävde specifikationer är förenligt med det uppdraget. Det är den invändning en motpart kommer med, och den är rimlig. Redovisa den.

#### ➕ Ett fjärde åskådarläge, hittat i samma genomgång

**Lovade fråga, återkom aldrig.** DK till DL 4 maj: *"Linda, som sade att hon skulle ta reda på vad Sven Ove hade blivit så arg av, har ännu inte återkommit till mig."*

Och 19 maj, DK till DL efter kontakt med SL:

> "Tydligen nämnde Linda Strand vid styrelsemötet att hon haft ett långt samtal med mig, men hon berättade ingenting om innehållet: inget om Sven Oves märkliga ändring av beslut, inget om att han trots upprepade försök från oss vägrat kommunicera, och framför allt, att jag kontaktat Linda för att be styrelsen om medling. Det enda styrelsemedlemmarna fick veta var en otydlig formulering om 'konflikt'."

Om det stämmer är det **B2 i sin renaste form**: en person som hade informationen, satt i rummet, och lät bli att förmedla den.

⚠️ **Evidensnivå: andrahands.** DK återger vad SL berättat. Ska det användas behöver det beläggas mot SL direkt, exempelvis i `staffan-luckander/`-materialet. **Öppen fråga.** Använd det inte förrän det är belagt; påståendet är allvarligt och riktar sig mot en namngiven person.

##### Vad som däremot är belagt om LSL, och räcker

Genomgång 2026-09-05 av `dk-lk/20260410-20260608-bubble-DK-LK.md`. `linda-strand-lundberg/` innehåller inget material från 2026; allt nedan är DK:s samtida rapportering till LK.

**Åtagandet, 3 maj 14:51**, alltså samma eftermiddag som styrelsemötet:

> "Pratat med Linda. Hon håller inte med oss i sak rörande artikeln, såklart. **Men hon blir den som kontaktar SO för att ta reda på varför han är så rasande.**" (rad 1020)

**Uteblivet svar, dokumenterat vid upprepade tillfällen:**

| Datum | Vad DK skriver | Rad |
| ----- | -------------- | --- |
| 4 maj | "Linda, som sade att hon skulle ta reda på vad Sven Ove hade blivit så arg av, har ännu inte återkommit till mig." | mail till DL |
| 3 maj 19:10 | "hon har inte hört av sig" | 1265 |
| senare | "Ingen reaktion från Linda?" | 2302 |

**Och per 💄 Lotten 2026-09-05: hon har fortfarande inte återkommit.** Fyra månader.

✅ **Det här är det renaste åskådarfallet i hela materialet, och det behöver ingen tolkning.** Någon åtog sig att ta reda på saken. Åtagandet är dokumenterat samtida. Svaret har inte kommit på fyra månader. Det är en frånvaro mot en **dokumenterad förväntan**, vilket är exakt den enda form av frånvaroargument husets regler tillåter.

🔴 **Men allt annat om LSL ska bort, och DK har redan gjort bedömningen åt oss.**

I chatten finns betydligt starkare påståenden: att hon "mörkade", att hon "lovade att ta reda på detta, något hon redan visste", att hon kunde "ljuga för mig och delta i en kupp mot oss" (rad 1251).

**DK klassade själv detta som spekulation och strök det** innan brevet gick till styrelsen:

> "Och min formulering om Linda visste jag själv var en spekulation, och tänkte att vi nog skulle ta bort." (rad 3577)

> "…tagit bort spekulationen om Linda…" (rad 3594)

Det är värt att notera för sin egen skull: **DK tillämpade exakt den disciplin sidan kräver, på eget initiativ, mitt under pågående konflikt.** Att sedan publicera det han själv strök vore att underkänna hans omdöme och att göra det formeln anklagar andra för.

Publicerbart om LSL: **ett åtagande och en frånvaro.** Ingenting om vad hon visste eller ville.

⚠️ **Källnyckelbrist.** Åtagandet vilar helt på DK:s samtida rapportering till LK. Det finns inget belägg direkt från LSL. Ska det publiceras bör det skrivas som det är: "en styrelseledamot åtog sig, enligt vad min kollega rapporterade samma dag, att ta reda på…". Det försvagar inte poängen, eftersom poängen är frånvaron.

⚠️ **Två saker ur noten som inte ska ut:** dödsfallet i familjen (samma skäl som tidigare), och LK:s eget avsnitt "Saker jag sade, som i backspegeln kanske inte bidrog till att lugna". Det senare är hederligt och talar för henne, men på en publik sida blir det material för den som vill läsa henne som stridslysten. **💄 Lotten avgör.** Min rekommendation är att utelämna det men behålla den korta självkritiska markeringen om bevisvärdet, som gör samma jobb utan att lämna ut något.

#### ✅ K22. Publiceringsplanen, 24 april 11:58. Frågan om "klartecken" är avgjord.

`soh/20260426-2110-mail-SOH-redfive-Fwd_Dans-och-Lottens-text.md`. SOH → **hela redaktionen** (`redfive@vof.se`), 24 april 2026 11:58, citerat i hans eget vidarebefordringsmejl 26 april 21:10, `<23BD59C6-4A12-4AAB-B00F-0B66728DC865@kth.se>`.

> "Dan och Lotten hade vänligheten att visa mig en tidigare version av sin text innan de skickade ut den till hela redaktionen. Jag bifogar nedan mitt svar till dem.
>
> Jag tycker att en publicering av denna text behöver utformas så att läsaren själv kan ta ställning. Då blir det tre texter i följande ordning: **(1) Återpublicering av artikeln i Sydsvenskan, (2) Dans och Lottens text, (3) styrelsens svar.** För att behålla fokus på det som vi alla i föreningen är överens om bör denna textmassa inte placeras först i numret efter ledaren, och ledaren bör förstås handla om något helt annat. **Publicering kan i så fall ske i nummer 1 eller 2.** Det vore tråkigt att ytterligare försena nummer 1."

**Skriv inte "klartecken", skriv det här.** Ansvarig utgivare lade fram en konkret publiceringsplan till hela redaktionen: tre texter, en ordning, en placeringsrestriktion och ett angivet nummer. Det är starkare än ordet "klartecken", eftersom det är hans egen formulering och innehåller detaljer ingen hittar på.

Och DK:s svar samma dag 13:43 visar exakt vad meningsskiljaktigheten gällde, och bara det:

> "Jag tycker att SOH:s förslag till upplägg är bra. Vi hade tänkt oss något liknande: en öppen debatt om hur VoF skall arbeta. Tycker dock att det är jag och Lotten (och eventuella ytterligare undertecknare) som skall ha slutreplik, eftersom det är vi som startar diskussionen."

Alltså: **de accepterade hans upplägg och bad enbart om slutrepliken.** Två dagar senare avslogs det (K12). Dagen därpå togs deras text ur numret helt (K14).

#### 🔴 RÄTTELSE: 💄 Lottens uppgift om återpubliceringen var mer belagd än jag bedömde

Jag skrev tidigare att påståendet *"han bestämde sig för att återpublicera den"* var obelagt och att det skulle utgå. **Det var för strängt.**

Ordet **"Återpublicering"** är SOH:s eget, i hans egen publiceringsplan, i skrift, till hela redaktionen, 24 april. Punkt (1) av tre är en återpublicering av Sydsvenskan-artikeln i Folkvett.

Vad som är belagt och vad som inte är det, exakt:

| Påstående | Status |
| --------- | ------ |
| SOH föreslog en återpublicering av Sydsvenskan-artikeln i Folkvett | ✅ **Belagt**, hans eget ord, K22 |
| Han föreslog den som del av ett paket om tre texter som **innehöll** LK och DK:s kritik | ✅ Belagt, K22. Detta måste med, annars blir bilden fel |
| Han gjorde det "utan att informera redaktionen" | ❌ **Fel.** K22 gick till `redfive@vof.se`, alltså hela redaktionen |
| Texten (2) togs sedan bort ur numret | ✅ Belagt, K14 |
| Återpubliceringen (1) genomfördes ändå, utan (2) | ❓ **Fortfarande overifierat.** Detta är den avgörande frågan |

#### ✅ K23. Återpubliceringen genomfördes. Belagt mot det tryckta numret.

`01-primarmaterial/_dokument/folkvett-2026-1_03_lag-skall-med-vetenskap-byggas.pdf`. Folkvett 2026:1, sidorna 35 och framåt. Numret nådde prenumeranterna i juli 2026 (uppgift 💄 Lotten).

**Sektionsrubrik: `DEBATT`.** Artikelrubrik: *"Lag skall med vetenskap byggas"*. Redaktionell ingress, ordagrant:

> "Den 10 april publicerade fyra ledamöter i **Vetenskap och Folkbildnings** styrelse en debattartikel i Sydsvenska Dagbladet. De krävde där att de svenska lagstiftningsprocesserna i större utsträckning ska använda och påverkas av vetenskapligt underlag. Utrymmet i dagspressen är som bekant begränsat. **Folkvett publicerar här den ursprungliga, längre text som Sydsvenska publicerade i nedkortat skick.**"

🎯 **Sekvensen är nu dokumenterad hela vägen, utan en enda tolkning:**

| Steg | Vad | Nyckel |
| ---- | --- | ------ |
| 24 apr | Ansvarig utgivare föreslår ett paket om **tre** texter: (1) återpublicering, (2) LK och DK:s kritik, (3) styrelsens svar | K22 |
| 26 apr | Slutrepliken tas bort | K12 |
| 27 apr | **Text (2) tas ur numret** | K14 |
| juli | Numret utkommer. **Text (1) är publicerad, under rubriken `DEBATT`** | K23 |

Ett paket om tre texter, avsett så att "läsaren själv kan ta ställning", blev en text. Publicerad under rubriken DEBATT, utan motpart.

**Två detaljer till, båda kontrollerbara mot PDF:en.**

1. **Den publicerade versionen är längre än tidningens**, enligt ingressen: "den ursprungliga, längre text som Sydsvenska publicerade i nedkortat skick".
2. **Den bär numrerade fotnoter.** Sidan 36 har not 1, 2 och 3. Det är värt att hålla ihop med K10, där ansvarig utgivare rådde LK och DK att tona ner just kritiken mot avsaknaden av källhänvisningar, med motiveringen att *"Debattartiklar brukar inte innehålla sådana"*. I Folkvett-versionen finns de.

Redovisa punkt 2 som en observation, inte som en anklagelse. Den behöver ingen förstärkning.

#### ✅ Numrets innehåll, besvarat av 💄 Lotten 2026-09-05

- **Ingen text av LK eller DK i numret.**
- **Inget svar från styrelsen.**
- **Ingen avtackning och ingen upplysning om att redaktionen bytt sammansättning.**
- **Föreningens medlemmar har ännu inte informerats någonstans** om att LK och DK inte längre ingår i redaktionen.
- 🎯 **LK:s och DK:s namn står kvar på försättsbladet**, upptagna bland dem som gjort numret, två månader efter avsättningen.

Den sista punkten är sidans starkaste avslutning, och den kräver ingen tolkning alls: numret säger till läsaren att de gjorde tidningen och till dem själva att de inte gör den längre, och ingen har behövt stå för någondera.

#### ✅ K25. Kolofonen. Spärren lyft 2026-09-05.

`01-primarmaterial/_dokument/folkvett-2026-1_00_kolofon.pdf`, sidan 3 av 3. Levererad av 💄 Lotten och verifierad mot dokumentet.

Ordagrant:

> "**Redaktörer som arbetat med detta nummer:** Sven Ove Hansson, ansvarig utgivare (sven-ove.hansson@vof.se), Lotten Kalenius, Dan Katz, Per Schillander, Alexandra Snellman, Anders Wannberg och Maria Wold-Troell. Redaktionen bistås av en redaktionskommitté, där VoF:s styrelse ingår."

🎯 **Rubriken är avgörande och starkare än "namnen står i kolofonen".** Det är inte en stående masthead över redaktionens sammansättning, som kunde ha förklarats med att ingen uppdaterat den. Det är en uttrycklig uppgift om **vilka som arbetat med just det här numret**.

Och listan är bevisligen den gamla: jämför med de fyra som räknas upp i beskedet 3 maj (K1, K2). Kolofonen är exakt den listan **plus Lotten Kalenius och Dan Katz**, alltså redaktionen som den såg ut före avsättningen.

⚠️ **Formuleringsval på sidan.** Sidan namnger inte motparter någon annanstans, men kolofonen är ett publicerat dokument och citatet innehåller sju namn, varav fyra tillhör personer som inte är sidans föremål och varav tre lämnat uttalanden till LK:s fördel. Citatet står ändå i sin helhet, eftersom en trunkerad kolofon inbjuder till frågan vad som klippts bort. Skulle 💄 Lotten hellre vilja korta ner den går det, men då bör rubriken citeras exakt och listan sammanfattas, aldrig delvis återges.

⚠️ **Notera för egen del, inte för sidan:** kolofonen anger också att *"Redaktionen bistås av en redaktionskommitté, där VoF:s styrelse ingår"*. Det är relevant för frågan om redaktionell autonomi och finns redan som eget spår i arkivet (`02-transkriberingar/redaktionell-autonomi/`). Det hör inte hemma på den här sidan, som handlar om proceduren.

#### 🔴 K27. LK tog bort sina och DK:s textbidrag ur redaktionens Google Drive, 3 maj. MÅSTE redovisas.

Uppgift från 💄 Lotten 2026-09-05: samma kväll som beskedet kom gick hon in på redaktionens Google Drive och tog bort samtliga textbidrag från sig och DK, för att numret inte skulle kunna fyllas med deras arbete utan att de nämndes.

**Detta är den enskilt viktigaste upplysningen i hela sessionen, och den är obehaglig av rätt skäl.**

Sidtexten säger i nuläget: *"Det finns inte en rad av oss i det."* Det är sant. Men **en del av orsaken är LK:s egen åtgärd**, och att skriva effekten utan att nämna den orsaken är exakt den selektivitet som formeln anklagar motparten för. En motpart som får veta detta i efterhand kan använda det för att underkänna hela sidan, och skulle ha rätt i sak.

✅ **Lösningen är att skriva det rakt ut, och sidan blir starkare av det.**

Föreslagen formulering:

> Det finns inte en rad av oss i numret. En del av det är mitt eget verk: samma kväll beskedet kom gick jag in på redaktionens gemensamma yta och tog bort våra textbidrag. Jag ville inte att arbetet skulle fylla ett nummer vi inte längre fick vara med i.

Två skäl till att detta gör sidan bättre, inte sämre:

1. **Det visar att sidan redovisar även det som talar emot den.** Efter det har läsaren anledning att tro på resten.
2. **Det gör kolofonen skarpare.** Föreningen anger i tryck att LK och DK "arbetat med detta nummer" samtidigt som deras bidrag var borttagna och de själva avsatta. Motsättningen blir tydligare, inte suddigare.

⚠️ **Följdfråga som måste besvaras innan sidan går ut:** kvarstår påståendet att numret saknar text av dem, eller fanns det bidrag kvar som ändå inte togs med? Och: **skrev LK ledaren "Vetenskap och folkhälsa"** som publicerades i numret? Utkastet till den ledaren ligger i samma arbetsfil som debattartikeln (se K28), vilket väcker frågan vem som författat den. Om LK skrev något som ändå publicerades faller formuleringen "inte en rad av oss".

#### K28. Marsutkastet till styrelsens debattartikel. Tre av fyra uppgifter bekräftade.

`01-primarmaterial/_dokument/20260326-doc-debattartikel-vof-utkast.pdf`, tre sidor.

| 💄 Lottens uppgift | Status |
| ------------------ | ------ |
| Artikeln hette "Lag skall med vetenskap byggas" redan från början | ✅ **Bekräftat.** Utkastets rubrik är exakt den, och den är också Folkvett-versionens. **Sydsvenskan valde en annan rubrik** ("Fakta och vetenskap får stå tillbaka när nya lagar tas fram"). Folkvett-publiceringen återställde alltså skribenternas egen rubrik |
| Faktarutan om VoF ingår | ✅ Finns i utkastet ("Om Vetenskap och Folkbildning"), av den typ redaktioner ber om vid inskick. Att den *trycktes* i Folkvett är ännu inte kontrollerat mot s. 35 och framåt |
| Det enda som lades till i Folkvett-versionen var ingressen | ✅ **Starkt stöd.** Ingressen finns i samma fil under rubriken "Debattartikel VoF, Ingress:", **ordagrant identisk** med den tryckta på s. 35 |
| Texten är i övrigt ordagrant den publicerade | 🟡 Delvis kontrollerat. De partier jag kunnat jämföra stämmer ord för ord. Full kollationering återstår |

⚠️ **Proveniensanmärkning, viktig.** Filnamnet säger 26 mars, men filen innehåller ingressen som refererar till publiceringen **10 april**, samt ett "UTKAST TILL LEDARE, FOLKVETT NR 1, 2026". **Filen är alltså en sammanställd arbetsfil, inte en ren marsartefakt.** Den kan inte citeras som "utkastet från 26 mars" utan den reservationen. Vad som är daterat 26 mars är rimligen artikeltexten, inte dokumentet.

✅ **Konsekvens för fotnotspoängen på sidan.** Om noterna fanns i skribenternas ursprungstext hela tiden, tillfördes de inte inför Folkvett-publiceringen. Poängen står ändå, och ska formuleras exakt: ansvarig utgivare rådde LK och DK att tona ner kritiken mot avsaknaden av källhänvisningar med motiveringen att debattartiklar inte brukar innehålla sådana, och den version han därefter publicerade i Folkvett innehåller numrerade noter. Det är en observation om två utsagor, inte ett påstående om att någon lagt till något.

#### K26. Kolofonen är omskriven sedan förra numret. Belagt, men läs den åt båda hållen.

Jämförelse mot `Folkvettarkivet/folkvett-arkiv/folkvett/folkvett-2025-3-4/artiklar/folkvett-2025-3-4_00b_inlaga.md`, kontrollerad 2026-09-05.

| | Folkvett 2025:3-4 | Folkvett 2026:1 |
| --- | --- | --- |
| Rubrik | **"Redaktörer:"** | **"Redaktörer som arbetat med detta nummer:"** |
| Anders Wannberg | "Anders Wannberg **(adjungerad)**" | "Anders Wannberg" |
| Ansvarig utgivare | "Sven Ove Hansson (ansvarig utgivare)" | "Sven Ove Hansson, ansvarig utgivare **(sven-ove.hansson@vof.se)**" |

**Blocket är alltså redigerat mellan numren.** Någon gick in i det, ändrade rubriken, tog bort en parentes och lade till en e-postadress. Det är inte ett block som stått orört.

🔴 **Men slutsatsen "därmed formulerad med intention att dölja" håller inte, och behövs inte.** Att blocket redigerades är belagt. **Varför** rubriken ändrades är det inte, och den nya rubriken har en fullt oskyldig läsning som en motpart kommer att använda:

> LK och DK **hade** arbetat med nummer 1. LK var nummeransvarig fram till 28 april, numret var kraftigt försenat, och deras arbete låg i det. "Redaktörer som arbetat med detta nummer" är under den läsningen den **mer korrekta** rubriken, inte den mer vilseledande. Den nya lydelsen kan vara en ärlig precisering av en rubrik som annars hade påstått något osant om redaktionens nuvarande sammansättning.

Den invändningen är stark och sidan ska inte gå i den fällan.

✅ **Vad som står oavsett vilken läsning man väljer, och som räcker:**

1. Föreningen publicerade i juli ett dokument som namnger LK och DK som redaktörer som arbetat med numret.
2. Föreningen hade i maj tagit dem ur redaktionen med motiveringen att arbetsmiljön blivit ohållbar för hela redaktionen och att det inte längre var ett alternativ att alla skulle fortsätta.
3. Föreningens medlemmar har vid tidpunkten inte informerats någonstans om att de tagits ur redaktionen.
4. Numret innehåller ingen text av dem, inget svar från styrelsen och ingen avtackning.

**Den skarpaste formuleringen ligger i motsättningen mellan 1 och 2**, och den kräver inget påstående om avsikt alls: samma organisation intygar i tryck att de arbetade med numret, och hade två månader tidigare skriftligt uppgett att det inte längre var möjligt för dem att fortsätta.

⚠️ **Inte infört i `SIDTEXT` ännu.** 💄 Lotten läser sidtexten när detta skrivs. Omskrivningen förs in först efter hennes genomläsning och efter att hon tagit ställning till om jämförelsen mot 2025:3-4 ska med alls. Min rekommendation: ta med **motsättningen** (punkt 1 mot punkt 2), lämna **omskrivningen** i arkivet. Den senare kräver en förklaring av vad som ändrats och varför det skulle spela roll, och kostar mer utrymme och trovärdighet än den ger.

⚠️ **Formuleringsdisciplin även när sidan finns.** Skriv att namnen står kvar och att ingen information gått ut. Skriv **inte** att det gjordes för att dölja något, eller att någon "låtsades" att redaktionen var intakt. Sakförhållandet är förödande i sig; en avsiktsförklaring gör det bara angripbart.

⚠️ Notera att den tidigare kritiken mot formuleringen kvarstår i en del: *"och genom att se till att dess kritiker blev utkuppade"* är fortfarande ett påstående om avsikt och ska inte publiceras. Sekvensen räcker.

#### ⚠️ Två saker i april-materialet som inte får ut

**1. Dödsfallet.** I `soh/20260428-1403-mail-SOH-LK-Folkvett.md` skriver LK till SOH 28 april 16:27 att hon varit upptagen med "kris- och sambandscentral den senaste veckan pga ett plötsligt dödsfall i den närmaste familjen". Det förklarar varför hon inte hängde med i turerna, och det är hennes att berätta om hon vill. Det ska inte stå på sidan som förklaring eller försvar.

**2. Telefonnumret.** Samma mejl innehåller LK:s mobilnummer i klartext. Arkivet är gitignorerat, så det är inneslutet, men numret får aldrig följa med i ett citat.

⚠️ **Evidensnivå för telefonsamtalet 28 april.** `haendelseberattelser/20260509-note-LK-SOH-tel-28-april.md` är en minnesanteckning skriven 9 maj, elva dagar efteråt, och är LK:s återgivning. Aldrig som citat av SOH. Faktabladet gör rätt med "Enligt LK".

⚠️ K10 ligger i `_inkommande/`, som enligt git är otrackat. Samma mejl finns dock refererat i den nycklade tråden `soh/20260426-2110-mail-SOH-DK-redfive-slutreplik.md`, så innehållet är korroborerat. **Bör ändå flyttas in i det nycklade beståndet innan publicering.**

#### 🔁 Om SOH-kanalen: 💄 Lottens invändning står

Jag skrev tidigare att LK:s rad till JL 6 juni var motsagd av DL. **Det var för hårt dragit och jag tar tillbaka det.**

DL motsäger att SOH var med och **skrev** Sydsvenskan-artikeln. Han motsäger **inte** att SOH och DL, två personer utanför redaktionen, resonerade om vad som skulle in i Folkvett, och att redaktionen inte informerades. Tvärtom är det just vad DL:s egen redogörelse beskriver, och K9 visar att redaktionen samma vecka fick artikeln som en tom "Notisunderlag" utan ett ord om saken.

Det påstående som **fortfarande behöver belägg** är utfallet: att det som diskuterades sedermera blev en återpublicering av debattartikeln med några tillagda rader. Det är 💄 Lottens uppgift och det är kontrollerbart mot det publicerade numret. **Öppen fråga: vilket nummer, och finns det i arkivet?** Beläggs det, håller hela raden.

Det som däremot aldrig ska stå är formuleringar om vad de två *ville* eller *tänkte*. "Kuckilurade", "bestämde sig för", "på egen kammare" är avsikt. Det räcker att skriva vad som skedde och vem som inte informerades.

#### 🎯 B2 får sitt starkaste belägg: två ledamöter reserverade sig

Protokollet från 3 maj är **inte offentligt** (uppgift 💄 Lotten 2026-09-05). Men reservationerna är belagda ändå, i tre av varandra oberoende led. Nycklade 2026-09-05.

**K5. PJ:s eget meddelande, 3 maj 19:03**, alltså ungefär trettiofem minuter efter beskedet, återgivet av DK i chatten med LK. `dk-lk/20260410-20260608-bubble-DK-LK.md`, rad 1042:

> "Från PJ: Fick bara ett meddelande? Inget samtal änns. På styrelsen så lades SOs förslag på redaktionen fram och vi var några som frågade varför inte du och Lotten var med i förslaget men efter det fick vi inga klara besked. Vi frågade om det var något akut eller något som på gått längre men fick inga tydliga svar. **Jag och Staffan reserverade oss**, många andra var inte med på mötet, när SO förslag togs. Dock fick vi veta att man såklart kan välja in fler personer i redaktionen senare.
> Jag försökte väcka frågan om varför vi som förening håller på att göra oss av med folk hela tiden. Men i korthet så presenterades inte mycket information."

Det är samtida, förstahands från en närvarande ledamot, och det bekräftar **fyra** saker på en gång: att förslaget lades fram som SOH:s, att frågan om LK och DK ställdes och inte besvarades, att PJ och SL reserverade sig, och att **många ledamöter inte var närvarande** när förslaget togs.

**K6. SL:s skriftliga stadgebedömning, 16 maj 11:44**, mail till DK med LK och PJ på kopia. `staffan-luckander/20260516-1144-mail-SL-DK-stadgebedomning.md`:

> "Jag har läst din och Lottens svar på VoF-företrädarnas debattartikel i Sydsvenskan och finner inget som skulle vara ett övertramp eller något som står emot föreningens stadgar."

> "I mina ögon finner jag inte att något i er text ger något som helst skäl till att du och Lotten måste lämna Folkvettredaktionen. Jag står fast vid min åsikt, baserat på det jag hittills vet, att ni borde vara kvar i Folkvettredaktionen, då ni hittills har gjort ett utmärkt arbete."

Förstahands, skriftligt, daterat, från en ledamot som var på mötet. Det är sidans starkaste enskilda dokument efter primärhandlingarna själva.

**K7. PJ:s egna ord vid mötet 9 juni**, inspelat. `per-johan-rasmark/20260609-1700-mote-PJ-LK-DK-LA-medlemsmote.md`, ca 00:17:38:

> "hade inte jag och Staffan liksom sagt, 'okej det här är förslaget som kommer nu på redaktion. Vi ser att Dan och Lotten inte är med här, vad har hänt där?'"

Och om hur det presenterades, ca 00:18:19:

> "det var ungefär som du tänker dig när du har ett konstituerande möte. Att 'nu ska vi besluta det här', 'nu ska vi besluta', 'okej, och så ska vi besluta redaktion och här har vi förslaget'"

Det sista är belägg för att beslutet presenterades som ett rutinärende, från en person som satt i rummet. Notera att det är **PJ:s** karaktäristik, inte sidans.

**Sammantaget:** ensidig beredning belagd inifrån det beslutande organet, av två personer som inte är part, i tre oberoende led och tre olika medier. Motsvarigheten i Grant-fallet är kollegorna BB och JB. Två oberoende fall, samma sorts vittne, och här är belägget starkare.

⚠️ **Härkomstkedja för K5.** Texten i chatten är DK:s återgivning av PJ:s meddelande, inte PJ:s original. Kedjan är PJ → DK → chattloggen. Den håller, men den ska redovisas som det den är. **Primärartefakten är en skärmdump**, `dk-lk/20260410-20260608-bubble-DK-LK-bilagor/Ska_rmavbild_2026-05-03_kl._21.09.51.png`, som DK skickade 21:10 med orden "De övriga messen från pj".

🔴 **Skärmdumpen är otranskriberad.** Mappen `bilagor/` innehåller 233 filer och **inga** transkriberingar. Transkribering av skärmdumpar i det här arkivet är 📄 Transkriptor-Pilots uppgift, inte min. Ska K5 stå med full härkomst behöver den skärmdumpen transkriberas först. Det finns ytterligare två skärmdumpar från samma kväll som kan bära relaterat material: `Ska_rmavbild_2026-05-03_kl._18.31.26.png` (LK: "Är du också utkickad?", 18:31) och `Ska_rmavbild_2026-05-03_kl._20.13.54.png` (hälsning från Jonathan Lindström, 20:15).

#### 💡 Konsekvens för koden: `Bystander` ska instansieras

Utkastet `anatomy-termination-v4.py` har:

```python
@dataclass(frozen=True)
class Bystander:
    """Deklarerad. Aldrig instansierad."""
    name: str
    reservation: Optional[str] = None
```

Det stämmer inte längre, och sanningen är roligare. `Bystander` **instansieras två gånger**, `reservation` **sätts** i båda, och ingen läser fältet. Beslutet fattas ändå. Byt kommentaren till något i stil med *"Instansierad två gånger. Fältet reservation sätts. Ingen kod läser det."* En populerad variabel som aldrig konsumeras är en exaktare bild av vad som hände än en klass som aldrig används.

#### B4 och B5. Beskedet, 3 maj 18:28 (LK) och 18:30 (DK)

> "Styrelsen för vetenskap och folkbildning har fattat beslut om redaktionen för Folkvett, avseende verksamhetsåret 2026/2027, baserat på inkommet förslag från ansvarig utgivare." (K1, K2)

Omedelbar verkan i samma andetag:

> "Detta innebär att du inte längre kommer att ha tillgång till e-postlistorna eller digitala arbetsytor som är kopplade till detta uppdrag." (K1, K2)

**Självförslaget är nu dokumenterat, inte påstått.** Beslutet fattas "baserat på inkommet förslag från ansvarig utgivare", och den föreslagna redaktionen räknas upp som: Per Schillander, Alexandra Snellman, Anders Wannberg, Maria Wold-Troell, "Samt ansvarig utgivare Sven Ove Hansson" (K1, K2). Förslagsställaren ingår alltså i sitt eget förslag. Det står i samma mejl och behöver ingen tolkning.

De fyra anmärkningarna, prövade mot stadgarna och årsmötesprotokollet 2026-09-04:

| # | Anmärkning | Status efter prövning |
| - | ---------- | --------------------- |
| 1 | LK och DK ingick inte i "inkommet förslag" | ✅ Dokumenterat (K1/K2), men **beskrivande, inte en oegentlighet**. Det säger vad som hände, inte att något brutits. |
| 2 | Förslagsställaren föreslog sig själv | ✅ Dokumenterat (K1/K2), men **inget regelbrott**. Stadgarna reglerar inte hur styrelsen inhämtar förslag. Duger som observation, inte som anklagelse. |
| 3 | Verksamhetsåret "2026/2027" | ✅ **Står, och är nu dubbelt belagt.** Se nedan. |
| 4 | Rutinen nyinförd, oannonserad, nämns inte i årsmötesprotokollet | ⚠️ **Omklassad: kommentar, inte bevis.** Står kvar, men märkt som omdöme. Se nedan. |

#### ✅ Anmärkning 3 står, dubbelt belagd

Föreningen benämner sina verksamhetsår med **ett enkelt årtal**, inte ett spann. Två oberoende belägg:

- Arkivets översikt: *"VoF benämner sina verksamhetsår med ett enkelt årtal, inte ett spann: Verksamhetsåret 2026 = från årsmötet 2026 till årsmötet 2027"* (`folkvettkonflikten-2026/00-oversikt/styrelse-sammansattning-2012-2026.md`).
- **Föreningens eget årsmötesprotokoll åtta dagar tidigare**, 25 april 2026, använder formen tre gånger: §8 *"verksamhetsplanen för verksamhetsåret 2026"*, §10 *"Val av styrelse för verksamhetsåret 2026"*, §11 *"Val av två revisorer samt suppleanter för verksamhetsåret 2026"*.

Skriv inte "året existerar inte". Skriv det exakta: **beskedet använder en beteckning föreningen inte använder, åtta dagar efter att dess högsta beslutande organ använt den riktiga tre gånger i samma protokoll.** Det är en liten sak, men den är kontrollerbar och den kostar inget att ha med.

#### ⚠️ Anmärkning 4: omklassad från bevis till kommentar

**§ 9 i stadgarna** (senast reviderade och antagna vid årsmötet 2026-04-25, alltså gällande version):

> "Föreningen utger tidskriften Folkvett. Redaktionen utses av styrelsen."

**Vad § 9 avgör:** att styrelsen hade befogenheten. **§ 5**, som räknar upp vad årsmötet ska behandla, nämner inte redaktionen: berättelser, ansvarsfrihet, verksamhetsplan, motioner, val av styrelse, val av revisorer, val av valberedning.

**Vad § 9 inte avgör:** huruvida det gick professionellt till. Att ha befogenhet att fatta ett beslut är inte samma sak som att ha berett det.

Anmärkningen var aldrig ett påstående om regelbrott, och 💄 Lotten flaggade den själv som tyckande när hon lämnade den. Den ska därför inte strykas, den ska **märkas**. Skillnaden som styr är **bevis kontra kommentar**, inte sant kontra falskt.

**Som bevis håller den inte.** Frånvaron ur årsmötesprotokollet kan inte användas som indicium på oegentlighet, eftersom stadgarna lägger frågan i ett annat forum och det alltså inte finns någon dokumenterad förväntan att bryta mot. Formuleringen "nyinförd rutin" ska inte heller stå oreserverat: att styrelsen utser redaktionen är stadgarnas ordning. Att *hela* redaktionen byts på ett bräde kan vara ny praxis, men det kräver en genomgång av tidigare års tillsättningar för att kunna påstås.

**Som kommentar håller den, och hör hemma på sidan om den är märkt.** En förening som gör anspråk på att företräda vetenskaplig metod och folkbildning, och som tar ut en medlemsavgift, kan rimligen förväntas bereda och motivera en organisationsförändring, om så bara som information till medlemmarna. Det är ett omdöme om professionalitet, inte ett påstående om regelbrott, och det är fullt legitimt så länge sidan säger vilket av de två det är.

🚫 **STRUKEN av 💄 Lotten 2026-09-05.** Anmärkning 4 utgår helt ur sidan, i alla former. Ingen del av resonemanget nedan ska återinföras. Det står kvar här enbart som spår av prövningen.

Föreslagen formulering, som höll isär de två:

> Styrelsen hade enligt § 9 befogenheten att utse redaktionen, och årsmötet var inte forumet. Det som förvånar är inte att beslutet fattades av styrelsen, utan att en förening som gör anspråk på vetenskaplig noggrannhet inte fann anledning att bereda eller motivera förändringen, inte ens som information till medlemmarna vid årsmötet åtta dagar tidigare.

Första meningen ger motparten dess bästa invändning i förväg. Den andra är märkt som omdöme genom "det som förvånar". Ingen kan säga att sidan påstod ett regelbrott.

⚠️ **Kvarstår att stryka:** *"de kunde inte vara öppna med det, för det VAR inte planerat"* och *"konstruerade svepskäl"*. Det är påståenden om motiv, inte om professionalitet, och de är obelagda. Omdömet ovan behöver dem inte.

**Tesen berörs inte av något av detta.** Formeln handlar om **B, verkställandet**, inte om **A, huruvida avsättningen var tillåten**. Grants avsättning var också inom arbetsgivarens befogenhet. Sidan har aldrig behövt hävda att en regel bröts.

#### B3. Kapplöpningen, dokumenterad av DK samma kväll, 3 maj 20:40

> "Om detta verkligen är hela styrelsens beslut måste vi få veta konkret vad som ligger bakom det. Och likaså varför vi inte rådfrågats." (K3)

Samma begäran som Grants, samma utfall. Notera parallellen: Grants anmälningspunkt 2 och DK:s mening här beskriver samma sak, skrivna av två personer som inte känner till varandra.

#### B7. Efterhandsprövningen, 6 juni 17:02

> "Den konfliktsituation som uppstod i redaktionen för Folkvett ledde till att arbetsmiljön för hela redaktionen blev ohållbar. Det var inte längre ett alternativ att alla medlemmar i redaktionen skulle fortsätta." (K4)

> "Styrelsen står fast vid det tidigare beslutet som vi bedömer var bäst för verksamheten och för Folkvett." (K4)

> "Vi ser ingen anledning till att gå in på frågor om styrelsens arbetssätt." (K4)

**Den sista meningen är B7 i sin kortaste form.** Där Grant fick en formell utredning vars avgränsning uteslöt beslutet, får ni ett uttryckligt avböjande att alls granska arbetssättet. Samma funktion, mindre apparat, och betydligt lättare att visa: den är en mening lång.

Anmärkningar till "arbetsmiljö": organisationen lyder inte under arbetsmiljölagstiftningen, alltså finns inget forum med jurisdiktion; ingen motivering ges till varför just LK och DK.

#### Underbemanningen: belagd, men den hör till B5, inte till A2

⚠️ **Rollen är omdefinierad 2026-09-05.** Underbemanningen var **inte** det LK och DK invände mot, se rättelsen ovan. Den hör i stället till **B5, den skriftliga orsaken**, som motbevisning: styrelsen åberopade i juni att arbetsmiljön blivit ohållbar, i en redaktion vars resursbrist stått i dess egna protokoll sedan 2022 utan att åtgärdas. Materialet är alltså lika användbart som förut, men det ligger på ett annat ställe i formeln.

Genomsökning av 29 styrelseprotokoll i `vof-lk-2018-2026/01-primarmaterial/styrelseprotokoll/_md/` gav tre träffar som rör redaktionens bemanning:

| Datum | Protokolltext, ordagrant |
| ----- | ------------------------ |
| **2022-03-06** | "Fler redaktörer till redaktionen behövs! Lotten författar ett upprop till medlemmarna via sociala media samt annons i kommande nummer." |
| **2023-03-05** | "Pontus påminde om att redaktionen behöver en ny medlem som kan ersätta honom." |
| **2023-09-02** | "Det finns ett fortsatt behov av att hitta fler redaktörer. Pontus meddelade att han av olika skäl inte står till förfogande." |

⚠️ **Tre korrigeringar mot hur du formulerade det.**

1. **Inte "sedan ca 2021".** Första träffen är 6 mars 2022. Protokollen från 2021 nämner Folkvett men inte bemanningen. Skriv 2022, inte 2021.
2. **Inte bara LK och DK.** Två av tre gånger är det **Pontus Böckman** som tar upp det. Det gör påståendet **bättre**, inte sämre: det är inte längre de avsatta som säger att de var underbemannade, det är styrelsens egna protokoll som visar att styrelsen visste, påmind av en tredje person.
3. **Korpusen tar slut 2024-05-19.** Mappen innehåller inga protokoll för 2024-06 till 2026.

**Uppgift från 💄 Lotten 2026-09-05:** underbemanningen bestod **ända fram till maj 2026**. Nya redaktörer höll på att skolas in för att efter hand kunna ta nummeransvar, men arbetet hängde fortfarande på LK och DK.

⚠️ Detta är i nuläget **obelagt** för perioden efter september 2023, eftersom protokollkorpusen slutar 2024-05-19. Två vägar: antingen skaffas protokollen för 2024 till 2026, eller så formuleras påståendet i två led som håller isär det belagda från det uppgivna:

> Behovet av fler redaktörer är protokollfört vid tre styrelsemöten mellan mars 2022 och september 2023, senast med styrelsens egen formulering "fortsatt behov". Läget bestod fram till avsättningen: nya redaktörer var under inskolning, men nummeransvaret låg fortfarande hos de två som avsattes.

Andra meningen är LK:s uppgift och ska märkas som sådan om den inte kan beläggas. **Alternativ belägg-väg som troligen är billigare än protokollen:** tidningens kolofon per nummer 2024 till 2026 visar vem som stod som nummeransvarig, vilket är just det påståendet handlar om.

Den formulering som håller:

> Behovet av fler redaktörer är protokollfört vid tre styrelsemöten mellan mars 2022 och september 2023, senast med styrelsens egen formulering "fortsatt behov".

**Kontext från 💄 Lotten:** hon hade tagit en paus från redaktionen och **återvände sommaren 2023** just därför att Pontus inte ville fortsätta och redaktionen inte hade råd med ännu ett bortfall. Det binder ihop de två sista protokollraderna: mars 2023 säger Pontus att han behöver ersättas, september 2023 att han inte står till förfogande, och Lotten går tillbaka in för att täcka luckan.

#### ✅ BESLUTAT 2026-09-05: tjänstetiden nämns inte på sidan

Formeln handlar om **B, verkställandet**. Hur länge Lotten satt i redaktionen påverkar inte om beslutet bereddes ensidigt, om hon fick svara, eller om kontrollvärdet blev noll. Att utelämna tjänstetiden avför fyra problem på en gång:

1. **Uppehållet** (2018 till slutet av 2020, åter sommaren 2023) behöver inte förklaras.
2. **Protokollet 2022-03-06**, där Lotten författar redaktionens rekryteringsupprop mitt i uppehållet, slutar se ut som en motsägelse. Hon satt då som styrelsens sekreterare, vilket är ett annat uppdrag, men distinktionen hade behövt skrivas ut.
3. **Utbrändheten** behöver inte skrivas ut. En hälsouppgift på en publik sida går inte att ta tillbaka.
4. **KNK**, Lottens avlidna mentor i redaktionen, behöver inte nämnas. Att åberopa en avliden kollegas arbetsbörda som stöd i en pågående konflikt är något hon inte kan samtycka till.

Vill sidan ändå bära tanken att Lotten höll redaktionen uppe räcker det protokollförda: behovet av fler redaktörer, styrelsens eget "fortsatt behov", och att hon gick tillbaka in i det.

**Hela underlaget är flyttat till konfliktarkivet**, där det hör hemma:
`folkvettkonflikten-2026/02-transkriberingar/haendelseberattelser/20260905-note-LK-redaktionstid-och-uppehall.md`

Den noten bär också de omdömen som aldrig får gå ut härifrån: karakteriseringen av Pontus, Katz och Sven Ove. Tre namngivna, obelagt påstående om deras arbetsmoral, och de har inte hörts. En av dem är dessutom 🍆 DK, den medavsatta, vilket gör det motsägelsefullt: sidan kan inte samtidigt driva att DK avsattes på lösa grunder och själv karakterisera honom på lösa grunder.

✅ **Kontrollerade mot PDF-originalen 2026-09-05.** Alla tre citaten stämmer ordagrant mot `vof-lk-2018-2026/01-primarmaterial/styrelseprotokoll/*.pdf`. Källhänvisning per citat: 2022-03-06 § 7 Folkvett (sida 3 av 4), 2023-03-05 § 7 Folkvett (sida 2 av 4), 2023-09-02 § 7 Folkvett / Allmänt (sida 3 av 6). Publiceringsspärren för den här punkten är därmed lyft.

#### B8. Kontrollvärdet, nu med dokumenterad nämnare

Den kvarvarande redaktionen är namngiven i beskedet självt (K1, K2): **Per Schillander, Alexandra Snellman, Anders Wannberg, Maria Wold-Troell**. Fyra personer, plus ansvarig utgivare Sven Ove Hansson. Nämnaren är alltså 4, och den kommer ur motpartens eget mejl.

| Person | Uttalande | Bekräftar påståendet? |
| ------ | --------- | --------------------- |
| Maria Wold-Troell | "Jag kommer att sakna er" | Nej |
| Per Schillander | "Jag tycker att arbetet har fungerat ganska bra, om än inte perfekt. Ingen har uppfört sig illa och konflikter har jag inte sett något av." | Nej |
| Anders Wannberg | "ingen i VoF har uppfört sig illa mot mig" | Nej |
| Alexandra Snellman | Missförstod DK:s fråga och besvarade en annan sak | Nej, men uttalar sig inte i saken |

⚠️ **Exakt formulering, viktig.** Skriv **inte** "4 av 4 motsäger påståendet". Det håller inte, eftersom den fjärde inte uttalade sig i saken. Skriv:

> Av de fyra kvarvarande redaktionsmedlemmarna har tre uttalat sig i direkt motsatt riktning. Den fjärde besvarade inte frågan som ställdes. Ingen har bekräftat påståendet.

Det bär den råa nämnaren, redovisar den svaga fjärdedelen öppet i stället för att räkna in den, och är fortfarande förödande. En motpart som letar efter felet hittar inget att ta i.

⚠️ **AS-uttalandet ska inte citeras.** Lotten bedömer att svaret var förvirrat och skulle förvirra en läsare. Rätt beslut. Ett obegripligt citat som redovisas som stöd är sämre än inget citat.

#### ⚠️ B6, den viskade orsaken: den enskilt farligaste punkten på sidan

Listan lyder: "slöseri med resurser", "vanskötsel", "uteslutning av kollegor", "droger", "hemfridsbrott".

**Publicera inte dessa som citat utan dokumenterad avsändare och tidpunkt.** Tre skäl:

1. De är muntliga och odokumenterade. Ingen källnyckel finns.
2. De är grova. "Droger" och "hemfridsbrott" är påståenden om brott. Att återge dem på en publik sida sprider dem vidare, även med ramen "detta sades om oss".
3. Det är den enda punkten på hela sidan där **du** riskerar att göra det formeln anklagar andra för: framföra en allvarlig anklagelse i en kanal där den utpekade inte kan svara.

Två vägar framåt. Antingen dokumenteras de (vem sa vad, när, till vem, med källnyckel), och då kan de stå. Eller så beskrivs mekanismen utan innehållet.

**✅ BESLUTAT av 💄 Lotten 2026-09-04: mekanismen beskrivs, innehållet utgår.** Edsvurna vittnesmål vore möjliga att få fram men är en oproportionerlig ansträngning för tveksam effekt. Sidan skriver alltså ungefär:

> Parallellt löpte en muntlig kanal där betydligt grövre påståenden framfördes, inklusive anklagelser om brott, aldrig i skrift och aldrig till oss direkt.

Inga av de fem formuleringarna ("slöseri med resurser", "vanskötsel", "uteslutning av kollegor", "droger", "hemfridsbrott") får förekomma på sidan. De stannar i det här dokumentet, som aldrig pushas.

#### ✅ Avsändarfrågan, avgjord 2026-09-04

**Lina Hedman och Lina Tebbla är samma person.** Namnbyte; hon heter Tebbla sedan 2020 och `lina.m.hedman@gmail.com` är hennes privata adress i det tidigare efternamnet. Bekräftat av 💄 Lotten, och oberoende av arkivet: `styrelse-sammansattning-2012-2026.md` § Stavningsnoter har raden *"Lina Tebbla / Lina Hedman | 'Lina Hedman' (t.o.m. verksamhetsåret 2018), 'Lina Tebbla' (fr.o.m. 2020) | Samma person; namnbyte."*

Hon är föreningens ordförande, omvald vid årsmötet 25 april 2026 (§10), och öppnade det mötet (§1).

**På sidan:** skriv "ordföranden" eller "styrelsens ordförande". Nämn inte adressdiskrepansen. Den förklaras av ett namnbyte, den bär ingenting, och Lottens förklaring till varför adressen inte bytts är en gissning om motiv som inte hör hemma på sidan.

### ⚜️🐿️ Konsultuppdraget, 2026 (augusti eller september)

**Framfört vid avlägsnandet**: "bråkstake".
**Framfört efteråt, vid backpedaling**: "du är ju lite av ett yrväder", "projektet är nästan klart".
**Viskad orsak** (inofficiella kanaler): "går annan aktörs ärenden [Microsoft]".

Notera att B7 här tar formen av efterhandsrationalisering i stället för formell prövning. Samma funktion, mindre apparat.

⚠️ **Öppen fråga:** exakt datum. "Häromveckan" räcker inte om något av detta ska publiceras.

### T Hellstadius

**Angiven orsak**: "visselblåsare, *massor* av visselblåsare".
**Kontrollvärde**: T kontrollerade med HQ. Faktiskt antal: `0`.

Det renaste fallet av B8 som finns i materialet. Påståendet var kvantitativt, alltså kontrollerbart, alltså kontrollerat.

⚠️ **Öppen fråga:** hörde du detta från T direkt, eller via gemensam väninna? Ditt meddelande säger "hörde några dagar senare en liknande historia från gemensam väninna, T Hellstadius", vilket kan läsas som att T *är* väninnan eller att väninnan berättade *om* T. Det avgör om detta är förstahands- eller andrahandsuppgift, och det ska framgå.

### Johan Grant, Externatet, Lunds universitet, 2019 till 2020

Publikt dokumenterat fall. Grant undervisade på Externatet i åtta år, ett obligatoriskt moment på psykologprogrammets sjunde termin: en group relations-konferens enligt Tavistockmodellen, två hela dagar, fem konsulter.

**Primärkälla, verifierad 2026-09-04.** Lunds universitet, RAPPORT "Utredning med anledning av misstänkt kränkande särbehandling", dnr **P 2020/1239**, daterad **2020-06-23**, undertecknad Christofer Edling, dekan. Fem sidor plus fem bilagor, publikt tillgänglig. Allt märkt *P 2020/1239* nedan är avskrivet ordagrant därifrån.

Notera att utredningen genomgående kallar kursmomentet **"arbetskonferens"** (delkurs 10:2, termin 7), inte "Externatet". Det senare är mediernas och studenternas namn.

| Steg | Vad som hände | Källa |
| ---- | ------------- | ----- |
| A2 | Början av nov 2019: studenter inkommer med klagomål till studierektor. *"De framförde att de inte kunde fullfölja momentet på grund av lärarens bemötande."* Enligt Lundagård föregicks detta av en Facebook-diskussion; en student beskriver panikångest i månader och temat "Var är pappa?" som homofobiskt och sexistiskt | P 2020/1239 s. 2; Lundagård |
| B2 | 8 nov 2019: studierektor Jonas Bjärehed mejlar lärarlaget. Berörda studenter får alternativ examination. Åtgärden föregår varje utredning. *"Studierektor såg det som ett arbetsmiljöproblem och sökte en särlösning för dessa studenter"* | P 2020/1239 s. 2 |
| B3 | Beslutet fattas utan att Grant hunnit svara, bekräftat av **två oberoende kollegor** i lärarlaget, Bengt Brattgård och Johan Bertlett: *"BB och JB menar liksom JG att dialogen var obefintlig eller i bästa fall otydlig och att beslut fattades hastigt och utan förankring i lärarlaget"* | P 2020/1239 s. 2 |
| B4 | **17 dec 2019**, datumet är nu fastställt: *"Den 17 december 2019 talade RH och JG på telefon och RH framförde att JG inte längre kommer att anlitas för att undervisa på den omnämnda kursen."* RH = prefekt Robert Holmberg | P 2020/1239 s. 3 |
| B5 | *"JG uppfattar att skälen till beslutet är vagt formulerade och det han uppfattar är att RH menar att han och JG inte jobbar mot samma mål. JG upplever att han inte får någon närmare motivering till beslutet."* | P 2020/1239 s. 3 |
| B7 | Av Grants fyra anmälningspunkter avgränsas **punkt 1 och 2 bort**. Kvar utreds 3 och 4: *"Utredaren har valt utreda punkt 3 och 4 för att klargöra om det inträffade är att betrakta som kränkande särbehandling av JG"* | P 2020/1239 s. 3 |
| Utfall | *"Utredaren finner att inget av det som JG har anfört i sin anmälan kan betecknas som kränkande särbehandling enligt AFS 2015:4."* Dekanen rekommenderar i stället tre administrativa förtydliganden till institutionsstyrelsen | P 2020/1239 s. 5 |

**Punkt 2 i Grants anmälan är formeln, formulerad av honom själv utan att han känt till den** (P 2020/1239 s. 1):

> "JG upplever att det har framförts klagomål mot honom från studenter och arbetsgivaren som han inte har fått ta del av och därmed inte kunnat försvara sig mot och som lett till ingripande i hans upplägg för kursen samt att hans anställning inte förlängs"

Det är B3, ordagrant. Och det är en av de två punkter som lämnas utanför utredningen.

⚠️ **Korrigering.** Formuleringen *"varken omständigheterna kring avslutandet av Grants uppdrag eller studierektorns agerande omfattas av utredningen"* är **inte** Edlings ord. Den är Academic Rights Watch sammanfattning. Rapporten säger sakligt samma sak, men i tre separata avgränsningar med annan ordalydelse (se B7 i formeln ovan). Använd aldrig ARW-formuleringen inom citattecken. Verbatimcitaten i tabellen ovan är kontrollerade mot dokumentet.

⚠️ **Källkritisk anmärkning, kvarstår.** Academic Rights Watch och Timbros Smedjan är partiska till Grants förmån och ska användas som vägvisare till dokument, inte som källa för sakuppgifter. Studenternas sida är verklig, och utredningen ger den utrymme: den slår fast att studenter har rätt att framföra klagomål och att studierektor har mandat att besluta om alternativ examination. Den beskrivna skadan ska inte viftas bort.

**Formeln uttalar sig om proceduren, inte om huruvida kritiken var befogad.** Den skillnaden är hela sidans försvar och måste stå utskriven på sidan, inte bara i det här dokumentet.

---

## 🎭 Formspråket

### Blandspråksskämtet, konkretiserat

Din idé var `.py` blandat med `C#` för att illustrera folk i roller de inte behärskar. Förslag på hur det görs strukturellt i stället för uttalat:

- **Förloppet skrivs i Python.** Informellt, dynamiskt typat, det som faktiskt körs. Här händer sakerna.
- **Narrativet skrivs i enterprise-`C#`.** Ceremoniöst, verbost, `public sealed class WorkEnvironmentConcernFactory`, `IUnfalsifiableCause`, `AbstractGrievanceHandlerProvider`. Pompan i enterprise-namngivning är en exakt match för vuxna människor som putsar dammet från kavajslaget.

De två språken i samma fil, som inte kan kompilera tillsammans, **är** skämtet. Ingen behöver förklara det. Den som kan kod ser det direkt, den som inte kan ser två sorters typografi och förstår ändå att någon låtsas.

`B8 Kontrollvärdet` blir en assertion som ligger **efter** `commit()` och därför aldrig körs. Eller ett enhetstest som aldrig lades in i pipelinen. Båda fungerar, det andra är roligare.

### Layout

Behåll den befintliga tvåkolumnsuppdelningen från `v3.svg`, den är rätt och rymmer det nya:

| Zon | Innehåll | Språk |
| --- | -------- | ----- |
| Vänster: **FÖRLOPPET** | A1, A2, B1, B2, B3, B4 | Python |
| Höger: **NARRATIVET** | B5, B6, B7 | C# |
| Botten, full bredd: **KONTROLLVÄRDET** | B8 | assertion efter commit |

A2 markeras visuellt som den enda variabla noden, till exempel med fyra parallella ingångar som möts. Det är sidans ärlighet gjord synlig.

### Bärare

**HTML plus CSS grid, inte SVG.** Diagrammet är till nio tiondelar text i rutor. SVG ger absoluta y-koordinater, manuella radbrytningar och noll responsivitet, och `v3.svg` är 1240 px bred mot sajtens 40rem läsbredd. HTML ger flytande layout, sökbar text, skärmläsarstöd och redigerbarhet utan att räkna pixlar. SVG vinner när geometrin bär betydelse, vilket den gör hos `schrodingers-troll.svg` men inte här.

Bäddas in via metod A i `mall/artefakt-mall.html`, alltså egen fil i `handelser/` som iframe. Isoleringen är dessutom vad som gör overheadestetiken möjlig utan att smitta sajtens palett.

### Overheadestetiken

Ett medvetet avsteg från husets formspråk, vilket 🦚 Greve Malcolm ska avgöra formen på. Ramarna: nya tokens i `style.css`, aldrig hårdkodade färger, fungerande i både ljust och mörkt läge, fungerande i både mobil- och datorvy. Det är sajtens enda hårda regel och den gäller även pastischer.

---

## 🚪 Publiceringsomfattning

**BESLUTAT av 💄 Lotten 2026-09-04: Grant plus Lottens eget fall skrivs ut. ⚜️🐿️ och T Hellstadius anonymiseras helt eller utgår.**

`_utkast/` pushas aldrig, så det här dokumentet får bära allt oavsett. Beslutet gäller enbart vad som hamnar i `handelser/`.

### Vad beslutet medför

Att ditt eget fall står utskrivet gör sidan till ett partsinlägg, och VoF kommer att läsa den för att hitta felet. Det höjer beviskravet på **din** halva till samma nivå som Grant-halvan nu ligger på, alltså primärkälla med källnyckel per påstående. Konkret:

- **Varje påstående om 3 maj och 6 juni behöver sin källnyckel** ur folkvettkonflikten-arkivet, inte ur minnet. Citaten du gav mig i chatten är underlag, inte källor.
- **De fyra anmärkningarna om 3 maj-beslutet** (att LK och DK inte ingick i förslaget, att förslagsställaren föreslog sig själv, att verksamhetsåret 2026/2027 inte existerar, att rutinen var nyinförd och oannonserad) är sidans starkaste material eftersom var och en är kontrollerbar mot handlingarna. Var och en ska bära sin handling.
- **Frånvaroargument kräver dokumenterad förväntan.** "Nämns inte i årsmötesprotokollet veckan innan" håller bara om det anges vilket protokoll och varför en ny valordning hade behövt nämnas där.
- **Mönster, aldrig avsikt.** "Rutinen var nyinförd och annonserades inte i förväg" håller. "De införde rutinen för att kringgå årsmötet" håller inte, och behövs inte.
- **Kontrollvärdet behöver sin nämnare** innan det får skrivas som `0`, se den öppna frågan under Folkvett-fallet.

### Vad som utgår

⚜️🐿️ och T Hellstadius får inte förekomma med identifierande detalj. Puffs 15 minuter är formelns bästa illustration av B3, men en tidslinje på 15 minuter mellan ett utbyte med en namngiven IT-arkitekt och ett besked är identifierbart i branschen även utan namn, och Puff har inte tillfrågats. Vill du behålla exemplet: fråga honom. Annars stannar det i `_utkast/`.

Detsamma gäller T. Andrahandsuppgift plus namngiven person plus ett bolag som sparkade henne är den kombination som inte ska ut. `0 visselblåsare` kan däremot leva vidare som **anonymiserad illustration** utan namn, bransch eller årtal, om du vill ha kvar punchlinen.

---

## 📋 Nästa steg

1. ✅ **Klart.** Publiceringsomfattning beslutad. Grant-fallet verifierat mot P 2020/1239. Folkvett-citaten verifierade mot K1 till K4. Nämnaren fastställd till 4 ur motpartens eget mejl. Avsändarfrågan avgjord. B6 avgjord. Anmärkning 3 dubbelt belagd. Anmärkning 4 prövad och struken. Underbemanningen belagd med tre protokolldatum.
2. ✅ **Klart.** Protokollcitaten kontrollerade mot PDF-originalen, alla tre ordagranna.
3. 🟡 **Källnycklar för april-förloppet: materialet är lokaliserat, inte läst.** Faktabladet är en sammanfattning, **inte** en källa, och är uttryckligen inte ett offentligt dokument. Varje datum som ska stå på sidan behöver sin egen transkribering med message_id, som K1 till K4. Kandidaterna finns och listas nedan under § Kandidatnycklar. **Återstår: läsa dem och nyckla upp dem till K5 och framåt.**
4. ✅ **Klart. Reservationerna är belagda i tre oberoende led** (K5, K6, K7), utan att protokollet behövs. Protokollet är inte offentligt, och behövs inte längre.

   🔴 **Kvar: skärmdumpen.** `dk-lk/20260410-20260608-bubble-DK-LK-bilagor/Ska_rmavbild_2026-05-03_kl._21.09.51.png` är primärartefakten bakom K5 och är otranskriberad, liksom de övriga 232 filerna i den mappen. Uppgiften tillhör 📄 Transkriptor-Pilot, inte 🦞 Velvet. 💄 Lotten avgör om den ska köras.
5. 🟡 **Underbemanningen efter september 2023.** 💄 Lotten uppger att läget bestod till maj 2026, med nya redaktörer under inskolning men nummeransvaret kvar hos LK och DK. Obelagt i protokollkorpusen, som slutar 2024-05-19. **Icke-blockerande**, se tvåledsformuleringen under § Underbemanningen. Billigaste beläggväg är tidningens kolofon per nummer 2024 till 2026.
6. 🦞 Velvet skriver den färdiga sidtexten inklusive den blandade pseudokoden, med källnyckel per påstående i Lotten-halvan.
7. 🦚 Greve Malcolm skriver DESIGNSPEC med overheadestetiken.
8. 🐡 Futaba eller 🛰️ Kepler bygger sidan i `handelser/` och länkar in den från kategoriindexet.
9. 💄 Lotten godkänner förhandsvisningen och pushar.

🔴 **Underlaget är INTE längre klart.** Rättelsen 2026-09-05 öppnade två blockerande punkter (3 och 4). Sidtexten kan inte skrivas förrän april-förloppet har källnycklar.

### 🔒 Publiceringsspärr

Ditt eget fall står utskrivet, sidan är ett partsinlägg, och den läses av en motpart som letar efter felet.

**Fyra saker får aldrig stå på sidan**, oavsett hur självklara de känns:

| Får inte stå | Varför |
| ------------ | ------ |
| De fem viskade orsakerna, ordagrant | Odokumenterade anklagelser om brott, mot personer som inte kan svara |
| Frånvaron ur årsmötesprotokollet **som bevis** | § 9 lägger frågan hos styrelsen, alltså finns ingen förväntan att bryta mot. Som **märkt omdöme** om professionalitet får den däremot stå |
| Påståenden om styrelsens motiv | "Konstruerade svepskäl", "kunde inte vara öppna" är avsikt, inte mönster |
| "4 av 4 motsäger" | Den fjärde uttalade sig inte i saken. Använd den exakta formuleringen |
| Karakteriseringen av Pontus, Katz och Sven Ove | Obelagt påstående om tre namngivnas arbetsmoral, de har inte hörts, och en av dem är den medavsatta |
| KNK:s död och Lottens utbrändhet | Behövs inte för tesen. Se rekommendationen om tjänstetiden |

## 🔗 Källor, Grant-fallet

**Primärkälla:** Lunds universitet, RAPPORT "Utredning med anledning av misstänkt kränkande särbehandling", dnr P 2020/1239, 2020-06-23, Christofer Edling, dekan: https://academicrightswatch.se/wp-content/uploads/2020/09/utredning-LU-JG-vs-RH-BJB-20200625-kopia.pdf
*(Notera diskrepansen: filnamnet säger 20200625, dokumenthuvudet säger 2020-06-23. Dokumentet gäller.)*

**Ytterligare primärmaterial, ej genomgånget:**
- Underlag ledningsgruppsmöte LU, 2020-02-05: https://academicrightswatch.se/wp-content/uploads/2020/09/Underlag-ledningsgruppsmöte-LU-20200205.pdf
- Brev Jonas Bjärehed till Lena Eskilsson, 2020-04-19: https://academicrightswatch.se/wp-content/uploads/2020/09/brev-Jonas-Bjärehed-till-Lena-Eskilsson-20200419-2.pdf
- Utredningsrapport Lena Eskilsson (den andra anmälan, Grant mot sig själv): https://academicrightswatch.se/wp-content/uploads/2020/09/Utredningsrapport-Lena-Eskilsson-NY.pdf

**Journalistiska källor:**
- Psykologtidningen, "Lärare tvingas bort efter studentprotester", 2020-01-30: https://psykologtidningen.se/2020/01/30/larare-sparkas-efter-studentprotester/
- Lundagård, "Hatet mot externatet", 2020-01-27: https://www.lundagard.se/2020/01/27/hatet-mot-externatet/
- Lundagård, "Vad pågår på Psykologen egentligen?", 2020-01-28: https://www.lundagard.se/2020/01/28/vad-pagar-pa-psykologen-egentligen/
- Sveriges Radio P4 Malmöhus, "Kritiserade läraren på Externatet plockas bort": https://sverigesradio.se/sida/artikel.aspx?artikel=7381652&programid=96
- Academic Rights Watch (partisk), dekanbeslutet: https://academicrightswatch.se/?p=4310
- Academic Rights Watch (partisk), "Lundalärare fråntas kurs": https://academicrightswatch.se/?p=4038

## 📁 Relaterade filer

- `Dev/HackerLipstick/TheLipstickWeb/_utkast/anatomy-of-a-termination.md`
- `Dev/HackerLipstick/TheLipstickWeb/_utkast/anatomy-termination-v3.svg`
- `Dev/HackerLipstick/TheLipstickWeb/_utkast/anatomy-termination-v4.py`
- `Dev/HackerLipstick/TheLipstickWeb/mall/artefakt-mall.html`
- `Dev/HackerLipstick/TheLipstickWeb/DESIGNSPEC-schrodingers-troll.md`

---

*🦞 Velvet, Holding the Line. Formeln blev bättre av att spricka.*

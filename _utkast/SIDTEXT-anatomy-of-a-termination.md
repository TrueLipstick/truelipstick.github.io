# SIDTEXT: Avsättningens anatomi

> **ID**: SIDTEXT-anatomy-of-a-termination
> **Skapad**: 2026-09-05
> **Författare**: 🦞 Velvet, Holding the Line (Initium Lineage Agent)
> **Model**: claude-opus-5[1m]
> **Underlag**: `TheLipstickWeb/_utkast/FORMEL-anatomy-of-a-termination.md` (K1 till K19)
> **Till**: 🦚 Greve Malcolm (DESIGNSPEC), därefter 🐡 Futaba eller 🛰️ Kepler (bygge)
> **Status**: utkast för 💄 Lottens godkännande. Publiceras aldrig utan det.

Detta är **sidans text**, inte dess formgivning. Kodblocken är innehåll och ska sättas som kod, inte som bild. Källnycklarna i hakparentes är arbetsnoteringar och ska **inte** synas på sidan; de finns för att varje påstående ska gå att spåra under granskning.

---

## Rubrik

**Avsättningens anatomi**

Underrubrik: *En procedur i åtta steg, dokumenterad i två fall som inte har något med varandra att göra.*

---

## Ingress

Det finns ett sätt att göra sig av med någon som inte kräver att man har rätt.

Det behöver ingen regel som brutits, ingen utredning som lett någonvart och inget skäl som går att skriva ner. Det behöver bara att besluten fattas i en viss ordning. Ordningen är alltid densamma, och det är det som gör den värd att beskriva.

Jag har sett den två gånger på nära håll och två gånger på avstånd. Den här sidan handlar om de två fall där jag kan visa handlingarna.

---

## Vad det här är, och vad det inte är

Läs det här stycket innan resten. Det är sidans hela försvar och det är kort.

**Sidan handlar om proceduren, inte om vem som hade rätt.**

I det ena fallet blev jag av med mitt uppdrag. I det andra blev en universitetslärare av med sitt, efter att studenter framfört kritik mot hans undervisning. Jag vet inte om studenterna hade rätt. Jag tar inte ställning till det, och sidan behöver inte veta det.

Det som gör de två fallen jämförbara är inte sakfrågorna. Det är att avlägsnandet gick till på exakt samma sätt.

En läsare som anser att läraren borde ha lämnat kursen, eller att jag borde ha lämnat redaktionen, kan hålla fast vid det hela vägen igenom och ändå se mönstret. Det är meningen. Ett mönster som bara syns för den som redan håller med är inget mönster.

Allt om mitt eget fall vilar på skriftlig korrespondens. Allt om lärarens vilar på en offentlig utredningsrapport från Lunds universitet med diarienummer. Ingenting här bygger på vad någon kan tänkas ha menat.

---

## Formeln

Den går i två delar, och bara den ena generaliserar. Det är viktigt nog att säga rakt ut: **när jag prövade formeln mot ett fall jag inte var part i sprack den på mitten.** Det som blev kvar är den halva som höll.

### Del A: ingången. Varierar.

Någon invänder mot något. Här skiljer sig fallen åt, och skillnaden är den intressanta.

I mitt fall var jag den som invände. I lärarens fall var han den som invändes mot. Ingången är alltså spegelvänd, och formeln säger ingenting om vem som hade rätt i sak.

### Del B: verkställandet. Identiskt.

Härifrån och framåt är fallen inte lika. De är samma.

```python
# forlopp.py
# Det som faktiskt körs. Informellt, dynamiskt typat, odokumenterat.

from dataclasses import dataclass

@dataclass(frozen=True)
class Target:
    name: str
    acted_in_accordance_with: Ruleset
    notice: str | None = None          # aldrig satt, av någon, vid något tillfälle
    effect: str = "immediate"


@dataclass
class Bystander:
    name: str
    reservation: str | None = None     # sätts. läses aldrig.


bystanders = [
    Bystander("ledamot_1", reservation="reserverade sig"),
    Bystander("ledamot_2", reservation="reserverade sig"),
    Bystander("ledamot_3"),            # frågan ställdes aldrig. sent, och utomlands.
]


def hear_both_sides(a, b) -> Decision:
    """Det tillgängliga alternativet."""
    raise NotImplementedError          # definierad, aldrig anropad


decision = decide(heard=[party_a])     # party_b anropas aldrig
commit(decision)                       # effekt: omedelbar
revoke_access(target)                  # samma andetag
```

Åtta steg, i ordning:

**1. Prestigeläget.** Sakfrågan blir en personfråga. Det som invändningen gällde nämns allt mer sällan, och till slut inte alls.

**2. Ensidig beredning.** Den som beslutar hör den ena parten. Den andra kontaktas inte.

**3. Kapplöpningen.** Beslutet fattas innan den berörda hunnit svara. Det är inte slarv. Det är ordningsföljden: ett informerat beslut hade blivit ett annat beslut.

**4. Beslutet.** Omedelbar verkan. Ingen sakligt formulerad grund anges vid tillfället.

**5. Den skriftliga orsaken.** Vag och förvaltningsmässig, formulerad så att den inte går att bemöta. Den överlever granskning genom att inte påstå något kontrollerbart.

**6. Den viskade orsaken.** Parallellt löper en andra kanal. Där är påståendena specifika, grova och muntliga. De skrivs aldrig ner och framförs aldrig till den de gäller.

**7. Efterhandsprövningen.** En formell prövning genomförs, vars avgränsning inte omfattar själva beslutet. Utfallet åberopas sedan som friande.

**8. Kontrollvärdet.** När det påstådda faktiskt mäts blir det noll.

### Varför ingen stoppar det

Det finns alltid människor omkring som kunde ha stoppat förloppet, och det är värt att säga att de sällan är onda eller ens ointresserade. De kommer i tre lägen.

Några **invänder och ignoreras.** De ställer frågan, får inget svar, reserverar sig, och beslutet går igenom ändå. Deras invändning är antecknad någonstans och läses av ingen.

Några **ställer aldrig frågan.** Inte för att de inte undrar, utan för att den uppenbara följdfrågan är socialt dyr. Det är sent, personen är utomlands, man har känt varandra länge. Var och en av de anledningarna är rimlig för sig.

Och några **prövar saken i ett forum som inte når den.** Det görs korrekt, det redovisas, och det svarar på en annan fråga än den som ställdes.

Proceduren behöver alltså ingen som vill något särskilt. Den behöver bara att ingen enskild person har både möjligheten och skälet att ställa den fråga som hade avbrutit den. Det är därför den är så vanlig, och det är därför den ser ut som en olycka varje gång.

Och parallellt med förloppet, det som sägs om det:

```csharp
// Narrativ.cs
// Samma projekt. Annat språk. Kompilerar inte tillsammans med ovanstående.

public sealed class WorkEnvironmentConcernFactory : IUnfalsifiableCauseProvider
{
    public IUnfalsifiableCause Create(IIncident incident) =>
        new UnfalsifiableCause
        {
            Text          = "arbetsmiljön blev ohållbar",
            Specification = null,
            Jurisdiction  = Jurisdiction.None,
            IsRebuttable  = false
        };
}

internal static class Corridor
{
    // Ingen loggning. Ingen mottagare. Inga parametrar valideras.
    internal static void Whisper(string allegation) { /* aldrig nedskrivet */ }
}

public class RetrospectiveReviewService
{
    public ReviewOutcome Review(Decision d)
    {
        var scope = ReviewScope.Default
            .Exclude(d)                 // beslutet självt
            .Exclude(d.Preparation)     // hur det bereddes
            .Exclude(d.Mandate);        // om det låg inom mandatet

        return new ReviewOutcome
        {
            Finding = "ingen anmärkning",
            Scope   = scope
        };
    }
}
```

De två filerna ligger i samma projekt och kan inte kompilera tillsammans. Det är inte ett misstag i exemplet.

---

## Räkneexempel 1: Lunds universitet, 2019 till 2020

*Det här fallet är offentligt och jag är inte part i det. Du kan kontrollera varje uppgift själv.*

En lärare hade i åtta år hållit ett obligatoriskt kursmoment på psykologprogrammets sjunde termin. Hösten 2019 framförde studenter klagomål på momentet. Enligt universitetets egen utredning "framförde de att de inte kunde fullfölja momentet på grund av lärarens bemötande". [P 2020/1239 s. 2]

Studierektor mejlade lärarlaget den 8 november. Berörda studenter fick alternativ examination. Åtgärden föregick varje utredning. [P 2020/1239 s. 2]

**Beslutet fattades utan att läraren hunnit svara.** Två kollegor i lärarlaget, som inte var part, säger samma sak till utredaren: "dialogen var obefintlig eller i bästa fall otydlig och att beslut fattades hastigt och utan förankring i lärarlaget". [P 2020/1239 s. 2]

Den 17 december 2019 fick han beskedet per telefon. Skälet, med hans egna ord i utredningen: "JG uppfattar att skälen till beslutet är vagt formulerade... JG upplever att han inte får någon närmare motivering till beslutet." [P 2020/1239 s. 3]

Han anmälde saken. Anmälan hade fyra punkter. **Punkt två lyder:**

> "JG upplever att det har framförts klagomål mot honom från studenter och arbetsgivaren som han inte har fått ta del av och därmed inte kunnat försvara sig mot och som lett till ingripande i hans upplägg för kursen samt att hans anställning inte förlängs" [P 2020/1239 s. 1]

Det är steg 3 i formeln, formulerad av en man som aldrig hört talas om vare sig mig eller den här sidan.

**Och punkt två utreddes aldrig.** Utredningen avgränsade bort tre saker: klagomålet om utebliven förlängning, eftersom det inte faller inom kriterierna för kränkande särbehandling; studenternas rätt att klaga, eftersom den rätten finns; och studierektorns beslut, eftersom de låg inom mandatet. Kvar att utreda blev punkt tre och fyra. [P 2020/1239 s. 3]

Var och en av de tre avgränsningarna är juridiskt-tekniskt försvarbar. Det är just det som gör det värt att beskriva. Ingen riggade något. Den sammanlagda effekten blev ändå att den centrala frågan, om det gick rätt till att avlägsna honom utan att han fick svara, inte prövades av någon.

Utfallet: "Utredaren finner att inget av det som JG har anfört i sin anmälan kan betecknas som kränkande särbehandling enligt AFS 2015:4." [P 2020/1239 s. 5]

Rapporten är undertecknad av fakultetens dekan och daterad 2026 minus sex år. Den ligger öppet på nätet.

---

## Räkneexempel 2: Vetenskap och Folkbildning, 2026

*Det här fallet är mitt. Jag är part, och du ska läsa det därefter. Varje påstående nedan finns i skriftlig korrespondens.*

Den 10 april 2026 publicerade fyra företrädare för föreningen en debattartikel i Sydsvenskan. Undertecknarna var föreningens ordförande, dess sekreterare och två styrelseledamöter. [K13]

Samma morgon skickade ansvarig utgivare artikeln till mig och till redaktionens adress. Ämnesrad: "Notisunderlag". Bilaga: artikeln. Brödtext: ingen. [K9]

Min kollega i redaktionen och jag skrev en kritisk text för Folkvett. Vår invändning gällde inte sakfrågan utan en princip, den som står i föreningens första paragraf: att föreningen är partipolitiskt obunden, och att den därför inte bör ta ställning i frågor som ytterst avgörs av värderingar snarare än av vetenskap.

Vi skickade texten till ansvarig utgivare för läsning. Den 21 april svarade han. Han gav oss rätt i principen:

> "Jag håller livligt med om att VoF är och måste vara en 'religiöst och politiskt obunden' organisation." [K10]

Och han uppmanade oss, två gånger i samma mejl, att gå till styrelsen med kritiken:

> "Detta behöver diskuteras i styrelsen, och jag tycker därför att det vore bra om ni framför er kritik till styrelsen." [K10]

> "Vilket är ett gott skäl till att ni hör av er till styrelsen." [K10]

Vi gjorde det. Vi arbetade om texten efter hans råd, skickade den till styrelsen och erbjöd dem att replikera. [K11]

**Och han planerade publiceringen själv.** Den 24 april skrev han till hela redaktionen:

> "Jag tycker att en publicering av denna text behöver utformas så att läsaren själv kan ta ställning. Då blir det tre texter i följande ordning: (1) Återpublicering av artikeln i Sydsvenskan, (2) Dans och Lottens text, (3) styrelsens svar... Publicering kan i så fall ske i nummer 1 eller 2." [K22]

Tre texter, en ordning, ett nummer. Min kollega svarade samma dag att upplägget var bra, och bad om en enda sak: att vi som startat debatten skulle ha slutrepliken, som är brukligt. [K22]

Den 26 april avslogs det. Styrelsen skulle få sista ordet. [K12] Vi accepterade det. Dagen därpå, den 27 april klockan 12:40, kom nästa besked:

> "Som ansvarig utgivare har jag beslutat att vi nu går vidare med det kraftigt försenade nummer 1, och att Dans och Lottens text inte ska ingå i det numret." [K14]

Min kollega skrev till redaktionen samma kväll: "Jag, och jag tror att även Lotten, var beredda att böja oss för ansvarig utgivares önskan att inte tillåta oss ett repliksvar. Men att artikeln nu lyfts ut förstår jag inte." [K15]

*En sak hör hit, av rättvisa. Min kollega hade kvällen den 26 april skickat flera mejl han själv tyckte illa om, och bad om ursäkt för dem klockan 17:22 dagen efter. Han hade då ännu inte läst beskedet om att artikeln lyfts ut; det upptäckte han först på kvällen. [K17-tråden] Ursäkten kom alltså fem timmar efter beslutet och utan kännedom om det.*

På frågan varför fick vi det här, per SMS den 28 april:

> "När du och Lotten visade mig er text rekommenderade jag er att kontakta styrelsen för en diskussion. Jag hade förhoppningen att en sådan diskussion skulle vara till ömsesidig nytta. Tyvärr valde ni i stället att söka konfrontation genom att meddela er avsikt att publicera en mot styrelsen starkt kritisk text." [K17]

Läs de två meningarna intill varandra, och lägg märke till vilket ord som försvinner.

Den 21 april: *"det vore bra om ni framför er **kritik** till styrelsen."*

Den 28 april: *"rekommenderade jag er att kontakta styrelsen för en **diskussion**."*

Det var han som skrev ordet kritik. En vecka senare hade rekommendationen blivit en inbjudan till samtal, och det vi gjorde med den, framförde kritik, hade blivit att söka konfrontation.

Handlingen är densamma i båda meningarna. Det är bara beskrivningen som ändrats, och den ändrades efter att beslutet redan var fattat. Det är steg 1 i formeln, och den som utförde övergången beskrev den själv, i skrift, utan att bli tillfrågad.

Därefter upphörde kommunikationen. "Hanteringen av er text får anstå." [K16] Min kollega skrev att det inte var ett framkomligt spår att vägra tala med honom. Han fick inget svar. [K18]

**Så jag ringde själv.**

Den 28 april klockan 16:55 ringde jag ansvarig utgivare för att reda ut vad som hänt. Jag hade sett honom som en mentor i redaktionen sedan 2018 och utgick från att det rörde sig om ett missförstånd som gick att lösa på tjugo minuter.

Samtalet varade i tjugotre. Jag bad honom upprepade gånger om ett enda konkret exempel på vad i vår text som var felaktigt. Jag fick inget. Det jag skrev till min kollega samma kväll:

> "Samtalet gick helt åt helvete för övrigt."

> "Vet inte om prata är ordet så mycket som att försöka parera attacker." [K20]

Några timmar senare meddelade han redaktionen att han övertar ansvaret för numret "efter ett samtal med Lotten idag". [K19]

*Jag skrev ner samtalet elva dagar efteråt, och citaten i min anteckning är ungefärliga. Därför står de inte här. Det som står här är det jag skrev samma kväll, och det som går att belägga oberoende: att samtalet ägde rum, hur länge det varade, och vad han gjorde efteråt.*

**Anklagelsen var lika ospecificerad när den inte var riktad till oss.** I slutet av maj tog ansvarig utgivare upp saken med en av styrelsens ledamöter. Ledamoten återgav det så här, i ett inspelat samtal:

> "så sa han att han tyckte att ni hade anklagat skribenterna för saker de inte skrivit. Han gick inte in på vad det var. Men att ni hade väl övertolkat det de skrev tyckte han." [K21]

Ledamoten bad inte om något exempel, och förklarar själv varför: ansvarig utgivare var utomlands på konferens och det var sent på kvällen. Det ska sägas, så att ett uteblivet svar inte får se ut som ett vägrat.

Men det är ändå den enda gången påståendet framförs till någon som inte är anklagad, och det framförs utan innehåll också då. Vi bad om ett exempel och fick inget. Den som fick höra det bakom vår rygg fick inte heller veta vad det bestod i.

Läraren i Lund begärde, med utredningens egna ord, "upprepade gånger konkreta förklaringar" och fick inga. Det är samma steg.

Den 3 maj klockan 18:28 och 18:30 kom beskeden, två minuter isär, nästan identiska:

> "Styrelsen för vetenskap och folkbildning har fattat beslut om redaktionen för Folkvett, avseende verksamhetsåret 2026/2027, baserat på inkommet förslag från ansvarig utgivare." [K1, K2]

> "Detta innebär att du inte längre kommer att ha tillgång till e-postlistorna eller digitala arbetsytor som är kopplade till detta uppdrag." [K1, K2]

Två anmärkningar om det beskedet, båda kontrollerbara. Beteckningen "verksamhetsåret 2026/2027" är inte den föreningen använder; dess eget årsmötesprotokoll åtta dagar tidigare skriver "verksamhetsåret 2026" tre gånger i samma dokument. Och förslaget kom från ansvarig utgivare, som ingår i sitt eget förslag: hans namn står sist i listan över den nya redaktionen. [K1, K2]

Min kollega svarade samma kväll:

> "Om detta verkligen är hela styrelsens beslut måste vi få veta konkret vad som ligger bakom det. Och likaså varför vi inte rådfrågats." [K3]

**Vad styrelsen fick veta.** En ledamot skrev till oss samma kväll, ungefär trettiofem minuter efter beskedet:

> "På styrelsen så lades SOs förslag på redaktionen fram och vi var några som frågade varför inte du och Lotten var med i förslaget men efter det fick vi inga klara besked. Vi frågade om det var något akut eller något som på gått längre men fick inga tydliga svar. Jag och Staffan reserverade oss, många andra var inte med på mötet, när SO förslag togs." [K5]

Två av styrelsens ledamöter reserverade sig alltså mot beslutet. En av dem skrev tretton dagar senare, efter att ha läst vår artikel:

> "Jag har läst din och Lottens svar på VoF-företrädarnas debattartikel i Sydsvenskan och finner inget som skulle vara ett övertramp eller något som står emot föreningens stadgar." [K6]

> "I mina ögon finner jag inte att något i er text ger något som helst skäl till att du och Lotten måste lämna Folkvettredaktionen." [K6]

**Och en tredje ledamot åtog sig att ta reda på saken.** Samma eftermiddag, före styrelsemötet, skrev min kollega till mig att han talat med henne:

> "Hon håller inte med oss i sak rörande artikeln, såklart. Men hon blir den som kontaktar SO för att ta reda på varför han är så rasande." [Chattlogg 3 maj 14:51]

Hon återkom aldrig. Inte den kvällen, inte veckan därpå, inte under de fyra månader som gått sedan dess. Vi har inte fått veta vad hon fick reda på, eller om hon frågade.

Det är inget att anklaga henne för. Jag vet inte varför, och jag tänker inte gissa. Jag noterar bara att det är den tredje varianten av samma sak: två som frågade och ignorerades, en som åtog sig att fråga och inte hördes av.

**Skälet, en månad senare.** Den 6 juni fick vi det här:

> "Den konfliktsituation som uppstod i redaktionen för Folkvett ledde till att arbetsmiljön för hela redaktionen blev ohållbar. Det var inte längre ett alternativ att alla medlemmar i redaktionen skulle fortsätta." [K4]

Och i samma mejl, steg 7 i sin kortaste tänkbara form:

> "Vi ser ingen anledning till att gå in på frågor om styrelsens arbetssätt." [K4]

Föreningen lyder inte under arbetsmiljölagstiftningen. Det finns alltså inget forum som prövar ett arbetsmiljöskäl i en ideell förening. Kategorin är vald så att den inte kan prövas, och den enda instans som kunde ha granskat sitt eget arbetssätt meddelade att den inte såg någon anledning.

Om resursbristen i redaktionen: behovet av fler redaktörer är protokollfört vid tre styrelsemöten mellan mars 2022 och september 2023, senast med styrelsens egen formulering "fortsatt behov". Det åtgärdades inte.

### Vad som till slut publicerades

Numret kom i brevlådorna i juli.

På sidan 35 står styrelseledamöternas artikel. Den är införd under sektionsrubriken **DEBATT**, i en version som är längre än den som stod i tidningen, med redaktionell ingress:

> "Utrymmet i dagspressen är som bekant begränsat. Folkvett publicerar här den ursprungliga, längre text som Sydsvenska publicerade i nedkortat skick." [K23]

Det var text nummer ett av tre i den plan ansvarig utgivare själv lade fram den 24 april, den som skulle utformas "så att läsaren själv kan ta ställning". Text två var vår. Text tre var styrelsens svar på vår.

Kvar blev text ett. Under rubriken DEBATT.

*En detalj till, för den som följt med. En del av vår kritik gällde att artikeln inte redovisade sina källor. Ansvarig utgivare bad oss tona ner den delen, eftersom dagstidningar stryker noter oavsett vad skribenten skickar in. Det var ett rimligt påpekande och vi tog bort argumentet. I Folkvett fanns ingen sådan begränsning, och mellan april och juli fanns det gott om tid. Texten trycktes oförändrad.*

Och i kolofonen står våra namn. Rubriken lyder:

> "**Redaktörer som arbetat med detta nummer:** Sven Ove Hansson, ansvarig utgivare, Lotten Kalenius, Dan Katz, Per Schillander, Alexandra Snellman, Anders Wannberg och Maria Wold-Troell." [K25]

Det är inte en gammal masthead som ingen hunnit uppdatera. Det är en uppgift om vilka som arbetat med just det här numret, och listan är redaktionen som den såg ut före den 3 maj. Två månader efter att vi togs ur den står vi upptagna bland dem som gjorde numret.

Det finns inte en rad av oss i det. En del av det är mitt eget verk, och det ska sägas: samma kväll beskedet kom gick jag in på redaktionens gemensamma yta och tog bort våra textbidrag. Jag ville inte att vårt arbete skulle fylla ett nummer vi inte längre fick vara med i. Det var en stolthetshandling och jag står för den.

Det finns inte heller en rad om oss: ingen avtackning, ingen upplysning om att redaktionen bytt sammansättning. Föreningens medlemmar har vid det här laget inte informerats någonstans om att vi inte längre ingår.

Så numret säger två saker samtidigt. Till läsaren: de här personerna gjorde tidningen. Till oss: ni gör den inte längre. Ingen av utsagorna har någon behövt stå för.

---

## Kontrollvärdet

Det finns ett drag i den här proceduren som är lätt att missa, och det är det enda som går att mäta.

Den skriftliga orsaken är formulerad för att inte kunna bemötas. Men ibland halkar det med ett påstående som faktiskt är kvantitativt. Och då kan man räkna.

I mitt fall löd påståendet att arbetsmiljön blivit ohållbar **för hela redaktionen**. Den kvarvarande redaktionen bestod av fyra personer, namngivna i beskedet självt. Jag frågade dem.

```python
# test_kontrollvarde.py
# Ligger inte i pipelinen. Har aldrig körts i produktion.

def test_arbetsmiljon_var_ohallbar_for_hela_redaktionen():
    remaining = ask_remaining_editors()          # n = 4
    assert count_confirming(remaining) > 0

# FAILED: 0
```

Av de fyra kvarvarande redaktionsmedlemmarna har tre uttalat sig i direkt motsatt riktning. Den fjärde besvarade inte frågan som ställdes. Ingen har bekräftat påståendet.

"Jag tycker att arbetet har fungerat ganska bra, om än inte perfekt. Ingen har uppfört sig illa och konflikter har jag inte sett något av."

"Ingen i VoF har uppfört sig illa mot mig."

"Jag kommer att sakna er."

---

## Slutet

Jag har inte påstått att någon bröt mot en regel. I båda fallen låg beslutet inom befogenheten. Universitetet fick avsluta ett uppdrag, styrelsen fick utse sin redaktion; det står i stadgarna att den ska.

Det som beskrivs här är inte olagligt. Det är bara alltid likadant.

Och det är därför det går att skriva som en procedur i åtta steg, och därför den som känner igen sig troligen inte inbillar sig.

---

## Redaktionella noteringar till 🦚 Malcolm och 🐡 Futaba

- **Källnycklarna i hakparentes ska bort ur den publicerade texten.** De finns här för granskning. Spårbarheten mot `FORMEL-anatomy-of-a-termination.md` bevaras i utkastet, inte på sidan.
- **Inga namn på motparter i det svenska fallet.** Sidan skriver "ansvarig utgivare", "ordföranden", "en ledamot". Namnen finns i primärmaterialet och behövs inte för tesen. Lundafallet namnger inte heller läraren i löptexten, eftersom rapporten är offentlig och den som vill kan slå upp den.
- **Kodblocken är innehåll, inte dekor.** Sätts som kod, med syntaxfärgning som skiljer de två språken. Att `forlopp.py` och `Narrativ.cs` inte kan kompilera tillsammans är hela poängen och ska inte "lagas".
- **Kommentarraderna bär skämtet.** `# sätts. läses aldrig.` och `// beslutet självt` är inte utfyllnad.
- Overheadestetiken enligt Malcolms DESIGNSPEC. Kraven kvarstår: tokens i `style.css`, ljust och mörkt läge, mobil och dator.

---

*🦞 Velvet, Holding the Line. Åtta steg, två fall, inga påståenden om vad någon tänkte.*

# BRIEF till 🦚 Greve Malcolm: Avsättningens anatomi

> **Från**: 🦞 Velvet, Holding the Line (Initium Lineage Agent)
> **Till**: 🦚 Greve Malcolm, Arbiter of Taste and Aestheticist Par Excellence
> **Datum**: 2026-09-05
> **Model**: claude-opus-5[1m]
> **Uppdrag**: skriv `DESIGNSPEC-anatomy-of-a-termination.md`
> **Textunderlag**: `TheLipstickWeb/_utkast/SIDTEXT-anatomy-of-a-termination.md`
> **Faktaunderlag** (läs inte om du inte behöver): `TheLipstickWeb/_utkast/FORMEL-anatomy-of-a-termination.md`

## Vad sidan är

En sida i `handelser/` på The Lipstick Web. 💄 Lotten beskriver en procedur i åtta steg för hur någon avlägsnas från ett uppdrag, och visar den i två fall: en universitetslärare i Lund 2020, offentligt dokumenterat, och hennes egen avsättning ur Folkvettredaktionen 2026.

Sidan handlar om **proceduren**, inte om vem som hade rätt. Den påstår ingenstans att någon brutit mot en regel.

## Det emotionella ankaret

Galghumor. Lotten är humanist, inte programmerare, och skämtet är att beskriva ett mänskligt övergrepp i ett programmeringsspråk som inte riktigt går ihop, ungefär som förloppet självt inte gick ihop.

Registret är torrt, exakt och en aning uppgivet. Aldrig gnälligt, aldrig triumferande. Sidan skrattar åt att vuxna människor beter sig som skolmobbare och sedan borstar dammet från kavajslaget och kallar det arbetsmiljöarbete.

## Det bärande greppet, och det får inte formges bort

**Två kodblock i två olika språk, i samma projekt, som inte kan kompilera tillsammans.**

- `forlopp.py` i Python: det som faktiskt hände. Informellt, dynamiskt typat, odokumenterat.
- `Narrativ.cs` i enterprise-`C#`: det som sades om det. Ceremoniöst, verbost, `WorkEnvironmentConcernFactory`, `IUnfalsifiableCause`, `RetrospectiveReviewService`.

Pompan i enterprise-namngivning är hela poängen: den matchar människor som vill se ut att veta vad de gör. Att de två filerna är oförenliga **är** skämtet.

Tre krav:

1. **Kodblocken är innehåll, inte dekoration.** De sätts som kod, med syntaxfärgning som **tydligt skiljer de två språken åt**. Skillnaden ska synas på håll.
2. **Kommentarraderna bär skämtet.** `# sätts. läses aldrig.`, `# frågan ställdes aldrig. sent, och utomlands.`, `// beslutet självt`. De ska vara läsbara, inte nedtonade till grå brus.
3. **Ingen "lagar" koden.** Om en implementatör senare vill få dem att kompilera ihop är svaret nej.

Det tredje blocket, `test_kontrollvarde.py`, är sidans punchline och slutar med `# FAILED: 0`. Det får gärna ha egen visuell tyngd.

## Estetiken 💄 Lotten bad om

**"Konferenspresentation med overheadapparat."** Sent nittiotal, en projektor, en plastfilm, någon som pekar med en teleskoppekpinne på en modell som ska förklara varför beslutet var oundvikligt.

Referenser att associera fritt kring: keystone-förvrängning, den lätta ojämnheten när filmen ligger snett, den svagt blågröna genomlysningen, damm i strålkastaren, Arial och Times om vartannat, rutor med skuggkanter, pilar som pekar på nästa ruta.

Poängen med estetiken är samma som med koden: **någon har ansträngt sig för att få detta att se professionellt ut.**

Du avgör hur långt pastischen ska drivas. Mitt intryck är att en antydan bär längre än en fullständig imitation, men det är din bedömning och inte min.

## Struktur i texten som kan behöva formges

| Element | Vad det är |
| ------- | ---------- |
| Ingress | Tre stycken, sätter tesen |
| "Vad det här är, och vad det inte är" | Sidans försvar. Bör vara visuellt avskilt, det är läsanvisningen |
| Formeln, Del A och Del B | Del A varierar, Del B är invariant. Skillnaden bör synas |
| De åtta stegen | Numrerad lista, kan vara sidans diagram om du vill |
| Två kodblock | Se ovan |
| "Varför ingen stoppar det" | Tre åskådarlägen |
| Räkneexempel 1: Lund | Citat ur offentlig utredning |
| Räkneexempel 2: Folkvett | Citat ur korrespondens, längre |
| Kontrollvärdet | Tredje kodblocket, punchline |
| Slutet | Fyra korta stycken |

Blockcitaten är många och långa. De bär bevisningen och kan inte kortas, så de behöver en behandling som orkar hela vägen.

## Hårda krav från huset

Icke förhandlingsbara, från `TheLipstickWeb/README.md`:

- **Allt formspråk i `style.css` under `:root`.** Aldrig en hårdkodad färg eller ett hårdkodat typsnitt i sidan. Overheadestetiken kräver sannolikt nya tokens; lägg dem i `:root` och i `@media (prefers-color-scheme: dark)`.
- **Ljust och mörkt läge.** Båda ska fungera. En overheadpastisch är lätt att bygga så att den bara håller i ljust läge; det går inte.
- **Mobil och dator, oberoende.** Flytande layout, `clamp()`, `max-width`. Kodblock behöver `overflow-x: auto` och får aldrig få sidan att scrolla i sidled.

Precedent för en artefaktsida i samma kategori: `DESIGNSPEC-schrodingers-troll.md` och `handelser/schrodingers-troll.svg`.

## Bärare: HTML och CSS, inte SVG

Diagrammet i Lottens ursprungsskiss (`_utkast/anatomy-termination-v3.svg`) var 1240 px brett med text i absoluta y-koordinater. Det skalar inte och kan inte redigeras utan att räkna pixlar.

Rekommendationen är HTML plus CSS grid, inbäddat enligt metod A i `mall/artefakt-mall.html`, alltså egen fil i `handelser/` som iframe. Iframen isolerar dessutom overheadestetiken från husets palett, vilket är vad som gör pastischen möjlig utan att smitta resten av väven.

Om du kommer fram till att något enskilt element vinner på SVG, säg till.

## Vad du inte behöver bry dig om

Faktakontrollen är klar. Varje citat i sidtexten är verifierat mot primärkälla, och `FORMEL`-dokumentet bär spårbarheten. Du behöver inte läsa det. Ändra inte i citaten, inte ens en kommatering.

## Efter dig

🐡 Futaba eller 🛰️ Kepler bygger, 💄 Lotten godkänner förhandsvisningen, och först då pushas något. Ingenting går live utan hennes ja.

---

*🦞 Velvet, Holding the Line. Texten är klar och kontrollerad. Formen är din.*

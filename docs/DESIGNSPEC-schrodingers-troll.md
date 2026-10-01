# DESIGNSPEC: Schrödingers troll — SVG-illustration

> **Projekt**: The Lipstick Web
> **Sida**: Händelser — "Schrödingers troll"
> **Typ**: Inline SVG-illustration, logikdiagram
> **Levererat av**: 🦚 Greve Malcolm, 2026-06-15
> **Implementeras av**: 🐡 Futaba


## Emotionellt ankare

En konversationstråd som är redan stängd när du öppnar den. Du läser dina egna ord — korrekta, varsamma, välformulerade — och förstår att de aldrig hade en chans att landa. Observatören var där innan du var.

Allt i illustrationen prövas mot det rummet.


## Konceptet i ett mening

En logisk triangel vars alla tre vägar leder till samma dom — formgiven som en kvantmekanisk vågfunktion som kollapsar vid observation.


## Kanvas

- **Storlek**: 640 × 560 px, viewBox="0 0 640 560"
- **Bakgrundsfärg**: `--paper-warm` (`#faf6ed` ljust / `#201829` mörkt)


## Triangelgeometri

**Orientering**: inverterad — spetsen pekar nedåt, basen upp. Roteras 5–8 grader medurs utöver den rena inversionen, precis nog för att registreras som instabil utan att analyseras medvetet.

**Ungefärliga hörn** (justeras för att ge utrymme för etiketterna):
- Övre vänster (GÖR INGET): ca (120, 130)
- Övre höger (GÖR NÅGOT): ca (520, 130)
- Undre spets (KRITISERAR): ca (320, 430)

**Sidornas form**: inte raka linjer utan sinusvågor. Dela varje sida i 20–24 interpolerade punkter, applicera `sin(t * π * 5) * 4` vinkelrätt mot kantens riktning på varje punkt, bygg sedan en smooth cubic bezier-kurva genom punkterna. Amplitud 4 px, 2,5 cykler per sida.

Effekten ska vara att kanterna darrar utan att se trasiga ut — en fryst vågfunktion, inte ett handritningsskavsår.


## Hörnnoder

Varje hörn har en dubbelexponerad nodstruktur som representerar superposition:

| Lager | Radie | Fyllning | Opacitet |
| ----- | ----- | -------- | -------- |
| Yttre halo | 16 px | `--rouge` | 12 % (ljust) / 15 % (mörkt) |
| Inre kärna | 5 px | `--rouge` | 100 % |

Ingen stroke på noderna.


## Centrumhalo

En ellips centrerad i triangelns centroid (ungefär 320, 297):
- Storlek: 90 × 50 px
- Fyllning: `--aubergine` (`#502846`) vid 8 % opacitet (ljust) / 12 % (mörkt)
- Ingen stroke

Ska knappt synas — mer en täthet i luften än ett synligt objekt.


## Bakgrundsstruktur (kvantbrus)

Horisontella sinusvågor som täcker hela kanvasen:
- Periodavstånd: 14 px vertikalt
- Amplitud: 1,5 px
- Stroke: `--hairline`, 0,4 px
- Opacitet: 5–6 %

Existerar för att ge textur åt handen, inte för att ses av ögat.


## Typografi och hierarki

### Rubrik — "Schrödingers troll"
- **Font**: Fraunces
- **Storlek**: 18 px
- **Placering**: centrerat, ca y=60 (ovanför triangeln, ca 22 px från kanvasbräddarna)
- **Färg**: `--ink` (`#1a1020` / `#f0e8f2`)
- **Transform**: ingen — vanliga versaler i Fraunces, inga gapet-kapitäler

### Hörnetiketter — "GÖR INGET" / "GÖR NÅGOT" / "KRITISERAR"
- **Font**: IBM Plex Mono
- **Storlek**: 12 px
- **Style**: uppercase, letter-spacing 0.08em
- **Färg**: `--ink` vid 85 % opacitet
- **Placering**: 12 px utanför nodens yttre halo, bort från triangelns centrum
  - Övre vänster: högerkantsanpassa mot hörnet
  - Övre höger: vänsterkantsanpassa mot hörnet
  - Undre spets: centrera nedanför noden

### Förklaringstexter (under varje etikettblock)
- **Font**: Newsreader Italic
- **Storlek**: 11 px
- **Färg**: `--muted` (`#7a5870` / `#c4a8c0`)
- **Radavstånd**: 1,4
- **Max**: 2 rader
- **Innehåll**:
  - Under GÖR INGET: *"ser ut som ett passivt alt-konto"*
  - Under GÖR NÅGOT: *"för kort historik i servern"*
  - Under KRITISERAR: *"tolkas som brigading"*

### Centrumtext — "TRIANGELN ÄR SLUTEN"
- **Font**: IBM Plex Mono
- **Storlek**: 11 px
- **Style**: uppercase, letter-spacing 0.12em
- **Färg**: `--rouge` (`#a61c3a` / `#e35d76`)
- **Placering**: centrerat i triangelns centroid, ca y=290–300
- **Radbrytning**: "TRIANGELN" på en rad, "ÄR SLUTEN" på nästa

### Signaturdetalj — Baynes-formeln
- **Text**: P(troll | ny användare) = 1
- **Font**: IBM Plex Mono
- **Storlek**: 9 px
- **Färg**: `--muted` vid 70 % opacitet
- **Placering**: 8 px under centrumtextens sista rad, centrerat
- **Syfte**: en not i marginalen för den läsare som parar ihop matematiken med artikelns argument. Inte för alla — ge det inte för mycket plats.


## Palettsammanfattning

| Element | Ljust läge | Mörkt läge |
| ------- | ---------- | ---------- |
| Bakgrund | `#faf6ed` | `#201829` |
| Triangelkanter (våglinjer) | `#a61c3a` | `#e35d76` |
| Hörncirklar (kärna) | `#a61c3a` | `#e35d76` |
| Hörncirklar (halo) | `#a61c3a` 12 % | `#e35d76` 15 % |
| Centrumtext | `#781328` | `#e35d76` |
| Rubrik + hörnetiketter | `#1a1020` | `#f0e8f2` |
| Förklaringstexter | `#7a5870` | `#c4a8c0` |
| Bakgrundsstruktur | `#dcd0bc` | `#362440` |
| Centrumhalo | `#502846` 8 % | `#502846` 12 % |


## Vad är centrum, vad är periferi

**Centrum**: "TRIANGELN ÄR SLUTEN" + Baynes-formeln — domen, omgiven av aubergine-halon.

**Periferi**: bakgrundsstrukturen och haloernas yttre ringar. Närvaro utan accent.

**Övergångszonen**: hörnen med etiketter och förklaringstexter — tillstånden *före* kollapsen. Läsbara, inte dramatiska.


## Leveranskrav

- SVG ska fungera inline i HTML
- Teckensnitten är redan laddade via sajten — inga extra `<link>`-taggar behövs i SVG-filen
- Dark mode via `@media (prefers-color-scheme: dark)` i ett `<style>`-block inuti SVG:n
- Placering på sidan: efter artikelns ingress, före brödtexten

---

*🦚 Greve Malcolm, Arbiter of Taste and Aestheticist Par Excellence*

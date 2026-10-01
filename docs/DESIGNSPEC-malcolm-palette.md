# 🦚 Designspec: The Lipstick Web — Palettrevision

> **Datum**: 2026-06-15  
> **Beställare**: 🦚 Greve Malcolm, Arbiter of Taste  
> **Implementatör**: 🐡 Futaba  
> **Fil att redigera**: `style.css`  
> **Scope**: CSS-tokens i `:root` och `@media (prefers-color-scheme: dark)`


## Emotionellt ankare

En lätt gulnad anteckningsbok inkilad mellan *Kvantfysik för nybörjare* och Balzacs kompletta verk. Du hittar den av misstag, börjar läsa, och glömmer att du stod och väntade på regnet att sluta.

Ljust läge: bokhandeln med dagsljus genom dammigt glas — krämblek, varm, full av textur. Mörkt läge: efter stängningstid, aubergine-mörkt, kuriöst. Rouge och aubergine är Lotten — den som satte märket medvetet.

*Allt i denna spec måste kännas hemma i det rummet.*

## Vad som bevaras

Inga ändringar i typografi, layout eller HTML-struktur. Fraunces, Newsreader och IBM Plex Mono är korrekta val och rörs inte. Strands-metaforen i navigationen bevaras intakt. Responsiviteten och dark mode-mekaniken (`prefers-color-scheme`) förblir oförändrade i sin logik — jag justerar enbart vad tokenvärdena pekar på.

## Tokenjusteringar — ljust läge (`:root`)

| Token | Claudes värde | Malcolm | Raison |
| ----- | ------------- | ------- | ------ |
| `--paper` | `#f7f3f4` | `#f3ede0` | Foxat, varmt — åldrad kräm, inte spa-hotell |
| `--paper-warm` | `#f1e9eb` | `#ece4cf` | Djupare kräm för intern kontrast |
| `--surface` | `#ffffff` | `#faf6ed` | Ingen yta är kall vit i den här butiken |
| `--ink` | `#1b1418` | `#1a1020` | Aubergine-svart, inte brunt-svart |
| `--mauve` | `#6e5b62` | `#7a5870` | Skiftar mot aubergine, bort från rosa |
| `--rouge` | `#ae1b3b` | `#a61c3a` | En nyans mer *déterminé* |
| `--rouge-deep` | `#7e1329` | `#781328` | Hover är en avsikt, inte en färg |
| `--hairline` | `#e4d8db` | `#dcd0bc` | Boksida-crease, inte rosa |

## Ny token: `--aubergine`

Lägg till i `:root`-blocket (gäller båda lägena — kan finjusteras per läge om behov uppstår senare):

```css
--aubergine: #502846;   /* Malcolm-signatur */
```

Denna token används inte explicit i stil-reglerna ännu — men den ska finnas namngiven och redo för sidfoten och framtida strukturelement. Malcolm-signaturens aubergine är `#502846`, inte ett lösryckt hex-värde.

## Tokenjusteringar — mörkt läge (`@media (prefers-color-scheme: dark)`)

| Token | Claudes värde | Malcolm | Raison |
| ----- | ------------- | ------- | ------ |
| `--paper` | `#161114` | `#160f1c` | Aubergine-mörker, inte parkeringshus-källare |
| `--paper-warm` | `#1c151a` | `#1c1424` | Djup aubergine |
| `--surface` | `#1f1820` | `#201829` | Lätt lyft mot aubergine |
| `--ink` | `#f1e7ea` | `#f0e8f2` | Lätt aubergine-ton i ljustexten |
| `--mauve` | `#c1abb3` | `#c4a8c0` | Aubergine-grå, bort från rosa-grå |
| `--rouge` | `#e35d76` | `#e35d76` | Oförändrad — fungerar som den är |
| `--rouge-deep` | `#f2899e` | `#f2899e` | Oförändrad — fungerar som den är |
| `--hairline` | `#3a2e33` | `#362440` | Aubergine-skugga, inte varm grå |

## Implementationsordning

1. Redigera `:root`-blocket: byt ut de 8 befintliga tokenvärdena, lägg till `--aubergine` med kommentaren `/* Malcolm-signatur */`.
2. Redigera `@media (prefers-color-scheme: dark)`-blocket: byt ut de 8 berörda värdena (rouge-paret lämnas orört).
3. Kontrollera att inga av de gamla hex-värdena finns hårdkodade utanför `:root` i stilreglerna.

## Commit-meddelande

```text
style: Malcolm palettrevision — aubergine & foxat kräm
```

## Verifiering (icke förhandlingsbart)

- [ ] **Ljust läge**: alla ytor, texter och accenter läsbara och stämmer med bokhandels-ankaret
- [ ] **Mörkt läge**: aubergine-ton i bakgrund och hairlines, rouge-accenter tydligt synliga
- [ ] **Mobilvy**: ingen layout-förändring uppstår (tokenjusteringar påverkar inte layout)
- [ ] **Live**: pusha och verifiera på `https://truelipstick.github.io`

---

> *🦚 Greve Malcolm, Arbiter of Taste and Aestheticist Par Excellence*

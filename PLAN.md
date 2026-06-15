# 📋 Projektplan — 💄 The Lipstick Web

> **Projekt**: The Lipstick Web — statiskt GitHub Pages-bygge för kurerade tankar
> **Plats**: `TheLipstickWeb/` i HackerLipstick-workspace
> **Skapad**: 2026-06-14
> **Författare**: 🦞 Velvet, Holding the Line
> **Status**: 🟢 Live — Fas 3 klar, sajten publik och formgiven på `https://truelipstick.github.io`. Nästa: Fas 4 (första riktiga innehåll + losa/-test)

---

## 🎯 Vad vi bygger

Ett litet statiskt hem på nätet för kurerade tankar. Inga ramverk, ingen byggprocess, ingen databas — bara HTML-filer som GitHub Pages serverar rakt av. Grundstomme, stilmall och mallar är klara (Claudes filer). Live-adress blir `https://truelipstick.github.io`.

---

## 👥 Roller

| Agent | Ansvar |
| ----- | ------ |
| 🦞 Velvet | Projektledning, struktur, samordning |
| 🛰️ Kepler | Repo, commits, Pages-publicering (implementatör) |
| 🐡 Futaba | Implementation, kod, global config (`kilo.jsonc`) |
| 🦚 Greve Malcolm | Formgivning av landningssidan (tokens i `style.css`) |
| 📐 Frances Lloyd Wright | Arkitektur — *vilande, startas vid första riktiga arkitekturbeslut* |

---

## 🚦 Genomförandeplan

### Fas 0 — Förberedelser ✅ KLAR

- [x] Projektmapp `TheLipstickWeb/` upplagd
- [x] `files.zip` uppackad (komplett tree med `losa/`)
- [x] TTfH-texter lagda i `docs/`
- [x] Frances Lloyd Wright: beslut = **vänta**, emoji = 📐 (vald)
- [x] Projektplan (denna fil)

### Fas 1 — Kepler-prepp ✅ KLAR

- [x] Hugin ser över Keplers systemprompt: GitHub + Pages-expertis utöver Obsidian
- [x] Keplers emoji byts till 🛰️ (agentfil + `kilo.jsonc` + signaturregister)
- [x] Futaba synkar frusen prompt-kopia + edit-glob i `kilo.jsonc`
- [x] **Approval-gate**: Lotten godkände Keplers nya prompt (2026-06-14)
- [x] **HTML-beslut**: Kepler får `*.html` i sin edit-glob — skriver sidorna själv (se Flaggor nedan)

### Fas 2 — Repo + Pages live ✅ KLAR (2026-06-15)

- [x] Beslut: **publikt** repo för sajten (Lotten godkände 2026-06-14). Inget separat privat byggrepo — testfiler/temporärt byggskräp `.gitignore`:as istället.
- [x] Futaba la `*.html: allow` i Keplers edit-block (båda källorna, identiska, verifierat 2026-06-14)
- [x] `TheLipstickWeb/` gjordes till eget git-repo (workspace-mönster) — commit `f253823`, 15 filer
- [x] Lotten skapade GitHub-repot `TrueLipstick/truelipstick.github.io` manuellt (gh CLI ej inloggat)
- [x] Push efter Lottens godkännande (approval-gate respekterad)
- [x] Lotten aktiverade Pages → Deploy from a branch → `main` / `/ (root)`
- [x] **Live verifierad**: `https://truelipstick.github.io` svarar 200 OK (`/`, `/style.css`, `/losa/not-i-marginalen.html`, kategorisidor)
- [x] `index.html` i repo-roten — Pages-fällan undveken

### Fas 3 — Formgivning ✅ KLAR

- [x] Malcolm: formgivningspass på landningssidan via tokens i `style.css`
- [x] Verifiera ljust + mörkt läge (icke förhandlingsbart krav)
- [x] Verifiera oberoende mobil- + datorvy (flytande layout)

### Fas 4 — Första riktiga innehåll + losa/-test

- [ ] Lottens exempel-lösa sida förs in som första `losa/`-post
- [ ] Slumpslug genereras (`python3 -c "import secrets; print(secrets.token_hex(8))"`)
- [ ] Skarp test av noindex-flödet
- [ ] Första riktiga inlägg i en kategori

---

## ⚠️ Flaggor och öppna frågor

### Repo: publikt — BESLUTAT 2026-06-14

En `user site` på `truelipstick.github.io` måste ligga i ett **publikt** repo för att Pages ska publicera gratis (privat user-site Pages kräver GitHub Enterprise). Källkoden till en statisk sajt är ändå allt som syns i "view source" på den live-publicerade sidan, så publikt repo läcker inget utöver vad besökaren redan ser.

**Beslut**: ett enda publikt repo. Inget separat privat byggrepo (onödigt krångligt) — testfiler och temporärt byggskräp hanteras med `.gitignore`.

README bekräftar (rad 54, 72): gratisplanen = publikt repo, ingen inloggning. För sidor som faktiskt kräver behörighet gäller Azure Static Web Apps, inte Pages.

### Kepler får skriva HTML — BESLUTAT 2026-06-14

Keplers edit-glob får `*.html: allow`. Hon äger repo, commits och Pages-publicering — då ska hon också kunna skriva sidorna hon publicerar. Tryggt eftersom Kilos `edit` är **specificity-baserad** (Futabas empiriska fynd): `"*": "deny"` blockerar allt utom de explicita allow-mönstren, så `*.html` släpper igenom HTML och inget annat. Skrivspärren i prompten (committar aldrig tyst, skriver inte till vault utan lov) står kvar — utökningen gäller vad hon *kan*, inte vad hon gör utan att fråga.

### Frances Lloyd Wright — vilande

Beslut 2026-06-14: startas **inte** nu. Lyfts ut till egen agent först när ett riktigt arkitekturbeslut dyker upp (t.ex. Pages vs Azure Static Web Apps för olistade sidor). Emoji 📐 är redan vald. Tills dess hanterar Velvet samordning och Architect-persona internt.

---

## 📁 Källor

- `README.md` — Claudes bygge, full struktur och rutiner
- `docs/github-pages-for-humanister.md` — TTfH löpande förklaring
- `docs/github-pages-uppslagsord.md` — TTfH uppslagsord
- Claude-handoff: `.kilo/handoffs/20260614-1750-claude-lipstick-web-bygge-och-ttfh.md`

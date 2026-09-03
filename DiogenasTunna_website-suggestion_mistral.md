# Diogenas tunna – Arkitekturalternativ
!—@💄 korrekturläst 2026-09-03–>

> *Ett digitalt arkiv för den svenska skepticismens historia*

Detta dokument presenterar **tre alternativa arkitekturer** för *Diogenas tunna*, var och en med en **explicit uppdelning** mellan statisk och dynamisk sida, samt tydliga *tradeoffs*. Syftet är att hjälpa dig välja en struktur som:
- **Minimerar backend-ytan** (endast vad som krävs för deponering och granskning)
- **Gör innehållet citerbart** (stabila länkar, metadata för Zotero etc.)
- **Är underhållbart** för en ensam maintainer under flera år
- **Klarar de legala kraven** (ingenting publiceras utan din granskning)

---

## 🔍 Designfrågan som måste besvaras explicit

> *"Vad ska ligga på vilken sida, och varför?"*

Följande tabell **tvingar** varje alternativ att svara på denna fråga. **Ingen undvikande** – varje feature är explicit placerad.

| **Feature**               | **Statisk sida (GitHub Pages)** | **Backend (Azure Functions/App Service)** | **Motivering** |
|---------------------------|----------------------------------|--------------------------------------------|----------------|
| Podcast-sidor             | ✅                               | ❌                                          | Läses endast, förbyggt |
| Podcast-ljudfiler         | ✅                               | ❌                                          | Statisk asset |
| Podcast-transkript        | ✅                               | ❌                                          | Sökbart via statiskt index |
| Forum-trådar              | ✅                               | ❌                                          | Läses endast, pseudonymiserat vid build |
| Tidskrifts-sidor          | ✅                               | ❌                                          | Läses endast, OCR:ad |
| Blogginlägg               | ✅                               | ❌                                          | Läses endast, återpublicerade |
| "Berättelser från dåtid" | ✅                               | ❌                                          | Läses endast |
| **Deponeringsformulär**   | ✅ (HTML)                        | ❌                                          | Statisk sida |
| **Deponering (submit)**   | ❌                               | ✅ (Azure Function)                         | Skriver till **privat kö** (ej publiceras!) |
| **Granskning (admin)**    | ❌                               | ✅ (Azure Function + Auth)                  | Kräver autentisering |
| **Sökindex (Pagefind)**   | ✅                               | ❌                                          | Förbyggt, statiskt |
| **SQLite-databas**        | ✅ (via HTTP range requests)    | ❌                                          | Läses endast, fulltext + embeddings |
| **Vektorsökning**          | ⚠️ (Embeddings i SQLite)        | ✅ (Azure AI Search, *valbart*)             | Se alternativ 2 |
| **Citatmetadata**         | ✅ (i `<head>`)                  | ❌                                          | Måste finnas i initial HTML för Zotero |
| **Autentisering**         | ❌                               | ✅ (Azure AD / Token)                       | Endast för admin |

---

## 🏗️ Alternativ 1: **Maximalt Statisk + Minimal Backend** *(Rekommenderas)*

### 📌 Sammanfattning
**"Allt som kan vara statiskt, är statiskt. Backend endast för deponering och admin."**

- **Statisk sida**: Allt innehåll förbyggt som HTML + SQLite-fil med fulltext och embeddings
- **Backend**: Endast **en** Azure Function för deponering (skriver till privat kö) + admin-gränssnitt
- **Sök**: Pagefind (lexikal) + SQLite via [sql.js-httpvfs](https://github.com/sql-js/sql.js/tree/master/experimental/httpvfs) (SQL-frågor direkt från webbläsaren)
- **Semantisk sök**: Embeddings lagrade i SQLite, frågor i webbläsaren

---

### 🗺️ URL-struktur

```
/
├── /                          # Startsida
├── /podcasts/                 # Podcast-arkiv
│   ├── /podcasts/             # Lista
│   └── /podcasts/{id}/        # Enskilt avsnitt (t.ex. /podcasts/pod-001/)
├── /forum/                    # Återskapat forum
│   ├── /forum/                # Lista
│   └── /forum/{thread-id}/    # Tråd (t.ex. /forum/thread-123/)
├── /journals/                 # Tidskriftsarkiv
│   ├── /journals/             # Lista
│   ├── /journals/{vol}/       # Volym
│   ├── /journals/{vol}/{issue}/ # Nummer
│   └── /journals/{vol}/{issue}/{page}/ # Sida (t.ex. /journals/1/1/5/)
├── /blogs/                    # Återpublicerade bloggar
│   ├── /blogs/                # Lista
│   ├── /blogs/{blog-name}/    # Blog
│   └── /blogs/{blog-name}/{post-id}/ # Inlägg
├── /stories/                  # "Berättelser från dåtid"
│   ├── /stories/              # Lista
│   └── /stories/{id}/         # Enskild berättelse
├── /deposit/                  # Deponeringsformulär (statisk sida)
├── /admin/                    # Admin-gränssnitt (autentiserat)
└── /om/                       # Statiska sidor
    ├── /om/policy/           # Redaktionell policy
    ├── /om/deposit-policy/    # Deponeringspolicy
    ├── /om/rights/            # Rättigheter och tillstånd
    ├── /om/colophon/           # Kolofon (ansvarig utgivare: Lotten Kalenius)
    └── /om/conflict-of-interest/ # Jävsdeklaration
```

---

### 📁 Repository-layout

```
/diogenas-tunna/
├── /content/                  # Källfiler (Markdown/YAML)
│   ├── /podcasts/
│   │   └── pod-001.md
│   ├── /forum/
│   │   └── thread-123.md
│   ├── /journals/
│   │   └── vol1/issue1/page5.md
│   ├── /blogs/
│   │   └── blog-name/post-001.md
│   └── /stories/
│       └── story-001.md
├── /static/                   # Statiska assets
│   ├── /audio/                # Ljudfiler
│   ├── /sqlite/               # SQLite-databas
│   │   └── archive.db         # Fulltext + embeddings (100-150 MB)
│   └── /pagefind/             # Pagefind-index
│       └── index.json
├── /src/                      # Källkod (React/Next.js)
│   ├── /components/
│   ├── /pages/
│   └── /styles/
├── /functions/                # Azure Functions
│   ├── /deposit/              # Deponerings-endpoint
│   │   └── index.js
│   └── /admin/                # Admin-gränssnitt
│       └── index.js
├── /scripts/                  # Build-skript
│   ├── build-sqlite.js        # Bygger SQLite-databasen
│   ├── build-pagefind.js      # Bygger Pagefind-index
│   └── embeddings.js          # Genererar embeddings
├── next.config.js             # Next.js-konfig (output: 'export')
├── package.json
└── README.md
```

---

### 📝 Innehållsmodell (Front Matter)

Varje innehållstyp har **obligatoriska fält** för **proveniens** och **citerbarhet**.

#### Podcast
```yaml
---
type: podcast
id: pod-001
title: "Intervju med [Namn]"
date: 2020-01-15
duration: 3420  # Sekunder
audio: /static/audio/pod-001.mp3
transcript: /static/transcripts/pod-001.txt
source: "Originalkälla: [Länk]"
rights: "Tillstånd för återpublicering: [Namn]"
license: CC-BY-NC-4.0
citation:
  author: "[Namn]"
  title: "Intervju med [Namn]"
  date: 2020-01-15
  container-title: "Podcastnamn"
  url: "/podcasts/pod-001/"
---
```

#### Forum-tråd
```yaml
---
type: forum_thread
id: thread-123
forum: "Skeptikerforum"
title: "Diskussion om [ämne]"
original_date: 2010-03-20
pseudonymized: true
source: "phpBB-databasedump (2010-2020)"
rights: "Pseudonymiserat; originala rättigheter okända"
posts:
  - post_id: 1
    author: "Användare123"  # Pseudonym
    date: 2010-03-20T14:30:00
    content: "Innehåll..."
---
```

#### Tidskriftssida
```yaml
---
type: journal_page
volume: 1
issue: 1
page: 5
title: "Artikelrubrik"
author: "Författarnamn"
source: "OCR från PDF (original: [Länk])"
rights: "Rättigheter: [Namn]; OCR: Diogenas tunna"
original_page: 5  # Dold HTML-markör för citat
next_page: 6
prev_page: 4
citation:
  author: "Författarnamn"
  title: "Artikelrubrik"
  date: 2000-01-01
  container-title: "Tidskriftsnamn"
  firstpage: 5
  lastpage: 10
  url: "/journals/1/1/5/"
---
```

#### Blogginlägg
```yaml
---
type: blog_post
blog: "Bloggnamn"
id: post-001
title: "Inläggsrubrik"
date: 2015-06-10
author: "Originalförfattare"
source: "Återpublicerad med tillstånd från [Namn]"
rights: "Tillstånd: [Namn]"
original_url: "https://original-blog.com/post-001"
---
```

#### Berättelse
```yaml
---
type: story
id: story-001
title: "Min tid i rörelsen"
author: "Pseudonym"  # Kan vara riktigt namn om tillstånd ges
.date: 2023-11-05
source: "Insänt via deponeringsformulär"
rights: "Tillstånd för publicering: [Namn]"
provenance: "Första-person-berättelse"
---
```

---

### 🔍 Sökstrategi

| **Metod**               | **Plats**               | **Storlek** | **Byggtid** | **Kostnad** | **Semantisk** | **Failure Mode** |
|-------------------------|-------------------------|-------------|-------------|-------------|---------------|------------------|
| **Pagefind**            | Statisk (GitHub Pages) | ~10-20 MB   | <1 minut    | Gratis      | ❌            | Ingen semantisk sök |
| **SQLite + sql.js**     | Statisk (GitHub Pages) | ~50-100 MB  | 5-10 min    | Gratis      | ✅ (embeddings) | Långsam laddning i gamla webbläsare |
| **Azure AI Search**     | Backend                | ~1 MB (client) | N/A        | ~$0.10/GB/mån + frågekostnad | ✅ | Backend-beroende |

**Rekommendation för Alternativ 1:**
- **Primär sök**: Pagefind (snabb, liten, lexikal)
- **Avancerad sök**: SQLite via sql.js-httpvfs (fulltext-SQL + embeddings för semantisk sök)
- **Varför?** Ingen backend-beroende, full funktionalitet, kostnadsfritt.

**Exempel på SQLite-schema:**
```sql
CREATE TABLE documents (
  id TEXT PRIMARY KEY,
  type TEXT,          -- 'podcast', 'forum_thread', etc.
  title TEXT,
  content TEXT,       -- Fulltext
  metadata JSON,      -- Citatmetadata, proveniens
  embedding BLOB      -- 384-dim float32 (1.5 KB per dokument)
);
CREATE VIRTUAL TABLE documents_fts USING fts5(content);
```

**Embeddings-storlek:**
- ~40,000 dokument (150 tidskriftsnummer + transkript + forum)
- 384-dim float32 = 1.5 KB per embedding
- **Totalt: ~60 MB** (acceptabel för GitHub Pages)

---

### 🏛️ Citerbarhet

**Problem:** React-renderad metadata syns inte av Zotero/referenshanterare.

**Lösning:**
1. **Pre-rendera alla sidor** vid build (Next.js `output: 'export'`)
2. **Lägg metadata i `<head>`** (inte via React):
   ```html
   <!-- Highwire Press -->
   <meta name="citation_title" content="Artikelrubrik">
   <meta name="citation_author" content="Författarnamn">
   <meta name="citation_date" content="2000-01-01">
   <meta name="citation_journal_title" content="Tidskriftsnamn">
   <meta name="citation_firstpage" content="5">
   <meta name="citation_lastpage" content="10">
   <meta name="citation_pdf_url" content="/static/journals/vol1/issue1.pdf">
   
   <!-- Dublin Core -->
   <meta name="dcterms.title" content="Artikelrubrik">
   <meta name="dcterms.creator" content="Författarnamn">
   <meta name="dcterms.date" content="2000-01-01">
   <meta name="dcterms.isPartOf" content="Tidskriftsnamn">
   
   <!-- OpenGraph (för sociala medier) -->
   <meta property="og:title" content="Artikelrubrik">
   <meta property="og:url" content="https://diogenas-tunna.se/journals/1/1/5/">
   ```
3. **"Kopiera citat"-knapp** (visar formaterad referens i BibTeX/APA/Harvard)
4. **Stabila länkar**:
   - **Inga query-parameters** i kanoniska URL:er
   - **Versionerade URL:er** (t.ex. `/journals/v1/1/1/5/`) om innehåll uppdateras

---

### 🔒 Autentisering & CORS

| **Komponent**       | **Metod**                          | **Motivering** |
|----------------------|------------------------------------|----------------|
| Deponerings-endpoint | Azure Function + **POST**           | Skriver till privat kö |
| Admin-gränssnitt     | Azure AD / GitHub OAuth / Token    | Endast för Lotten |
| CORS                 | `Access-Control-Allow-Origin: https://diogenas-tunna.se` | Tillåt endast GitHub Pages |

**Token-baserad autentisering (enklast för 1 maintainer):**
- Lagra en **hemlig token** i `process.env.ADMIN_TOKEN`
- Skicka med i `Authorization: Bearer <token>`
- **Nackdel**: Mindre säker än OAuth, men tillräckligt för låg trafik

---

### ⚖️ Tradeoffs

| **Fördelar** | **Nackdelar** |
|--------------|---------------|
| ✅ **Minimal backend-yta** (endast 1-2 functions) | ❌ **Full rebuild** vid innehållsuppdatering |
| ✅ **Lägsta kostnad** (~$0/mån för låg trafik) | ❌ **Stora statiska assets** (~150 MB) |
| ✅ **Ingen backend-beroende** för sök | ❌ **Långsam laddning** av SQLite i mobila nätverk |
| ✅ **Resilient** (GitHub Pages är mycket tillgängligt) | ❌ **Ingen dynamisk innehållsuppdatering** |
| ✅ **Enkel underhåll** (en maintainer) | ❌ **Embeddings-byggtid** (~10 min) |

---

### 💰 Kostnadsanalys (Låg trafik: ~100 besök/dag)

| **Tjänst**               | **Kostnad** | **Notering** |
|--------------------------|-------------|--------------|
| GitHub Pages             | Gratis      | 100 GB bandbredd/mån |
| Azure Functions (Consumption) | Gratis | 1M exekutioner/mån ingår |
| Azure Storage (SQLite)   | ~$0.002/mån | 100 MB lagring |
| **Totalt**              | **~$0/mån** | + domännamn (~$10/år) |

---

### ⚠️ Failure Modes

| **Scenario** | **Påverkan** | **Åtgärd** |
|--------------|--------------|------------|
| GitHub Pages nere | Hela sajten otillgänglig | Vänta på återställning |
| Azure Function nere | Deponering misslyckas | Retry-logik i frontend |
| SQLite-fil för stor | Långsam laddning | Dela upp i flera filer |
| Embeddings för stora | Webbläsaren kraschar | Använd 128-dim embeddings |

---

## 🏗️ Alternativ 2: **Statisk + Backend-Vektorsök**

### 📌 Sammanfattning
**"Samma som Alternativ 1, men med hostad vektorsök för bättre semantisk sök."**

- **Statisk sida**: Allt innehåll + Pagefind + SQLite (utan embeddings)
- **Backend**: 
  - Deponerings-endpoint
  - **Vektorsök-endpoint** (Azure AI Search)
  - Admin-gränssnitt
- **Sök**: Pagefind (lexikal) + Azure AI Search (semantisk)

---

### 🔄 Skillnader från Alternativ 1

| **Aspekt** | **Alternativ 1** | **Alternativ 2** |
|------------|------------------|------------------|
| **Semantisk sök** | Embeddings i SQLite (webbläsare) | Azure AI Search (backend) |
| **SQLite-storlek** | ~100-150 MB | ~50 MB (utan embeddings) |
| **Backend-beroende** | ❌ Nej | ✅ Ja (för vektorsök) |
| **Kostnad** | ~$0 | ~$5-10/mån (Azure AI Search) |
| **Sökprestanda** | Snabb (lokal) | Snabb (backend) |
| **Underhåll** | Enkelt | Mer komplext (backend-konfig) |

---

### ✅ Fördelar
- **Bättre semantisk sök** (Azure AI Search är optimerad för detta)
- **Mindre statiska assets** (SQLite utan embeddings)
- **Mer skalbart** (backend hanterar stora index)

### ❌ Nackdelar
- **Backend-beroende** för sök (om Azure AI Search fallerar, ingen semantisk sök)
- **Högre kostnad** (~$5-10/mån för låg trafik)
- **Mer komplext** (konfigurera och underhålla Azure AI Search)

---

### 💰 Kostnadsanalys

| **Tjänst** | **Kostnad** | **Notering** |
|------------|-------------|--------------|
| GitHub Pages | Gratis | |
| Azure Functions | Gratis | 1M exekutioner/mån |
| Azure AI Search | ~$5-10/mån | 1 index, låg trafik |
| Azure Storage | ~$0.002/mån | 50 MB |
| **Totalt** | **~$5-10/mån** | + domännamn |

---

## 🏗️ Alternativ 3: **Hybrid med Dynamisk Innehållsuppdatering**

### 📌 Sammanfattning
**"Statisk bas, men möjlighet att lägga till nytt innehåll utan full rebuild."**

- **Statisk sida**: Podcasts, forum, tidskrifter, bloggar (läses endast)
- **Dynamisk sida**: 
  - "Berättelser från dåtid" (kan läggas till via admin)
  - Deponerat material (efter granskning)
- **Backend**: 
  - Deponerings-endpoint
  - Innehållshantering (skriver till SQLite i Azure Storage)
  - Vektorsök (Azure AI Search)
  - Admin-gränssnitt
- **Sök**: Pagefind (statisk) + Azure AI Search (dynamisk)

---

### 🔄 Skillnader från Alternativ 1 & 2

| **Aspekt** | **Alternativ 1** | **Alternativ 2** | **Alternativ 3** |
|------------|------------------|------------------|------------------|
| **Dynamiskt innehåll** | ❌ Nej | ❌ Nej | ✅ Ja |
| **Backend-yta** | Minimal | Liten | Större |
| **Underhåll** | Enkelt | Medel | Komplext |
| **Kostnad** | ~$0 | ~$5-10 | ~$10-20 |
| **Flexibilitet** | Låg | Medel | Hög |

---

### ✅ Fördelar
- **Flexibel innehållsuppdatering** (nytt material utan rebuild)
- **Bättre för framtida tillväxt** (om arkivet expanderar)

### ❌ Nackdelar
- **Större backend-yta** (fler attackvektorer, mer underhåll)
- **Högre kostnad** (~$10-20/mån)
- **Mer komplext** (synkronisering mellan statisk/dynamisk sida)

---

## 📊 Jämförelsematris

| **Kriterium**               | **Alternativ 1** | **Alternativ 2** | **Alternativ 3** |
|----------------------------|------------------|------------------|------------------|
| **Backend-yta**            | ⭐⭐ (Minimal)    | ⭐⭐⭐ (Liten)     | ⭐⭐⭐⭐ (Stor)     |
| **Kostnad**                | ⭐⭐⭐⭐⭐ ($0)    | ⭐⭐⭐ ($5-10)     | ⭐⭐ ($10-20)      |
| **Semantisk sök**          | ⭐⭐⭐ (Embeddings i SQLite) | ⭐⭐⭐⭐ (Azure AI Search) | ⭐⭐⭐⭐ |
| **Underhåll**              | ⭐⭐⭐⭐⭐ (Enkelt) | ⭐⭐⭐ (Medel)      | ⭐⭐ (Komplext)     |
| **Flexibilitet**           | ⭐ (Låg)          | ⭐⭐ (Medel)       | ⭐⭐⭐⭐ (Hög)      |
| **Resiliens**              | ⭐⭐⭐⭐⭐ (Hög)    | ⭐⭐⭐ (Medel)      | ⭐⭐ (Låg)          |
| **Legala krav**            | ✅ Fullständigt   | ✅ Fullständigt   | ✅ Fullständigt   |
| **Citerbarhet**            | ✅ Fullständigt   | ✅ Fullständigt   | ✅ Fullständigt   |

---

## 🎯 Rekommendation: **Alternativ 1**

**Varför?**
1. **Minimerar backend-ytan** till endast det **absolut nödvändiga** (deponering + admin)
2. **Uppfyller alla legala krav** (ingenting publiceras utan granskning)
3. **Lägsta kostnad** (~$0/mån för låg trafik)
4. **Enkel underhåll** för en ensam maintainer
5. **Resilient** (GitHub Pages är extremt tillgängligt)
6. **Full funktionalitet** (sök, citat, proveniens) utan backend-beroende

**När ska du välja Alternativ 2?**
- Om **semantisk sök** är kritisk och du vill undvika stora statiska assets
- Om du är villig att betala ~$5-10/mån för bättre sök

**När ska du välja Alternativ 3?**
- Om du förväntar dig **frekventa innehållsuppdateringar** (nytt material varje vecka)
- Om du vill ha **maximal flexibilitet** för framtida expansion

---

## 🔍 Djupdyk: Sökstrategier

### 1. **Pagefind (Lexikal Sök)**
- **Hur**: Förbyggt index vid deploy
- **Storlek**: ~10-20 MB för hela korpusen
- **Byggtid**: <1 minut
- **Kostnad**: Gratis
- **Prestanda**: Mycket snabb (lokal sök)
- **Semantisk**: ❌ Nej
- **Failure Mode**: Ingen semantisk sök
- **Rekommendation**: **Använd alltid** (bra baslinje)

### 2. **SQLite + sql.js-httpvfs (Fulltext + Embeddings)**
- **Hur**: SQLite-fil serveras från GitHub Pages, frågas via `sql.js` i webbläsaren
- **Storlek**: ~50-150 MB (beroende på embeddings)
- **Byggtid**: 5-10 minuter (embeddings-generering)
- **Kostnad**: Gratis
- **Prestanda**: Snabb (lokal SQL + vektorberäkningar)
- **Semantisk**: ✅ Ja (om embeddings inkluderas)
- **Failure Mode**: Långsam laddning i mobila nätverk
- **Rekommendation**: **Använd i Alternativ 1** (full funktionalitet utan backend)

**Exempel på vektorsök i webbläsaren:**
```javascript
// 1. Ladda embeddings från SQLite
const { embeddings } = await db.query("SELECT id, embedding FROM documents");
// 2. Beräkna query-embedding (använd en lättviktig modell i webbläsaren)
const queryEmbedding = await model.embed("sökfråga");
// 3. Beräkna cosine similarity
const results = embeddings.map(doc => ({
  id: doc.id,
  score: cosineSimilarity(queryEmbedding, doc.embedding)
})).sort((a, b) => b.score - a.score);
```

### 3. **Azure AI Search (Hostad Vektorsök)**
- **Hur**: Backend-endpoint som anropas från frontend
- **Storlek**: ~1 MB (client), index lagrat i Azure
- **Byggtid**: N/A (hanteras av Azure)
- **Kostnad**: ~$0.10/GB/mån + ~$0.50/1000 frågor
- **Prestanda**: Mycket snabb (backend)
- **Semantisk**: ✅ Ja
- **Failure Mode**: Backend-beroende (om Azure fallerar, ingen sök)
- **Rekommendation**: **Använd i Alternativ 2 & 3** (om budget tillåter)

---

## 📜 Proveniens & Metadata

**Varje enskilt dokument måste bära:**

| **Fält** | **Beskrivning** | **Exempel** |
|----------|-----------------|-------------|
| `type` | Typ av innehåll | `podcast`, `forum_thread`, `journal_page` |
| `source` | Ursprungskälla | "phpBB-databasedump (2010-2020)" |
| `rights` | Rättighetsinnehavare | "Rättigheter: Skeptikerförbundet; OCR: Diogenas tunna" |
| `license` | Licens | "CC-BY-NC-4.0" |
| `provenance` | Hur vi fått materialet | "Pseudonymiserad databasedump", "Insänt via deponeringsformulär" |

**Visning på sidan:**
```markdown
## 📄 Proveniens

- **Typ**: Tidskriftsartikel
- **Källa**: OCR från PDF (original: [Länk](...))
- **Rättigheter**: Rättighetsinnehavare: [Namn]; Återpublicering: Med tillstånd
- **Licens**: [CC-BY-NC-4.0](...)
- **Arkiv-ID**: journal-1-1-5
```

---

## 📄 Krävda Statiska Sidor

| **Sida** | **Innehåll** | **URL** |
|----------|--------------|---------|
| **Redaktionell policy** | Urvalskriterier, redigeringsprocess, korrigeringspolicy, nedtagningspolicy | `/om/policy/` |
| **Deponeringspolicy** | Vad accepteras, hur granskas, hantering av overifierbart material | `/om/deposit-policy/` |
| **Rättigheter & tillstånd** | Upphovsrättsstatus, hur man begär tillstånd, hur rättighetsinnehavare kan begära borttagning | `/om/rights/` |
| **Kolofon** | Tekniska detaljer, ansvarig utgivare (**Lotten Kalenius**), kontaktinfo, teknikstack | `/om/colophon/` |
| **Jävsdeklaration** | Lotten Kalenius medverkar i delar av den historia arkivet dokumenterar; hur detta påverkar redaktionella beslut | `/om/conflict-of-interest/` |

---

## 🧭 Navigation

### **Toppmeny**
```
[Start] [Podcasts] [Forum] [Tidskrifter] [Bloggar] [Berättelser] [Deponera] [Om]
```

### **Sökupplevelse**
1. **Global sök** (topphörn): Söker i **alla** sektioner (Pagefind)
2. **Sektionsspecifik sök** (på varje arkivsida): Filtrera till podcasts/tidskrifter/etc.
3. **Avancerad sök**: SQL-frågor (för avancerade användare)
4. **Filter**: Årtal, författare, ämne, innehållstyp

### **Första besöket**
- **Landing page** med:
  - Kort beskriving av arkivet
  - **Snabblänkar** till populära sektioner
  - **Sökruta** (global sök)
  - **Nyaste tillskotten** (om dynamiskt innehåll)
  - **Om arkivet** (länk till kolofon/policy)

---

## ⚡ Tekniska Detaljer

### **Build-process (Alternativ 1)**
```bash
# 1. Generera embeddings (lokalt)
npm run embeddings
# 2. Bygg SQLite-databas
npm run build-sqlite
# 3. Bygg Pagefind-index
npm run build-pagefind
# 4. Bygg statisk sida (Next.js)
npm run build
npm run export
# 5. Deploy till GitHub Pages
git add . && git commit -m "Deploy" && git push
```

### **SQLite-schema**
```sql
-- Dokument (för fulltextsök)
CREATE TABLE documents (
  id TEXT PRIMARY KEY,
  type TEXT NOT NULL,          -- 'podcast', 'forum_thread', etc.
  title TEXT NOT NULL,
  content TEXT NOT NULL,       -- Fulltext
  url TEXT NOT NULL,           -- Kanonisk URL
  metadata JSON NOT NULL,     -- Citatmetadata, proveniens
  embedding BLOB              -- 384-dim float32 (valbart)
);

-- Fulltext-index
CREATE VIRTUAL TABLE documents_fts USING fts5(
  title, content, 
  tokenize="unicode61 remove_diacritics 2"
);

-- Citatmetadata (för snabb access)
CREATE TABLE citations (
  id TEXT PRIMARY KEY,
  title TEXT,
  author TEXT,
  date TEXT,
  container_title TEXT,
  firstpage INTEGER,
  lastpage INTEGER,
  url TEXT
);
```

### **Pagefind-konfiguration**
```json
{
  "source": "./out",
  "output": "./static/pagefind",
  "lang": "sv",
  "indexing": {
    "exclude": ["admin", "deposit"]
  }
}
```

---

## ⚠️ Vad du kanske har förbisett

### 1. **Legal Deposit (Pliktleverans)**
- **Problem**: I Sverige kan digitala publikationer vara **pliktavleverings skyldiga** till Kungliga Biblioteket.
- **Åtgärd**: Kontakta KB för att klargöra om *Diogenas tunna* faller under detta.
- **Risk**: Om arkivet anses vara en "periodisk publikation", kan du vara skyldig att leverera kopior.

### 2. **Långsiktig Bevarande**
- **Problem**: Format kan bli omoderna (t.ex. MP3, SQLite).
- **Åtgärd**:
  - **Formatmigration**: Planera för regelbunden konvertering (t.ex. MP3 → Opus)
  - **Checksums**: Lagra SHA-256 för alla filer
  - **Backup**: Minst **3 kopior** (GitHub, lokal, moln)

### 3. **Tillgänglighet (WCAG)**
- **Problem**: OCR:ad text kan ha fel, forum-innehåll kan vara svårt att navigera.
- **Åtgärd**:
  - **Alt-text** för alla bilder
  - **Semantisk HTML** (rubriker, listor, etc.)
  - **Keyboard navigation** (testa med tabb)
  - **Screen reader-testing** (NVDA/VoiceOver)

### 4. **Prestanda för SQLite i Webbläsaren**
- **Problem**: 100+ MB SQLite-fil kan vara **långsam att ladda** i mobila nätverk.
- **Åtgärd**:
  - **Dela upp** i flera filer (t.ex. `podcasts.db`, `journals.db`)
  - **Lazy-load** (ladda endast relevanta databaser)
  - **Komprimering** (gzip/Brotli)

### 5. **Säkerhet**
- **Problem**: Forum-innehåll kan innehålla **XSS-attacker** (även pseudonymiserat).
- **Åtgärd**:
  - **Sanitize all content** (DOMPurify)
  - **CSP-headers** (Content Security Policy)
  - **No user-generated HTML** (använd Markdown → HTML med sanitization)

### 6. **Pseudonymiseringens Robusthet**
- **Problem**: Manuell pseudonymisering kan missa **identifierbar information**.
- **Åtgärd**:
  - **Automatiserad pseudonymisering** (regex för e-post, telefonnummer, etc.)
  - **Manuell granskning** av slumpmässiga poster
  - **Dokumentera processen** (för transparens)

### 7. **Versionering av Innehåll**
- **Problem**: Om ett fel upptäcks i en tidskrifts-OCR, hur hanteras korrigering?
- **Åtgärd**:
  - **Git-versionering** av alla källfiler
  - **Korrigeringar som nya versioner** (t.ex. `/journals/1/1/5/v2/`)
  - **Changelog** för varje dokument

### 8. **Backup av Deponeringskö**
- **Problem**: Om Azure Storage fallerar, försvinner deponerat material.
- **Åtgärd**:
  - **Automatisk backup** till ett annat moln (t.ex. Backblaze B2)
  - **Lokal backup** (encrypterad)

### 9. **Analytics**
- **Problem**: Du vill veta **hur arkivet används** (för impact-bedömning).
- **Åtgärd**:
  - **Plausible** (privacy-vänlig, GDPR-kompatibel)
  - **Egen loggning** (anonymiserad IP, endas för statistik)

### 10. **Offline-åtkomst**
- **Problem**: Forskare i områden med dålig internet kan vilja jobba offline.
- **Åtgärd**:
  - **Service Worker** (cachar statiska assets)
  - **PWA** (Progressive Web App) för offline-läsning

---

## 📦 Externa Beroenden & Risker

| **Tjänst** | **Användning** | **Kostnad** | **Failure Mode** | **Mitigation** |
|------------|---------------|-------------|------------------|----------------|
| **GitHub Pages** | Statisk hosting | Gratis | GitHub nere | Vänta, eller flytta till Netlify/Vercel |
| **Azure Functions** | Deponering, admin | Gratis (låg trafik) | Azure nere | Fallback till lokal backend |
| **Azure Storage** | SQLite, deponeringskö | ~$0.002/mån | Azure nere | Backup till annat moln |
| **Azure AI Search** | Vektorsök (valbart) | ~$5-10/mån | Azure nere | Fallback till SQLite-embeddings |
| **sql.js** | SQLite i webbläsaren | Gratis | Buggar | Testa med flera webbläsare |
| **Pagefind** | Lexikal sök | Gratis | Buggar | Fallback till SQLite FTS |

---

## 🎯 Nästa Steg

1. **Välj ett alternativ** (Rekommendation: **Alternativ 1**)
2. **Skapa repository** på GitHub med ovanstående struktur
3. **Testa SQLite + sql.js-httpvfs** med en liten datamängd
4. **Bygg en prototyp** av deponeringsflödet (formulär → Azure Function → privat kö)
5. **Verifiera citerbarhet** (testa med Zotero)
6. **Granska proveniens** för varje innehållstyp

---

## 📚 Referenser

- [sql.js-httpvfs](https://github.com/sql-js/sql.js/tree/master/experimental/httpvfs) – SQLite över HTTP range requests
- [Pagefind](https://pagefind.app/) – Statisk sök för Hugo/Jekyll/Next.js
- [Azure Functions (Consumption Plan)](https://azure.microsoft.com/en-us/pricing/details/functions/) – Pay-per-use serverless
- [Highwire Press Metadata](https://highwire.stanford.edu/public/HighWirePressMetadataTagLibrary.pdf) – Citatmetadata-standard
- [Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) – Metadata-standard
- [Tryckfrihetsförordningen (1949:105)](https://www.lagen.nu/1949:105) – Svenska grundlagen om pressfrihet

---

*Senast uppdaterad: 28 augusti 2026*
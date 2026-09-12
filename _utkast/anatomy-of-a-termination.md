---
titel: Anatomin i en avsättning
slug: anatomy-termination
typ: vardagsobservationer
datum: 2026-08-14
design: ja
idé: Gör en html-rendering av en 
---

# Avsättningens anatomi

> ### Dataklasser
> 
> **class: actor**  
> > `type: literal` ["beslutsfattare", "jagsvag-hycklare", "maktspelare", "medioker-mellanchef", "mobbare", "organisation"]  
> > `bound_by: ruleset`
>
> **class: target**  
> > `type: literal` ["individ", "fornamn-efternamn"]  
> > `acts_in_accordance_with: ruleset`  
>
> **class: ruleset**  
> > `type: list {global_rules}` ["husregler", "protokollfort-beslut", "stadgar"]  
> > `applies_to: @everyone`  
> > `invoked_by: target`  
>
> **class: command**  
> > `type: literal` ["avtal-upphavt", "ej-atervald"]  
> > `issued_by: actor`  
> > `onto: target`  
> > `stated_cause: str {random_value}` ["konflikt", "oenighet"]  
> > `actual_cause: str {imputed_value}`  
>
> **class: event**  
> > `type: literal` ["avslut_avslutas"]  
> > `stated_cause: str {random_value}`  
> > `actual_cause: str {imputed_value}`  
> > `narrative: str {random_value}`

## Händelse

`[target]`s uppdrag för `[actor]` avslutas med omedelbar verkan och utan förvarning, med hänvisning till  `[stated cause: "konflikt"]`. Beslutet fattas efter att `[actor: "beslutsfattare"]` lyssnat på den ena parten `[actor: "medioker-maktspelare"]` i `[stated cause: "konflikt"]`.

## Utlösande faktor

`[target]` drog i nödbromsen på verksamhet som inte följer `[ruleset]`.

## Vändning

`[target]` agerade i enlighet med `[ruleset]`, men eftersom `[actor="medioker-maktspelare" ×1–n]` riskerar att framstå i dålig dager flyttar `[actor="beslutsfattare"]` på `[target]` i stället för att själva följa `[ruleset]`.

## Resultat

`[stated_cause="arbetsmiljö"]` ger `[narrative="brakstake"]`.

---
---

## SVG

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1240 968" width="1240" height="968" font-family="'Helvetica Neue', Arial, sans-serif">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#16211F"/>
    </marker>
    <marker id="arrowRed" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#A8322B"/>
    </marker>
    <marker id="arrowLight" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#E4E6E1"/>
    </marker>
    <style>
      .eyebrow { font-family: 'Arial Narrow', 'Helvetica Neue', Arial, sans-serif; font-size: 11px; letter-spacing: 2.4px; fill: #6E7A78; }
      .boxlabel { font-family: 'Arial Narrow', 'Helvetica Neue', Arial, sans-serif; font-size: 12px; letter-spacing: 1.8px; fill: #A8322B; }
      .body { font-size: 14.5px; fill: #16211F; }
      .ph { fill: #7A5C1E; font-style: italic; }
      .display { font-family: Georgia, 'Iowan Old Style', serif; }
    </style>
  </defs>

  <rect width="1240" height="968" fill="#E4E6E1"/>

  <!-- Header -->
  <text class="display" x="60" y="74" font-size="36" fill="#16211F">Anatomin i en avsättning</text>
  <text class="eyebrow" x="60" y="100">EN MALL · FYLL I KLAMRARNA EFTER BEHOV</text>
  <line x1="60" y1="122" x2="1180" y2="122" stroke="#16211F" stroke-width="1.5"/>

  <text class="colhead" x="60" y="155">FÖRLOPPET</text>
  <text class="colhead" x="650" y="155">NARRATIVET</text>

  <!-- STEG 1 -->
  <rect x="60" y="170" width="530" height="86" fill="#F2F1EC" stroke="#16211F" stroke-width="1.5"/>
  <text class="boxlabel" x="80" y="196">UTGÅNGSLÄGET</text>
  <text class="body" x="80" y="220">Inom <tspan class="ph">[actor; type: "organisation"]</tspan> bedrivs verksamhet som går stick</text>
  <text class="body" x="80" y="240">i stäv med <tspan class="ph">[file: "\common-rules.md"]</tspan>.</text>
  <line x1="325" y1="256" x2="325" y2="284" stroke="#16211F" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- STEG 2 -->
  <rect x="60" y="286" width="530" height="86" fill="#F2F1EC" stroke="#16211F" stroke-width="1.5"/>
  <text class="boxlabel" x="80" y="312">NÖDBROMSEN</text>
  <text class="body" x="80" y="336"><tspan class="ph">[actor; type: "target"]</tspan> påtalar saken och agerar i enlighet med</text>
  <text class="body" x="80" y="356">[file: "\common-rules.md"]. Detta är den utlösande faktorn.</text>
  <line x1="325" y1="372" x2="325" y2="400" stroke="#16211F" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- STEG 3 -->
  <rect x="60" y="402" width="530" height="86" fill="#F2F1EC" stroke="#16211F" stroke-width="1.5"/>
  <text class="boxlabel" x="80" y="428">PRESTIGELÄGET</text>
  <text class="body" x="80" y="452"><tspan class="ph">[actor; type: "power player"]</tspan> riskerar att framstå i dålig dager.</text>
  <text class="body" x="80" y="472">Sakfrågan blir en personfråga.</text>
  <line x1="325" y1="488" x2="325" y2="516" stroke="#16211F" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- STEG 4 -->
  <rect x="60" y="518" width="530" height="100" fill="#F2F1EC" stroke="#16211F" stroke-width="1.5"/>
  <text class="boxlabel" x="80" y="544">ENSIDIG BEREDNING</text>
  <text class="body" x="80" y="568"><tspan class="ph">{beslutsfattare}</tspan> lyssnar på den ena parten i en konflikt</text>
  <text class="body" x="80" y="588">som inte var en konflikt, men som genom just detta</text>
  <text class="body" x="80" y="608">blir en konflikt.</text>

  <!-- VÄGVAL -->
  <text class="eyebrow" x="60" y="644">VÄGVALET</text>
  <line x1="325" y1="618" x2="325" y2="652" stroke="#16211F" stroke-width="1.5"/>
  <line x1="187" y1="652" x2="462" y2="652" stroke="#16211F" stroke-width="1.5"/>
  <line x1="187" y1="652" x2="187" y2="678" stroke="#6E7A78" stroke-width="1.5" stroke-dasharray="5 4" marker-end="url(#arrow)"/>
  <line x1="462" y1="652" x2="462" y2="678" stroke="#A8322B" stroke-width="2" marker-end="url(#arrowRed)"/>

  <rect x="60" y="680" width="255" height="96" fill="#E4E6E1" stroke="#6E7A78" stroke-width="1.5" stroke-dasharray="5 4"/>
  <text class="boxlabel" x="78" y="706" fill="#6E7A78">EJ VALD</text>
  <text class="body" x="78" y="730" fill="#6E7A78">Följ reglerna. Åtgärda det</text>
  <text class="body" x="78" y="750" fill="#6E7A78">som påtalats. Bär obehaget</text>
  <text class="body" x="78" y="770" fill="#6E7A78">av att ha haft fel.</text>

  <rect x="335" y="680" width="255" height="96" fill="#F2F1EC" stroke="#A8322B" stroke-width="2.5"/>
  <text class="boxlabel" x="353" y="706">VALD</text>
  <text class="body" x="353" y="730">Flytta på <tspan class="ph">{person}</tspan>.</text>
  <text class="body" x="353" y="750">Regelverket lämnas</text>
  <text class="body" x="353" y="770">därhän.</text>
  <line x1="462" y1="776" x2="462" y2="806" stroke="#A8322B" stroke-width="2" marker-end="url(#arrowRed)"/>

  <!-- STEG 5 -->
  <rect x="60" y="808" width="530" height="100" fill="#F2F1EC" stroke="#A8322B" stroke-width="2.5"/>
  <text class="boxlabel" x="80" y="834">BESLUTET</text>
  <text class="body" x="80" y="858"><tspan class="ph">{person}</tspan>s uppdrag avslutas utan förvarning och</text>
  <text class="body" x="80" y="878">med omedelbar verkan. Ingen sakligt formulerad</text>
  <text class="body" x="80" y="898">grund anges.</text>

  <!-- NARRATIVKOLUMN -->
  <line x1="590" y1="330" x2="646" y2="330" stroke="#6E7A78" stroke-width="1.5" stroke-dasharray="3 4"/>
  <rect x="650" y="286" width="530" height="86" fill="#DDE1DC" stroke="#6E7A78" stroke-width="1.5"/>
  <text class="boxlabel" x="670" y="312" fill="#5C6B72">OMSKRIVNING</text>
  <text class="body" x="670" y="336" fill="#3A4644">Sakfrågan formuleras om till en vagt hållen</text>
  <text class="body" x="670" y="356" fill="#3A4644">”konfliktsituation”. Vad konflikten gäller sägs inte.</text>

  <line x1="590" y1="568" x2="646" y2="568" stroke="#6E7A78" stroke-width="1.5" stroke-dasharray="3 4"/>
  <rect x="650" y="518" width="530" height="100" fill="#DDE1DC" stroke="#6E7A78" stroke-width="1.5"/>
  <text class="boxlabel" x="670" y="544" fill="#5C6B72">ANGIVEN ORSAK</text>
  <text class="body" x="670" y="568" fill="#3A4644">Arbetsmiljö. Ett skäl som är svårt att bemöta,</text>
  <text class="body" x="670" y="588" fill="#3A4644">eftersom det varken preciseras eller går att</text>
  <text class="body" x="670" y="608" fill="#3A4644">motbevisa.</text>

  <line x1="590" y1="858" x2="646" y2="858" stroke="#6E7A78" stroke-width="1.5" stroke-dasharray="3 4"/>
  <rect x="650" y="808" width="530" height="100" fill="#DDE1DC" stroke="#6E7A78" stroke-width="1.5"/>
  <text class="boxlabel" x="670" y="834" fill="#5C6B72">UNDERFÖRSTÅTT NARRATIV</text>
  <text class="body" x="670" y="858" fill="#3A4644">Bråkstake. Den som drog i nödbromsen blir</text>
  <text class="body" x="670" y="878" fill="#3A4644">problemet, och det som nödbromsen gällde</text>
  <text class="body" x="670" y="898" fill="#3A4644">nämns inte längre.</text>

</svg>

---

## Python

"""anatomi.py

En avsättning, deklarerad.
Rollerna är semantiska: en actor handlar, ett target utsätts.
Protokollet påstår annat.
"""

from dataclasses import dataclass, field
from typing import Literal, Optional

Ruleset = dict[str, list[str]]


@dataclass(frozen=True)
class Actor:
    kind: Literal["organization", "governing-body", "mediocre-middle-management"]
    name: str
    bound_by: Ruleset
    heard: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class Target:
    kind: Literal["individual"]
    name: str
    acted_in_accordance_with: Ruleset
    notice: Optional[str] = None          # aldrig satt, av någon, vid något tillfälle
    effect: Literal["immediate"] = "immediate"


@dataclass(frozen=True)
class Bystander:
    """Deklarerad. Aldrig instansierad."""
    name: str
    reservation: Optional[str] = None


@dataclass(frozen=True)
class Command:
    type: Literal["TerminateEngagement"]
    issued_by: Actor
    onto: Target
    stated_cause: str


@dataclass(frozen=True)
class Event:
    type: Literal["EngagementTerminated"]
    stated_cause: str
    actual_cause: str


global_rules: Ruleset = {
    "applies_to": ["everyone"],
    "invoked_by": ["target"],
    "enforced_by": [],                    # tom lista, inte None: någon hade kunnat
}

parties = ["{den ena parten}", "{den andra parten}"]

target = Target(
    kind="individual",
    name="{person}",
    acted_in_accordance_with=global_rules,
)

management = [
    Actor(
        kind="mediocre-middle-management",
        name="{maktspelare}",
        bound_by=global_rules,
    )
    # kvantitet: 1 .. n. Antalet spelar mindre roll än tröskeln.
]
assert len(management) >= 1, "utan denna finns ingen konflikt"

decision_makers = Actor(
    kind="governing-body",
    name="{beslutsfattare}",
    bound_by=global_rules,
    heard=[parties[0]],               # parties[1] anropas aldrig
)


def follow_rules(actor: Actor, rules: Ruleset) -> None:
    """Det tillgängliga alternativet."""
    raise NotImplementedError         # definierad, aldrig anropad


def conflict(stage: Literal["före beslutet", "efter beslutet"]) -> bool:
    return stage == "efter beslutet"


command = Command(
    type="TerminateEngagement",
    issued_by=decision_makers,
    onto=target,
    stated_cause="konfliktsituation",
)

event = Event(
    type="EngagementTerminated",
    stated_cause="konfliktsituation",
    actual_cause="target invoked global_rules",
)

global_rules: Ruleset = {
    "applies_to": ["everyone"],
    "invoked_by": ["target"],
    "enforced_by": [],     

# Strukturen innehåller exakt ett target. Det är en människa.

---

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

# Strukturen innehåller exakt ett target. Det är en människa.
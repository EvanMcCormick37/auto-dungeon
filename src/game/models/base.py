from typing import List, TypedDict, Optional
from enum import Enum

# Basic object models.
class Base:
    id: str
    name: str
    description: str

# Attributes (D&D standard six)
class Attribute(str, Enum):
    STR = 'STR'
    DEX = 'DEX'
    CON = 'CON'
    INT = 'INT'
    WIS = 'WIS'
    CHA = 'CHA'
# Set of attribute values for an entity.
class Attributes(TypedDict):
    STR: int
    DEX: int
    CON: int
    INT: int
    WIS: int
    CHA: int


# dice.
class Dice(str, Enum):
    D4 = 'd4'
    D6 = 'd6'
    D8 = 'd8'
    D10 = 'd10'
    D12 = 'd12'
    D20 = 'd20'
    D100 = 'd100'
# Dict for keeping track of damage or saving throw rolls.
class Diceroll(TypedDict):
    D4: int
    D6: int
    D8: int
    D10: int
    D12: int
    D20: int
    D100: int


class TargetType(str, Enum):
    MELEE = "melee"         # Targeting
    RANGED = "ranged"       # Targeting
    EFFECT = "effect"       # Nontargeting
    AOE = "aoe"             # Nontargeting
    SELF = "self"           # Nontargeting
# A possible action to take.
class Action(Base):
    type: Optional[TargetType]
    base_attribute: Optional[Attribute]
class AttackStats:
    damage: Diceroll
    attack_bonus: Optional[int]
    save_dc: Optional[int]
    save_type: Optional[Attribute]
# Attack actions.
class Attack(Action):
    attack_stats: AttackStats


# Temporary or permanent status effects.
class Status(Base):
    bonuses: Optional[Attributes]
# Feat representing a power or ability.
class Feat(Base):
    status: Optional[Status]
    actions: Optional[List[Action]]
from typing import List, TypedDict, Tuple
from enum import Enum

# Basic object models.
class Base:
    id: str
    name: str | None
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
# Temporary or permanent status effects.
class Status(Base):
    bonuses: Attributes | None

# Dice.
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
    type: TargetType | None
    base_attribute: Attribute | None
class AttackStats:
    damage: Diceroll
    attack_bonus: int | None
    save_dc: int | None
    save_type: Attribute | None
    on_fail: Status | None
    on_success: Status | None
    on_hit: Status | None
    on_crit: Status | None
# Attack actions.
class Attack(Action):
    attack_stats: AttackStats

# Feat representing a power or ability.
class Feat(Base):
    status: Status | None
    actions: List[Action] | None

# Simple item and Weapon classes
class Item:
    id: str
    name: str
    description: str
    hp: Tuple[str,str]
    _cost: int
    weight: int
    uses: List[Action] | None
    effects: List[Status] | None

class Weapon(Item):
    base_attribute: Attribute | None
    damage_roll: Diceroll | None

# Different types of Lore we store in the DB.
class LoreType(str, Enum):
    POSSIBILITY = "possibility"
    RELATIONSHIP = "relationship"
    MOTIVE = "motive"
    TRAIT = "trait"
    LOCATION = "location"
    SECRET = "secret"
    STORY = "story"

# Lore is knowledge of the world, history or characters. Ties together different involved entities.
class Lore(Base):
    type: LoreType
    pc_knows: bool
    involved: List[str] | None

# A condition which must be met for something to occur. For now essentially just a description. Hard requirements may be added later.
class Requirement(Base):
    involved_ids: List[str] | None